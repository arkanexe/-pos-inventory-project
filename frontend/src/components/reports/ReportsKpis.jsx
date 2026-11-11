import Icon from '../ui/Icon';

export default function ReportsKpis({ kpis }) {
  const {
    revenue = 0,
    grossProfit = null,
    transactions = 0,
    averageBasket = 0,
    unitsSold = 0,
  } = kpis || {};

  const unitsPerTxn = transactions > 0 ? (unitsSold / transactions).toFixed(1) : '0.0';

  return (
    <div className="reports-kpi-grid">
      <div className="reports-kpi-card">
        <div className="reports-kpi-header">
          <span className="reports-kpi-label">REVENUE</span>
          <div className="reports-kpi-icon-wrap reports-kpi-icon-wrap--green">
            <Icon name="pos" size={16} />
          </div>
        </div>
        <div className="reports-kpi-value">
          ₦{Number(revenue).toLocaleString()}
        </div>
      </div>

      <div className="reports-kpi-card">
        <div className="reports-kpi-header">
          <span className="reports-kpi-label">GROSS PROFIT</span>
          <div className="reports-kpi-icon-wrap reports-kpi-icon-wrap--amber">
            <Icon name="reports" size={16} />
          </div>
        </div>
        <div className="reports-kpi-value">
          {grossProfit === null ? '—' : `₦${Number(grossProfit).toLocaleString()}`}
        </div>
        <div className="reports-kpi-badge reports-kpi-badge--amber">
          <span>Historical unit costs are not recorded</span>
        </div>
      </div>

      <div className="reports-kpi-card">
        <div className="reports-kpi-header">
          <span className="reports-kpi-label">TRANSACTIONS</span>
          <div className="reports-kpi-icon-wrap reports-kpi-icon-wrap--gray">
            <Icon name="receipt" size={16} />
          </div>
        </div>
        <div className="reports-kpi-value">{transactions}</div>
        <div className="reports-kpi-badge reports-kpi-badge--gray">
          <span>₦{Number(averageBasket).toLocaleString()} avg basket</span>
        </div>
      </div>

      <div className="reports-kpi-card">
        <div className="reports-kpi-header">
          <span className="reports-kpi-label">UNITS SOLD</span>
          <div className="reports-kpi-icon-wrap reports-kpi-icon-wrap--gray">
            <Icon name="inventory" size={16} />
          </div>
        </div>
        <div className="reports-kpi-value">{unitsSold}</div>
        <div className="reports-kpi-badge reports-kpi-badge--gray">
          <span>{unitsPerTxn} items / txn</span>
        </div>
      </div>
    </div>
  );
}
