# Hands-On Lab: Creating Column-Store Tables & Updating Optimizer Statistics

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 03 — openGauss Architecture, Resource Pooling & High Performance (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Optimizers-CBO-ABO-Statistics-and-Row-vs-Column-Store`  
**Interactive Workbench:** Open **[`06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab.html`](./06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Create a column-store analytical table `orders_olap` with high compression, declare multi-column statistics on `(region, category)`, and run `ANALYZE` so the CBO/ABO can generate optimal execution plans.

### Step-by-Step Instructions
1. Step 1: Create table `orders_olap (order_id INT, region VARCHAR(20), category VARCHAR(20), amount NUMERIC(10,2))` as a column-store table using `WITH (ORIENTATION = COLUMN, COMPRESSION = HIGH);`.
2. Step 2: Collect statistics on `orders_olap` for columns `(region, category)` using `ANALYZE orders_olap (region, category);`.

### Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Create a column-store table with HIGH compression
CREATE TABLE orders_olap (
    order_id INT,
    region VARCHAR(20),
    category VARCHAR(20),
    amount NUMERIC(10,2)
) WITH (____ = ____, COMPRESSION = HIGH);

-- Step 2: Collect statistics on (region, category) in orders_olap
____ orders_olap (region, category);
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `WITH (ORIENTATION = COLUMN, COMPRESSION = HIGH)` to create a compressed column-store table.
- Use the `ANALYZE orders_olap (region, category);` statement to collect column statistics into `PG_STATISTIC`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
CREATE TABLE orders_olap (
    order_id INT,
    region VARCHAR(20),
    category VARCHAR(20),
    amount NUMERIC(10,2)
) WITH (ORIENTATION = COLUMN, COMPRESSION = HIGH);

ANALYZE orders_olap (region, category);
```

#### Expected Console / Query Output:
```text
CREATE TABLE
ANALYZE
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Multiple-Choice (Select ALL)]
**(Official Ch.04 Quiz Q3) Which of the following statements about row-store tables and column-store tables are TRUE?**

- A. Row-store tables are used in scenarios where INSERT and UPDATE operations are frequently performed.
- B. Row-store tables are applicable to point queries, that is, simple index-based queries that return a small number of records.
- C. Column-store tables are more efficient in compression and projection.
- D. Row-store tables are used in scenarios where there are a large number of queries for statistical analysis.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 03 (pp. 171–172) and Chapter 04 Quiz Q3 (p. 347), A, B, and C are true. D is false because statistical analysis queries over large volumes of data are suited to column-store tables.
</details>

### Question 2 [Single-Choice]
**Which system catalog in openGauss stores the table and index column statistics collected by the `ANALYZE` statement?**

- A. PG_STAT_ACTIVITY
- B. PG_STATISTIC
- C. PG_ATTRIBUTE
- D. PG_DEPEND

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (pp. 168–170), the `ANALYZE` statement collects statistics on tables in the database and stores them in the system catalog `PG_STATISTIC`.
</details>

### Question 3 [True / False]
**The openGauss AI-Based Optimizer (ABO) uses a Bayesian network (`BAYESNET`) model to characterize the joint distribution of multi-column data for intelligent cardinality estimation.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True (Ch.03 p. 162). The ABO employs a Bayesian network model (`enable_ai_stats = on`, `multi_stats_type = 'BAYESNET'`) to accurately estimate cardinality for multi-column equality queries.
</details>
