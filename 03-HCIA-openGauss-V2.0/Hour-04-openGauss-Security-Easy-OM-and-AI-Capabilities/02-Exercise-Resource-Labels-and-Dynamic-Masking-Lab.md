# Hands-On Lab: Configuring Resource Labels & Dynamic Data Masking Policies

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 04 — openGauss High Security, Easy O&M & AI Capabilities (DBMind) (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-Fully-Encrypted-Database-and-Dynamic-Data-Masking`  
**Interactive Workbench:** Open **[`02-Exercise-Resource-Labels-and-Dynamic-Masking-Lab.html`](./02-Exercise-Resource-Labels-and-Dynamic-Masking-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Protect customer privacy on `user1.table1`: create a resource label `label_for_creditcard` on column `user1.table1.creditcard` and apply the `creditcardmasking` policy `msk_creditcard` so only the last 4 digits are visible.

### Step-by-Step Instructions
1. Step 1: Create the resource label using `CREATE RESOURCE LABEL label_for_creditcard ADD COLUMN(user1.table1.creditcard);`.
2. Step 2: Create the masking policy using `CREATE MASKING POLICY msk_creditcard creditcardmasking ON LABEL(label_for_creditcard);`.
3. Step 3: Query `SELECT creditcard FROM user1.table1;` to verify the masked output.

### Starter Workspace (`openGauss=#`)
```bash
-- Step 1: Create a resource label on user1.table1.creditcard
CREATE ____ LABEL label_for_creditcard ADD COLUMN(user1.table1.creditcard);

-- Step 2: Create a masking policy using creditcardmasking
CREATE ____ POLICY msk_creditcard ____ ON LABEL(label_for_creditcard);

-- Step 3: Query the masked column
SELECT creditcard FROM user1.table1;
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `CREATE RESOURCE LABEL <label_name> ADD COLUMN(<schema.table.col>);`.
- Use `CREATE MASKING POLICY <policy_name> creditcardmasking ON LABEL(<label_name>);`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
CREATE RESOURCE LABEL label_for_creditcard ADD COLUMN(user1.table1.creditcard);

CREATE MASKING POLICY msk_creditcard creditcardmasking ON LABEL(label_for_creditcard);

SELECT creditcard FROM user1.table1;
```

#### Expected Console / Query Output:
```text
CREATE RESOURCE LABEL
CREATE MASKING POLICY
     creditcard      
---------------------
 xxxx-xxxx-xxxx-2525
(1 row)
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In openGauss Dynamic Data Masking, how will the string `'abcd@gmail.com'` be displayed when masked by `basicemailmasking` versus `fullemailmasking`?**

- A. `basicemailmasking`: `'xxxx@gmail.com'`; `fullemailmasking`: `'xxxx@xxxxx.com'`
- B. `basicemailmasking`: `'xxxx@xxxxx.com'`; `fullemailmasking`: `'xxxxxxxxxxxxxx'`
- C. `basicemailmasking`: `'a***@gmail.com'`; `fullemailmasking`: `'a***@g****.com'`
- D. `basicemailmasking`: `'abcd@xxxxx.com'`; `fullemailmasking`: `'xxxx@gmail.com'`

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Per Chapter 03 (p. 207), `basicemailmasking` masks all text before `@` (`'xxxx@gmail.com'`), whereas `fullemailmasking` masks all text before the first dot `.` except `@` (`'xxxx@xxxxx.com'`).
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**Which of the following statements about openGauss Fully-Encrypted Database equality queries are TRUE?**

- A. It uses a three-layer key hierarchy consisting of the Root Key, Client Master Key (CMK), and Column Encryption Key (CEK)
- B. The CEK is encrypted by the CMK on the client and stored in ciphertext on the database server
- C. Data is encrypted and decrypted on the client side, while the server processes ciphertext
- D. Plaintext encryption keys are stored in the `pg_class` system catalog on the server so the server can decrypt columns before comparison

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Chapter 01 (p. 56) and Chapter 03 (p. 201), A, B, and C are true. Option D is false: plaintext key information is NEVER stored on the database server, and the server cannot decrypt ciphertext.
</details>

### Question 3 [True / False]
**In openGauss, any ordinary database user can create a Dynamic Data Masking policy on tables within the `public` schema.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False (Ch.03 p. 208). A dynamic data masking policy must be created by a user with the `POLADMIN` or `SYSADMIN` attribute, or by the initial user.
</details>
