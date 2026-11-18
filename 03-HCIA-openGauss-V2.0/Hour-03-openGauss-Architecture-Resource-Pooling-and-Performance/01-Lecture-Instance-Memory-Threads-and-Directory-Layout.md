# 📖 Instance Architecture — Memory, Multi-Threading & Directory Layout

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 03 — openGauss Architecture, Resource Pooling & High Performance (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-Memory-Threads-and-Data-Directory-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.03, pp. 135–144

---

## 🎯 Learning Objectives
- Distinguish Shared Memory (`shared_buffers`, `cstore_buffers`, `wal_buffers`, `MOT`) from Session/Local Memory (`work_mem`, `maintenance_work_mem`, `temp_buffers`)
- Describe the roles of core openGauss threads (`GaussMaster`, `pagewriter`, `bgwriter`, `walwriter`, `checkpointer`, `WalSender`, `WalReceiver`)
- Navigate the logical storage hierarchy (Tablespace -> Database -> Datafile Segment -> 8 KB Block) and physical data directory (`base`, `global`, `pg_xlog`, `pg_clog`, `pg_audit`)

---

### 1. Memory Structure: Shared vs. Local Memory (pp. 135–137)

| Memory Region | Scope | Purpose & Tuning Guidance |
| :--- | :--- | :--- |
| **`shared_buffers` (Shared buffer)** | Shared | Main memory cache bridging disk and CPU for row-store read/write operations. |
| **`cstore_buffers` (cstore buffer)** | Shared | Shared buffer dedicated to **column-store tables**. When using mostly column-store tables, reduce `shared_buffers` and increase `cstore_buffers`. |
| **`MOT` (Memory-Optimized Table)** | Shared / Local | Stores all MOT data and indexes in memory (`CREATE FOREIGN TABLE test(x int);`). Supports ACID with RC or RR isolation. |
| **`wal_buffers` (wal buffer)** | Shared | Shared memory staging area for Write-Ahead Logs (WALs) before flushing to disk. |
| **`maintenance_work_mem`** | Local (Session) | Local memory used for maintenance tasks: `VACUUM`, `CREATE INDEX`, and `ALTER TABLE`. |
| **`work_mem`** | Local (Session) | Local memory per query operator for **sorting (`Sort`)** and **hash tables (`HashJoin`/`HashAgg`)**. |
| **`temp_buffers` (temp buffer)** | Local (Session) | Session-private buffer for accessing **temporary tables**. |

---

### 2. Main Threads in `gaussdb` (pp. 135, 138)
- **`GaussMaster` (`postmaster`)**: Main management thread handling startup, shutdown, client connections, and message forwarding.
- **`pagewriter`**: Copies dirty pages to the **double-write (double-writer) space** and flushes them to disk (preventing torn-page corruption), then forwards dirty pages to `bgwriter` subthreads.
- **`bgwriter`**: Flushes dirty pages from `shared_buffers` to disk in the background so user query threads do not wait for free buffers and checkpoint spikes are smoothed.
- **`walwriter`**: Flushes WAL records from `wal_buffers` in memory to WAL files on disk to guarantee durability of committed transactions.
- **`checkpointer` (`checkpoint`)**: Periodically triggered to flush all dirty pages to disk and advance the recovery redo point.
- **Other Key Background Threads**: `WalSender` / `WalReceiver` (primary/standby WAL streaming), `AutoVacLauncher` (vacuuming), `Stat_collector` (statistics), `Auditor` (audit logs), `sysLogger` (run logs), `LWLockMonitor`.

---

### 3. Logical Architecture & Physical Directory Structure (pp. 141–144)
- **Logical Hierarchy**:
  - **Tablespace**: Physical directory mapping; one tablespace can store objects from multiple databases, and one database can span multiple tablespaces.
  - **Table & Datafile Segment**: Each table belongs to **only one database and one tablespace**. Each datafile segment belongs to only one table; **tables > 1 GB are split across multiple 1 GB datafile segments**.
  - **Block (Page)**: Basic unit of database I/O management; **default size is 8 KB**.
- **Physical Data Directory (`$GAUSSHOME/bin`, `lib`, `share`, and Instance Data Dir `0700`)**:
  - **`base/`**: Subdirectories for each database's tables/indexes.
  - **`global/`**: Cluster-wide system catalogs (e.g., `pg_database`, `pg_authid`, `pg_tablespace`).
  - **`pg_xlog/`**: Stores Write-Ahead Logs (WAL / redo logs).
  - **`pg_clog/` & `pg_csnlog/`**: Transaction commit status logs and Commit Sequence Number logs.
  - **`pg_audit/` & `pg_log/`**: Audit logs (`0600`) and instance run logs (`<= 0640`).
  - **`postgresql.conf` / `pg_hba.conf` / `postmaster.opts`**: Parameter file, client auth file, and startup CLI args.

---

## 🔑 Key Takeaways
- **In openGauss logical storage, a table exceeding 1 GB is split into multiple 1 GB datafile segments, and the default block size is 8 KB.**
- **`pagewriter` writes dirty pages to the double-writer space first to prevent torn-page corruption, while `walwriter` flushes WAL buffers to `pg_xlog`.**
- **`base/` holds per-database subdirectories, `global/` holds cluster-wide tables, `pg_xlog/` holds WAL files, and directory permissions are `0750` (program), `0700` (data dir), and `0600` (data/audit files).**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Column-store tables rarely use `shared_buffers`; they use `cstore_buffers`! For column-store workloads, decrease `shared_buffers` and increase `cstore_buffers` (Ch.03 p. 136).

> [!WARNING]
> EXAM TRAP: Do not confuse `pg_log` (instance runtime logs) with `pg_xlog` (Write-Ahead Logs / redo logs used for crash recovery) or `pg_clog` (transaction commit status logs).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Memory-Threads-and-Data-Directory-Lab.html`](./02-Exercise-Memory-Threads-and-Data-Directory-Lab.html)** (or [`02-Exercise-Memory-Threads-and-Data-Directory-Lab.md`](./02-Exercise-Memory-Threads-and-Data-Directory-Lab.md)) to apply this concept in an interactive lab workbench!
