# Hands-On Lab: Configuring Row-Level Security (RLS) & Unified Audit Policies

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 04 — openGauss High Security, Easy O&M & AI Capabilities (DBMind) (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-RBAC-Row-Level-Security-Unified-Auditing-and-TDE`  
**Interactive Workbench:** Open **[`04-Exercise-RLS-and-Unified-Audit-Policy-Lab.html`](./04-Exercise-RLS-and-Unified-Audit-Policy-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Enable Row-Level Security on `tb_for_audit` so each user can only query rows where `role = CURRENT_USER`, and create a Unified Audit Policy `adt3` that audits `CREATE` operations on resource label `adt_lb0` for role `dev_audit`.

### Step-by-Step Instructions
1. Step 1: Enable RLS on `tb_for_audit` using `ALTER TABLE tb_for_audit ENABLE ROW LEVEL SECURITY;`.
2. Step 2: Create RLS policy `tb_rls` on `tb_for_audit` with `CREATE ROW LEVEL SECURITY POLICY tb_rls ON tb_for_audit USING(role = CURRENT_USER);`.
3. Step 3: Create unified audit policy `adt3` with `CREATE AUDIT POLICY adt3 PRIVILEGES CREATE ON LABEL(adt_lb0) FILTER ON ROLES(dev_audit);`.

### Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Enable Row-Level Security on tb_for_audit
ALTER TABLE tb_for_audit ENABLE ____;

-- Step 2: Create RLS policy so users only see rows where role = CURRENT_USER
CREATE ROW LEVEL SECURITY POLICY tb_rls ON tb_for_audit ____(role = CURRENT_USER);

-- Step 3: Create Unified Audit Policy adt3 auditing CREATE on adt_lb0 for dev_audit
CREATE ____ POLICY adt3 PRIVILEGES CREATE ON LABEL(adt_lb0) FILTER ON ROLES(dev_audit);
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `ALTER TABLE <table_name> ENABLE ROW LEVEL SECURITY;`.
- In `CREATE ROW LEVEL SECURITY POLICY`, use the `USING(role = CURRENT_USER)` clause.
- Use `CREATE AUDIT POLICY adt3 PRIVILEGES CREATE ON LABEL(adt_lb0) FILTER ON ROLES(dev_audit);`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
ALTER TABLE tb_for_audit ENABLE ROW LEVEL SECURITY;

CREATE ROW LEVEL SECURITY POLICY tb_rls ON tb_for_audit USING(role = CURRENT_USER);

CREATE AUDIT POLICY adt3 PRIVILEGES CREATE ON LABEL(adt_lb0) FILTER ON ROLES(dev_audit);
```

#### Expected Console / Query Output:
```text
ALTER TABLE
CREATE ROW LEVEL SECURITY POLICY
CREATE AUDIT POLICY
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Which SQL operations can be restricted by a Row-Level Security (RLS) policy in openGauss?**

- A. SELECT, INSERT, UPDATE, and DELETE
- B. SELECT, UPDATE, and DELETE only (not INSERT or MERGE)
- C. INSERT and MERGE only
- D. CREATE, ALTER, and DROP only

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Chapter 03 (pp. 213, 215), Row-Level Security policies can be applied only to `SELECT`, `UPDATE`, and `DELETE` operations, and cannot be applied to `INSERT` and `MERGE` operations.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**Which of the following statements about Transparent Data Encryption (TDE) in openGauss are TRUE?**

- A. TDE uses a three-layer key structure: Root Key (RK), Cluster Master Key (CMK), and Data Encryption Key (DEK)
- B. TDE supports `AES_128_CTR` (default) and `SM4_CTR` encryption algorithms
- C. If the encryption function is not enabled when a table is created, the table cannot later be switched to an encrypted table
- D. TDE supports encrypting column-store tables, Ustore tables, indexes, and Xlogs

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 03 (pp. 225–226), A, B, and C are true. Option D is false: TDE supports only heap row-store tables; column-store, Ustore, materialized views, indexes, sequences, Xlogs, and MOTs are NOT supported.
</details>

### Question 3 [True / False]
**In openGauss Unified Auditing, a single unified audit policy can simultaneously audit both DDL operations (`PRIVILEGES`) and DML operations (`ACCESS`).**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.03 p. 224). The unified audit policy syntax applies to either DDL or DML operations; a single unified audit policy cannot contain both DDL and DML operations.
</details>
