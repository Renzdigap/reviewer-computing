# 📖 Data Management Evolution, DBS Components & Classical Data Models

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 01 — openGauss Overview & Database Fundamentals (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-DBS-Components-and-Data-Models-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.01, pp. 4–19

---

## 🎯 Learning Objectives
- Distinguish Data, Database (DB), Database Management System (DBMS), and Database System (DBS)
- Compare the 3 stages of data management technology development: Manual Management, File System, and DBS
- Contrast Hierarchical, Network, and Relational database models and trace SQL standardization history

---

### 1. Core Concepts: Data, DB, DBMS, and DBS
- **Data**: Facts or statistics represented as discrete **digital data** (symbols, characters, numerals) or continuous **analog data** (audio, video, images). Raw data is meaningless until processed into **information**.
- **Database (DB)**: A **permanent**, **organized**, and **sharable** collection of structured data stored in a computer according to a data model with minimal redundancy and high independence.
- **Database Management System (DBMS)**: System software between the user/application and OS that manages the DB. Its 5 core functions are:
  1. **Data Definition (DDL)** — defining tables, views, indexes, and schemas.
  2. **Data Manipulation (DML)** — querying, inserting, deleting, and updating data.
  3. **Database Operation Management** — ensuring security, integrity checks, concurrency control, and fault recovery.
  4. **Interfaces & Tools** — APIs for developers and O&M tools for DBAs.
  5. **Creation & Maintenance** — initial data conversion, dump/restore, and performance monitoring.
- **Database System (DBS)**: The complete operational ecosystem. Per Huawei's official definition (p. 9), **a DBS consists of three core parts**:
  1. **Database (DB)** — stores data.
  2. **DBMS** — manages the database.
  3. **Database Applications** — supplement the DBMS to provide intuitive user-facing data processing (along with DBAs and users).

---

### 2. Three Stages of Data Management Technology Development

| Dimension | 1. Manual Management (Mid-1950s) | 2. File System (Late 1950s – Mid-1960s) | 3. DBS Stage (Late 1960s – Present) |
| :--- | :--- | :--- | :--- |
| **Application** | Scientific computing | Scientific computing & management | Large-scale & distributed data management |
| **Hardware** | Paper tapes, punch cards (no direct access storage) | Magnetic tapes, disks, magnetic drums | Large-capacity disks, arrays, on-demand expansion |
| **Software / Manager** | None (managed by User/Program) | File System | **DBMS / DBS** |
| **Data Sharing** | No sharing; high redundancy | Poor sharing; high redundancy | **Good sharing; low redundancy** |
| **Data Independence** | Poor (program-bound) | Good physical independence; poor logical independence | **High physical & good logical independence** |
| **Data Structuring** | Unstructured | Structured inside a record; unstructured as a whole | **Unified data model & overall structuring** |

---

### 3. Classical Database Models & SQL Evolution
- **Hierarchical Model (1960s, e.g., IBM IMS, DNS, LDAP, Linux/Windows FS)**: Tree structure where only the **root node** has no parent, and every other node has **exactly one parent node** (1:N).
- **Network Model**: Graph structure allowing **more than one node to have no parent**, and a node can have **more than one parent** (M:N).
- **Relational Model (1969/1970, E.F. Codd)**: Uses rigorous two-dimensional tables (**Relations**) composed of rows (**Tuples**), columns (**Attributes**), and primary identifiers (**Keys / Codes**). Relationships must be normalized so every attribute is an indivisible atomic data item.
- **SQL Standardization Milestones**:
  - **SQL-86 (1986)**: First ANSI SQL standard.
  - **SQL-89 (1989)**: Added integrity constraints.
  - **SQL-92 / SQL2 (1992)**: Introduced standard classification concepts.
  - **SQL:1999 / SQL3 (1999)**: Major revision adding object-oriented features, regular expressions, triggers, and recursive queries.
  - **SQL:2003**: XML & Window functions; **SQL:2008**: `TRUNCATE`; **SQL:2011**: Temporal/time-series; **SQL:2016**: JSON.

---

## 🔑 Key Takeaways
- **A Database System (DBS) consists of three parts: Database (DB), DBMS, and Database Application (storage medium is hardware, NOT one of the three logical DBS components in Ch.01 Quiz Q1).**
- **Data management evolved through exactly three stages: Manual Management, File System, and Database System (DBS).**
- **In the relational model, each cell must be an indivisible data item; in the hierarchical model, every non-root node has only one parent; in the network model, a node can have multiple parents.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.01 Quiz Q1): 'Which of the following is NOT a component of a database system?' -> D. Database storage medium! The three components are Database, DBMS, and Database application.

> [!WARNING]
> EXAM TRAP (Ch.01 Quiz Q3): 'Which phases are involved in the development of data management technologies?' -> A. Manual management, B. File system, C. DBS (ABC). 'AI management' (D) is NOT one of the three historical stages!

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-DBS-Components-and-Data-Models-Lab.html`](./02-Exercise-DBS-Components-and-Data-Models-Lab.html)** (or [`02-Exercise-DBS-Components-and-Data-Models-Lab.md`](./02-Exercise-DBS-Components-and-Data-Models-Lab.md)) to apply this concept in an interactive lab workbench!
