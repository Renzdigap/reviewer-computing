# Tablespaces, Users, Roles & Permission Management

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 05 — Database & Object Management (MOT, Tablespaces, Users/Roles, Backup/Export) (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-Tablespaces-Users-Roles-and-Account-Lock-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.04, pp. 306–321, 346

---

## Learning Objectives
- Create, inspect, size, rename, and drop Tablespaces (`CREATE TABLESPACE ... RELATIVE LOCATION`, `PG_TABLESPACE_SIZE`, `\db`, 90% read-only threshold)
- Explain why Users and Roles are NOT fully equivalent (Ch.04 Quiz Q1: False! Users have `LOGIN` by default, Roles do not)
- Manage Users/Roles (`CREATE/ALTER/DROP USER/ROLE`), Account Validity (`VALID BEGIN ... VALID UNTIL`), Locking (`ACCOUNT LOCK/UNLOCK`), and Private Users (`WITH INDEPENDENT`)

---

### 1. Tablespace Management & 90% Read-Only Threshold (pp. 307–310)
- **Why Use Tablespaces?**:
  1. Expand storage onto other disk partitions when the initial volume is full.
  2. Separate hot objects (e.g., frequently accessed indexes on fast SSDs) from cold archived tables (on slower disks).
  3. **90% Read-Only Protection Rule (p. 307)**: If the disk usage where a tablespace resides reaches **90%**, openGauss **automatically switches the database to read-only mode**! It switches back to read/write mode once disk usage drops below 90%.
- **Tablespace SQL Operations (pp. 308–310)**:
  ```sql
  -- 1. Create tablespace (relative to instance data directory; must be an empty r/w directory)
  CREATE TABLESPACE fastspace RELATIVE LOCATION 'tablespace/tablespace_1';
  -- 2. Grant CREATE permission on tablespace
  GRANT CREATE ON TABLESPACE fastspace TO jack;
  -- 3. Create table in tablespace (or SET default_tablespace = 'fastspace';)
  CREATE TABLE foo(i INT) TABLESPACE fastspace;
  -- 4. Inspect tablespaces & check size
  \db
  SELECT * FROM pg_tablespace;
  SELECT PG_TABLESPACE_SIZE('fastspace');
  -- 5. Rename & drop tablespace (owner or sysadmin only; must be empty)
  ALTER TABLESPACE fastspace RENAME TO fspace;
  DROP TABLESPACE fspace;
  ```

---

### 2. Users vs. Roles (`pg_authid`, `PUBLIC`, Ch.04 Quiz Q1!)
- **User vs. Role Distinction (pp. 312–315, 324, 346)**:
  - **User**: An entity/individual that connects to the database (`rolcanlogin = true` / **`LOGIN` privilege enabled by default**).
  - **Role**: A carrier of permission sets representing behavioral constraints (**does NOT have `LOGIN` permission by default**).
  - **CRITICAL EXAM FACT (Ch.04 Quiz Q1: False!)**: Although `CREATE USER` and `CREATE ROLE` share the same syntax in openGauss, **users and roles are NOT fully equivalent** because `CREATE USER` grants `LOGIN` by default whereas `CREATE ROLE` does not (`NOLOGIN` by default)!
- **Implicit `PUBLIC` Group (p. 313)**: All new users and roles implicitly inherit permissions granted to `PUBLIC` (use `GRANT/REVOKE ... TO/FROM PUBLIC` to manage).
- **System Catalog & Views (p. 317, 324)**: User/role attributes are stored in the cluster-wide system catalog **`pg_authid`** (accessible **only to `SYSADMIN`**) and exposed via **`pg_user`** and **`pg_roles`** views.

---

### 3. Account Validity, Manual Lock/Unlock & Private (`INDEPENDENT`) Users (pp. 318–321)
- **Dropping Users (`DROP USER`, p. 318)**: Uses **`RESTRICT` by default** — if the user owns database objects, `DROP USER` fails unless **`CASCADE`** is specified (`DROP USER IF EXISTS joe CASCADE;`).
- **Setting Account Validity Period (p. 319)**:
  ```sql
  CREATE USER joe WITH PASSWORD 'Bigdata@123'
      VALID BEGIN '2015-10-10 08:00:00' VALID UNTIL '2016-10-10 08:00:00';
  ALTER USER joe WITH VALID BEGIN '2016-11-10 08:00:00' VALID UNTIL '2017-11-10 08:00:00';
  ```
- **Manually Locking and Unlocking Accounts (p. 320)**:
  ```sql
  ALTER USER user_read ACCOUNT LOCK;
  ALTER USER user_read ACCOUNT UNLOCK;
  ```
- **Private User (`WITH INDEPENDENT`, p. 321)**:
  ```sql
  CREATE USER user_independent WITH INDEPENDENT IDENTIFIED BY '1234@abc';
  ```
  - Isolates DBA control permissions from data access permissions in non-separation-of-duties mode: **DBAs (`SYSADMIN`) can manage (`DROP`, `ALTER`, `TRUNCATE`) objects of an `INDEPENDENT` user, but CANNOT access (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `COPY`, `GRANT`, `REVOKE`, `ALTER OWNER`) their data without explicit authorization from that user!**

---

## Key Takeaways
- **Users and roles have the same syntax in openGauss, but they are NOT fully equivalent (Ch.04 Quiz Q1: False) because `CREATE USER` includes `LOGIN` by default whereas `CREATE ROLE` does not.**
- **If the disk hosting a tablespace reaches 90% usage, openGauss automatically switches to read-only mode.**
- **For a Private User (`CREATE USER ... WITH INDEPENDENT`), DBAs can manage (`DROP`, `ALTER`, `TRUNCATE`) their objects but cannot access (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `COPY`) their data without authorization.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.04 Quiz Q1): '(True or False) Users and roles have the same syntax in the openGauss database. Therefore, they are fully equivalent.' -> B. False!

> [!WARNING]
> EXAM TRAP: If a user owns database objects, `DROP USER username;` fails because `RESTRICT` is the default; you must use `DROP USER username CASCADE;` (Ch.04 p. 318).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-Tablespaces-Users-Roles-and-Account-Lock-Lab.html`](./06-Exercise-Tablespaces-Users-Roles-and-Account-Lock-Lab.html)** (or [`06-Exercise-Tablespaces-Users-Roles-and-Account-Lock-Lab.md`](./06-Exercise-Tablespaces-Users-Roles-and-Account-Lock-Lab.md)) to apply this concept in an interactive lab workbench!
