# Hands-On Lab: Inspecting Memory Parameters & Physical Data Directories

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 03 — openGauss Architecture, Resource Pooling & High Performance (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-Instance-Memory-Threads-and-Directory-Layout`  
**Interactive Workbench:** Open **[`02-Exercise-Memory-Threads-and-Data-Directory-Lab.html`](./02-Exercise-Memory-Threads-and-Data-Directory-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are auditing an openGauss instance's memory settings (`shared_buffers`, `cstore_buffers`, `work_mem`, `maintenance_work_mem`) and checking the database OID mapping inside the `base/` directory.

### Step-by-Step Instructions
1. Step 1: Query `SHOW shared_buffers;`, `SHOW cstore_buffers;`, and `SHOW work_mem;`.
2. Step 2: Query `SELECT oid, datname FROM pg_database WHERE datname = 'postgres';` to find the subdirectory OID under `base/`.

### Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Check shared, column-store, and operator work memory buffers
SHOW ____;
SHOW ____;
SHOW work_mem;

-- Step 2: Query OID and database name from pg_database
SELECT oid, datname FROM ____ WHERE datname = 'postgres';
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `SHOW shared_buffers;` and `SHOW cstore_buffers;`.
- The system catalog storing available databases and their OIDs is `pg_database`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
SHOW shared_buffers;
SHOW cstore_buffers;
SHOW work_mem;

SELECT oid, datname FROM pg_database WHERE datname = 'postgres';
```

#### Expected Console / Query Output:
```text
shared_buffers 
----------------
 1GB
(1 row)

 cstore_buffers 
----------------
 512MB
(1 row)

 work_mem 
----------
 64MB
(1 row)

  oid  | datname  
-------+----------
 15749 | postgres
(1 row)
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In the openGauss instance directory structure, which directory stores Write-Ahead Logs (WALs)?**

- A. pg_log
- B. pg_xlog
- C. pg_audit
- D. global

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (p. 143), `pg_xlog` stores Write-Ahead Logs (WALs), whereas `pg_log` stores runtime logs, `pg_audit` stores audit logs, and `global` stores cluster-wide system catalogs.
</details>

### Question 2 [Single-Choice]
**In the openGauss logical storage architecture, what is the default size of a data Block, and at what size is a table split into multiple Datafile segments?**

- A. 4 KB block; 512 MB datafile segment
- B. 8 KB block; 1 GB datafile segment
- C. 16 KB block; 2 GB datafile segment
- D. 32 KB block; 4 GB datafile segment

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (p. 141), the basic unit of database management is a Block with a default size of 8 KB, and a table containing more than 1 GB of data is stored in multiple 1 GB datafile segments.
</details>

### Question 3 [True / False]
**Column-store tables primarily use `shared_buffers`, so you should increase `shared_buffers` and decrease `cstore_buffers` for column-store workloads.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.03 p. 136). Column-store tables rarely use `shared_buffers`; they use `cstore_buffers`. Users should reduce `shared_buffers` and increase `cstore_buffers` for column-store workloads.
</details>
