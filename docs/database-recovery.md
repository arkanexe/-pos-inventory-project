# Database backup and recovery (MySQL / XAMPP)

The POS stores sales and stock changes in MySQL. A Git clone does not contain live store records. Back up the database separately and test a restore before relying on it.

## Backup

Run from a PowerShell terminal on the machine hosting MySQL. Replace the output path with a secured location outside the repository. The command prompts for the database password; do not put it on the command line.

```powershell
& 'C:\xampp\mysql\bin\mysqldump.exe' --host=127.0.0.1 --port=3306 --user=root --password --single-transaction --quick --routines --triggers --default-character-set=utf8mb4 --result-file='D:\secure-backups\cwg_retail_suite.sql' cwg_retail_suite
```

`--single-transaction` takes a consistent InnoDB snapshot without holding a long table lock. `--quick` streams rows instead of buffering the whole database. Keep dated copies in a protected location, restrict access to them, and store at least one copy off the POS machine. Set a schedule appropriate to how much sales data the business can afford to lose.

## Restore rehearsal

Restore into a **separate empty test database**, never over the live database without a recovery plan. Create `cwg_retail_suite_restore_test` first in MySQL or phpMyAdmin, then run:

```powershell
& 'C:\xampp\mysql\bin\mysql.exe' --host=127.0.0.1 --port=3306 --user=root --password --database=cwg_retail_suite_restore_test --execute="SOURCE D:/secure-backups/cwg_retail_suite.sql"
```

Compare counts of `sales`, `sale_items`, `products`, `inventories`, and `stock_adjustments` with the source database. Open the app against the test database and verify a recent receipt and product stock. Record the backup time, restore time, and elapsed recovery time. Test periodically; a backup file alone does not prove recovery works.

## Faster reads

The dashboard now uses `GET /api/dashboard?period=7d` or `30d`. Laravel calculates summaries in MySQL and returns only seven or thirty daily totals, five top products, six recent sales, and low-stock items. It no longer transfers hundreds of sales with every line item on a twelve-second poll. The endpoint refreshes on window focus and every sixty seconds. Sales history still uses pagination; avoid `all=1` for unbounded reporting.
