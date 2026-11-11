import Icon from '../ui/Icon';
import { formatCategory } from '../../utils/categories';
import { REPORT_TABS, RANGE_OPTIONS } from './reportOptions';
import '../../styles/reports.css';

export default function ReportsHeader({
  activeTab,
  onTabChange,
  activeRange,
  onRangeChange,
  categories = [],
  selectedCategory,
  onCategoryChange,
  searchQuery,
  onSearchChange,
  onExportCsv,
  onExportPdf,
}) {
  const currentTabInfo = REPORT_TABS.find(t => t.id === activeTab) || REPORT_TABS[0];

  return (
    <div className="reports-header-container">
      <header className="reports-header-readdy">
        <div className="reports-title-area">
          <span className="reports-badge-icon">
            <Icon name={currentTabInfo.icon} size={18} />
          </span>
          <div>
            <h2>{currentTabInfo.title}</h2>
            <p>{currentTabInfo.desc}</p>
          </div>
        </div>

        <div className="reports-actions-btns">
          <button type="button" className="btn-reports-action" onClick={onExportCsv}>
            <Icon name="download" size={13} />
            <span>Export CSV</span>
          </button>
          <button type="button" className="btn-reports-action" onClick={onExportPdf}>
            <Icon name="printer" size={13} />
            <span>Export PDF</span>
          </button>
        </div>
      </header>

      {/* Push-down Top Nav Tabs */}
      <div className="reports-tabs-bar">
        {REPORT_TABS.map(tab => (
          <button
            key={tab.id}
            type="button"
            className={`reports-sub-tab-btn ${activeTab === tab.id ? 'active' : ''}`}
            onClick={() => onTabChange(tab.id)}
          >
            <Icon name={tab.icon} size={14} />
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      {/* Universal Filter Toolbar */}
      <div className="reports-filter-toolbar">
        <div className="reports-search-box">
          <Icon name="search" size={14} />
          <input
            type="search"
            placeholder={`Search in ${currentTabInfo.label}...`}
            value={searchQuery}
            onChange={e => onSearchChange(e.target.value)}
            aria-label="Search report"
          />
        </div>

        <div className="reports-filter-right">
          {activeTab !== 'users' && categories.length > 0 && (
            <select
              value={selectedCategory}
              onChange={e => onCategoryChange(e.target.value)}
              className="reports-select-filter"
            >
              <option value="all">All Categories</option>
              {categories.filter(c => c !== 'all').map(c => (
                <option key={c} value={c}>
                  {formatCategory(c)}
                </option>
              ))}
            </select>
          )}

          <div className="reports-range-pills">
            {RANGE_OPTIONS.map(opt => (
              <button
                key={opt.id}
                type="button"
                className={`range-pill-btn ${activeRange === opt.id ? 'range-pill-btn--active' : ''}`}
                onClick={() => onRangeChange(opt.id)}
              >
                {opt.label}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
