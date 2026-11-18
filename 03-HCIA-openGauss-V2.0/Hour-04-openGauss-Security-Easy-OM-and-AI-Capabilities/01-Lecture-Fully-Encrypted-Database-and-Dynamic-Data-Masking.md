# High Security Part 1 — Fully-Encrypted Database & Dynamic Data Masking

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 04 — openGauss High Security, Easy O&M & AI Capabilities (DBMind) (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-Resource-Labels-and-Dynamic-Masking-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.03, pp. 199–208

---

## Learning Objectives
- Explain the 3-layer key hierarchy (Root Key, CMK, CEK) and workflow of Fully-Encrypted Equality Queries
- Create Resource Labels (`CREATE RESOURCE LABEL`) and Dynamic Data Masking Policies (`CREATE MASKING POLICY`)
- Compare all 7 preset masking functions (`creditcardmasking`, `basicemailmasking`, `fullemailmasking`, `alldigitsmasking`, `shufflemasking`, `randommasking`, `maskall`) and their constraints

---

### 1. Equality Query in a Fully-Encrypted Database (pp. 56, 200–204)
Protects data privacy across its **entire lifecycle (transmission, computing, and storage)** so data on the server is always in ciphertext — even cloud admins or attackers with root access cannot read plaintext data:
- **3-Layer Key Hierarchy & Workflow (p. 201)**:
  1. **Root Key (RK)**: Managed locally via `keytool` on the client host.
  2. **Client Master Key (`CMK`)**: Stored on the client side and registered in the database metadata; used to encrypt the CEK.
  3. **Column Encryption Key (`CEK`)**: Encrypted by the CMK on the client and stored as ciphertext on the server; used by the **client driver (`ODBC`/`JDBC`/`gsql -C`)** to encrypt/decrypt column data.
  - **Encryption Types (`enc_type`)**: **`DETERMINISTIC`** (supports equality queries `=`; server column type becomes `BYTEAWITHOUTORDERWITHEQUALCOL`) vs. **`RANDOMIZED`** (higher security, non-deterministic ciphertext).
  - **Hardware TEE Support**: Can leverage Intel SGX / Huawei Kunpeng ARM **TEE (`secGear`)** for isolated computation.

---

### 2. Dynamic Data Masking (pp. 205–208)
Masks sensitive column data dynamically at query time (`SELECT`) based on the user's identity (`ROLES`), client tool (`APP`), and IP (`IP`) **without modifying the underlying stored data**:
```sql
-- Step 1: Create Resource Labels on target table columns
CREATE RESOURCE LABEL label_for_creditcard ADD COLUMN(user1.table1.creditcard);
CREATE RESOURCE LABEL label_for_name ADD COLUMN(user1.table1.name);

-- Step 2: Create Masking Policies bound to Resource Labels
CREATE MASKING POLICY msk_creditcard creditcardmasking ON LABEL(label_for_creditcard);
CREATE MASKING POLICY msk_name randommasking ON LABEL(label_for_name)
    FILTER ON IP(local), ROLES(dev);
```

---

### 3. Seven Preconfigured Masking Functions & Constraints (pp. 207–208)

| Preset Masking Function | Masking Rule | Official Example (`Input` -> `Output`) |
| :--- | :--- | :--- |
| **`creditcardmasking`** | Masks all digits **except the last 4 digits** with `'x'` | `'4880-9898-4545-2525'` -> **`'xxxx-xxxx-xxxx-2525'`** |
| **`basicemailmasking`** | Masks all text **before `@`** with `'x'` | `'abcd@mymail.com'` -> **`'xxxx@mymail.com'`** |
| **`fullemailmasking`** | Masks text **before the first dot (`.`) (except `@`)** with `'x'` | `'abcd@gmail.com'` -> **`'xxxx@xxxxx.com'`** |
| **`alldigitsmasking`** | Masks **only digits** with `'0'` | `'alex123alex'` -> **`'alex000alex'`** |
| **`shufflemasking`** | Randomly shuffles character positions (weak masking) | `'hello world'` -> **`'hlwoeor dl'`** |
| **`randommasking`** | Randomly replaces each character | `'hello world'` -> **`'ad5f5ghdf5'`** |
| **`maskall`** | Replaces every character with `'x'` | `'4880-9898-4545-2525'` -> **`'xxxxxxxxxxxxxxxxxxx'`** |

- **Key Constraints (p. 208)**:
  - Must be created by **`POLADMIN`**, **`SYSADMIN`**, or the **initial user** (with GUC `enable_security_policy = on`).
  - Maximum of **98 dynamic data masking policies**; only the **7 preset masking functions** above can be used.
  - Applies **only to `COLUMN` resource labels on base tables** and takes effect **only on `SELECT`** queries (Note: `INSERT INTO ... SELECT` or `MERGE INTO` from a masked source column permanently writes the **masked value**!).

---

## Key Takeaways
- **In a Fully-Encrypted Database, the Client Master Key (CMK) encrypts the Column Encryption Key (CEK), and the client driver encrypts/decrypts data so the server only ever sees ciphertext.**
- **Dynamic Data Masking uses Resource Labels (`CREATE RESOURCE LABEL ... ADD COLUMN(...)`) and Masking Policies (`CREATE MASKING POLICY ... ON LABEL(...)`) and supports 7 preset functions.**
- **`basicemailmasking` masks only before `@` (`xxxx@gmail.com`), whereas `fullemailmasking` masks everything before the last domain dot except `@` (`xxxx@xxxxx.com`).**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Dynamic Data Masking can only be created by a user with `POLADMIN`, `SYSADMIN`, or initial user privileges, supports at most 98 policies, and only masks `SELECT` queries on base table columns.

> [!WARNING]
> EXAM TRAP: If a user subject to dynamic masking runs `INSERT INTO t2 SELECT masked_col FROM t1`, the inserted data in `t2` is the MASKED value and cannot be restored!

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Resource-Labels-and-Dynamic-Masking-Lab.html`](./02-Exercise-Resource-Labels-and-Dynamic-Masking-Lab.html)** (or [`02-Exercise-Resource-Labels-and-Dynamic-Masking-Lab.md`](./02-Exercise-Resource-Labels-and-Dynamic-Masking-Lab.md)) to apply this concept in an interactive lab workbench!
