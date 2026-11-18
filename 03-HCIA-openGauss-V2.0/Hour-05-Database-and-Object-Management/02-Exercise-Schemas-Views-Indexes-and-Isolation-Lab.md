# Hands-On Lab: Managing Schemas, Views, Partial Indexes & `gsql` Meta-Commands

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 05 — Database & Object Management (MOT, Tablespaces, Users/Roles, Backup/Export) (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-Logical-Structure-and-Core-Database-Objects`  
**Interactive Workbench:** Open **[`02-Exercise-Schemas-Views-Indexes-and-Isolation-Lab.html`](./02-Exercise-Schemas-Views-Indexes-and-Isolation-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Create a dedicated schema `hr_schema`, rename it to `hr_prod`, create a partial index on `customer_t1(Amount)` for high-value orders (`WHERE Amount > 1000`), and create a view `vip_customers`.

### Step-by-Step Instructions
1. Step 1: Create schema `hr_schema` and rename it to `hr_prod` using `ALTER SCHEMA hr_schema RENAME TO hr_prod;`.
2. Step 2: Create a partial index `idx_high_amount` on `customer_t1 (Amount) WHERE Amount > 1000;`.
3. Step 3: Create view `vip_customers` using `CREATE VIEW vip_customers AS SELECT c_customer_id, Amount FROM customer_t1 WHERE Amount > 1000;`.

### Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Create schema hr_schema and rename it to hr_prod
CREATE SCHEMA hr_schema;
ALTER SCHEMA hr_schema ____ TO hr_prod;

-- Step 2: Create partial index idx_high_amount where Amount > 1000
CREATE INDEX idx_high_amount ON customer_t1 (Amount) ____ Amount > 1000;

-- Step 3: Create view vip_customers
CREATE ____ vip_customers AS
SELECT c_customer_id, Amount FROM customer_t1 WHERE Amount > 1000;
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `ALTER SCHEMA hr_schema RENAME TO hr_prod;` to rename a schema.
- A partial index uses a `WHERE` predicate at the end of `CREATE INDEX`.
- Use `CREATE VIEW vip_customers AS SELECT ...` to define the virtual table.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
CREATE SCHEMA hr_schema;
ALTER SCHEMA hr_schema RENAME TO hr_prod;

CREATE INDEX idx_high_amount ON customer_t1 (Amount) WHERE Amount > 1000;

CREATE VIEW vip_customers AS
SELECT c_customer_id, Amount FROM customer_t1 WHERE Amount > 1000;
```

#### Expected Console / Query Output:
```text
CREATE SCHEMA
ALTER SCHEMA
CREATE INDEX
CREATE VIEW
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In `gsql`, which meta-command is used to view the column structure and index definitions of a specific table `customer_t1`?**

- A. \l customer_t1
- B. \c customer_t1
- C. \d customer_t1
- D. \h customer_t1

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Chapter 04 (p. 285), `\d tablename` displays the table structure, whereas `\l` lists all databases, `\c dbname` switches databases, `\dt` lists all tables, and `\h` shows SQL command syntax help.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**Which of the following statements about schemas in openGauss are TRUE?**

- A. When a database is initially created, it has a `public` schema by default
- B. When `CREATE USER` is executed, the system automatically creates a schema with the same name as the user in that database
- C. Different schemas within the same database can contain tables with the exact same name without conflict
- D. Schemas can be nested inside other schemas just like OS directories

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 04 (p. 291), A, B, and C are true. Option D is false: 'A schema is similar to an OS directory but cannot be nested.'
</details>

### Question 3 [True / False]
**At the `READ COMMITTED` transaction isolation level in openGauss, two consecutive `SELECT` statements within the same transaction always see the exact same snapshot even if another concurrent transaction commits changes in between.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.04 p. 293). At `READ COMMITTED`, each statement starts with a new snapshot, so two consecutive `SELECT` statements in the same transaction may see different snapshots if another transaction commits in between. `REPEATABLE READ` keeps the initial transaction snapshot.
</details>
