# 💻 Hands-On Lab: Managing Tablespaces, Account Validity, Locking & `INDEPENDENT` Users

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 05 — Database & Object Management (MOT, Tablespaces, Users/Roles, Backup/Export) (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Tablespaces-Users-Roles-and-Permission-Management`  
**Interactive Workbench:** Open **[`06-Exercise-Tablespaces-Users-Roles-and-Account-Lock-Lab.html`](./06-Exercise-Tablespaces-Users-Roles-and-Account-Lock-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Create a tablespace `fastspace` at relative path `'tablespace/tablespace_1'`, create user `joe` with a validity window, lock and unlock account `user_read`, and create a private user `user_independent` with the `INDEPENDENT` attribute.

### 📋 Step-by-Step Instructions
1. Step 1: Create tablespace `fastspace` using `CREATE TABLESPACE fastspace RELATIVE LOCATION 'tablespace/tablespace_1';`.
2. Step 2: Create user `joe` with `VALID BEGIN '2026-01-01 08:00:00' VALID UNTIL '2027-01-01 08:00:00'`, and lock `user_read` using `ALTER USER user_read ACCOUNT LOCK;`.
3. Step 3: Create private user `user_independent` using `CREATE USER user_independent WITH INDEPENDENT IDENTIFIED BY '1234@abc';`.

### 📝 Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Create tablespace fastspace at relative path
CREATE TABLESPACE fastspace ____ LOCATION 'tablespace/tablespace_1';

-- Step 2: Create user joe with validity period and lock user_read
CREATE USER joe WITH PASSWORD 'Bigdata@123'
    VALID ____ '2026-01-01 08:00:00' VALID ____ '2027-01-01 08:00:00';
ALTER USER user_read ACCOUNT ____;

-- Step 3: Create private user with INDEPENDENT attribute
CREATE USER user_independent WITH ____ IDENTIFIED BY '1234@abc';
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `RELATIVE LOCATION` when specifying a tablespace directory relative to the data node directory.
- Use `VALID BEGIN '...' VALID UNTIL '...'` for account validity and `ACCOUNT LOCK` to lock an account.
- Use `WITH INDEPENDENT` to create a private user.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
CREATE TABLESPACE fastspace RELATIVE LOCATION 'tablespace/tablespace_1';

CREATE USER joe WITH PASSWORD 'Bigdata@123'
    VALID BEGIN '2026-01-01 08:00:00' VALID UNTIL '2027-01-01 08:00:00';
ALTER USER user_read ACCOUNT LOCK;

CREATE USER user_independent WITH INDEPENDENT IDENTIFIED BY '1234@abc';
```

#### Expected Console / Query Output:
```text
CREATE TABLESPACE
CREATE ROLE
ALTER ROLE
CREATE ROLE
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [True / False]
**(Official Ch.04 Quiz Q1) Users and roles have the same syntax in the openGauss database. Therefore, they are fully equivalent.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.04 p. 314 & p. 346). Although users and roles share the same O&M syntax, a user is an entity with `LOGIN` permission by default (`rolcanlogin = true`), whereas a role is a set of permissions that does not have login permission by default.
</details>

### Question 2 [Single-Choice]
**What happens in openGauss when the disk usage of a partition where a tablespace resides reaches 90%?**

- A. The database automatically deletes the oldest partition in the tablespace
- B. The database switches to read-only mode until disk usage drops below 90%
- C. The database immediately shuts down the cluster via `gs_om -t stop`
- D. The database converts all row-store tables in the tablespace into MOTs

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 04 (p. 307), if the usage of a disk where a tablespace resides reaches 90%, the database switches to read-only mode, and switches back to read/write mode when disk usage becomes less than 90%.
</details>

### Question 3 [Single-Choice]
**Which user attribute in openGauss creates a 'private user' whose objects can be managed (`DROP`, `ALTER`, `TRUNCATE`) by database administrators, but whose data cannot be accessed (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `COPY`) by administrators without explicit authorization?**

- A. SYSADMIN
- B. INDEPENDENT
- C. AUDITADMIN
- D. VCADMIN

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 04 (p. 321), creating a user with the `INDEPENDENT` attribute (`CREATE USER ... WITH INDEPENDENT`) isolates control permissions (`DROP`, `ALTER`, `TRUNCATE`) from data access permissions (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `COPY`).
</details>
