# Optimizers (CBO vs ABO), Statistics (`ANALYZE`) & Row-Store vs Column-Store

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 03 — openGauss Architecture, Resource Pooling & High Performance (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.03, pp. 160–173

---

## Learning Objectives
- Compare the Cost-Based Optimizer (CBO, v1.0.0+) and AI-Based Optimizer (ABO, v3.1.0+)
- Collect single-column and multi-column statistics using `ANALYZE` and inspect `PG_STATISTIC` / `PG_CLASS`
- Contrast Row-Store and Column-Store tables (`WITH (ORIENTATION = COLUMN, COMPRESSION = ...)` — Ch.04 Quiz Q3)

---

### 1. Query Optimizers: CBO vs. ABO (pp. 161–166)
- **CBO (Cost-Based Optimizer, introduced in v1.0.0)**:
  - Consists of **3 key components**:
    1. **Query converter**: Rewrites SQL statements into lower-cost equivalent forms.
    2. **Cost estimator**: Calculates execution cost based on table tuples, column width, NULL ratio, distinct count, and **MCV (`most_common_vals`)**.
    3. **Execution plan generator**: Explores access paths, join methods, and join orders to pick the lowest-cost plan.
- **ABO (AI-Based Optimizer, 3rd-gen intelligent optimizer introduced in v3.1.0)**:
  - **Sub-feature 1 — Intelligent Cardinality Estimation**: Uses a **Bayesian network (`BAYESNET`)** model to capture joint distributions across correlated/skewed columns for multi-column equality queries.
    - Enable via GUC: `SET enable_ai_stats = on; SET multi_stats_type = 'BAYESNET';` (or `'ALL'`), then run `ANALYZE`.
  - **Sub-feature 2 — Adaptive Plan Selection**: Maintains multiple cached execution plans using range linear expansion and range coverage matching (especially for partial indexes and offsets) rather than a single rigid generic cached plan.

---

### 2. Statistics Collection (`ANALYZE`) & `PG_STATISTIC` (pp. 167–170)
- **Where Statistics Live**:
  - **`pg_class`**: Stores global table-level **`relpages`** (disk pages) and **`reltuples`** (estimated rows).
  - **`pg_statistic`**: Stores column-level statistics (`starelid`, `staattnum`, `stanullfrac` [NULL ratio], `stawidth` [avg byte width], `stadistinct` [distinct values], `stanumbersN`, `stavaluesN`, `histogram_bounds`). Accessible **only to system administrators** (ordinary users query the `PG_STATS` view if authorized).
- **Sampling Rule**: By default, `default_statistics_target = 100` samples **30,000 rows**. If a table exceeds **1,600,000 rows**, Huawei recommends setting `default_statistics_target = -2` (which samples **2%** of the rows).
- **Commands**:
  ```sql
  ANALYZE tablename;                                    -- Single table
  ANALYZE;                                              -- Entire database
  ANALYZE tablename (col_1, col_2);                     -- Specific columns
  ALTER TABLE tablename ADD STATISTICS ((col_1, col_2)); -- Declare multi-column stats for future ANALYZE
  ```

---

### 3. Row-Store vs. Column-Store Tables (pp. 171–173, 296–301, Ch.04 Quiz Q3!)

| Feature | Row-Store Table (`ORIENTATION = ROW`, Default) | Column-Store Table (`ORIENTATION = COLUMN`) |
| :--- | :--- | :--- |
| **Storage Layout** | All attributes of a row are stored contiguously together | Values of the same column across rows are stored together |
| **Strengths** | Fast **`INSERT` / `UPDATE` / `DELETE`**; fast **point queries** (index lookup returning a few rows) or `SELECT *` | High **compression ratio**; efficient **projection** (reads only queried columns, drastically reducing disk I/O) |
| **Weaknesses** | Reading 2 columns out of 50 still reads the entire row from disk | Tuple reconstruction overhead; **inefficient for frequent single-row `INSERT`/`UPDATE` and point queries** |
| **Best Scenario** | **OLTP**: frequent small writes/updates and point queries | **OLAP**: batch inserts, statistical aggregations (`SUM`/`GROUP BY`), wide tables where queries touch **< 50% of columns** |

```sql
CREATE TABLE sales_col (id INT, region VARCHAR(20), amount NUMERIC(10,2))
WITH (ORIENTATION = COLUMN, COMPRESSION = HIGH);
```

---

## Key Takeaways
- **A CBO consists of three components: Query converter, Cost estimator, and Execution plan generator.**
- **ABO (v3.1.0+) introduces Bayesian Network (`BAYESNET`) intelligent multi-column cardinality estimation (`enable_ai_stats = on`) and Adaptive Plan Selection.**
- **Row-store (default) excels at frequent INSERT/UPDATE and point queries; Column-store (`WITH (ORIENTATION = COLUMN)`) excels at compression, projection, and OLAP statistical aggregations (Ch.04 Quiz Q3: ABC).**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.04 Quiz Q3): Statement D claims 'Row-store tables are used in scenarios where there are a large number of queries for statistical analysis.' FALSE! Statistical analysis queries over massive data use Column-store tables (Answer: ABC).

> [!WARNING]
> EXAM TRAP: The `PG_STATISTIC` system catalog is accessible ONLY to system administrators; non-admin users must use authorized views (`PG_STATS`).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab.html`](./06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab.html)** (or [`06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab.md`](./06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab.md)) to apply this concept in an interactive lab workbench!
