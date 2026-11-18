# Join Queries — Cartesian Product, Inner Join & Outer Joins

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 06 — SQL Basics — Classification, Data Types, DQL, Joins & DML (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-Inner-Left-Right-Full-Outer-Join-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.05, pp. 383–389

---

## Learning Objectives
- Calculate the row count (I × J) and column count (N + M) of a Cartesian Product (`SELECT * FROM A, B;`)
- Write `INNER JOIN ... ON` queries and understand the legacy `(+)` operator caveat
- Contrast `LEFT [OUTER] JOIN`, `RIGHT [OUTER] JOIN`, and `FULL [OUTER] JOIN` on Huawei's `education` and `training` tables

---

### 1. Cartesian Product & Join Basics (pp. 383–384)
- **Cartesian Product (Direct Product, X \× Y, p. 383)**:
  - If table X has **I tuples (rows)** and **N attributes (columns)**, and table Y has **J tuples** and **M attributes**, then `SELECT * FROM X, Y;` (a join without any `WHERE` or `ON` join condition) produces:
    - **I \× J tuples (rows)** (e.g., 4 rows in A \× 5 rows in B = **20 rows**).
    - **N + M attributes (columns)**.
- **Table References in `FROM`**: Can be ordinary tables, views, or subqueries (`(SELECT ...) AS alias`).
- **Note on `(+)` Outer Join Operator (p. 384)**: openGauss supports Oracle's `(+)` operator in `WHERE` clauses to convert a join into an outer join, **but it is NOT recommended** because it is not standard SQL syntax.

---

### 2. Inner Join vs. Outer Joins (`LEFT`, `RIGHT`, `FULL`, pp. 385–389)

| Join Type | Syntax (`OUTER` / `INNER` keyword is optional) | Returned Rows & `NULL` Padding Behavior |
| :--- | :--- | :--- |
| **Inner Join** | `A [INNER] JOIN B ON A.id = B.id` | Returns **only** rows that satisfy the join condition in **both** tables. |
| **Left Outer Join** | `A LEFT [OUTER] JOIN B ON A.id = B.id` | Driven by the **left table (`A`)**: returns all rows from `A` + matched data from `B`. Unmatched columns from `B` are filled with **`NULL`**. |
| **Right Outer Join** | `A RIGHT [OUTER] JOIN B ON A.id = B.id` | Driven by the **right table (`B`)**: returns all rows from `B` + matched data from `A`. Unmatched columns from `A` are filled with **`NULL`**. |
| **Full Outer Join** | `A FULL [OUTER] JOIN B ON A.id = B.id` | Returns all matched rows **plus** unmatched rows from `A` (padded with `NULL` on the right) **and** unmatched rows from `B` (padded with `NULL` on the left). |

---

### 3. Official Walkthrough: `education e` (`staff_id` 11, 12, 13) \\bowtie `training t` (`staff_id` 10, 11, 12) (pp. 387–389)
- **`education e`**: `(11, 'master')`, `(12, 'doctor')`, `(13, 'scholar')`
- **`training t`**: `(10, 90)`, `(11, 92)`, `(12, 95)`
  - **`INNER JOIN`**: Returns only `11` and `12` (2 rows).
  - **`e LEFT JOIN t`**: Returns `11` (`92`), `12` (`95`), and `13` (`score = NULL`) (3 rows).
  - **`e RIGHT JOIN t`**: Returns `NULL` (`staff_id` from `e` is `NULL`, `score = 90`), `11` (`92`), and `12` (`95`) (3 rows).
  - **`e FULL JOIN t`**: Returns `11`, `12`, `13` (`score = NULL`), and `NULL` (`score = 90`) (4 rows).

---

## Key Takeaways
- **A Cartesian product between table X (I rows, N columns) and table Y (J rows, M columns) produces I * J rows and N + M columns.**
- **`LEFT JOIN` preserves all rows from the left table (padding right columns with `NULL`), `RIGHT JOIN` preserves all rows from the right table, and `FULL JOIN` preserves unmatched rows from both sides.**
- **In `LEFT JOIN`, `ON` clause conditions determine row matching (driving `NULL` extension), whereas outer `WHERE` conditions filter the resulting joined rows afterwards.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: In `SELECT e.staff_id, e.higest_degree, t.score FROM education e RIGHT JOIN training t ON (e.staff_id = t.staff_id);`, why is `e.staff_id` displayed as empty/NULL for `t.staff_id = 10`? Because the `SELECT` list projected `e.staff_id` (from the left table), which has no match for `10`!

> [!WARNING]
> EXAM TRAP: If table A has 4 records and table B has 5 records, `SELECT * FROM A, B;` without a join condition returns 20 (4 x 5) records.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-Inner-Left-Right-Full-Outer-Join-Lab.html`](./06-Exercise-Inner-Left-Right-Full-Outer-Join-Lab.html)** (or [`06-Exercise-Inner-Left-Right-Full-Outer-Join-Lab.md`](./06-Exercise-Inner-Left-Right-Full-Outer-Join-Lab.md)) to apply this concept in an interactive lab workbench!
