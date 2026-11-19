import { useEffect, useMemo, useRef, useState } from 'react';
import Icon from '../ui/Icon';
import { formatMoney } from '../../utils/dashboardStats';
import '../../styles/pos-scanner.css';

export default function BarcodeScannerModal({ isOpen, products = [], onScanSku, onClose }) {
  const [code, setCode] = useState('');
  const [camStatus, setCamStatus] = useState('Starting camera...');
  const [camActive, setCamActive] = useState(false);
  const videoRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => {
    if (!isOpen) return undefined;
    setCode('');
    setTimeout(() => inputRef.current?.focus(), 60);

    let stream = null;
    let rafId = null;
    let cancelled = false;

    async function startCamera() {
      if (!navigator.mediaDevices?.getUserMedia) {
        setCamStatus('Camera not available in this browser. Type or use a USB scanner below.');
        return;
      }
      try {
        stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } });
        if (cancelled) {
          stream.getTracks().forEach(t => t.stop());
          return;
        }
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
          await videoRef.current.play();
        }
        setCamActive(true);

        if (!('BarcodeDetector' in window)) {
          setCamStatus('Camera active, but live BarcodeDetector is unsupported here. Enter SKU below.');
          return;
        }
        setCamStatus('');
        const detector = new window.BarcodeDetector({
          formats: ['ean_13', 'ean_8', 'upc_a', 'upc_e', 'code_128', 'code_39', 'qr_code'],
        });

        const tick = async () => {
          if (cancelled) return;
          try {
            if (videoRef.current?.readyState >= 2) {
              const found = await detector.detect(videoRef.current);
              if (found.length > 0 && found[0].rawValue) {
                onScanSku(found[0].rawValue);
                onClose();
                return;
              }
            }
          } catch {
            // ignore transient frame read errors
          }
          rafId = requestAnimationFrame(tick);
        };
        rafId = requestAnimationFrame(tick);
      } catch {
        setCamActive(false);
        setCamStatus('Camera permission denied or no webcam found. Use USB scanner or enter SKU below.');
      }
    }

    startCamera();
    return () => {
      cancelled = true;
      if (rafId) cancelAnimationFrame(rafId);
      if (stream) stream.getTracks().forEach(t => t.stop());
      setCamActive(false);
    };
  }, [isOpen, onScanSku, onClose]);

  const matches = useMemo(() => {
    const q = code.trim().toLowerCase();
    const list = q
      ? products.filter(p => p.sku?.toLowerCase().includes(q) || p.name?.toLowerCase().includes(q))
      : products.slice(0, 4);
    return list.slice(0, 5);
  }, [code, products]);

  if (!isOpen) return null;

  function handleSubmit(e) {
    e.preventDefault();
    if (!code.trim()) return;
    onScanSku(code.trim());
    setCode('');
  }

  return (
    <div className="scanner-backdrop" role="dialog" aria-modal="true" aria-label="Scan barcode">
      <div className="scanner-modal">
        <div className="scanner-head">
          <h3><Icon name="barcode" size={18} /> Scan Barcode / SKU</h3>
          <button type="button" className="scanner-close" onClick={onClose} aria-label="Close scanner">
            <Icon name="x" size={16} />
          </button>
        </div>

        <div className="scanner-body">
          <div className="scanner-video-box">
            <video ref={videoRef} muted playsInline style={{ display: camActive ? 'block' : 'none' }} />
            {camActive && !camStatus && <div className="scanner-reticle" />}
            {camStatus && <span style={{ position: 'relative', zIndex: 3 }}>{camStatus}</span>}
          </div>

          <form onSubmit={handleSubmit} className="scanner-manual-form">
            <input
              ref={inputRef}
              type="text"
              value={code}
              onChange={e => setCode(e.target.value)}
              placeholder="Scan with USB scanner or type SKU (e.g. NES-MILO-500)..."
              autoComplete="off"
            />
            <button type="submit">Add Item</button>
          </form>

          {matches.length > 0 && (
            <div className="scanner-suggestions">
              {matches.map(p => (
                <button
                  key={p.id}
                  type="button"
                  className="scanner-suggestion-item"
                  onClick={() => {
                    onScanSku(p.sku);
                    onClose();
                  }}
                >
                  <span><strong>{p.name}</strong> <small>({p.sku})</small></span>
                  <span>{formatMoney(p.sell_price)}</span>
                </button>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
