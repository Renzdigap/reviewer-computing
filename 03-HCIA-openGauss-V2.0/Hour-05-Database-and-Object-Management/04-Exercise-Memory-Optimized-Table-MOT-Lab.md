# 💻 Hands-On Lab: Granting `mot_server` Access, Creating an MOT & Indexing It

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 05 — Database & Object Management (MOT, Tablespaces, Users/Roles, Backup/Export) (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-Storage-Engine-Selection-and-MOT`  
**Interactive Workbench:** Open **[`04-Exercise-Memory-Optimized-Table-MOT-Lab.html`](./04-Exercise-Memory-Optimized-Table-MOT-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Configure a high-throughput Memory-Optimized Table (MOT) `trade_mot` for user `jack`: grant `USAGE` on `FOREIGN SERVER mot_server` to `jack`, create the MOT `trade_mot(trade_id INT, price NUMERIC(10,2))`, create an index `idx_trade_id` on it, and write the statement to drop the MOT.

### 📋 Step-by-Step Instructions
1. Step 1: Grant MOT usage permission using `GRANT USAGE ON FOREIGN SERVER mot_server TO jack;`.
2. Step 2: Create the MOT using `CREATE FOREIGN TABLE trade_mot(trade_id INT, price NUMERIC(10,2)) SERVER mot_server;`.
3. Step 3: Create index `idx_trade_id` on `trade_mot(trade_id)` using `CREATE INDEX idx_trade_id ON trade_mot(trade_id);` (without `FOREIGN`) and drop the table with `DROP FOREIGN TABLE trade_mot;`.

### 📝 Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Authorize user jack to access mot_server
GRANT USAGE ON ____ SERVER ____ TO jack;

-- Step 2: Create MOT trade_mot
CREATE ____ TABLE trade_mot(trade_id INT, price NUMERIC(10,2)) SERVER mot_server;

-- Step 3: Create index on trade_mot (note: no FOREIGN keyword!) and drop MOT
CREATE ____ idx_trade_id ON trade_mot(trade_id);
DROP ____ TABLE trade_mot;
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- MOT uses the foreign server `mot_server` (`GRANT USAGE ON FOREIGN SERVER mot_server TO jack;`).
- Use `CREATE FOREIGN TABLE` and `DROP FOREIGN TABLE` for MOT tables, but standard `CREATE INDEX` for MOT indexes.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
GRANT USAGE ON FOREIGN SERVER mot_server TO jack;

CREATE FOREIGN TABLE trade_mot(trade_id INT, price NUMERIC(10,2)) SERVER mot_server;

CREATE INDEX idx_trade_id ON trade_mot(trade_id);
DROP FOREIGN TABLE trade_mot;
```

#### Expected Console / Query Output:
```text
GRANT
CREATE FOREIGN TABLE
CREATE INDEX
DROP FOREIGN TABLE
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Which memory configuration formula must be satisfied when configuring openGauss Memory-Optimized Tables (MOT)?**

- A. `(max_mot_global_memory + max_mot_local_memory) + 2 GB < max_process_memory`
- B. `max_mot_global_memory + shared_buffers < work_mem`
- C. `max_mot_local_memory > max_mot_global_memory + 2 GB`
- D. `cstore_buffers + wal_buffers < max_mot_local_memory`

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Per Chapter 04 (p. 305), the MOT memory configuration must satisfy `(max_mot_global_memory + max_mot_local_memory) + 2 GB < max_process_memory`.
</details>

### Question 2 [Single-Choice]
**Which SQL statement correctly creates a Memory-Optimized Table (MOT) named `test` with an integer column `x` in openGauss?**

- A. `CREATE TABLE test(x int) WITH (ORIENTATION = MOT);`
- B. `CREATE FOREIGN TABLE test(x int) SERVER mot_server;`
- C. `CREATE MEMORY TABLE test(x int);`
- D. `CREATE UNLOGGED TABLE test(x int);`

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 04 (p. 305), MOT is integrated via the FDW mechanism and created using `CREATE FOREIGN TABLE test(x int) [SERVER mot_server];`.
</details>

### Question 3 [True / False]
**When creating an index on a Memory-Optimized Table (MOT), you must specify `CREATE FOREIGN INDEX` before the index name.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.04 p. 305). When creating or deleting an index on an MOT, you do NOT specify the `FOREIGN` keyword (`CREATE INDEX text_index1 ON test(x);`); `FOREIGN` is used only when creating and dropping the table.
</details>
