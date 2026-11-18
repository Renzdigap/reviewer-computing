# Hands-On Lab: Creating Databases with `template0`, Schemas with Sub-Commands & Table Constraints

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 07 — SQL DDL Objects, Sequences, Operators & Built-in Functions (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-DDL-Databases-Schemas-Tables-and-Constraints`  
**Interactive Workbench:** Open **[`02-Exercise-DDL-Database-Schema-and-Table-Constraints-Lab.html`](./02-Exercise-DDL-Database-Schema-and-Table-Constraints-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Create database `music` owned by `jim` using `template0`, create a schema for `role1` with an embedded `CREATE TABLE`, and add `CHECK` and `UNIQUE` constraints to `bank_card`.

### Step-by-Step Instructions
1. Step 1: Create database `music` owned by `jim` using `CREATE DATABASE music OWNER jim TEMPLATE template0;` and set its connection limit to 30 (`ALTER DATABASE music WITH CONNECTION LIMIT 30;`).
2. Step 2: Add a `CHECK(b_c_id > 0)` constraint `ck_bank_card` and a `UNIQUE(full_masks)` constraint `uk_bank_card` to `bank_card` using `ALTER TABLE`.

### Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Create database music using template0 and limit connections to 30
CREATE DATABASE music OWNER jim TEMPLATE ____;
ALTER DATABASE music WITH ____ LIMIT 30;

-- Step 2: Add CHECK and UNIQUE constraints to bank_card
ALTER TABLE bank_card ADD CONSTRAINT ck_bank_card ____(b_c_id > 0);
ALTER TABLE bank_card ADD CONSTRAINT uk_bank_card ____(full_masks);
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `TEMPLATE template0` when creating a database that may customize encoding/locale.
- Use `WITH CONNECTION LIMIT 30` in `ALTER DATABASE`.
- Use `CHECK(b_c_id > 0)` and `UNIQUE(full_masks)`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
CREATE DATABASE music OWNER jim TEMPLATE template0;
ALTER DATABASE music WITH CONNECTION LIMIT 30;

ALTER TABLE bank_card ADD CONSTRAINT ck_bank_card CHECK(b_c_id > 0);
ALTER TABLE bank_card ADD CONSTRAINT uk_bank_card UNIQUE(full_masks);
```

#### Expected Console / Query Output:
```text
CREATE DATABASE
ALTER DATABASE
ALTER TABLE
ALTER TABLE
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**(Official Ch.05 Quiz p. 446 Q2) SQL integrates data query, data manipulation, data definition, and data control. Which of the following functions is implemented by the `CREATE`, `DROP`, and `ALTER` statements?**

- A. Data query
- B. Data manipulation
- C. Data definition
- D. Data control

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Chapter 05 (p. 408 & p. 446), `CREATE`, `DROP`, and `ALTER` are Data Definition Language (DDL) statements used to define, modify, and remove database objects.
</details>

### Question 2 [Single-Choice]
**When creating a new database in openGauss with a custom character encoding format (different from the default template), which template database must be specified?**

- A. postgres
- B. template0
- C. template1
- D. sys_dummy

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 05 (p. 410), the encoding format of `template1` cannot be changed. If you need to change the encoding format when creating a database, you must use `template0`.
</details>

### Question 3 [True / False]
**In openGauss, column-store tables support table-level `PRIMARY KEY` and `FOREIGN KEY` constraints just like row-store tables.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.05 p. 421). Column-store tables support only `PARTIAL CLUSTER KEY` table-level constraints and do NOT support primary key and foreign key table-level constraints.
</details>
