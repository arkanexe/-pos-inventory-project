import { ApiError, getAuthToken, saveAuth, clearAuth } from './authStorage';
export { ApiError, getAuthToken, getStoredUser, clearAuth } from './authStorage';

const API_BASE_URL = (
  import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api'
).replace(/\/$/, '');

async function readJson(response) {
  return response.json().catch(() => ({}));
}

export async function apiRequest(path, options = {}) {
  const token = getAuthToken();
  const headers = { Accept: 'application/json', ...options.headers };

  if (token) headers.Authorization = `Bearer ${token}`;
  if (options.body && !(options.body instanceof FormData) && !headers['Content-Type']) {
    headers['Content-Type'] = 'application/json';
  }

  const response = await fetch(`${API_BASE_URL}${path}`, { ...options, headers });
  const data = await readJson(response);

  if (response.status === 401) {
    clearAuth();
    throw new ApiError('Your session has expired. Please sign in again.', 401, data);
  }

  if (!response.ok) {
    const errorMsg = data.message || `Request failed (HTTP ${response.status}).`;
    throw new ApiError(errorMsg, response.status, data);
  }

  return data;
}

export async function loginUser(email, password) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 8000);

  try {
    const response = await fetch(`${API_BASE_URL}/login`, {
      method: 'POST',
      headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
      signal: controller.signal,
    });
    const data = await readJson(response);

    if (!response.ok) {
      if (response.status === 401) throw new ApiError('Invalid email or password.', 401, data);
      if (response.status === 403) {
        throw new ApiError(data.message || 'Your account is awaiting approval.', 403, data);
      }
      throw new ApiError(data.message || `Login failed (HTTP ${response.status}).`, response.status, data);
    }

    if (!data.token || !data.user) {
      throw new ApiError('Unexpected login response from server.', 200, data);
    }

    saveAuth(data.token, data.user);
    return data;
  } catch (err) {
    if (err.name === 'AbortError') {
      throw new ApiError(
        'Sign in timed out. The server took too long to respond. Please check that MySQL and the backend service are running.',
        408
      );
    }
    throw err;
  } finally {
    clearTimeout(timeoutId);
  }
}

export async function registerUser({ name, email, password, role = 'cashier' }) {
  const response = await fetch(`${API_BASE_URL}/register`, {
    method: 'POST',
    headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, email, password, password_confirmation: password, role }),
  });
  const data = await readJson(response);

  if (!response.ok) {
    const errorMsg = data?.errors ? Object.values(data.errors).flat()[0] : data?.message;
    throw new ApiError(errorMsg || 'Account creation failed.', response.status, data);
  }

  if (data.token && data.user) saveAuth(data.token, data.user);
  return data;
}

export async function getCurrentUser() {
  return apiRequest('/user');
}

export async function getDashboard(period = '7d', branchId) {
  const params = new URLSearchParams({ period });
  if (branchId && branchId !== 'all') params.set('branch_id', String(branchId));
  return apiRequest(`/dashboard?${params.toString()}`);
}

export async function getProducts(branchId) {
  const q = branchId && branchId !== 'all' ? `?branch_id=${encodeURIComponent(branchId)}` : '';
  const data = await apiRequest(`/products${q}`);
  return Array.isArray(data) ? data : data.products || [];
}

export async function createProduct(payload) {
  try {
    return await apiRequest('/products/create', { method: 'POST', body: JSON.stringify(payload) });
  } catch (error) {
    if (error instanceof ApiError && error.status === 422 && error.data?.errors) {
      const first = Object.values(error.data.errors).flat()[0];
      if (first) throw new ApiError(first, 422, error.data);
    }
    throw error;
  }
}

export async function updateProduct(id, payload) {
  try {
    return await apiRequest(`/products/${id}`, { method: 'PATCH', body: JSON.stringify(payload) });
  } catch (error) {
    if (error instanceof ApiError && error.status === 422 && error.data?.errors) {
      const first = Object.values(error.data.errors).flat()[0];
      if (first) throw new ApiError(first, 422, error.data);
    }
    throw error;
  }
}

export async function deactivateProduct(id) {
  return apiRequest(`/products/${id}`, { method: 'DELETE' });
}

export async function getStockAdjustments(branchId) {
  const q = branchId && branchId !== 'all' ? `?branch_id=${encodeURIComponent(branchId)}` : '';
  return apiRequest(`/stock-adjustments${q}`);
}

export async function adjustStock(productId, { type, quantity, reason }) {
  try {
    return await apiRequest(`/products/${productId}/stock-adjustments`, {
      method: 'POST',
      body: JSON.stringify({ type, quantity, reason }),
    });
  } catch (error) {
    if (error instanceof ApiError && error.status === 422 && error.data?.errors) {
      const first = Object.values(error.data.errors).flat()[0];
      if (first) throw new ApiError(first, 422, error.data);
    }
    throw error;
  }
}

export async function adjustStockBulk(items) {
  try {
    return await apiRequest('/stock-adjustments/bulk', {
      method: 'POST',
      body: JSON.stringify({ items }),
    });
  } catch (error) {
    if (error instanceof ApiError && error.status === 422 && error.data?.errors) {
      const first = Object.values(error.data.errors).flat()[0];
      if (first) throw new ApiError(first, 422, error.data);
    }
    throw error;
  }
}

export async function getSales({ branch_id, from, to, payment_method, product_id, page = 1, per_page, all } = {}) {
  const params = new URLSearchParams();
  if (branch_id && branch_id !== 'all') params.set('branch_id', String(branch_id));
  if (from) params.set('from', from);
  if (to) params.set('to', to);
  if (payment_method && payment_method !== 'all') params.set('payment_method', payment_method);
  if (product_id) params.set('product_id', String(product_id));
  if (all) {
    params.set('all', '1');
  } else {
    params.set('page', String(page));
    if (per_page) params.set('per_page', String(per_page));
  }
  return apiRequest(`/sales?${params.toString()}`);
}

export async function getSalesInRange({ branch_id, from, to } = {}) {
  const res = await getSales({ branch_id, from, to, all: true });
  const sales = Array.isArray(res.data) ? res.data : [];
  return {
    sales,
    total: Number(res.total) || sales.length,
    truncated: Number(res.total) > sales.length,
  };
}

export async function getSalesReport({ branch_id, from, to } = {}) {
  const params = new URLSearchParams();
  if (branch_id && branch_id !== 'all') params.set('branch_id', String(branch_id));
  if (from) params.set('from', from);
  if (to) params.set('to', to);
  const query = params.toString();
  return apiRequest(query ? `/reports/sales?${query}` : '/reports/sales');
}

export async function createSale({ branch_id, paymentMethod, items }) {
  try {
    const body = { payment_method: paymentMethod, items };
    if (branch_id && branch_id !== 'all') body.branch_id = Number(branch_id);
    const data = await apiRequest('/sales', {
      method: 'POST',
      body: JSON.stringify(body),
    });
    return data.sale;
  } catch (error) {
    if (error instanceof ApiError && error.status === 422 && error.data?.errors) {
      const first = Object.values(error.data.errors).flat()[0];
      if (first) throw new ApiError(first, 422, error.data);
    }
    throw error;
  }
}

export async function uploadProductImage(file) {
  const formData = new FormData();
  formData.append('image', file);
  return apiRequest('/products/upload-image', {
    method: 'POST',
    body: formData,
  });
}

export async function getStaff() {
  return apiRequest('/staff');
}

export async function updateStaffStatus(userId, payload) {
  return apiRequest(`/staff/${userId}/approve`, {
    method: 'PATCH',
    body: JSON.stringify(payload),
  });
}

export async function deleteStaffMember(userId) {
  return apiRequest(`/staff/${userId}`, {
    method: 'DELETE',
  });
}

export async function updateUserProfile({ name }) {
  return apiRequest('/user/profile', {
    method: 'PATCH',
    body: JSON.stringify({ name }),
  });
}

export async function resetPasswordWithCode({ email, code, password }) {
  const response = await fetch(`${API_BASE_URL}/reset-password-with-code`, {
    method: 'POST',
    headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, code, password }),
  });
  const data = await readJson(response);
  if (!response.ok) {
    const errorMsg = data?.errors ? Object.values(data.errors).flat()[0] : data?.message;
    throw new ApiError(errorMsg || 'Password reset failed.', response.status, data);
  }
  return data;
}

export async function changePassword({ current_password, new_password }) {
  return apiRequest('/user/change-password', {
    method: 'POST',
    body: JSON.stringify({ current_password, new_password }),
  });
}

export async function getStoreSettings() {
  const response = await fetch(`${API_BASE_URL}/store-settings`, {
    headers: { Accept: 'application/json' },
  });
  return readJson(response);
}

export async function updateStoreSettings(payload) {
  return apiRequest('/store-settings', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}
