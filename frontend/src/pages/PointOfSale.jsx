import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { toast } from 'react-toastify';
import Icon from '../components/ui/Icon';
import ProductSearchBar from '../components/pos/ProductSearchBar';
import ProductGrid from '../components/pos/ProductGrid';
import CartPanel from '../components/pos/CartPanel';
import ReceiptModal from '../components/pos/ReceiptModal';
import BarcodeScannerModal from '../components/pos/BarcodeScannerModal';
import useProducts, { stockOf } from '../hooks/useProducts';
import useBranches from '../hooks/useBranches';
import useCart from '../hooks/useCart';
import { createSale } from '../services/api';
import '../styles/pos.css';
import '../styles/pos-cart.css';

/** PointOfSale — product browser + cart + checkout + receipt. */
function PointOfSale({ user, onSessionExpired }) {
  const [branchId, setBranchId] = useState(user?.branch_id ? String(user.branch_id) : 'all');
  const { branches } = useBranches({ activeOnly: true });
  const catalog = useProducts({ branchId, onSessionExpired });
  const cart = useCart();
  const [method, setMethod] = useState('cash');
  const [tendered, setTendered] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  const [receipt, setReceipt] = useState(null);
  const [scannerOpen, setScannerOpen] = useState(false);
  const searchRef = useRef(null);

  const cartQty = useMemo(
    () => Object.fromEntries(cart.lines.map(l => [l.product.id, l.quantity])),
    [cart.lines]
  );

  // "/" focuses search, like most POS / admin tools.
  useEffect(() => {
    const onKey = e => {
      if (e.key === '/' && document.activeElement?.tagName !== 'INPUT') {
        e.preventDefault();
        searchRef.current?.focus();
      }
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, []);

  function handleAdd(product) {
    setError('');
    cart.add(product);
  }

  function handleSku(sku) {
    const clean = String(sku || '').trim();
    if (!clean) return;
    const match = catalog.findBySku(clean) || (catalog.products.length === 1 ? catalog.products[0] : null);
    if (!match) {
      toast.error(`No product found matching "${clean}".`);
      return;
    }
    const available = stockOf(match);
    const inCartCount = cartQty[match.id] || 0;
    if (available <= 0 || inCartCount >= available) {
      toast.warning(`${match.name} is out of stock or max available reached.`);
      return;
    }
    handleAdd(match);
    catalog.setQuery('');
    toast.success(`Added ${match.name} to cart.`);
  }

  async function handleCheckout() {
    setSubmitting(true);
    setError('');
    try {
      const sale = await createSale({
        branch_id: branchId !== 'all' ? branchId : undefined,
        paymentMethod: method,
        items: cart.lines.map(l => ({ product_id: l.product.id, quantity: l.quantity })),
      });
      setReceipt({ sale, tendered });
      cart.clear();
      catalog.reload();
    } catch (err) {
      if (err.status === 401) onSessionExpired?.();
      else setError(err.message || 'Checkout failed. Please try again.');
      // Stock may have changed under us — refresh so the cart caps update.
      if (err.status === 422) catalog.reload();
    } finally {
      setSubmitting(false);
    }
  }

  const closeReceipt = useCallback(() => {
    setReceipt(null);
    setTendered('');
    setMethod('cash');
    searchRef.current?.focus();
  }, []);

  return (
    <div className="pos">
      <header className="pos-header" style={{ justifyContent: 'space-between', flexWrap: 'wrap', gap: '12px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <span className="pos-header-icon"><Icon name="pos" size={20} /></span>
          <div>
            <h2>Point of Sale</h2>
            <p>Scan or tap items to build a sale — stock updates automatically.</p>
          </div>
        </div>
        {branches.length > 0 && (
          <select
            value={branchId}
            onChange={e => setBranchId(e.target.value)}
            className="reports-select-filter"
            aria-label="Select POS branch"
          >
            <option value="all">All Branches</option>
            {branches.map(b => (
              <option key={b.id} value={String(b.id)}>{b.name} ({b.code})</option>
            ))}
          </select>
        )}
      </header>

      <div className="pos-layout">
        <section className="pos-catalog" aria-label="Products">
          <ProductSearchBar
            inputRef={searchRef}
            query={catalog.query}
            onQuery={catalog.setQuery}
            onSubmitSku={handleSku}
            onOpenScanner={() => setScannerOpen(true)}
            categories={catalog.categories}
            category={catalog.category}
            onCategory={catalog.setCategory}
          />
          <ProductGrid
            products={catalog.products}
            total={catalog.total}
            loading={catalog.loading}
            error={catalog.error}
            cartQty={cartQty}
            onAdd={handleAdd}
          />
        </section>

        <CartPanel
          cart={cart}
          payment={{ method, setMethod, tendered, setTendered }}
          submitting={submitting}
          error={error}
          onCheckout={handleCheckout}
        />
      </div>

      {receipt && (
        <ReceiptModal
          sale={receipt.sale}
          tendered={receipt.tendered}
          cashier={user?.name || user?.email || 'Staff'}
          onClose={closeReceipt}
        />
      )}

      <BarcodeScannerModal
        isOpen={scannerOpen}
        products={catalog.allProducts}
        onScanSku={handleSku}
        onClose={() => setScannerOpen(false)}
      />
    </div>
  );
}

export default PointOfSale;
