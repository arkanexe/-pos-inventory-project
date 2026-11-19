import { useState } from 'react';
import WelcomeSection from '../components/dashboard/WelcomeSection';
import MetricGrid from '../components/dashboard/MetricGrid';
import SalesTrendPanel from '../components/dashboard/SalesTrendPanel';
import LiveActivityPanel from '../components/dashboard/LiveActivityPanel';
import TopProductsPanel from '../components/dashboard/TopProductsPanel';
import LowStockPanel from '../components/dashboard/LowStockPanel';
import useDashboardData from '../hooks/useDashboardData';
import useBranches from '../hooks/useBranches';
import '../styles/dashboard-home.css';
import '../styles/dashboard-panels.css';

function DashboardHome({ user, onNavigate, onSessionExpired }) {
  const isOwner = user?.role === 'owner';
  const isManager = user?.role === 'manager';
  const canManageInventory = isOwner || isManager;
  const [period, setPeriod] = useState('7d');
  const [branchId, setBranchId] = useState('all');
  const { branches } = useBranches();
  const d = useDashboardData({ period, branchId, onSessionExpired });

  return (
    <div className="dash-home">
      {branches.length > 0 && (
        <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: '-8px' }}>
          <select
            value={branchId}
            onChange={e => setBranchId(e.target.value)}
            className="reports-select-filter"
            aria-label="Filter dashboard by branch"
          >
            <option value="all">All Branches</option>
            {branches.map(b => (
              <option key={b.id} value={String(b.id)}>{b.name} ({b.code})</option>
            ))}
          </select>
        </div>
      )}
      <WelcomeSection
        user={user}
        isOwner={isOwner || isManager}
        error={d.error}
        truncated={d.trend.truncated}
        onNavigate={onNavigate}
      />

      <MetricGrid
        loading={d.loading}
        isOwner={isOwner || isManager}
        todayMetrics={d.todayMetrics}
        lowStock={d.lowStock}
        salesError={d.salesError}
        productsError={d.productsError}
      />

      <section className="dash-middle" aria-label="Sales trend and activity">
        <SalesTrendPanel
          period={period}
          onPeriodChange={setPeriod}
          loading={d.loading}
          error={d.salesError}
          points={d.trend.points}
          totalRevenue={d.trend.totalRevenue}
          dailyAverage={d.trend.dailyAverage}
        />
        <LiveActivityPanel
          loading={d.loading}
          error={d.salesError && d.productsError ? d.error : ''}
          items={d.activity}
        />
      </section>

      <section className="dash-bottom" aria-label="Products and inventory">
        <TopProductsPanel
          items={d.topProducts}
          loading={d.loading}
          error={d.salesError}
          isOwner={isOwner || isManager}
          onNavigate={onNavigate}
        />
        <LowStockPanel
          items={d.lowStock}
          loading={d.loading}
          error={d.productsError}
          canManage={canManageInventory}
          onNavigate={onNavigate}
        />
      </section>
    </div>
  );
}

export default DashboardHome;
