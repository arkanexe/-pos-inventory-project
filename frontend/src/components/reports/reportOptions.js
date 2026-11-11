export const REPORT_TABS = [
  { id: 'sales', label: 'Sales Report', icon: 'sales', title: 'Financial & Sales Analysis', desc: 'Comprehensive breakdown of sales performance, revenue and payment methods.' },
  { id: 'inventory', label: 'Inventory Report', icon: 'inventory', title: 'Inventory Valuation & Margins', desc: 'Detailed stock asset valuation, cost vs sell prices, and profit margins.' },
  { id: 'stock', label: 'Stock Level Report', icon: 'alert', title: 'Stock Health & Reorder Deficits', desc: 'Monitors low stock alerts, stockout warnings, and reorder urgency.' },
  { id: 'products', label: 'Product Report', icon: 'products', title: 'Product Velocity & Performance', desc: 'Sales velocity, units sold per product, and catalog contribution.' },
  { id: 'users', label: 'User Report', icon: 'users', title: 'Staff & Cashier Audit', desc: 'Cashier checkout statistics, revenue generated, and payment collections.' },
];

export const RANGE_OPTIONS = [
  { id: '7d', label: '7 days', days: 7 },
  { id: '30d', label: '30 days', days: 30 },
  { id: '90d', label: '90 days', days: 90 },
  { id: 'all', label: 'All time', days: 365 },
];
