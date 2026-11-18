# 💻 Hands-On Lab: Exporting Partial Data with `COPY`, Running `gs_dump`/`gs_restore`, and `VACUUM FULL`

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 05 — Database & Object Management (MOT, Tablespaces, Users/Roles, Backup/Export) (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-System-Catalogs-Views-and-Data-Import-Export`  
**Interactive Workbench:** Open **[`08-Exercise-COPY-gs-dump-gs-restore-and-VACUUM-Lab.html`](./08-Exercise-COPY-gs-dump-gs-restore-and-VACUUM-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Export partial data from table `t1` where `a2 = 1` using the SQL `COPY` command with delimiter `'^'`, and perform post-import space reclamation and statistics collection on `product_info` using `VACUUM FULL` and `ANALYZE`.

### 📋 Step-by-Step Instructions
1. Step 1: Export rows where `a2 = 1` from `t1` using `COPY (SELECT * FROM t1 WHERE a2 = 1) TO '/data/input/t1_output.txt' DELIMITER '^';`.
2. Step 2: Reclaim disk page fragments on `product_info` and return them to the OS using `VACUUM FULL product_info;`.
3. Step 3: Update optimizer statistics on `product_info` using `ANALYZE product_info;`.

### 📝 Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Export partial data from t1 where a2 = 1 using COPY
____ (SELECT * FROM t1 WHERE a2 = 1) TO '/data/input/t1_output.txt' DELIMITER '^';

-- Step 2: Reclaim disk page fragments on product_info and return space to OS
____ ____ product_info;

-- Step 3: Update table statistics in PG_STATISTIC
____ product_info;
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `COPY (SELECT * FROM t1 WHERE a2 = 1) TO ...` to export partial table data.
- Use `VACUUM FULL product_info;` before `ANALYZE product_info;`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
COPY (SELECT * FROM t1 WHERE a2 = 1) TO '/data/input/t1_output.txt' DELIMITER '^';

VACUUM FULL product_info;

ANALYZE product_info;
```

#### Expected Console / Query Output:
```text
COPY 15
VACUUM
ANALYZE
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**(Official Ch.04 Quiz Q2) Which of the following commands can be used to export partial data from the `student` table?**

- A. gs_dump
- B. gs_dumpall
- C. copy Conditional statement
- D. gs_backup

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Chapter 04 (p. 332 & p. 346), `COPY (SELECT * FROM student WHERE ...) TO '...'` (a `copy` conditional statement) exports a query result set (partial table data), whereas `gs_dump` and `gs_dumpall` export entire tables, schemas, or databases.
</details>

### Question 2 [Single-Choice]
**When using `gs_restore` to import an archive exported by `gs_dump`, which option specifies importing ONLY object definitions (schemas/tables) without importing any table data?**

- A. -c
- B. -e
- C. -s
- D. -d

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Chapter 04 (p. 342), `-s` imports only object definitions in schemas and does not import data. `-c` cleans existing objects before import, `-e` exits on error, and `-d` specifies the target database.
</details>

### Question 3 [True / False]
**Unlike the SQL `COPY` statement (which reads and writes files on the database server), the `gsql` meta-command `\copy` performs read and write operations on local files on the client host.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True (Ch.04 p. 333). The `\copy` meta-command in `gsql` reads and writes files on the local client machine using the local user's permissions.
</details>
