# DML Statements — `INSERT`, `UPDATE` & `DELETE`

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 06 — SQL Basics — Classification, Data Types, DQL, Joins & DML (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `08-Exercise-DML-INSERT-ON-DUPLICATE-UPDATE-and-DELETE-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.05, pp. 396–406

---

## Learning Objectives
- Master the 3 forms of `INSERT` (`INSERT ... VALUES`, `INSERT ... SELECT`, and `INSERT ... ON DUPLICATE KEY UPDATE` / `INSERT IGNORE`)
- Write `UPDATE table SET col = expr [WHERE condition]` statements (`UPDATE STAFFS SET AGE = AGE + 5` — Ch.05 Quiz Q1!)
- Write `DELETE FROM table [WHERE condition]` statements (`DELETE FROM student WHERE cid = 6;` — Ch.05 Quiz Q3!) and know column-store DML limitations

---

### 1. Inserting Data (`INSERT`, pp. 397–399)
openGauss supports **three `INSERT` syntax patterns**:
1. **Insert explicit row values**:
   ```sql
   INSERT INTO bank_card(b_number, b_type, b_c_id) VALUES ('6222021302020000001', 'Credit Card', 1);
   ```
2. **Insert from a query (`INSERT ... SELECT`)**:
   ```sql
   INSERT INTO bank_card1 SELECT * FROM bank_card;
   -- Number of columns in SELECT list must match the target columns!
   ```
3. **Upsert on primary/unique key conflict (`ON DUPLICATE KEY UPDATE` vs. `IGNORE`)**:
   ```sql
   INSERT INTO bank_card VALUES ('6222021302020000001', 'Credit Card', 1)
       ON DUPLICATE KEY UPDATE b_type = 'Savings Card';
   ```
   - **`IGNORE`** (`INSERT IGNORE INTO ...`): Silently ignores rows that cause duplicate key errors (**cannot** be used together with `ON DUPLICATE KEY UPDATE`!).
   - **Permissions**:
     - `RETURNING` clause requires `SELECT` permission on the table.
     - `ON DUPLICATE KEY UPDATE` requires `INSERT`, `SELECT`, and `UPDATE` on the table plus `SELECT` on the unique/primary key index.
   - **Record Size Limit (p. 397)**: Data size of a single inserted record must be **< 64,000 bytes** in standard row-store insert precautions.

---

### 2. Updating Data (`UPDATE`, pp. 400–401, Ch.05 p. 405 Quiz Q1!)
```sql
UPDATE table_reference SET col_name = expression [, ...] [ WHERE condition ];
```
- **Official Exam Question (Ch.05 p. 405 Quiz Q1: C!)**:
  - To increase the value of the `AGE` column in the `STAFFS` table by 5 years:
    ```sql
    UPDATE STAFFS SET AGE = AGE + 5;
    ```
  - *(Why are A, B, D wrong? Because SQL `UPDATE` uses `UPDATE <table> SET <col> = <expr>`, NEVER `WITH`!)*
- **Column-Store `UPDATE` Precautions (p. 400)**:
  - `RETURNING` clause is **not supported** for column-store tables.
  - Memory/space holding old records in a column-store table is **not automatically recycled** after `UPDATE` — you must run **`VACUUM FULL table_name;`** to reclaim it.
  - `UPDATE` is **not supported** on column-store replication tables.

---

### 3. Deleting Data (`DELETE`, pp. 402–404, Ch.05 p. 406 Quiz Q3!)
```sql
DELETE FROM [schema_name.]table_name [ WHERE condition ];
```
- **Official Exam Question (Ch.05 p. 406 Quiz Q3: A!)**:
  - To delete records for all students whose class ID (`cid`) is `6` from the `student` table:
    ```sql
    DELETE FROM student WHERE cid = 6;
    ```
  - **CRITICAL SYNTAX TRAP**: Never put `*` after `DELETE` (`DELETE * FROM ...` is a syntax error!), and use `WHERE` (not `ON`) for the filter condition!
  - If the `WHERE` clause is omitted (`DELETE FROM student;`), **all rows in the table are deleted**, leaving the empty table structure intact.

---

## Key Takeaways
- **To increment `AGE` by 5 in `STAFFS`, use `UPDATE STAFFS SET AGE = AGE + 5;` (Ch.05 p. 405 Quiz Q1: C).**
- **To delete rows where `cid = 6` from `student`, use `DELETE FROM student WHERE cid = 6;` — there is NO `*` between `DELETE` and `FROM`, and the filter uses `WHERE`, not `ON` (Ch.05 p. 406 Quiz Q3: A).**
- **`INSERT ... ON DUPLICATE KEY UPDATE` updates specified columns when a primary/unique key conflict occurs, and cannot be combined with `INSERT IGNORE`.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.05 p. 406 Quiz Q3): `DELETE * FROM student WHERE cid = 6;` (B) is INVALID SQL! `DELETE` deletes entire rows, so `*` is never used after `DELETE`. The correct statement is `DELETE FROM student WHERE cid = 6;` (A).

> [!WARNING]
> EXAM TRAP: After updating rows in a column-store table, old record space is not recycled automatically; you must run `VACUUM FULL table_name;` (Ch.05 p. 400).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-DML-INSERT-ON-DUPLICATE-UPDATE-and-DELETE-Lab.html`](./08-Exercise-DML-INSERT-ON-DUPLICATE-UPDATE-and-DELETE-Lab.html)** (or [`08-Exercise-DML-INSERT-ON-DUPLICATE-UPDATE-and-DELETE-Lab.md`](./08-Exercise-DML-INSERT-ON-DUPLICATE-UPDATE-and-DELETE-Lab.md)) to apply this concept in an interactive lab workbench!
