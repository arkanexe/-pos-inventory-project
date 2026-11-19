import { ApiError, apiRequest } from './api';

export async function getBranches({ active = false } = {}) {
  const path = active ? '/branches?active=1' : '/branches';
  const data = await apiRequest(path);
  return Array.isArray(data) ? data : [];
}

function extractValidationError(error) {
  if (error instanceof ApiError && error.status === 422 && error.data?.errors) {
    const first = Object.values(error.data.errors).flat()[0];
    if (first) throw new ApiError(first, 422, error.data);
  }
  throw error;
}

export async function createBranch(payload) {
  try {
    return await apiRequest('/branches', { method: 'POST', body: JSON.stringify(payload) });
  } catch (error) {
    extractValidationError(error);
  }
}

export async function updateBranch(id, payload) {
  try {
    return await apiRequest(`/branches/${id}`, { method: 'PATCH', body: JSON.stringify(payload) });
  } catch (error) {
    extractValidationError(error);
  }
}

export async function deleteBranch(id) {
  return apiRequest(`/branches/${id}`, { method: 'DELETE' });
}
