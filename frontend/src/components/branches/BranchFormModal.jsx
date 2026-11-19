import { useEffect, useState } from 'react';
import Icon from '../ui/Icon';
import { humanizeErrorMessage } from '../../utils/errorMessage';
import '../../styles/products-modal.css';

function initialBranch(branch) {
  return {
    name: branch?.name || '',
    code: branch?.code || '',
    address: branch?.address || '',
    phone: branch?.phone || '',
    is_active: branch ? Boolean(branch.is_active) : true,
  };
}

export default function BranchFormModal({ branch, isOpen, onClose, onSave }) {
  const isEditing = Boolean(branch);
  const [form, setForm] = useState(() => initialBranch(branch));
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (isOpen) {
      setForm(initialBranch(branch));
      setError('');
    }
  }, [branch, isOpen]);

  if (!isOpen) return null;

  async function handleSubmit(e) {
    e.preventDefault();
    setError('');
    setSubmitting(true);
    try {
      await onSave(
        {
          name: form.name.trim(),
          code: form.code.trim().toUpperCase(),
          address: form.address.trim() || null,
          phone: form.phone.trim() || null,
          is_active: form.is_active,
        },
        branch?.id
      );
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
          <h3>{isEditing ? 'Edit branch' : 'Add branch'}</h3>
          <button type="button" className="product-modal-close" onClick={onClose} aria-label="Close modal">
            <Icon name="x" size={16} />
          </button>
        </div>

        {error && <div className="product-form-error" role="alert">{error}</div>}

        <form onSubmit={handleSubmit} className="product-form">
          <div className="form-row">
            <div className="form-group">
              <label htmlFor="branch-name">Branch name</label>
              <input
                id="branch-name"
                type="text"
                required
                value={form.name}
                onChange={e => setForm({ ...form, name: e.target.value })}
                placeholder="Lekki Phase 1 Branch"
              />
            </div>
            <div className="form-group">
              <label htmlFor="branch-code">Branch code</label>
              <input
                id="branch-code"
                type="text"
                required
                value={form.code}
                onChange={e => setForm({ ...form, code: e.target.value })}
                placeholder="BR-003"
              />
            </div>
          </div>

          <div className="form-group full-width">
            <label htmlFor="branch-address">Address</label>
            <input
              id="branch-address"
              type="text"
              value={form.address}
              onChange={e => setForm({ ...form, address: e.target.value })}
              placeholder="15 Admiralty Way, Lekki Phase 1, Lagos"
            />
          </div>

          <div className="form-row align-items-center">
            <div className="form-group">
              <label htmlFor="branch-phone">Phone number</label>
              <input
                id="branch-phone"
                type="text"
                value={form.phone}
                onChange={e => setForm({ ...form, phone: e.target.value })}
                placeholder="+234 800 000 0000"
              />
            </div>
            <div className="form-group">
              <label htmlFor="branch-status">Status</label>
              <select
                id="branch-status"
                value={form.is_active ? '1' : '0'}
                onChange={e => setForm({ ...form, is_active: e.target.value === '1' })}
              >
                <option value="1">Active</option>
                <option value="0">Inactive</option>
              </select>
            </div>
          </div>

          <div className="product-modal-actions">
            <button type="button" className="btn-modal-cancel" onClick={onClose} disabled={submitting}>
              Cancel
            </button>
            <button type="submit" className="btn-modal-save" disabled={submitting}>
              {submitting ? 'Saving...' : 'Save branch'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
