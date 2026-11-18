# Official Answer Key & Explanations — HCIA-openGauss V2.0 — National Stage Final Mock Exam

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Total Questions:** 60 (1000 Points)

---

### Q1 (Ch.01 openGauss Overview) — [15 pts]
- **Question:** (Official Ch.01 Quiz Q1) Which of the following is NOT a component of a database system (DBS)?
- **Correct Answer:** `D`
- **Explanation:** Per Chapter 01 (p. 9 & p. 67), a DBS consists of three logical parts: Database, DBMS, and Database application. Database storage medium is hardware, not one of the three DBS components.

### Q2 (Ch.01 openGauss Overview) — [15 pts]
- **Question:** (Official Ch.01 Quiz Q2) Which of the following statements about the ACID feature of database transactions is INCORRECT?
- **Correct Answer:** `C`
- **Explanation:** Per Chapter 01 (p. 22 & p. 67), 'I' in ACID stands for Isolation (concurrent transactions do not interfere with one another), NOT Availability.

### Q3 (Ch.01 openGauss Overview) — [15 pts]
- **Question:** According to the openGauss technical specifications (Ch.01 p. 57), what is the maximum number of partitions supported in a single partitioned table for Range partitioning versus Hash/List partitioning?
- **Correct Answer:** `B`
- **Explanation:** Per Chapter 01 (p. 57), a partitioned table in openGauss supports up to 32,768 partitions for range partitioning and 64 partitions for hash or list partitioning.

### Q4 (Ch.02 Database Installation and Deployment) — [15 pts]
- **Question:** (Official Ch.02 Quiz Q1) Which of the following is NOT an openGauss server tool?
- **Correct Answer:** `C`
- **Explanation:** Per Chapter 02 (p. 102 & p. 126), `gsql` is a Client tool used to connect to the database, whereas `gs_check`, `gs_guc`, and `gs_collector` are Server tools.

### Q5 (Ch.02 Database Installation and Deployment) — [15 pts]
- **Question:** (Official Ch.02 Quiz Q2) When the `gs_checkperf` tool is used to check system performance, which of the following can be viewed ONLY by user `root`?
- **Correct Answer:** `D`
- **Explanation:** Per Chapter 02 (p. 109, p. 110 & p. 126), SSD read/write performance (`gs_checkperf -U USER -i SSD`) can be viewed ONLY by user `root`.

### Q6 (Ch.02 Database Installation and Deployment) — [15 pts]
- **Question:** When using `gs_dump` to export a database, which `-F` (`--format`) option generates a binary archive with medium compression by default that is recommended for medium or large databases and restored using `gs_restore`?
- **Correct Answer:** `B`
- **Explanation:** Per Chapter 02 (p. 114), `-F c` (Custom) generates a binary archive with medium compression by default, is recommended for medium or large databases, and allows selective object restoration using `gs_restore`.

### Q7 (Ch.03 openGauss Architecture and Key Features) — [15 pts]
- **Question:** In the openGauss instance architecture, which background thread copies dirty pages to the double-writer space and flushes them to disk to prevent torn-page corruption before forwarding them to `bgwriter` subthreads?
- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (p. 138), `pagewriter` copies dirty page data to the double-writer space and flushes it to disk to prevent data page corruption, then forwards dirty pages to `bgwriter` subthreads.

### Q8 (Ch.03 openGauss Architecture and Key Features) — [15 pts]
- **Question:** In the openGauss Resource Pooling architecture, which component includes an independent server process (`DSS Server`) that directly manages raw devices of disk arrays and provides capabilities similar to distributed file systems?
- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (p. 147), DSS (Distributed Storage Service) includes DSS API and DSS Server (an independent process that directly manages raw devices of disk arrays).

### Q9 (Ch.03 openGauss Architecture and Key Features) — [15 pts]
- **Question:** In openGauss Dynamic Data Masking, which preset masking function displays `'4880-9898-4545-2525'` as `'xxxx-xxxx-xxxx-2525'` (masking all digits except the last four)?
- **Correct Answer:** `C`
- **Explanation:** Per Chapter 03 (p. 207), `creditcardmasking` masks all digits with `'x'` except the last four digits (`'xxxx-xxxx-xxxx-2525'`).

### Q10 (Ch.03 openGauss Architecture and Key Features) — [15 pts]
- **Question:** In openGauss Workload Diagnosis Report (WDR), what are the default values of `enable_wdr_snapshot`, `wdr_snapshot_interval`, and `wdr_snapshot_retention_days`?
- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (p. 230), `enable_wdr_snapshot` is `off` by default, `wdr_snapshot_interval` is 1 hour by default, and `wdr_snapshot_retention_days` is 8 days by default.

### Q11 (Ch.03 openGauss Architecture and Key Features) — [15 pts]
- **Question:** Which built-in openGauss function generates a single-query index recommendation (returning `table` and `column`) when passed a single `SELECT` statement string?
- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (pp. 255–257), `gs_index_advise('SELECT ...')` generates a recommended index (table name and column names) for a single `SELECT` query.

### Q12 (Ch.04 Database and Object Management) — [15 pts]
- **Question:** (Official Ch.04 Quiz Q2) Which of the following commands can be used to export partial data from the `student` table?
- **Correct Answer:** `C`
- **Explanation:** Per Chapter 04 (p. 332 & p. 346), `COPY (SELECT * FROM student WHERE ...) TO '...'` (a `copy` conditional statement) exports a query result set (partial table data).

### Q13 (Ch.04 Database and Object Management) — [15 pts]
- **Question:** Which system catalog in openGauss stores information about database authorization identifiers (roles and users, including `rolcanlogin`) across the entire cluster and is accessible only to system administrators?
- **Correct Answer:** `B`
- **Explanation:** Per Chapter 04 (p. 317 & p. 324), `PG_AUTHID` stores information about database authorization identifiers (roles/users, where a user is a role with `rolcanlogin` set) and is accessible only to system administrators.

### Q14 (Ch.05 SQL Basics) — [15 pts]
- **Question:** (Official Ch.05 Quiz p. 394 Q1) Which of the following logical expressions is used to search for records whose position is an engineer and salary is greater than 6000?
- **Correct Answer:** `D`
- **Explanation:** Per Chapter 05 (p. 381 & p. 394), character literals must be enclosed in single quotes (`'Engineer'`) and combined with `AND`.

### Q15 (Ch.05 SQL Basics) — [15 pts]
- **Question:** (Official Ch.05 Quiz p. 394 Q2) In a `WHERE` clause, the expression `age between 20 and 30` is equivalent to:
- **Correct Answer:** `A`
- **Explanation:** Per Chapter 05 (p. 394), `BETWEEN 20 AND 30` is inclusive of both 20 and 30 (`age >= 20 and age <= 30`).

### Q16 (Ch.05 SQL Basics) — [15 pts]
- **Question:** (Official Ch.05 Quiz p. 405 Q1) Which of the following SQL commands can be used to increase the value of the `AGE` column in the `STAFFS` table by five years?
- **Correct Answer:** `C`
- **Explanation:** Per Chapter 05 (p. 401 & p. 405), the standard `UPDATE` syntax is `UPDATE STAFFS SET AGE = AGE+5`.

### Q17 (Ch.05 SQL Basics) — [15 pts]
- **Question:** (Official Ch.05 Quiz p. 405 Q2) Which of the following four groups of SQL commands belong to the DML commands?
- **Correct Answer:** `B`
- **Explanation:** Per Chapter 05 (p. 359 & p. 405), `INSERT`, `UPDATE`, and `DELETE` are Data Manipulation Language (DML) commands.

### Q18 (Ch.05 SQL Basics) — [15 pts]
- **Question:** (Official Ch.05 Quiz p. 406 Q3) Which of the following SQL statements will delete records for all students whose class ID (specified by `cid`) is 6 from the `student` table?
- **Correct Answer:** `A`
- **Explanation:** Per Chapter 05 (p. 403 & p. 406), `delete FROM student where cid = 6;` is the valid SQL `DELETE` statement (never put `*` after `DELETE`, and use `WHERE` rather than `ON`).

### Q19 (Ch.05 SQL Basics) — [15 pts]
- **Question:** (Official Ch.05 Quiz p. 446 Q2) SQL integrates data query, data manipulation, data definition, and data control. Which of the following functions is implemented by the `CREATE`, `DROP`, and `ALTER` statements?
- **Correct Answer:** `C`
- **Explanation:** Per Chapter 05 (p. 408 & p. 446), `CREATE`, `DROP`, and `ALTER` implement Data Definition (DDL).

### Q20 (Ch.06 GaussDB) — [15 pts]
- **Question:** (Official Ch.06 Quiz Q1) In the GaussDB distributed architecture, which of the following components is used for sharing configuration and service discovery (service registration and search)?
- **Correct Answer:** `D`
- **Explanation:** Per Chapter 06 (p. 495 & p. 527), `ETCD` is used for sharing configurations and discovering services (service registration and search).

### Q21 (Ch.01 openGauss Overview) — [20 pts]
- **Question:** (Official Ch.01 Quiz Q3) Which of the following phases are involved in the development of data management technologies?
- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 01 (p. 10 & p. 68), data management technologies went through three stages: Manual management, File system, and DBS.

### Q22 (Ch.01 openGauss Overview) — [20 pts]
- **Question:** Which three significant common features are shared by all NewSQL database systems (`SQL + NoSQL = NewSQL`)?
- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 01 (p. 30), all NewSQL systems share three significant common features: they support the relational data model, use SQL as the main interface, and meet the features of a distributed database while preserving ACID transactions.

### Q23 (Ch.01 openGauss Overview) — [20 pts]
- **Question:** Which of the following are categories of execution plan nodes in the openGauss Execution Engine (Ch.01 pp. 53–54)?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Chapter 01 (pp. 53–54), the operators in the openGauss execution engine are classified into four types: Scan plan nodes, Control plan nodes, Materialize plan nodes, and Join plan nodes.

### Q24 (Ch.02 Database Installation and Deployment) — [20 pts]
- **Question:** (Official Ch.02 Quiz Q3) Which of the following are the prerequisites for installing openGauss on a single node?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Chapter 02 (p. 92 & p. 127), all four statements (ABCD) are required prerequisites for installing openGauss on a single node.

### Q25 (Ch.02 Database Installation and Deployment) — [20 pts]
- **Question:** Which of the following `HOSTTYPE` and `authentication-options` values are supported in `pg_hba.conf` when configuring client authentication via `gs_guc -h`?
- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 02 (p. 96 & p. 118), A, B, and C are true. Option D is false: remote hosts are NOT allowed to access openGauss if `trust` is configured.

### Q26 (Ch.02 Database Installation and Deployment) — [20 pts]
- **Question:** Which two parts are exported when `gs_dumpall` is used to export all databases in an openGauss cluster (Ch.02 p. 115)?
- **Correct Answer:** `AB`
- **Explanation:** Per Chapter 02 (p. 115), `gs_dumpall` exports all databases in two parts: (1) all global objects (users/groups, tablespaces, attributes) and (2) SQL scripts from each database by calling `gs_dump`. Both exported parts are plain-text SQL scripts restored using `gsql`.

### Q27 (Ch.03 openGauss Architecture and Key Features) — [20 pts]
- **Question:** (Official Ch.03 Quiz Q1) Which of the following are the openGauss deployment modes?
- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 03 Quiz Q1 (p. 268), openGauss supports single-node deployment, one primary and one standby, and one primary and multiple standbys (`ABC`). Dual primary nodes (`D`) is not supported.

### Q28 (Ch.03 openGauss Architecture and Key Features) — [20 pts]
- **Question:** Which three key components make up the Cost-Based Optimizer (CBO) in openGauss (Ch.03 p. 165)?
- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 03 (p. 165), a CBO consists of three key components: Query converter, Cost estimator, and Execution plan generator.

### Q29 (Ch.03 openGauss Architecture and Key Features) — [20 pts]
- **Question:** Which of the following are advantages of a partitioned table over an ordinary table in openGauss (Ch.03 p. 174 & Ch.05 p. 427)?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Chapter 03 (p. 174) and Chapter 05 (p. 427), partitioned tables provide all four advantages: high query efficiency, high availability, easy maintenance, and balanced I/O.

### Q30 (Ch.03 openGauss Architecture and Key Features) — [20 pts]
- **Question:** How does Symmetric Multi-Processing (SMP) parallel technology improve openGauss database performance on multi-core servers (Ch.03 pp. 187–188)?
- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 03 (pp. 187–188), A, B, and C are true. Option D is false: severe data skew or high system concurrency deteriorates SMP performance.

### Q31 (Ch.03 openGauss Architecture and Key Features) — [20 pts]
- **Question:** In openGauss Role-Based Access Control (RBAC), authorization defines relationships among which three core elements (Ch.03 p. 211)?
- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 03 (p. 211), RBAC authorization defines relationships among Who, What, and How.

### Q32 (Ch.03 openGauss Architecture and Key Features) — [20 pts]
- **Question:** Which system catalogs in openGauss store metadata related to Unified Auditing policies (Ch.03 p. 223)?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Chapter 03 (p. 223), the four system catalogs related to unified auditing are `GS_AUDITING_POLICY` (main info), `GS_AUDITING_POLICY_ACCESS` (DML), `GS_AUDITING_POLICY_FILTERS` (filters), and `GS_AUDITING_POLICY_PRIVILEGES` (DDL).

### Q33 (Ch.03 openGauss Architecture and Key Features) — [20 pts]
- **Question:** Which of the following are the three running modes of the `X-Tuner` parameter tuning tool in openGauss (Ch.03 p. 247)?
- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 03 (p. 247), X-Tuner runs in three modes: `recommend`, `train`, and `tune`.

### Q34 (Ch.04 Database and Object Management) — [20 pts]
- **Question:** (Official Ch.04 Quiz Q3) Which of the following statements about row-store tables and column-store tables are TRUE?
- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 04 Quiz Q3 (p. 347), A, B, and C are true (`ABC`). D is false because statistical analysis queries over large datasets are suited for column-store tables.

### Q35 (Ch.05 SQL Basics) — [20 pts]
- **Question:** (Official Ch.05 Quiz p. 395 Q3) Assume that you want to query student names, ages, and scores from the `student` table, and want the results sorted in descending order by age. If there are students of the same age, they are sorted in ascending order by score instead. Which of the following SQL statements can be used?
- **Correct Answer:** `AC`
- **Explanation:** Per Chapter 05 (p. 395), Option A (`order by age desc, score` where `score` defaults to `ASC`) and Option C (`order by 2 desc, 3 asc` referencing the 2nd and 3rd selected columns) are correct (`AC`).

### Q36 (Ch.05 SQL Basics) — [20 pts]
- **Question:** Which of the following `LIMIT` / `OFFSET` clauses in openGauss are equivalent and output 20 rows after skipping the first 5 rows (Ch.05 p. 392)?
- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 05 (p. 392), `LIMIT 5, 20` is equivalent to `LIMIT 20 OFFSET 5` and `OFFSET 5 LIMIT 20` — all three skip 5 rows and return 20 rows.

### Q37 (Ch.05 SQL Basics) — [20 pts]
- **Question:** (Official Ch.05 Quiz p. 447 Q3) Create a decremental sequence named `seq_1`. The starting value is 400, the step is –4, and the minimum value is 100. When the sequence reaches the minimum value, it can be cyclically executed. Which of the following statements are correct?
- **Correct Answer:** `BD`
- **Explanation:** Per Chapter 05 (p. 442 & p. 447), for a descending sequence (`INCREMENT BY -4`), default `MAXVALUE` is `-1` and default `START WITH` is `maxvalue`. Thus `MAXVALUE 400` must be specified, and `START WITH 400` is optional (`BD`).

### Q38 (Ch.05 SQL Basics) — [20 pts]
- **Question:** (Official Ch.05 Quiz p. 468 Q2) Which of the following are arithmetic functions in openGauss?
- **Correct Answer:** `BC`
- **Explanation:** Per Chapter 05 (p. 468), `sin(n)` and `round(v numeric, s int)` are arithmetic functions (`BC`), whereas `length(str)` and `hex(p1)` are string functions.

### Q39 (Ch.05 SQL Basics) — [20 pts]
- **Question:** (Official Ch.05 Quiz p. 469 Q3 & Q4) Which three separate approaches to pattern matching are provided by openGauss?
- **Correct Answer:** `ACD`
- **Explanation:** Per Chapter 05 (p. 469), the three pattern matching approaches are `LIKE`, `SIMILAR TO`, and `POSIX regular expressions` (`ACD`).

### Q40 (Ch.06 GaussDB) — [20 pts]
- **Question:** (Official Ch.06 Quiz Q2) Which of the following are core functions of UGO (Database and Application Migration UGO)?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Chapter 06 (p. 512 & p. 527), all six items listed across A, B, C, and D constitute the exact 6 core functions of UGO.

### Q41 (Ch.01 openGauss Overview) — [10 pts]
- **Question:** openGauss uses a single-process multi-threaded architecture (`gaussdb`) and incremental checkpoints (performance fluctuation < 5%), whereas PostgreSQL uses a multi-process architecture and full checkpoints (fluctuation > 15%).
- **Correct Answer:** `A`
- **Explanation:** True (Ch.01 pp. 48–49). openGauss uses a single-process multi-threaded model with 64-bit XIDs/CSNs and incremental checkpoints.

### Q42 (Ch.02 Database Installation and Deployment) — [10 pts]
- **Question:** Only user `root` is authorized to run the `gs_checkos` and `gs_postuninstall` commands in openGauss.
- **Correct Answer:** `A`
- **Explanation:** True (Ch.02 p. 107 & p. 125). Both `gs_checkos` and `gs_postuninstall` require `root` privileges.

### Q43 (Ch.03 openGauss Architecture and Key Features) — [10 pts]
- **Question:** When Ultimate RTO is enabled in openGauss (`recovery_parse_workers > 1` and `recovery_parallelism > 1`), cascaded standby nodes are fully supported.
- **Correct Answer:** `B`
- **Explanation:** False (Ch.03 p. 192). When Ultimate RTO is enabled, cascaded standby nodes are NOT supported because the standby node cannot synchronize data with a cascaded standby node during parallel recovery.

### Q44 (Ch.03 openGauss Architecture and Key Features) — [10 pts]
- **Question:** In openGauss Row-Level Security (RLS), initial users and system administrators (`SYSADMIN`) are not affected by row-level security policies.
- **Correct Answer:** `A`
- **Explanation:** True (Ch.03 p. 215). Initial users and system administrators bypass row-level security policies.

### Q45 (Ch.04 Database and Object Management) — [10 pts]
- **Question:** (Official Ch.04 Quiz Q1) Users and roles have the same syntax in the openGauss database. Therefore, they are fully equivalent.
- **Correct Answer:** `B`
- **Explanation:** False (Ch.04 p. 314 & p. 346). Users have the `LOGIN` attribute by default, whereas roles do not have login permission by default.

### Q46 (Ch.05 SQL Basics) — [10 pts]
- **Question:** (Official Ch.05 Quiz p. 372 Q1) `BIGINT` occupies four bytes.
- **Correct Answer:** `B`
- **Explanation:** False (Ch.05 p. 362 & p. 372). `BIGINT` (`INT8`) occupies eight (8) bytes.

### Q47 (Ch.05 SQL Basics) — [10 pts]
- **Question:** (Official Ch.05 Quiz p. 372 Q2) `CLOB` is used to store large object data of the `TEXT` type.
- **Correct Answer:** `A`
- **Explanation:** True (Ch.05 p. 366 & p. 372). `CLOB` is the alias of `TEXT` (up to 1 GB minus 1 byte) for storing large text data.

### Q48 (Ch.05 SQL Basics) — [10 pts]
- **Question:** (Official Ch.05 Quiz p. 446 Q1) When an index is created for a table, the corresponding base table is deleted if the index is canceled.
- **Correct Answer:** `B`
- **Explanation:** False (Ch.05 p. 446). Dropping an index (`DROP INDEX`) removes only the index and never deletes the base table.

### Q49 (Ch.05 SQL Basics) — [10 pts]
- **Question:** In openGauss, `CREATE DATABASE` and `DROP DATABASE` statements cannot be executed inside a transaction block, and the preinstalled `POSTGRES`, `TEMPLATE0`, and `TEMPLATE1` databases cannot be deleted.
- **Correct Answer:** `A`
- **Explanation:** True (Ch.05 p. 410 & p. 414). Neither `CREATE DATABASE` nor `DROP DATABASE` can run inside a transaction block, and the three preinstalled databases are protected.

### Q50 (Ch.06 GaussDB) — [10 pts]
- **Question:** In GaussDB Cloud Trace Service (CTS), operation records from the last seven days can be queried on the management console, and traces are regularly dumped to OBS buckets and encrypted using KMS keys.
- **Correct Answer:** `A`
- **Explanation:** True (Ch.06 p. 514). CTS allows querying the last 7 days of traces on the management console and dumps compressed trace files to OBS encrypted with KMS keys.

### Q51 (Ch.02 Database Installation and Deployment) — [20 pts]
- **Question:** Lab 1: Write the `gs_guc` command to dynamically add and immediately reload a client authentication rule in `pg_hba.conf` across all nodes (`-N all -I all`) allowing `host` access to `all` databases by user `testuser` from `10.252.95.191/32` using `sha256` authentication.
- **Correct Answer:** `gs_guc reload -N all -I all -h "host all testuser 10.252.95.191/32 sha256"`
- **Explanation:** Use `gs_guc reload` (which modifies `pg_hba.conf` and signals the database process to reload immediately) and specify `sha256` as the authentication method (Ch.02 p. 96 & p. 118).

### Q52 (Ch.02 Database Installation and Deployment) — [20 pts]
- **Question:** Lab 2: Write the command (executed as user `root`) to check SSD read/write performance using `gs_checkperf` for cluster user `omm`.
- **Correct Answer:** `gs_checkperf -U omm -i SSD`
- **Explanation:** Per Chapter 02 (p. 109 & Quiz Q2), SSD performance can only be viewed by `root` using `gs_checkperf -U omm -i SSD`.

### Q53 (Ch.03 openGauss Architecture and Key Features) — [20 pts]
- **Question:** Lab 3: Write the two commands (executed as user `omm` on the standby node) to perform a planned primary/standby switchover for data directory `/home/omm/cluster/dn1/` and then record the updated primary/standby roles in the dynamic configuration file.
- **Correct Answer:** `gs_ctl switchover -D /home/omm/cluster/dn1/
gs_om -t refreshconf`
- **Explanation:** Per Chapter 03 (pp. 192–193), run `gs_ctl switchover -D /home/omm/cluster/dn1/` on the standby node followed by `gs_om -t refreshconf`.

### Q54 (Ch.03 openGauss Architecture and Key Features) — [20 pts]
- **Question:** Lab 4: Write the SQL statements to create a resource label `label_for_creditcard` on column `user1.table1.creditcard` and create a dynamic data masking policy `msk_creditcard` using the `creditcardmasking` function.
- **Correct Answer:** `CREATE RESOURCE LABEL label_for_creditcard ADD COLUMN(user1.table1.creditcard);
CREATE MASKING POLICY msk_creditcard creditcardmasking ON LABEL(label_for_creditcard);`
- **Explanation:** Per Chapter 03 (p. 206), first create the resource label with `CREATE RESOURCE LABEL ... ADD COLUMN(...)`, then bind the masking policy with `CREATE MASKING POLICY msk_creditcard creditcardmasking ON LABEL(label_for_creditcard);`.

### Q55 (Ch.04 Database and Object Management) — [20 pts]
- **Question:** Lab 5: Write the SQL statements to create a column-store table `customer_t2(state_ID CHAR(2), state_NAME VARCHAR2(40), area_ID NUMBER)` and a Memory-Optimized Table (MOT) `mot_test(x INT)` on `mot_server`.
- **Correct Answer:** `CREATE TABLE customer_t2(state_ID CHAR(2), state_NAME VARCHAR2(40), area_ID NUMBER) WITH (ORIENTATION = COLUMN);
CREATE FOREIGN TABLE mot_test(x INT) SERVER mot_server;`
- **Explanation:** Per Chapter 04 (p. 299 & p. 305), column-store tables are declared with `WITH (ORIENTATION = COLUMN)` and MOTs are created with `CREATE FOREIGN TABLE ... SERVER mot_server;`.

### Q56 (Ch.04 Database and Object Management) — [20 pts]
- **Question:** Lab 6 (Official Ch.04 Quiz Q2): Write the SQL `COPY` statement to export partial data from table `t1` where `a2 = 1` to `/data/input/t1_output.txt` using delimiter `'^'`.
- **Correct Answer:** `COPY (SELECT * FROM t1 WHERE a2 = 1) TO '/data/input/t1_output.txt' DELIMITER '^';`
- **Explanation:** Per Chapter 04 (p. 332 & p. 346), `COPY (SELECT * FROM t1 WHERE a2 = 1) TO '/data/input/t1_output.txt' DELIMITER '^';` exports a filtered query result set to a file.

### Q57 (Ch.05 SQL Basics) — [20 pts]
- **Question:** Lab 7 (Official Ch.05 Quiz p. 405 Q1 & p. 406 Q3): Write the two DML statements to: (1) increase the `AGE` column in the `STAFFS` table by 5 years, and (2) delete all records from the `student` table where `cid = 6`.
- **Correct Answer:** `UPDATE STAFFS SET AGE = AGE + 5;
DELETE FROM student WHERE cid = 6;`
- **Explanation:** Per Chapter 05 (pp. 405–406), use `UPDATE STAFFS SET AGE = AGE + 5;` and `DELETE FROM student WHERE cid = 6;`.

### Q58 (Ch.05 SQL Basics) — [20 pts]
- **Question:** Lab 8 (Official Ch.05 Quiz p. 447 Q3): Write the SQL statement to create a decremental sequence named `seq_1` with starting value `400`, minimum value `100`, maximum value `400`, step `-4`, and cyclic execution.
- **Correct Answer:** `CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 MAXVALUE 400 INCREMENT BY -4 CYCLE;`
- **Explanation:** Per Chapter 05 (p. 447 Quiz Q3), a decremental sequence starting at 400 with step -4 and minimum 100 must specify `MAXVALUE 400` and `MINVALUE 100` (`CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 MAXVALUE 400 INCREMENT BY -4 CYCLE;`).

### Q59 (Ch.05 SQL Basics) — [20 pts]
- **Question:** Lab 9 (Official Ch.05 Quiz p. 468 Q1): Write the SQL query to add 7 days (`integer '7'`) to `date '2021-4-28'` aliased as `RESULT`, and include a SQL comment (`-- YYYY-MM-DD`) stating the resulting date.
- **Correct Answer:** `SELECT date '2021-4-28' + integer '7' AS RESULT;
-- Resulting date: 2021-05-05`
- **Explanation:** Per Chapter 05 (p. 459 & p. 468), `SELECT date '2021-4-28' + integer '7' AS RESULT;` adds 7 days to April 28, returning May 5 (`2021-05-05` / `2021-05-05 00:00:00`).

### Q60 (Ch.06 GaussDB) — [20 pts]
- **Question:** Lab 10 (Official Ch.06 Quiz Q1 & Q2): Complete the SQL query returning the GaussDB distributed component used for sharing configuration and service discovery, and the Huawei tool used for heterogeneous database structure and application SQL migration.
- **Correct Answer:** `SELECT 'ETCD' AS config_discovery_component, 'UGO' AS heterogeneous_migration_tool;`
- **Explanation:** Per Chapter 06 (p. 495, p. 512 & p. 527), `ETCD` is used for sharing configurations and service discovery, and `UGO` is used for heterogeneous database structure and application SQL migration.
