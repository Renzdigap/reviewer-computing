# System Catalogs/Views & Data Import/Export (`COPY`, `gs_dump`, `gs_dumpall`, `gs_restore`, `ANALYZE`, `VACUUM`)

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 05 — Database & Object Management (MOT, Tablespaces, Users/Roles, Backup/Export) (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `08-Exercise-COPY-gs-dump-gs-restore-and-VACUUM-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.04, pp. 322–347

---

## Learning Objectives
- Identify key openGauss System Catalogs (`PG_CLASS`, `PG_ATTRIBUTE`, `PG_AUTHID`, `PG_DATABASE`, `PG_INDEX`, `PG_NAMESPACE`, `PG_PARTITION`) and Views (`PG_STAT_ACTIVITY`, `PG_SETTINGS`, `PG_LOCKS`)
- Export partial table data using `COPY (SELECT ...) TO` or `\copy` (Ch.04 Quiz Q2: C!)
- Execute `gs_dump`, `gs_dumpall`, `gs_restore` (`-c`, `-e`, `-s`), `VACUUM FULL`, and `ANALYZE`

---

### 1. Essential System Catalogs & System Views (pp. 323–328)

| System Catalog (`PG_*`) | Stored Metadata | System View | Displayed Information |
| :--- | :--- | :--- | :--- |
| **`PG_DATABASE`** | Available databases | **`PG_STAT_ACTIVITY`** | Current user sessions and running queries |
| **`PG_CLASS`** | Tables, indexes, views, sequences & relationships | **`PG_SETTINGS`** | Runtime GUC parameters of the database |
| **`PG_ATTRIBUTE`** | Table columns | **`PG_LOCKS`** | Locks held by open transactions |
| **`PG_AUTHID`** | Roles & users (`rolcanlogin`; `SYSADMIN` only) | **`PG_ROLES` / `PG_USER`** | Role and user information |
| **`PG_CONSTRAINT`** | Check, PK, Unique, and FK constraints | **`PG_STATS`** | Single-column statistics from `pg_statistic` |
| **`PG_INDEX`** | Index metadata (rest in `PG_CLASS`) | **`GS_SQL_COUNT`** | Counts of `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE INTO` |
| **`PG_NAMESPACE`** | Schemas (namespaces) | **`GS_AUDITING` / `GS_MASKING` / `GS_LABELS`** | Audit info, masking policies, and resource labels (`SYSADMIN`/`POLADMIN`) |
| **`PG_PARTITION`** | Partitioned tables, table partitions, index partitions | **`PLAN_TABLE`** | Session-level execution plan info from `EXPLAIN PLAN` |
| **`PG_DEPEND` / `PG_PROC` / `PG_JOB`** | Object dependencies (`CASCADE`/`RESTRICT`), functions/procedures, scheduled jobs | **`GS_WLM_USER_RESOURCE_HISTORY`** | Reserved catalog for user resource usage history |

---

### 2. Data Import & Export: `INSERT`, `COPY`, and `\copy` (pp. 330–333, Ch.04 Quiz Q2!)
1. **`INSERT`**: Simplest way to add data via client or JDBC/ODBC; suitable for **small data volume and low concurrency**.
2. **SQL `COPY` (`COPY FROM` / `COPY TO`, server-side file I/O) & JDBC `CopyManager` (`org.postgresql.copy.CopyManager`)**:
   - Applies **only to tables, NOT views**.
   - **Exporting Partial Table Data (Exact Ch.04 Quiz Q2: C!)**:
     ```sql
     COPY t1 FROM '/data/input/t1.txt' DELIMITER '^';
     COPY t1 TO '/data/input/t1_output.txt' DELIMITER '^';
     -- Export partial data using a conditional SELECT query:
     COPY (SELECT * FROM student WHERE age > 20) TO '/data/input/student_part.txt' DELIMITER '^';
     ```
3. **`gsql` `\copy` Meta-Command (Client-side file I/O, p. 333)**:
   - Unlike SQL `COPY` (which reads/writes files on the **database server**), `\copy` reads/writes files on the **local `gsql` client host** using the local OS user's file permissions!
   - Default delimiters: **Tab** in `TEXT` format, **Comma (`,`)** in `CSV` format, none in `FIXED` format.

---

### 3. `gs_dump`, `gs_dumpall`, `gs_restore`, `VACUUM FULL` & `ANALYZE` (pp. 334–345)
- **`gs_dump` Key Flags (p. 335)**:
  - `-U <user>`, `-W <pass>`, `-p <port>`, `-f <file>`, `-F p|c|d|t` (format), **`-n <schema>`** (include schema), **`-t <schema.table>`** (include table), **`-T <schema.table>`** (exclude table; if both `-t` and `-T` are given, exports objects in `-t` that are not in `-T`).
  - **Exporting without direct permission (p. 340)**: Use **`--role <rolename> --rolepassword <pass>`** to assume a role that has export privileges!
- **`gs_restore` Key Flags (pp. 341–343)**:
  - Imports `.tar` (`t`), custom (`c`), or directory (`d`) archives exported by `gs_dump`.
  - **`-d <dbname>`** (target DB), **`-c`** (clean/drop existing objects before recreating), **`-e`** (exit immediately on SQL error), **`-s`** (import **schema/object definitions only**, no data).
- **Post-Import Maintenance (pp. 344–345)**:
  - **`VACUUM FULL tablename;`**: Reclaims disk page fragments left by mass updates/deletions and **returns free space to the OS** (run **before** `ANALYZE`).
  - **`ANALYZE tablename;`**: Updates `PG_STATISTIC` so the CBO generates optimal query plans after data import.

---

## Key Takeaways
- **To export partial data from a table (e.g., rows matching a condition), use `COPY (SELECT ... WHERE ...) TO '/path/file'` (Ch.04 Quiz Q2: C). `gs_dump` and `gs_dumpall` export whole tables/databases, not conditional subsets.**
- **SQL `COPY` reads/writes files on the database server, whereas the `gsql` meta-command `\copy` reads/writes files on the local client machine.**
- **After bulk imports/updates/deletes, run `VACUUM FULL <table_name>;` (to reclaim disk page fragments to the OS) followed by `ANALYZE <table_name>;` (to update `PG_STATISTIC`).**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.04 Quiz Q2): 'Which of the following commands can be used to export partial data from the student table?' -> C. `copy` Conditional statement (`COPY (SELECT ...) TO ...`)!

> [!WARNING]
> EXAM TRAP: In `gs_restore`, `-s` imports ONLY object definitions (schemas/tables without data), `-c` drops existing objects before recreating them, and `-e` exits immediately if an error occurs.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-COPY-gs-dump-gs-restore-and-VACUUM-Lab.html`](./08-Exercise-COPY-gs-dump-gs-restore-and-VACUUM-Lab.html)** (or [`08-Exercise-COPY-gs-dump-gs-restore-and-VACUUM-Lab.md`](./08-Exercise-COPY-gs-dump-gs-restore-and-VACUUM-Lab.md)) to apply this concept in an interactive lab workbench!
