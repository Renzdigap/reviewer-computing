# DDL for Partitioned Tables & Indexes

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 07 — SQL DDL Objects, Sequences, Operators & Built-in Functions (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `04-Exercise-Partition-Maintenance-and-Index-DDL-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.05, pp. 427–437, 446

---

## Learning Objectives
- Create Range, Interval, List, and Hash Partitioned Tables with `ENABLE ROW MOVEMENT` and understand partition key constraint rules
- Execute partition maintenance clauses (`MOVE`, `EXCHANGE`, `MERGE`, `SPLIT`, `ADD`, `DROP`, `RENAME`)
- Create, rebuild, rename, mark `UNUSABLE`, and drop Indexes (`LOCAL` vs `GLOBAL`, `DROP INDEX CONCURRENTLY`), avoiding the Ch.05 Quiz Q1 index-drop trap

---

### 1. Creating & Maintaining Partitioned Tables (pp. 427–431)
- **Important Partitioning Rules (p. 428)**:
  1. **Unique / Primary Key Constraint Rule**: A partitioned table supports `UNIQUE` and `PRIMARY KEY` constraints, **but the constraint key columns MUST contain all partition keys**!
  2. **Single-Column vs. Multi-Column**: **Range partitioning** supports one or multiple partition key columns; **Hash partitioning** and **List partitioning** currently support **only a single partition key column**!
  3. **`ENABLE | DISABLE ROW MOVEMENT`**: Controls whether an `UPDATE` that changes a row's partition key value automatically moves the tuple across partitions (`ENABLE ROW MOVEMENT`) or raises an error (`DISABLE`).
  4. **Execution Order of Multiple Maintenance Clauses (p. 430)**: When multiple partition clauses are combined in `ALTER TABLE`, openGauss executes **`DROP PARTITION` first**, then **`ADD PARTITION`**, and finally the remaining clauses in order (`MOVE`, `EXCHANGE`, `MERGE`, `SPLIT`, `RENAME`).

```sql
CREATE TABLE training(staff_id INT NOT NULL, course_name CHAR(20), score INT)
TABLESPACE example1
PARTITION BY RANGE(staff_id) (
    PARTITION training1 VALUES LESS THAN(100),
    PARTITION training2 VALUES LESS THAN(200),
    PARTITION training3 VALUES LESS THAN(300),
    PARTITION training4 VALUES LESS THAN(MAXVALUE) TABLESPACE example2
) ENABLE ROW MOVEMENT;

ALTER TABLE training MOVE PARTITION training1 TABLESPACE example3;
ALTER TABLE training MERGE PARTITION training1, training2 INTO PARTITION training3;
ALTER TABLE training DROP PARTITION training4;
ALTER TABLE training RENAME PARTITION training3 TO training5;
```

---

### 2. Defining, Modifying & Dropping Indexes (pp. 432–437, 446)
- **Index Classifications (p. 432)**:
  - **Single-column** vs. **Multi-column (Composite)**: A composite index is used only when the **leading (first) column** is referenced in the query condition; supports up to **16 columns** and max key length **3,900 bytes** (p. 432).
  - **Common (B-Tree default)**, **Unique** (auto-created on `PRIMARY KEY`), **Function-based**, and **Partitioned (`LOCAL` vs. `GLOBAL`)**.
- **Modifying & Dropping Indexes (pp. 435–437)**:
  ```sql
  CREATE INDEX idx_bank_card ON bank_card(b_number ASC, b_type);
  CREATE INDEX idx_education ON education(staff_id ASC, higest_degree)
      LOCAL (PARTITION doctor, PARTITION master, PARTITION undergraduate);

  ALTER INDEX idx_bank_card REBUILD;
  ALTER INDEX idx_bank_card RENAME TO idx_bank_card_temp;
  ALTER INDEX idx_bank_card UNUSABLE;
  DROP INDEX CONCURRENTLY idx_bank_card;
  ```
  - **`DROP INDEX CONCURRENTLY` Rules (p. 437)**:
    - Drops the index **without locking** the table against concurrent reads/writes.
    - Allows **only one index name** per statement, **does NOT support `CASCADE`**, and **cannot be executed inside a transaction block**!
  - **CRITICAL EXAM FACT (Ch.05 p. 446 Quiz Q1: False!)**:
    - **Dropping (canceling) an index on a table NEVER deletes the underlying base table!** (Whereas `DROP TABLE` forcibly deletes the table *and* all indexes/partitions depending on it.)

---

## Key Takeaways
- **Dropping an index (`DROP INDEX`) deletes ONLY the index structure — it NEVER deletes the corresponding base table (Ch.05 p. 446 Quiz Q1: False!). Conversely, `DROP TABLE` deletes the table and all its dependent indexes and partitions.**
- **On a partitioned table, any `UNIQUE` or `PRIMARY KEY` constraint must include all partition key columns. Range partitioning supports multi-column keys, while List and Hash partitioning support only single-column keys.**
- **`DROP INDEX CONCURRENTLY` drops an index without locking concurrent table access, but accepts only one index name, does not support `CASCADE`, and cannot run inside a transaction block.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.05 p. 446 Quiz Q1): '(True or false) When an index is created for a table, the corresponding base table is deleted if the index is canceled.' -> B. False!

> [!WARNING]
> EXAM TRAP: `DROP INDEX` can run inside a transaction block, but `DROP INDEX CONCURRENTLY` CANNOT run inside a transaction block and does NOT support `CASCADE` (Ch.05 p. 437).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-Partition-Maintenance-and-Index-DDL-Lab.html`](./04-Exercise-Partition-Maintenance-and-Index-DDL-Lab.html)** (or [`04-Exercise-Partition-Maintenance-and-Index-DDL-Lab.md`](./04-Exercise-Partition-Maintenance-and-Index-DDL-Lab.md)) to apply this concept in an interactive lab workbench!
