# HCIA-openGauss V2.0 — National Stage Final Mock Exam

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Time Limit:** 60 Minutes  
**Total Score:** 1000 Points (Passing / National Finalist Target: 800 Points)  
**Instructions:** 60 Questions in 60 Minutes: 20 Single-Choice (15 pts each), 20 Multiple-Choice (20 pts each, strict all-or-nothing grading), 10 True/False (10 pts each), and 10 Hands-On Command/SQL/Scenario Fill-in Labs (20 pts each).

> **Interactive Timed Mode:** Open **[`Final-Mock-Exam.html`](./Final-Mock-Exam.html)** in your browser for a realistic 60-minute countdown timer, question navigator palette, strict Huawei multi-choice auto-grading, and chapter-by-chapter analytics!

---

### Q1. [Single-Choice — 15 pts] (Ch.01 openGauss Overview)
**(Official Ch.01 Quiz Q1) Which of the following is NOT a component of a database system (DBS)?**

- [ ] A. Database
- [ ] B. DBMS
- [ ] C. Database application
- [ ] D. Database storage medium

### Q2. [Single-Choice — 15 pts] (Ch.01 openGauss Overview)
**(Official Ch.01 Quiz Q2) Which of the following statements about the ACID feature of database transactions is INCORRECT?**

- [ ] A. A indicates atomicity, whereby operations in a transaction are either all successful or all failed.
- [ ] B. C refers to consistency, whereby the system status can only be the status before the transaction or after the transaction is successful. No inconsistent intermediate status can occur.
- [ ] C. I refers to availability, whereby the database system must provide the highest availability possible for transaction execution in order to ensure as many successfully executed transactions as possible.
- [ ] D. D refers to durability, whereby the status of a successful transaction can be maintained, even if the machine is powered off.

### Q3. [Single-Choice — 15 pts] (Ch.01 openGauss Overview)
**According to the openGauss technical specifications (Ch.01 p. 57), what is the maximum number of partitions supported in a single partitioned table for Range partitioning versus Hash/List partitioning?**

- [ ] A. 1,024 (Range) / 32 (Hash or List)
- [ ] B. 32,768 (Range) / 64 (Hash or List)
- [ ] C. 65,536 (Range) / 256 (Hash or List)
- [ ] D. Unlimited (Range) / 1,024 (Hash or List)

### Q4. [Single-Choice — 15 pts] (Ch.02 Database Installation and Deployment)
**(Official Ch.02 Quiz Q1) Which of the following is NOT an openGauss server tool?**

- [ ] A. gs_check
- [ ] B. gs_guc
- [ ] C. gsql
- [ ] D. gs_collector

### Q5. [Single-Choice — 15 pts] (Ch.02 Database Installation and Deployment)
**(Official Ch.02 Quiz Q2) When the `gs_checkperf` tool is used to check system performance, which of the following can be viewed ONLY by user `root`?**

- [ ] A. openGauss level
- [ ] B. Host level
- [ ] C. Session/Process level
- [ ] D. SSD performance

### Q6. [Single-Choice — 15 pts] (Ch.02 Database Installation and Deployment)
**When using `gs_dump` to export a database, which `-F` (`--format`) option generates a binary archive with medium compression by default that is recommended for medium or large databases and restored using `gs_restore`?**

- [ ] A. p (Plain-text)
- [ ] B. c (Custom)
- [ ] C. d (Directory)
- [ ] D. t (.tar)

### Q7. [Single-Choice — 15 pts] (Ch.03 openGauss Architecture and Key Features)
**In the openGauss instance architecture, which background thread copies dirty pages to the double-writer space and flushes them to disk to prevent torn-page corruption before forwarding them to `bgwriter` subthreads?**

- [ ] A. walwriter
- [ ] B. pagewriter
- [ ] C. GaussMaster
- [ ] D. Stat_collector

### Q8. [Single-Choice — 15 pts] (Ch.03 openGauss Architecture and Key Features)
**In the openGauss Resource Pooling architecture, which component includes an independent server process (`DSS Server`) that directly manages raw devices of disk arrays and provides capabilities similar to distributed file systems?**

- [ ] A. DMS (Distributed Memory Service)
- [ ] B. DSS (Distributed Storage Service)
- [ ] C. SPQ (Shared-Everything Parallel Query)
- [ ] D. OCK RDMA

### Q9. [Single-Choice — 15 pts] (Ch.03 openGauss Architecture and Key Features)
**In openGauss Dynamic Data Masking, which preset masking function displays `'4880-9898-4545-2525'` as `'xxxx-xxxx-xxxx-2525'` (masking all digits except the last four)?**

- [ ] A. maskall
- [ ] B. alldigitsmasking
- [ ] C. creditcardmasking
- [ ] D. randommasking

### Q10. [Single-Choice — 15 pts] (Ch.03 openGauss Architecture and Key Features)
**In openGauss Workload Diagnosis Report (WDR), what are the default values of `enable_wdr_snapshot`, `wdr_snapshot_interval`, and `wdr_snapshot_retention_days`?**

- [ ] A. `on`, 30 minutes, 7 days
- [ ] B. `off`, 1 hour, 8 days
- [ ] C. `on`, 1 hour, 30 days
- [ ] D. `off`, 10 minutes, 14 days

### Q11. [Single-Choice — 15 pts] (Ch.03 openGauss Architecture and Key Features)
**Which built-in openGauss function generates a single-query index recommendation (returning `table` and `column`) when passed a single `SELECT` statement string?**

- [ ] A. hypopg_create_index
- [ ] B. gs_index_advise
- [ ] C. create_wdr_snapshot
- [ ] D. hypopg_estimate_size

### Q12. [Single-Choice — 15 pts] (Ch.04 Database and Object Management)
**(Official Ch.04 Quiz Q2) Which of the following commands can be used to export partial data from the `student` table?**

- [ ] A. gs_dump
- [ ] B. gs_dumpall
- [ ] C. copy Conditional statement
- [ ] D. gs_backup

### Q13. [Single-Choice — 15 pts] (Ch.04 Database and Object Management)
**Which system catalog in openGauss stores information about database authorization identifiers (roles and users, including `rolcanlogin`) across the entire cluster and is accessible only to system administrators?**

- [ ] A. PG_CLASS
- [ ] B. PG_AUTHID
- [ ] C. PG_DEPEND
- [ ] D. PG_NAMESPACE

### Q14. [Single-Choice — 15 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 394 Q1) Which of the following logical expressions is used to search for records whose position is an engineer and salary is greater than 6000?**

- [ ] A. Position = 'Engineer' OR Salary > 6000
- [ ] B. Position = Engineer AND Salary > 6000
- [ ] C. Position = Engineer OR Salary > 6000
- [ ] D. Position = 'Engineer' AND Salary > 6000

### Q15. [Single-Choice — 15 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 394 Q2) In a `WHERE` clause, the expression `age between 20 and 30` is equivalent to:**

- [ ] A. age >= 20 and age <= 30
- [ ] B. age >= 20 or age <= 30
- [ ] C. age > 20 and age < 30
- [ ] D. age > 20 or age < 30

### Q16. [Single-Choice — 15 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 405 Q1) Which of the following SQL commands can be used to increase the value of the `AGE` column in the `STAFFS` table by five years?**

- [ ] A. UPDATE SET AGE WITH AGE+5
- [ ] B. UPDATE AGE WITH AGE+5
- [ ] C. UPDATE STAFFS SET AGE = AGE+5
- [ ] D. UPDATE STAFFS AGE WITH AGE+5

### Q17. [Single-Choice — 15 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 405 Q2) Which of the following four groups of SQL commands belong to the DML commands?**

- [ ] A. CREATE, DROP, UPDATE
- [ ] B. INSERT, UPDATE, DELETE
- [ ] C. INSERT, DROP, ALTER
- [ ] D. UPDATE, DELETE, ALTER

### Q18. [Single-Choice — 15 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 406 Q3) Which of the following SQL statements will delete records for all students whose class ID (specified by `cid`) is 6 from the `student` table?**

- [ ] A. delete FROM student where cid = 6;
- [ ] B. delete * FROM student where cid = 6;
- [ ] C. delete FROM student on cid = 6;
- [ ] D. delete * FROM student on cid = 6;

### Q19. [Single-Choice — 15 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 446 Q2) SQL integrates data query, data manipulation, data definition, and data control. Which of the following functions is implemented by the `CREATE`, `DROP`, and `ALTER` statements?**

- [ ] A. Data query
- [ ] B. Data manipulation
- [ ] C. Data definition
- [ ] D. Data control

### Q20. [Single-Choice — 15 pts] (Ch.06 GaussDB)
**(Official Ch.06 Quiz Q1) In the GaussDB distributed architecture, which of the following components is used for sharing configuration and service discovery (service registration and search)?**

- [ ] A. CN
- [ ] B. DN
- [ ] C. GTM
- [ ] D. ETCD

### Q21. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.01 openGauss Overview)
**(Official Ch.01 Quiz Q3) Which of the following phases are involved in the development of data management technologies?**

- [ ] A. Manual management
- [ ] B. File system
- [ ] C. DBS
- [ ] D. AI management

### Q22. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.01 openGauss Overview)
**Which three significant common features are shared by all NewSQL database systems (`SQL + NoSQL = NewSQL`)?**

- [ ] A. They support the relational data model
- [ ] B. They use SQL as the main interface
- [ ] C. They meet the features of a distributed database (scalable across nodes)
- [ ] D. They completely abandon ACID transactions in favor of eventual consistency only

### Q23. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.01 openGauss Overview)
**Which of the following are categories of execution plan nodes in the openGauss Execution Engine (Ch.01 pp. 53–54)?**

- [ ] A. Scan plan node (e.g., SeqScan, IndexScan, SubQueryScan)
- [ ] B. Control plan node (e.g., Limit, RecursiveUnion, Union)
- [ ] C. Materialize plan node (e.g., Agg, Sort)
- [ ] D. Join plan node (e.g., MergeJoin, SortJoin, HashJoin)

### Q24. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.02 Database Installation and Deployment)
**(Official Ch.02 Quiz Q3) Which of the following are the prerequisites for installing openGauss on a single node?**

- [ ] A. User groups and common users have been created, and the operating systems and networks of all servers are running properly.
- [ ] B. Common users must have the read, write, and execute permissions on the database package decompression directory and installation directory, and the installation directory must be empty.
- [ ] C. A common user has the execution permission on the downloaded openGauss package.
- [ ] D. Before the installation, check whether the specified openGauss port is occupied. If the port is occupied, change the port number or stop the process that uses the port.

### Q25. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.02 Database Installation and Deployment)
**Which of the following `HOSTTYPE` and `authentication-options` values are supported in `pg_hba.conf` when configuring client authentication via `gs_guc -h`?**

- [ ] A. `HOSTTYPE` can be `local`, `host`, `hostssl`, or `hostnossl`
- [ ] B. `sha256` is the recommended password authentication method
- [ ] C. `trust`, `reject`, `md5`, `cert`, and `gss` are valid authentication options
- [ ] D. Remote hosts are permitted to connect using `trust` authentication by default

### Q26. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.02 Database Installation and Deployment)
**Which two parts are exported when `gs_dumpall` is used to export all databases in an openGauss cluster (Ch.02 p. 115)?**

- [ ] A. All global objects, including database users and groups, tablespaces, and global attributes/permissions
- [ ] B. SQL scripts from each openGauss database (by calling `gs_dump`) containing all SQL statements required to restore the databases
- [ ] C. Binary `.tar` archives that can only be imported using `gs_restore`
- [ ] D. Operating system kernel parameters and SSD `dd` benchmark logs

### Q27. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.03 openGauss Architecture and Key Features)
**(Official Ch.03 Quiz Q1) Which of the following are the openGauss deployment modes?**

- [ ] A. Single-node deployment
- [ ] B. Deployment with one primary and one standby
- [ ] C. Deployment with one primary and multiple standbys
- [ ] D. Deployment with dual primary nodes

### Q28. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.03 openGauss Architecture and Key Features)
**Which three key components make up the Cost-Based Optimizer (CBO) in openGauss (Ch.03 p. 165)?**

- [ ] A. Query converter
- [ ] B. Cost estimator
- [ ] C. Execution plan generator
- [ ] D. Redo log replayer

### Q29. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.03 openGauss Architecture and Key Features)
**Which of the following are advantages of a partitioned table over an ordinary table in openGauss (Ch.03 p. 174 & Ch.05 p. 427)?**

- [ ] A. High query efficiency (queries can specify partitions / use partition pruning)
- [ ] B. High availability (if one partition is faulty, data in other partitions remains available)
- [ ] C. Easy maintenance (if a partition is faulty, only that partition needs to be repaired)
- [ ] D. Balanced I/O (partitions can be mapped to different disks to balance I/O)

### Q30. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.03 openGauss Architecture and Key Features)
**How does Symmetric Multi-Processing (SMP) parallel technology improve openGauss database performance on multi-core servers (Ch.03 pp. 187–188)?**

- [ ] A. Significantly reduces the time needed to execute a single complex query
- [ ] B. Improves system throughput for a given period of time and improves system resource utilization
- [ ] C. Operates parallel threads within the same process and exchanges data directly through memory via the `Stream` operator without occupying network bandwidth
- [ ] D. Eliminates all resource contention even when system concurrency is extremely high and data is severely skewed

### Q31. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.03 openGauss Architecture and Key Features)
**In openGauss Role-Based Access Control (RBAC), authorization defines relationships among which three core elements (Ch.03 p. 211)?**

- [ ] A. Who (owner or subject of the permission, e.g., a user)
- [ ] B. What (object such as a table or function to which the permission applies)
- [ ] C. How (specific permission, positive or negative authorization)
- [ ] D. Where (physical disk sector and NUMA node distance)

### Q32. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.03 openGauss Architecture and Key Features)
**Which system catalogs in openGauss store metadata related to Unified Auditing policies (Ch.03 p. 223)?**

- [ ] A. GS_AUDITING_POLICY
- [ ] B. GS_AUDITING_POLICY_ACCESS
- [ ] C. GS_AUDITING_POLICY_FILTERS
- [ ] D. GS_AUDITING_POLICY_PRIVILEGES

### Q33. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.03 openGauss Architecture and Key Features)
**Which of the following are the three running modes of the `X-Tuner` parameter tuning tool in openGauss (Ch.03 p. 247)?**

- [ ] A. recommend
- [ ] B. train
- [ ] C. tune
- [ ] D. compile

### Q34. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.04 Database and Object Management)
**(Official Ch.04 Quiz Q3) Which of the following statements about row-store tables and column-store tables are TRUE?**

- [ ] A. Row-store tables are used in scenarios where INSERT and UPDATE operations are frequently performed.
- [ ] B. Row-store tables are applicable to point queries, that is, simple index-based queries that return a small number of records.
- [ ] C. Column-store tables are more efficient in compression and projection.
- [ ] D. Row-store tables are used in scenarios where there are a large number of queries for statistical analysis.

### Q35. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 395 Q3) Assume that you want to query student names, ages, and scores from the `student` table, and want the results sorted in descending order by age. If there are students of the same age, they are sorted in ascending order by score instead. Which of the following SQL statements can be used?**

- [ ] A. SELECT name, age, score FROM student order by age desc, score;
- [ ] B. SELECT name, age, score FROM student order by age, score asc;
- [ ] C. SELECT name, age, score FROM student order by 2 desc, 3 asc;
- [ ] D. SELECT name, age, score FROM student order by 1 desc, 2;

### Q36. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.05 SQL Basics)
**Which of the following `LIMIT` / `OFFSET` clauses in openGauss are equivalent and output 20 rows after skipping the first 5 rows (Ch.05 p. 392)?**

- [ ] A. LIMIT 5, 20
- [ ] B. LIMIT 20 OFFSET 5
- [ ] C. OFFSET 5 LIMIT 20
- [ ] D. LIMIT 5 OFFSET 20

### Q37. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 447 Q3) Create a decremental sequence named `seq_1`. The starting value is 400, the step is –4, and the minimum value is 100. When the sequence reaches the minimum value, it can be cyclically executed. Which of the following statements are correct?**

- [ ] A. CREATE SEQUENCE seq_1 START WITH 400 MAXVALUE 100 INCREMENT BY -4 CYCLE;
- [ ] B. CREATE SEQUENCE seq_1 MAXVALUE 400 MINVALUE 100 INCREMENT BY -4 CYCLE;
- [ ] C. CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 INCREMENT BY -4 CYCLE;
- [ ] D. CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 MAXVALUE 400 INCREMENT BY -4 CYCLE;

### Q38. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 468 Q2) Which of the following are arithmetic functions in openGauss?**

- [ ] A. length(str)
- [ ] B. sin(n)
- [ ] C. round(v numeric, s int)
- [ ] D. hex(p1)

### Q39. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 469 Q3 & Q4) Which three separate approaches to pattern matching are provided by openGauss?**

- [ ] A. LIKE
- [ ] B. Same
- [ ] C. SIMILAR TO
- [ ] D. POSIX regular expressions

### Q40. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.06 GaussDB)
**(Official Ch.06 Quiz Q2) Which of the following are core functions of UGO (Database and Application Migration UGO)?**

- [ ] A. Source database profiling
- [ ] B. Destination database selection and specification recommendation & Destination database compatibility analysis
- [ ] C. Migration workload evaluation
- [ ] D. Database structure migration & Application SQL migration

### Q41. [True / False — 10 pts] (Ch.01 openGauss Overview)
**openGauss uses a single-process multi-threaded architecture (`gaussdb`) and incremental checkpoints (performance fluctuation < 5%), whereas PostgreSQL uses a multi-process architecture and full checkpoints (fluctuation > 15%).**

- [ ] A. True
- [ ] B. False

### Q42. [True / False — 10 pts] (Ch.02 Database Installation and Deployment)
**Only user `root` is authorized to run the `gs_checkos` and `gs_postuninstall` commands in openGauss.**

- [ ] A. True
- [ ] B. False

### Q43. [True / False — 10 pts] (Ch.03 openGauss Architecture and Key Features)
**When Ultimate RTO is enabled in openGauss (`recovery_parse_workers > 1` and `recovery_parallelism > 1`), cascaded standby nodes are fully supported.**

- [ ] A. True
- [ ] B. False

### Q44. [True / False — 10 pts] (Ch.03 openGauss Architecture and Key Features)
**In openGauss Row-Level Security (RLS), initial users and system administrators (`SYSADMIN`) are not affected by row-level security policies.**

- [ ] A. True
- [ ] B. False

### Q45. [True / False — 10 pts] (Ch.04 Database and Object Management)
**(Official Ch.04 Quiz Q1) Users and roles have the same syntax in the openGauss database. Therefore, they are fully equivalent.**

- [ ] A. True
- [ ] B. False

### Q46. [True / False — 10 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 372 Q1) `BIGINT` occupies four bytes.**

- [ ] A. True
- [ ] B. False

### Q47. [True / False — 10 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 372 Q2) `CLOB` is used to store large object data of the `TEXT` type.**

- [ ] A. True
- [ ] B. False

### Q48. [True / False — 10 pts] (Ch.05 SQL Basics)
**(Official Ch.05 Quiz p. 446 Q1) When an index is created for a table, the corresponding base table is deleted if the index is canceled.**

- [ ] A. True
- [ ] B. False

### Q49. [True / False — 10 pts] (Ch.05 SQL Basics)
**In openGauss, `CREATE DATABASE` and `DROP DATABASE` statements cannot be executed inside a transaction block, and the preinstalled `POSTGRES`, `TEMPLATE0`, and `TEMPLATE1` databases cannot be deleted.**

- [ ] A. True
- [ ] B. False

### Q50. [True / False — 10 pts] (Ch.06 GaussDB)
**In GaussDB Cloud Trace Service (CTS), operation records from the last seven days can be queried on the management console, and traces are regularly dumped to OBS buckets and encrypted using KMS keys.**

- [ ] A. True
- [ ] B. False

### Q51. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.02 Database Installation and Deployment)
**Lab 1: Write the `gs_guc` command to dynamically add and immediately reload a client authentication rule in `pg_hba.conf` across all nodes (`-N all -I all`) allowing `host` access to `all` databases by user `testuser` from `10.252.95.191/32` using `sha256` authentication.**

```bash
gs_guc ____ -N all -I all -h "host all testuser 10.252.95.191/32 ____"
```
*Write your command / SQL / answer below:*
```text

```

### Q52. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.02 Database Installation and Deployment)
**Lab 2: Write the command (executed as user `root`) to check SSD read/write performance using `gs_checkperf` for cluster user `omm`.**

```bash
gs_checkperf -U omm -i ____
```
*Write your command / SQL / answer below:*
```text

```

### Q53. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.03 openGauss Architecture and Key Features)
**Lab 3: Write the two commands (executed as user `omm` on the standby node) to perform a planned primary/standby switchover for data directory `/home/omm/cluster/dn1/` and then record the updated primary/standby roles in the dynamic configuration file.**

```bash
gs_ctl ____ -D /home/omm/cluster/dn1/
gs_om -t ____
```
*Write your command / SQL / answer below:*
```text

```

### Q54. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.03 openGauss Architecture and Key Features)
**Lab 4: Write the SQL statements to create a resource label `label_for_creditcard` on column `user1.table1.creditcard` and create a dynamic data masking policy `msk_creditcard` using the `creditcardmasking` function.**

```bash
CREATE ____ LABEL label_for_creditcard ADD COLUMN(user1.table1.creditcard);
CREATE ____ POLICY msk_creditcard ____ ON LABEL(label_for_creditcard);
```
*Write your command / SQL / answer below:*
```text

```

### Q55. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.04 Database and Object Management)
**Lab 5: Write the SQL statements to create a column-store table `customer_t2(state_ID CHAR(2), state_NAME VARCHAR2(40), area_ID NUMBER)` and a Memory-Optimized Table (MOT) `mot_test(x INT)` on `mot_server`.**

```bash
CREATE TABLE customer_t2(state_ID CHAR(2), state_NAME VARCHAR2(40), area_ID NUMBER) WITH (____ = ____);
CREATE ____ TABLE mot_test(x INT) SERVER mot_server;
```
*Write your command / SQL / answer below:*
```text

```

### Q56. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.04 Database and Object Management)
**Lab 6 (Official Ch.04 Quiz Q2): Write the SQL `COPY` statement to export partial data from table `t1` where `a2 = 1` to `/data/input/t1_output.txt` using delimiter `'^'`.**

```bash
____ (SELECT * FROM t1 WHERE a2 = 1) ____ '/data/input/t1_output.txt' DELIMITER '^';
```
*Write your command / SQL / answer below:*
```text

```

### Q57. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.05 SQL Basics)
**Lab 7 (Official Ch.05 Quiz p. 405 Q1 & p. 406 Q3): Write the two DML statements to: (1) increase the `AGE` column in the `STAFFS` table by 5 years, and (2) delete all records from the `student` table where `cid = 6`.**

```bash
UPDATE STAFFS ____ AGE = ____;
____ ____ student ____ cid = 6;
```
*Write your command / SQL / answer below:*
```text

```

### Q58. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.05 SQL Basics)
**Lab 8 (Official Ch.05 Quiz p. 447 Q3): Write the SQL statement to create a decremental sequence named `seq_1` with starting value `400`, minimum value `100`, maximum value `400`, step `-4`, and cyclic execution.**

```bash
CREATE SEQUENCE seq_1 START WITH 400 ____ 100 ____ 400 INCREMENT BY -4 ____;
```
*Write your command / SQL / answer below:*
```text

```

### Q59. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.05 SQL Basics)
**Lab 9 (Official Ch.05 Quiz p. 468 Q1): Write the SQL query to add 7 days (`integer '7'`) to `date '2021-4-28'` aliased as `RESULT`, and include a SQL comment (`-- YYYY-MM-DD`) stating the resulting date.**

```bash
SELECT date '2021-4-28' + ____ '7' AS RESULT;
-- Resulting date: ____-__-__
```
*Write your command / SQL / answer below:*
```text

```

### Q60. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.06 GaussDB)
**Lab 10 (Official Ch.06 Quiz Q1 & Q2): Complete the SQL query returning the GaussDB distributed component used for sharing configuration and service discovery, and the Huawei tool used for heterogeneous database structure and application SQL migration.**

```bash
SELECT '____' AS config_discovery_component, '____' AS heterogeneous_migration_tool;
```
*Write your command / SQL / answer below:*
```text

```
