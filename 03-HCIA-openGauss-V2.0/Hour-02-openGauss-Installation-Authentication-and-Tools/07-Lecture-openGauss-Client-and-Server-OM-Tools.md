# 📖 openGauss Client & Server O&M Tools (`gsql`, `gs_check*`, `gs_dump*`, `gs_om`, `gs_ssh`)

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 02 — openGauss Installation, Authentication & O&M Tools (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `08-Exercise-Server-Inspection-and-Backup-Tools-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.02, pp. 101–126

---

## 🎯 Learning Objectives
- Distinguish openGauss Client Tools (`gsql`) from Server Tools (`gs_check`, `gs_checkos`, `gs_checkperf`, `gs_clean`, `gs_collector`, `gs_dump`, `gs_dumpall`, `gs_guc`, `gs_om`, `gs_restore`, `gs_ssh`)
- Identify which tool and check item require `root` privileges (`gs_checkos`, `gs_checkperf -i SSD`)
- Master the key options of `gs_check`, `gs_checkos`, `gs_checkperf`, `gs_clean`, `gs_collector`, `gs_dump`, `gs_dumpall`, `gs_restore`, `gs_om`, and `gs_ssh`

---

### 1. Client Tools vs. Server Tools Classification (pp. 102–104, Ch.02 Quiz Q1!)
All tools are located in `$GPHOME/script` and `$GAUSSHOME/bin`.
- **Client Tool (ONLY ONE in this table!)**:
  - **`gsql`**: CLI database connection tool used by clients to connect to the server, run interactive/scripted SQL statements, and execute meta-commands (`\l`, `\c`, `\dt`, `\d`, `\q`). **(`gsql` is NOT a server tool — exact Ch.02 Quiz Q1: C!)**
- **11 Server Tools (p. 104)**:
  1. **`gs_check`**: Comprehensive environment check (OS, network, DB runtime) before major operations. Must specify **`-i ITEM`** (single item, e.g., `-i CheckCPU`) or **`-e SCENE_NAME`** (scenario: `inspect`, `upgrade`, `binary_upgrade`, `health`, `install`). Use `--skip-root-items` to skip root checks.
  2. **`gs_checkos`**: Checks OS version, kernel parameters, disk/I/O/network settings, and THP. **Only `root` is authorized to run `gs_checkos`!**
     - `-i A1..A14`: **Checks** OS parameters without modifying them.
     - `-i B1..B8`: **Sets** OS parameters to expected values (A and B items cannot be used simultaneously; `-f` and `-h` cannot be used together).
  3. **`gs_checkperf`**: Routinely checks performance at 4 levels:
     - **openGauss level** (Host/GaussDB CPU usage, shared memory hit rate, in-memory sort ratio, I/O, disk, transaction stats) — run as `omm` (`-i PMK`). *Note*: If PMK statistics are missing, run `ANALYZE pmk.pmk_snapshot;` etc.
     - **Host level** (CPU, memory, I/O usage) — run as `omm`.
     - **Session/Process level** (CPU, memory, shared buffer hits) — run as `omm`.
     - **SSD performance** (read every 7s / write every 10s via `dd flag=direct bs=8M count=2560`) — **Can be viewed ONLY by user `root` (`gs_checkperf -U omm -i SSD`)! (Exact Ch.02 Quiz Q2: D!)**
  4. **`gs_clean`**: Connects to the primary DN and clears residual temporary tables (`-a`/`--all`, `-e`/`--exclusive`) or rolls back abnormal two-phase transactions (`-r`/`--rollback`) after an unexpected crash. Default concurrency `-j` is 3 (range 1–10).
  5. **`gs_collector`**: Collects OS info, logs, and config files (`--begin-time`, `--end-time`, `--keyword`, `-C CONFIGFILE`) into a `.tar.gz` package when openGauss is faulty (depends on `gstack`).
  6. **`gs_dump`**: Exports a **single database** or its objects (schemas, tables, views) consistently without blocking user R/W (acquires shared lock; tune wait via `--lock-wait-timeout`). Supports 4 formats via **`-F`**:
     - **`p` (Plain-text SQL)**: Restore with **`gsql`** (recommended for small DBs).
     - **`c` (Custom binary)**: Medium compression by default; restore with **`gs_restore`** (recommended for medium/large DBs).
     - **`d` (Directory)** & **`t` (`.tar` archive, max 8 GB per table)**: Restore with **`gs_restore`**.
  7. **`gs_dumpall`**: Exports **all databases** in the cluster + **global objects** (roles/users, tablespaces, global permissions) as a **plain-text SQL script** (restore with **`gsql`**).
  8. **`gs_guc`**: Modifies `postgresql.conf` / `pg_hba.conf` (`check`, `set`, `reload`, `encrypt -M server|client|source` generating `.key.cipher` and `.key.rand`).
  9. **`gs_om`**: Cluster lifecycle & config maintenance (`-t start | stop | restart | status | generateconf | refreshconf | view | query | cert | kerberos`).
  10. **`gs_restore`**: Imports custom (`c`), directory (`d`), or `.tar` (`t`) archives exported by `gs_dump`. Imports incrementally by default; use **`-c`** to clean/drop existing objects before recreating.
  11. **`gs_ssh`**: Runs the same Linux shell command synchronously across all cluster nodes (`gs_ssh -c "cmd"`).

---

## 🔑 Key Takeaways
- **`gsql` is a Client tool, NOT a Server tool (Ch.02 Quiz Q1).**
- **When using `gs_checkperf`, SSD performance (`-i SSD`) can be viewed ONLY by user `root` (Ch.02 Quiz Q2). Similarly, `gs_checkos` can only be run by `root`.**
- **`gs_dump` supports 4 formats (`p` plain-text restored via `gsql`; `c` custom, `d` directory, and `t` tar restored via `gs_restore`), whereas `gs_dumpall` exports only plain-text SQL scripts of all databases and global objects.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.02 Quiz Q1): 'Which of the following is not an openGauss server tool?' -> C. `gsql` (`gsql` is a client tool!).

> [!WARNING]
> EXAM TRAP (Ch.02 Quiz Q2): 'When the `gs_checkperf` tool is used to check system performance, which of the following can be viewed only by user `root`?' -> D. SSD performance!

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-Server-Inspection-and-Backup-Tools-Lab.html`](./08-Exercise-Server-Inspection-and-Backup-Tools-Lab.html)** (or [`08-Exercise-Server-Inspection-and-Backup-Tools-Lab.md`](./08-Exercise-Server-Inspection-and-Backup-Tools-Lab.md)) to apply this concept in an interactive lab workbench!
