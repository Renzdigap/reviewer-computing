# Hands-On Lab: Maintaining Partitioned Tables & Managing Indexes (`REBUILD`, `UNUSABLE`, `DROP`)

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 07 — SQL DDL Objects, Sequences, Operators & Built-in Functions (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-DDL-Partitioned-Tables-and-Indexes`  
**Interactive Workbench:** Open **[`04-Exercise-Partition-Maintenance-and-Index-DDL-Lab.html`](./04-Exercise-Partition-Maintenance-and-Index-DDL-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Perform partition maintenance on the `training` range-partitioned table (`MOVE PARTITION`, `MERGE PARTITION`) and manage the `idx_bank_card` index (`REBUILD`, `UNUSABLE`, and `DROP INDEX CONCURRENTLY`).

### Step-by-Step Instructions
1. Step 1: Move partition `training1` to tablespace `example3` (`ALTER TABLE training MOVE PARTITION training1 TABLESPACE example3;`) and merge `training1, training2` into `training3` (`ALTER TABLE training MERGE PARTITION training1, training2 INTO PARTITION training3;`).
2. Step 2: Rebuild index `idx_bank_card` (`ALTER INDEX idx_bank_card REBUILD;`), mark it unusable (`ALTER INDEX idx_bank_card UNUSABLE;`), and drop it without locking the table (`DROP INDEX CONCURRENTLY idx_bank_card;`).

### Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Move partition training1 to example3 and merge training1, training2 into training3
ALTER TABLE training ____ PARTITION training1 TABLESPACE example3;
ALTER TABLE training ____ PARTITION training1, training2 INTO PARTITION training3;

-- Step 2: Rebuild idx_bank_card, set it UNUSABLE, and drop it CONCURRENTLY
ALTER INDEX idx_bank_card ____;
ALTER INDEX idx_bank_card ____;
DROP INDEX ____ idx_bank_card;
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `MOVE PARTITION` and `MERGE PARTITION ... INTO PARTITION ...`.
- Use `ALTER INDEX idx_bank_card REBUILD;`, `ALTER INDEX idx_bank_card UNUSABLE;`, and `DROP INDEX CONCURRENTLY idx_bank_card;`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
ALTER TABLE training MOVE PARTITION training1 TABLESPACE example3;
ALTER TABLE training MERGE PARTITION training1, training2 INTO PARTITION training3;

ALTER INDEX idx_bank_card REBUILD;
ALTER INDEX idx_bank_card UNUSABLE;
DROP INDEX CONCURRENTLY idx_bank_card;
```

#### Expected Console / Query Output:
```text
ALTER TABLE
ALTER TABLE
REINDEX
ALTER INDEX
DROP INDEX
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [True / False]
**(Official Ch.05 Quiz p. 446 Q1) When an index is created for a table, the corresponding base table is deleted if the index is canceled (dropped).**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.05 p. 437 & p. 446). Dropping an index deletes only the index; the base table and its data remain intact.
</details>

### Question 2 [Single-Choice]
**Which option in `DROP INDEX` deletes an index without locking concurrent access to the underlying table, but cannot be executed inside a transaction block and does not support `CASCADE`?**

- A. RESTRICT
- B. CONCURRENTLY
- C. LOCAL
- D. UNUSABLE

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 05 (p. 437), `DROP INDEX CONCURRENTLY` deletes an index without locking the table, supports only one index name, does not support `CASCADE`, and cannot run within a transaction.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about partitioned tables in openGauss are TRUE?**

- A. A partitioned table supports `UNIQUE` and `PRIMARY KEY` constraints, provided the constraint keys contain all partition keys
- B. Range partitioning supports multi-column partition keys, whereas Hash and List partitioning support only single-column partition keys
- C. Enabling `ROW MOVEMENT` allows an `UPDATE` on the partition key to move the tuple between partitions
- D. Dropping a single partition automatically deletes all other partitions and the entire partitioned table

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 05 (pp. 428, 432), A, B, and C are true. Option D is false: dropping a partition removes only that partition without affecting other partitions (whereas `DROP TABLE` deletes all partitions).
</details>
