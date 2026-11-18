# DDL for Views & Sequences

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 07 — SQL DDL Objects, Sequences, Operators & Built-in Functions (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-Views-and-Decremental-Sequences-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.05, pp. 438–447

---

## Learning Objectives
- Create, replace, and drop Views (`CREATE OR REPLACE [TEMP] VIEW`, `DROP VIEW ... CASCADE | RESTRICT`)
- Create, modify, and drop Sequences (`CREATE/ALTER/DROP SEQUENCE`, `nextval()`, `CACHE`, `CYCLE`, `OWNED BY`)
- Master the default `MINVALUE`/`MAXVALUE`/`START WITH` rules for ascending vs. descending sequences (Ch.05 p. 447 Quiz Q3: BD!)

---

### 1. Defining Views (`CREATE [OR REPLACE] VIEW`, `DROP VIEW`, pp. 438–440)
- **3 Core Benefits of Views (p. 438)**:
  1. **Simplify complex queries**: Encapsulate frequently used multi-table joins/filters into a single virtual table (`SELECT * FROM view_name;`).
  2. **Enhance security**: Expose only non-sensitive columns/rows while hiding sensitive columns in the base table.
  3. **Ensure logical data independence**: Decouple application queries from physical base table restructuring.
- **Syntax**:
  ```sql
  CREATE OR REPLACE VIEW privilege_view AS SELECT b_number, b_type FROM bank_card;
  SELECT * FROM privilege_view;
  \d privilege_view
  DROP VIEW IF EXISTS privilege_view RESTRICT; -- RESTRICT is default; CASCADE drops dependent views
  ```

---

### 2. Defining Sequences (`CREATE / ALTER / DROP SEQUENCE`, pp. 441–445)
A **sequence** is a special single-row object that generates arithmetic progressions (typically used for auto-incrementing primary keys via `DEFAULT nextval('seq_name')`):
```sql
CREATE SEQUENCE name
    [ INCREMENT [ BY ] increment ]
    [ MINVALUE minvalue | NO MINVALUE | NOMINVALUE ]
    [ MAXVALUE maxvalue | NO MAXVALUE | NOMAXVALUE ]
    [ START [ WITH ] start ]
    [ CACHE cache ]
    [ [ NO ] CYCLE | NOCYCLE ]
    [ OWNED BY { table_name.column_name | NONE } ];
```

---

### 3. Ascending vs. Descending Sequence Default Rules (p. 442, Ch.05 p. 447 Quiz Q3: BD!)
This table is **one of the highest-yield exam topics in HCIA-openGauss V2.0**:

| Parameter | Ascending Sequence (`INCREMENT > 0`, Default `+1`) | Descending (Decremental) Sequence (`INCREMENT < 0`, e.g., `-4`) |
| :--- | :--- | :--- |
| **Default `MINVALUE`** | **`1`** | **`-2^63 - 1`** (minimum 64-bit signed integer) |
| **Default `MAXVALUE`** | **`2^63 - 1`** (maximum 64-bit signed integer) | **`-1`** (**CRITICAL!** If `MAXVALUE` is omitted on a negative-increment sequence, `MAXVALUE` defaults to **`-1`**!) |
| **Default `START WITH`** | **`minvalue`** | **`maxvalue`** (**CRITICAL!** If `START WITH` is omitted on a descending sequence, `START WITH` defaults to **`maxvalue`**!) |
| **Default `CACHE` / `CYCLE`** | `CACHE 1` (no cache), `NO CYCLE` | `CACHE 1`, `NO CYCLE` |

#### Why Ch.05 p. 447 Quiz Q3 Answer is **BD**!
*Question*: Create a decremental sequence `seq_1` starting at `400`, step `-4`, minimum `100`, cycling at minimum:
- **A. `CREATE SEQUENCE seq_1 START WITH 400 MAXVALUE 100 INCREMENT BY -4 CYCLE;`** -> **WRONG!** (`START WITH 400` cannot be greater than `MAXVALUE 100`, and `MINVALUE 100` is missing!)
- **B. `CREATE SEQUENCE seq_1 MAXVALUE 400 MINVALUE 100 INCREMENT BY -4 CYCLE;`** -> **CORRECT!** Because for a descending sequence (`INCREMENT BY -4`), when `START WITH` is omitted, **`START WITH` automatically defaults to `MAXVALUE` (`400`)**!
- **C. `CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 INCREMENT BY -4 CYCLE;`** -> **WRONG!** Because `MAXVALUE` was omitted on a descending sequence, **`MAXVALUE` defaults to `-1`**, which fails because `START WITH 400 > MAXVALUE -1`!
- **D. `CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 MAXVALUE 400 INCREMENT BY -4 CYCLE;`** -> **CORRECT!** Explicitly sets `START WITH 400`, `MINVALUE 100`, `MAXVALUE 400`, `INCREMENT BY -4`, and `CYCLE`.

---

## Key Takeaways
- **For an ascending sequence (`INCREMENT > 0`), default `MINVALUE = 1`, default `MAXVALUE = 2^63 - 1`, and default `START WITH = minvalue`.**
- **For a descending sequence (`INCREMENT < 0`), default `MINVALUE = -2^63 - 1`, default `MAXVALUE = -1`, and default `START WITH = maxvalue`.**
- **Therefore, for a decremental sequence starting at 400 down to 100 with step -4, you MUST specify `MAXVALUE 400` (`START WITH 400` is optional because it defaults to `MAXVALUE 400`) — making both B and D correct in Ch.05 p. 447 Quiz Q3!**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.05 p. 447 Quiz Q3): Why does `CREATE SEQUENCE seq_1 START WITH 400 MINVALUE 100 INCREMENT BY -4 CYCLE;` (Option C) FAIL with an error? Because for a negative increment, default `MAXVALUE` is `-1`, and `START (400)` cannot be greater than `MAXVALUE (-1)`! Both B and D are the official correct answers (`BD`).

> [!WARNING]
> EXAM TRAP: `OWNED BY table_name.column_name` automatically drops the sequence when that column or table is dropped, but it does NOT automatically increment the column on `INSERT` unless `DEFAULT nextval('seq')` is also declared on the column (Ch.05 p. 442).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-Views-and-Decremental-Sequences-Lab.html`](./06-Exercise-Views-and-Decremental-Sequences-Lab.html)** (or [`06-Exercise-Views-and-Decremental-Sequences-Lab.md`](./06-Exercise-Views-and-Decremental-Sequences-Lab.md)) to apply this concept in an interactive lab workbench!
