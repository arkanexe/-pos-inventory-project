import { useEffect, useState } from 'react';
import { ApiError, getDashboard } from '../services/api';
import {
  buildActivity,
  buildDashboardChartPoints,
  formatMoney,
} from '../utils/dashboardStats';

const EMPTY_STATE = {
  todayMetrics: { revenue: 0, count: 0, average: 0 },
  trend: { totalRevenue: 0, dailyAverage: 0, points: [], truncated: false },
  activity: [],
  topProducts: [],
  lowStock: [],
  error: '',
  salesError: '',
  productsError: '',
};

export default function useDashboardData({ period, branchId = 'all', onSessionExpired }) {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(EMPTY_STATE);

  useEffect(() => {
    let cancelled = false;

    async function load(silent = false) {
      if (!silent) setLoading(true);

      try {
        const response = await getDashboard(period, branchId);
        if (cancelled) return;

        const lowStock = response.low_stock.map(product => ({
          id: product.id,
          name: product.name,
          qty: Number(product.quantity),
          reorder: Number(product.reorder_threshold),
          status: Number(product.quantity) <= 0 ? 'out' : 'low',
        }));
        const points = buildDashboardChartPoints(
          response.daily_sales,
          response.period.from,
          response.period.to
        );
        const totalRevenue = points.reduce((sum, point) => sum + point.value, 0);

        setData({
          todayMetrics: response.today,
          trend: {
            totalRevenue,
            dailyAverage: totalRevenue / response.period.days,
            points,
            truncated: false,
          },
          activity: buildActivity({ sales: response.recent_sales, lowStock }),
          topProducts: response.top_products.map((product, index) => ({
            id: product.product_id,
            name: product.name || `Product #${product.product_id}`,
            sku: product.sku || '—',
            units: Number(product.units),
            rank: index + 1,
            amount: formatMoney(product.revenue),
          })),
          lowStock,
          error: '',
          salesError: '',
          productsError: '',
        });
      } catch (error) {
        if (cancelled) return;
        if (error instanceof ApiError && error.status === 401) {
          onSessionExpired?.();
          return;
        }
        const message = error.message || 'Could not load dashboard data.';
        setData(previous => ({
          ...previous,
          error: message,
          salesError: message,
          productsError: message,
        }));
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    function handleFocus() {
      load(true);
    }

    load();
    const intervalId = setInterval(() => load(true), 60000);
    window.addEventListener('focus', handleFocus);

    return () => {
      cancelled = true;
      clearInterval(intervalId);
      window.removeEventListener('focus', handleFocus);
    };
  }, [onSessionExpired, period, branchId]);

  return { loading, ...data };
}
