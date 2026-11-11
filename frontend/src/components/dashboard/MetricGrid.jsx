import MetricCard from './MetricCard';
import { formatMoney } from '../../utils/dashboardStats';

/** MetricGrid — the row of four KPI cards at the top of the dashboard. */
function MetricGrid({ loading, isOwner, todayMetrics, lowStock, salesError, productsError }) {
  const showSales = value => (loading || salesError ? '—' : value);
  const showStock = value => (loading || productsError ? '—' : value);
  const outCount = lowStock.filter(item => item.status === 'out').length;

  return (
    <section className="dash-metrics" aria-label="Store KPIs" aria-busy={loading}>
      <MetricCard
        label="Today's Sales"
        value={showSales(formatMoney(todayMetrics.revenue))}
        sub={isOwner ? 'All cashiers, today' : 'Your sales today'}
        icon="money"
        tone="green"
      />
      <MetricCard
        label="Transactions"
        value={showSales(String(todayMetrics.count))}
        sub="Completed sales today"
        icon="basket"
        tone="amber"
      />
      <MetricCard
        label="Avg. Basket"
        value={showSales(formatMoney(todayMetrics.average))}
        sub="Per completed sale"
        icon="sales"
        tone="violet"
      />
      <MetricCard
        label="Low Stock Alerts"
        value={showStock(String(lowStock.length))}
        sub={productsError ? 'Could not load inventory' : `${outCount} out of stock`}
        icon="alert"
        tone="rose"
      />
    </section>
  );
}

export default MetricGrid;
