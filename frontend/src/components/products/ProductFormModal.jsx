import { useState, useEffect } from 'react';
import Icon from '../ui/Icon';
import { PRODUCT_PAGE_CATEGORIES } from '../../utils/categories';
import { humanizeErrorMessage } from '../../utils/errorMessage';
import { uploadProductImage } from '../../services/api';
import '../../styles/products-modal.css';

const UNITS = ['bag', 'tin', 'bottle', 'pack', 'carton', 'piece', 'sachet', 'roll', 'kg', 'litre'];

function getInitialState(p, branches = []) {
  return {
    branch_id: p?.branch_id ? String(p.branch_id) : (branches[0]?.id ? String(branches[0].id) : ''),
    name: p?.name || '',
    sku: p?.sku || '',
    category: p?.category || 'grains_staples',
    unit: p?.unit || 'piece',
    cost_price: p?.cost_price ?? '',
    sell_price: p?.sell_price ?? '',
    image_path: p?.image_path || '',
    current_stock: p?.inventory?.quantity ?? '0',
    reorder_threshold: p?.inventory?.reorder_threshold ?? '5',
  };
}

export default function ProductFormModal({ product, branches = [], isOpen, onClose, onSave }) {
  const isEditing = Boolean(product);
  const [formData, setFormData] = useState(() => getInitialState(product, branches));
  const [imageMode, setImageMode] = useState('upload');
  const [imageFile, setImageFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(product?.image_path || '');
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (isOpen) {
      setFormData(getInitialState(product, branches));
      setImageFile(null);
      setImagePreview(product?.image_path || '');
      setImageMode(product?.image_path?.startsWith('http') ? 'url' : 'upload');
      setError('');
    }
  }, [product, branches, isOpen]);

  if (!isOpen) return null;

  const cost = parseFloat(formData.cost_price) || 0;
  const sell = parseFloat(formData.sell_price) || 0;
  const profit = sell - cost;
  const marginPercent = sell > 0 ? Math.round((profit / sell) * 100) : 0;

  function handleFileChange(e) {
    const file = e.target.files?.[0];
    if (!file) return;
    setImageFile(file);
    setImagePreview(URL.createObjectURL(file));
  }

  function handleUrlChange(e) {
    const val = e.target.value;
    setFormData(prev => ({ ...prev, image_path: val }));
    setImagePreview(val);
  }

  function clearImage() {
    setImageFile(null);
    setImagePreview('');
    setFormData(prev => ({ ...prev, image_path: '' }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setError('');
    setSubmitting(true);

    try {
      let finalImagePath = formData.image_path ? formData.image_path.trim() : null;

      if (imageMode === 'upload' && imageFile) {
        const uploadRes = await uploadProductImage(imageFile);
        finalImagePath = uploadRes.url;
      }

      const payload = {
        branch_id: formData.branch_id ? parseInt(formData.branch_id, 10) : null,
        name: formData.name.trim(),
        sku: formData.sku.trim(),
        category: formData.category,
        unit: formData.unit,
        cost_price: parseFloat(formData.cost_price),
        sell_price: parseFloat(formData.sell_price),
        image_path: finalImagePath || null,
        current_stock: parseInt(formData.current_stock, 10) || 0,
        reorder_threshold: parseInt(formData.reorder_threshold, 10) || 0,
      };

      await onSave(payload, product?.id);
      onClose();
    } catch (err) {
      setError(humanizeErrorMessage(err));
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="product-modal-backdrop" role="dialog" aria-modal="true">
      <div className="product-modal">
        <div className="product-modal-head">
          <h3>{isEditing ? 'Edit product' : 'Add product'}</h3>
          <button type="button" className="product-modal-close" onClick={onClose} aria-label="Close modal">
            <Icon name="x" size={16} />
          </button>
        </div>

        {error && <div className="product-form-error" role="alert">{error}</div>}

        <form onSubmit={handleSubmit} className="product-form">
          <div className="form-group full-width">
            <label htmlFor="prod-name">Product name</label>
            <input
              id="prod-name"
              type="text"
              required
              value={formData.name}
              onChange={e => setFormData({ ...formData, name: e.target.value })}
              placeholder="Basmati Rice 5kg"
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="prod-sku">SKU / Barcode</label>
              <input
                id="prod-sku"
                type="text"
                required
                value={formData.sku}
                onChange={e => setFormData({ ...formData, sku: e.target.value })}
                placeholder="CWG-GRN-001"
              />
            </div>
            <div className="form-group">
              <label htmlFor="prod-category">Category</label>
              <select
                id="prod-category"
                value={formData.category}
                onChange={e => setFormData({ ...formData, category: e.target.value })}
              >
                {PRODUCT_PAGE_CATEGORIES.filter(c => c.id !== 'all').map(c => (
                  <option key={c.id} value={c.id}>{c.label}</option>
                ))}
              </select>
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="prod-sell">Selling price (₦)</label>
              <input
                id="prod-sell"
                type="number"
                step="any"
                min="0"
                required
                value={formData.sell_price}
                onChange={e => setFormData({ ...formData, sell_price: e.target.value })}
                placeholder="9500"
              />
            </div>
            <div className="form-group">
              <label htmlFor="prod-cost">Cost price (₦)</label>
              <input
                id="prod-cost"
                type="number"
                step="any"
                min="0"
                required
                value={formData.cost_price}
                onChange={e => setFormData({ ...formData, cost_price: e.target.value })}
                placeholder="7800"
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="prod-stock">Stock on hand</label>
              <input
                id="prod-stock"
                type="number"
                min="0"
                required
                value={formData.current_stock}
                onChange={e => setFormData({ ...formData, current_stock: e.target.value })}
                placeholder="42"
              />
            </div>
            <div className="form-group">
              <label htmlFor="prod-reorder">Reorder level</label>
              <input
                id="prod-reorder"
                type="number"
                min="0"
                required
                value={formData.reorder_threshold}
                onChange={e => setFormData({ ...formData, reorder_threshold: e.target.value })}
                placeholder="12"
              />
            </div>
          </div>

          <div className="form-row align-items-center">
            <div className="form-group">
              <label htmlFor="prod-unit">Unit</label>
              <select id="prod-unit" value={formData.unit} onChange={e => setFormData({ ...formData, unit: e.target.value })}>
                {UNITS.map(u => (<option key={u} value={u}>{u}</option>))}
              </select>
            </div>
            {branches.length > 0 && (
              <div className="form-group">
                <label htmlFor="prod-branch">Branch</label>
                <select id="prod-branch" value={formData.branch_id} onChange={e => setFormData({ ...formData, branch_id: e.target.value })}>
                  {branches.map(b => (<option key={b.id} value={String(b.id)}>{b.name} ({b.code})</option>))}
                </select>
              </div>
            )}
            <div className="form-group profit-margin-col">
              <label className="profit-margin-label">Profit margin</label>
              <div className={`profit-margin-value ${profit < 0 ? 'profit-margin-value--negative' : ''}`}>{sell > 0 ? `${marginPercent}%` : '—'}</div>
            </div>
          </div>

          <div className="form-group full-width prod-image-section">
            <label>Product image (Upload from computer or paste online URL)</label>
            <div className="prod-image-mode-toggle">
              <button
                type="button"
                className={`btn-mode ${imageMode === 'upload' ? 'btn-mode--active' : ''}`}
                onClick={() => setImageMode('upload')}
              >
                Upload from computer
              </button>
              <button
                type="button"
                className={`btn-mode ${imageMode === 'url' ? 'btn-mode--active' : ''}`}
                onClick={() => setImageMode('url')}
              >
                Online image URL
              </button>
            </div>
            <div className="prod-image-input-row">
              {imageMode === 'upload' ? (
                <input
                  id="prod-file"
                  type="file"
                  accept="image/jpeg,image/png,image/webp,image/gif"
                  onChange={handleFileChange}
                />
              ) : (
                <input
                  id="prod-url"
                  type="url"
                  value={formData.image_path}
                  onChange={handleUrlChange}
                  placeholder="https://example.com/product-image.jpg"
                />
              )}
              {imagePreview && (
                <div className="prod-image-preview">
                  <img src={imagePreview} alt="Preview" onError={() => setImagePreview('')} />
                  <button type="button" onClick={clearImage} title="Remove image">✕</button>
                </div>
              )}
            </div>
          </div>

          <div className="product-modal-actions">
            <button type="button" className="btn-modal-cancel" onClick={onClose} disabled={submitting}>
              Cancel
            </button>
            <button type="submit" className="btn-modal-save" disabled={submitting}>
              {submitting ? 'Saving...' : 'Save changes'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
