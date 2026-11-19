import { useState } from 'react';
import { toast } from 'react-toastify';
import Icon from '../../components/ui/Icon';
import BranchFormModal from '../../components/branches/BranchFormModal';
import useBranches from '../../hooks/useBranches';
import { createBranch, updateBranch, deleteBranch } from '../../services/branchApi';
import { humanizeErrorMessage } from '../../utils/errorMessage';
import '../../styles/branches.css';

export default function Branches({ onSessionExpired }) {
  const { branches, loading, reload } = useBranches();
  const [modalOpen, setModalOpen] = useState(false);
  const [editing, setEditing] = useState(null);

  async function handleSave(payload, id) {
    try {
      if (id) {
        await updateBranch(id, payload);
        toast.success('Branch updated successfully.');
      } else {
        await createBranch(payload);
        toast.success('Branch created successfully.');
      }
      reload();
    } catch (err) {
      if (err.status === 401) onSessionExpired?.();
      throw err;
    }
  }

  async function handleToggle(branch) {
    try {
      await updateBranch(branch.id, { is_active: !branch.is_active });
      toast.success(`Branch ${branch.is_active ? 'deactivated' : 'activated'}.`);
      reload();
    } catch (err) {
      if (err.status === 401) onSessionExpired?.();
      else toast.error(humanizeErrorMessage(err));
    }
  }

  async function handleDelete(branch) {
    if (!window.confirm(`Delete branch "${branch.name}"?`)) return;
    try {
      await deleteBranch(branch.id);
      toast.success('Branch deleted.');
      reload();
    } catch (err) {
      if (err.status === 401) onSessionExpired?.();
      else toast.error(humanizeErrorMessage(err));
    }
  }

  return (
    <div className="branches-page">
      <header className="branches-header">
        <div className="branches-title-wrap">
          <span className="branches-icon-badge">
            <Icon name="branches" size={20} />
          </span>
          <div>
            <h2>Branch Management</h2>
            <p>Create, edit, and manage retail store locations across your business.</p>
          </div>
        </div>
        <button
          type="button"
          className="btn-branch-add"
          onClick={() => {
            setEditing(null);
            setModalOpen(true);
          }}
        >
          <Icon name="plus" size={16} />
          <span>Add Branch</span>
        </button>
      </header>

      {loading ? (
        <div className="products-loading">Loading branches...</div>
      ) : (
        <div className="branches-grid">
          {branches.map(b => (
            <div key={b.id} className="branch-card">
              <div className="branch-card-top">
                <div>
                  <span className="branch-code">{b.code}</span>
                  <h3 className="branch-name">{b.name}</h3>
                </div>
                <span className={`branch-status branch-status--${b.is_active ? 'active' : 'inactive'}`}>
                  {b.is_active ? 'Active' : 'Inactive'}
                </span>
              </div>

              <div className="branch-meta">
                <span>{b.address || 'No address set'}</span>
                <span>{b.phone || 'No phone set'}</span>
              </div>

              <div className="branch-stats">
                <div className="branch-stat-item">
                  <strong>{b.products_count ?? 0}</strong>
                  <span>Products</span>
                </div>
                <div className="branch-stat-item">
                  <strong>{b.sales_count ?? 0}</strong>
                  <span>Sales</span>
                </div>
                <div className="branch-stat-item">
                  <strong>{b.users_count ?? 0}</strong>
                  <span>Staff</span>
                </div>
              </div>

              <div className="branch-actions">
                <button
                  type="button"
                  className="btn-branch-sm"
                  onClick={() => {
                    setEditing(b);
                    setModalOpen(true);
                  }}
                >
                  Edit
                </button>
                <button type="button" className="btn-branch-sm" onClick={() => handleToggle(b)}>
                  {b.is_active ? 'Deactivate' : 'Activate'}
                </button>
                <button
                  type="button"
                  className="btn-branch-sm btn-branch-sm--danger"
                  onClick={() => handleDelete(b)}
                >
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      <BranchFormModal
        branch={editing}
        isOpen={modalOpen}
        onClose={() => setModalOpen(false)}
        onSave={handleSave}
      />
    </div>
  );
}
