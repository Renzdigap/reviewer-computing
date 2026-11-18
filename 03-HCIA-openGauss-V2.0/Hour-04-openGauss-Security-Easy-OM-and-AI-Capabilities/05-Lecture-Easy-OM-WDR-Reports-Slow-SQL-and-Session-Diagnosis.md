# 📖 Easy Maintenance — WDR Reports, One-Click Log Collection, Slow SQL & Session Diagnosis

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 04 — openGauss High Security, Easy O&M & AI Capabilities (DBMind) (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-WDR-Snapshot-and-Session-Diagnosis-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.03, pp. 227–242

---

## 🎯 Learning Objectives
- Enable and generate Workload Diagnosis Reports (WDR) using `enable_wdr_snapshot`, `create_wdr_snapshot()`, and `generate_wdr_report()`
- Distinguish WDR Summary vs. Detail report sections and configure Slow SQL diagnosis (`log_min_duration_statement`, `track_stmt_stat_level`, `statement_history`)
- Diagnose blocked sessions and top wait events using `pg_thread_wait_status` and `DBE_PERF.local_active_session`

---

### 1. Workload Diagnosis Report (WDR, pp. 228–233)
WDR compares performance data between **two snapshots (`>= 2` snapshots required)** to diagnose long-term kernel performance bottlenecks:
- **Key GUC Parameters (p. 230)**:
  - **`enable_wdr_snapshot`**: Default is **`off`** (must be set to **`on`**).
  - **`wdr_snapshot_interval`**: Automatic background snapshot interval; default is **1 hour**.
  - **`wdr_snapshot_retention_days`**: Snapshot retention period; default is **8 days**.
- **Generating a WDR HTML Report (pp. 230–231)**:
  ```sql
  SELECT * FROM snapshot.snapshot;          -- View existing snapshot IDs
  SELECT create_wdr_snapshot();             -- Manually create a snapshot (sysadmin only)
  \a \t \o /home/om/wdrTestNode.html        -- Unaligned, tuples-only, redirect output to file
  SELECT generate_wdr_report(1, 2, 'all', 'node', 'dn_6001_6002');
  \o \a \t                                  -- Close output file & restore formatting
  ```
  - `report_type`: `'summary'`, `'detail'`, or `'all'`; `report_scope`: `'cluster'` or `'node'`.
- **Summary vs. Detail Report Contents (pp. 232–233)**:
  - **Summary Report**: `Database Stat`, `Load Profile` (incl. SQL P85/P90 response time), `Instance Efficiency Percentages` (cache hit ratio), `Events`, `Wait Classes` (`STATUS`, `LWLOCK_EVENT`, `LOCK_EVENT`, `IO_EVENT`), `CPU`, `I/O Profile`, `Memory Statistics`.
  - **Detail Report**: `Time Model`, `SQL Statistics`, `Wait Events`, `Cache I/O Stats`, `Utility status`, `Object stats`, `Configuration settings`.

---

### 2. One-Click Collection & Slow SQL Diagnosis (pp. 234–238)
- **One-Click Diagnosis Collection**: Extracts OS info, system catalogs/views, run/cluster logs, config files, core dumps, stack/trace info, and redo logs (xlogs) for rapid fault demarcation.
- **Slow SQL Diagnosis (v3.1.0+, pp. 236–238)**:
  - Records SQL jobs whose execution time exceeds **`log_min_duration_statement`**, controlled by **`track_stmt_stat_level`** (default `'OFF,L0'` — part 1 is Full SQL, part 2 is Slow SQL).
  - **Primary vs. Standby Querying**:
    - On the **Primary node**, query the **`statement_history`** table (must be queried inside the **`postgres`** database; empty in other DBs) or `DBE_PERF.get_global_full_sql_by_timestamp(start_ts, end_ts)`.
    - On the **Standby node** (which cannot write to tables), query the function **`dbe_perf.standby_statement_history`** inside the **`postgres`** database (memory/disk bounded by `track_stmt_standby_chain_size`).
    - Decode the binary `details` column via `pg_catalog.statement_detail_decode(details, 'plaintext', true)`. Sensitive query parameters in plans are automatically masked (`Filter: (name = '***'::text)`).

---

### 3. Active Session Performance Diagnosis (pp. 239–242)
Samples active sessions at 2 levels: **Level 1 (in-memory real-time, last few minutes)** and **Level 2 (persistent disk history)**:
```sql
-- 1. Check session blocking relationships
SELECT sessionid, block_sessionid FROM pg_thread_wait_status;
-- 2. Check blocked session and final blocker in active session samples
SELECT sessionid, block_sessionid, final_block_sessionid FROM DBE_PERF.local_active_session;
```

---

## 🔑 Key Takeaways
- **Generating a WDR report requires `enable_wdr_snapshot = on` (default `off`) and at least 2 snapshots (`create_wdr_snapshot()` can only be run by `sysadmin`). Default interval is 1 hour and retention is 8 days.**
- **Slow SQL diagnosis records queries exceeding `log_min_duration_statement` (controlled by `track_stmt_stat_level`, default `'OFF,L0'`), and `statement_history` / `dbe_perf.standby_statement_history` must be queried in the `postgres` database.**
- **Session blocking relationships are inspected via `pg_thread_wait_status` and `DBE_PERF.local_active_session`.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: If you query `statement_history` (or `dbe_perf.standby_statement_history` on a standby node) in any database other than `postgres`, the result is empty or unavailable (Ch.03 p. 238)!

> [!WARNING]
> EXAM TRAP: `enable_wdr_snapshot` is `off` by default, and at least 2 snapshots must exist before `generate_wdr_report()` can generate a report.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-WDR-Snapshot-and-Session-Diagnosis-Lab.html`](./06-Exercise-WDR-Snapshot-and-Session-Diagnosis-Lab.html)** (or [`06-Exercise-WDR-Snapshot-and-Session-Diagnosis-Lab.md`](./06-Exercise-WDR-Snapshot-and-Session-Diagnosis-Lab.md)) to apply this concept in an interactive lab workbench!
