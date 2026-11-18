# DDL for Databases, Schemas, Tables & Constraints

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 07 — SQL DDL Objects, Sequences, Operators & Built-in Functions (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `02-Exercise-DDL-Database-Schema-and-Table-Constraints-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.05, pp. 407–426

---

## Learning Objectives
- Create, modify, and drop Databases (`CREATE/ALTER/DROP DATABASE`), understanding `template0` vs `template1`, `DBCOMPATIBILITY`, and transaction block restrictions
- Create Schemas with embedded sub-commands (`CREATE SCHEMA AUTHORIZATION role1 CREATE TABLE ...`) and inspect `SHOW SEARCH_PATH`
- Create and alter Tables and Constraints (`PRIMARY KEY`, `UNIQUE`, `CHECK`, `FOREIGN KEY`, and Column-Store constraint rules)

---

### 1. Defining Databases (`CREATE / ALTER / DROP DATABASE`, pp. 409–414)
- **Three Default Databases After Installation**: **`postgres`** (default user DB), **`template0`**, and **`template1`** (protected system databases — **cannot be dropped**!).
- **Template Rule (`template0` vs. `template1`, p. 410)**:
  - openGauss creates a new database by copying a template database (`template1` by default).
  - The encoding/locale of `template1` cannot be changed. **If you need to specify a custom `ENCODING` (e.g., `UTF8`, `GBK`, `Latin1`) when creating a database, you MUST specify `TEMPLATE template0`!**
- **Critical Restrictions (pp. 410, 414)**:
  - Neither **`CREATE DATABASE`** nor **`DROP DATABASE`** can be executed inside a transaction block (`BEGIN ... COMMIT`)!
  - A database cannot be dropped while active user sessions are connected (check via **`v$session`** or `pg_stat_activity`).
  - `ALTER DATABASE db SET TABLESPACE ts_new;` physically moves tables/indexes that are in the database's old default tablespace to `ts_new` (objects explicitly placed in other tablespaces are unaffected).

```sql
CREATE DATABASE music OWNER jim TEMPLATE template0 ENCODING 'UTF8';
ALTER DATABASE music WITH CONNECTION LIMIT 30;
ALTER DATABASE music RENAME TO music01;
ALTER DATABASE music01 SET TABLESPACE tablespace01;
ALTER DATABASE music01 OWNER TO jim01;
DROP DATABASE IF EXISTS music01;
```

---

### 2. Defining Schemas (`CREATE / ALTER / DROP SCHEMA`, pp. 415–419)
- **Creating a Schema with Sub-Commands (pp. 416–417)**:
  ```sql
  CREATE SCHEMA AUTHORIZATION role1
      CREATE TABLE films (title text, release date, awards text[])
      CREATE VIEW winners AS SELECT title, release FROM films WHERE awards IS NOT NULL;
  ```
  - Supported sub-commands inside `CREATE SCHEMA`: `CREATE TABLE`, `CREATE VIEW`, `CREATE INDEX`, `CREATE PARTITION`, and `GRANT`. All created objects are owned by `role1`.
  - **Ownership Rule (p. 416)**: If a `SYSADMIN` creates an object inside a schema that has the same name as a common user, the owner of that object is **that common user**, NOT the `SYSADMIN`!
  - Check current schema resolution order via **`SHOW SEARCH_PATH;`**.

---

### 3. Defining Tables & Constraints (`CREATE / ALTER / DROP TABLE`, pp. 420–426)
- **Row-Store vs. Column-Store Constraint Support (p. 421)**:
  - **Row-Store Tables**: Support `NOT NULL`, `NULL`, `DEFAULT`, **`UNIQUE`** (no duplicate values, **but `NULL` is allowed**), **`PRIMARY KEY`** (unique + `NOT NULL`, auto-creates unique index), **`CHECK (expression)`**, and **`FOREIGN KEY ... REFERENCES ...`** (can have duplicate or `NULL` values).
  - **Column-Store Tables**: Support **ONLY `PARTIAL CLUSTER KEY`** at the table level (**do NOT support `PRIMARY KEY` or `FOREIGN KEY` table-level constraints**), and **ONLY `NULL`, `NOT NULL`, and `DEFAULT` constant values** at the column level!
- **Modifying Tables (`ALTER TABLE`, pp. 423–425)**:
  ```sql
  ALTER TABLE bank_card ADD full_masks INTEGER;
  ALTER TABLE bank_card MODIFY full_masks NVARCHAR2(20);
  ALTER TABLE bank_card ADD CONSTRAINT ck_bank_card CHECK(b_c_id > 0);
  ALTER TABLE bank_card ADD CONSTRAINT uk_bank_card UNIQUE(full_masks);
  ALTER TABLE bank_card DROP full_masks;
  DROP TABLE IF EXISTS training CASCADE;
  ```

---

## Key Takeaways
- **To change the character encoding when creating a database, you must specify `TEMPLATE template0` (`template1`'s encoding cannot be changed). `CREATE DATABASE` and `DROP DATABASE` cannot run inside a transaction block.**
- **Column-store tables support ONLY `PARTIAL CLUSTER KEY` table constraints (no `PRIMARY KEY` or `FOREIGN KEY`) and ONLY `NULL`, `NOT NULL`, and `DEFAULT` column constraints.**
- **`UNIQUE` constraints disallow duplicate non-null values but allow `NULL`, whereas `FOREIGN KEY` columns can contain duplicate or `NULL` values.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.05 p. 446 Quiz Q2): 'Which function is implemented by the `CREATE`, `DROP`, and `ALTER` statements?' -> C. Data definition (DDL)!

> [!WARNING]
> EXAM TRAP: If a `SYSADMIN` creates an object inside a schema named after a common user (e.g., `jack.t1`), the owner of `t1` is the common user (`jack`), NOT the `SYSADMIN` (Ch.05 p. 416)!

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-DDL-Database-Schema-and-Table-Constraints-Lab.html`](./02-Exercise-DDL-Database-Schema-and-Table-Constraints-Lab.html)** (or [`02-Exercise-DDL-Database-Schema-and-Table-Constraints-Lab.md`](./02-Exercise-DDL-Database-Schema-and-Table-Constraints-Lab.md)) to apply this concept in an interactive lab workbench!
