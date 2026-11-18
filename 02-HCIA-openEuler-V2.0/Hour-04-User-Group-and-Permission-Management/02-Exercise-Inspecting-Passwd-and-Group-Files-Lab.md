# 💻 Hands-On Lab: Auditing `/etc/passwd` and `/etc/group` Field Structures

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 04 — User, Group & File Permission Management (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-User-and-Group-Architecture-and-Config-Files`  
**Interactive Workbench:** Open **[`02-Exercise-Inspecting-Passwd-and-Group-Files-Lab.html`](./02-Exercise-Inspecting-Passwd-and-Group-Files-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are performing a security audit of user accounts on openEuler. Inspect the `root` and `openeuler` entries in `/etc/passwd`, extract usernames and login shells (fields 1 and 7), and inspect `/etc/group`.

### 📋 Step-by-Step Instructions
1. Step 1: Use `grep` to view the `root` entry in `/etc/passwd` (`grep '^root:' /etc/passwd`).
2. Step 2: Use `awk -F: '{print 1, 3, $7}' /etc/passwd` to print the username (field 1), UID (field 3), and login shell (field 7).
3. Step 3: View the first 5 lines of `/etc/group` using `head -n 5 /etc/group`.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Match the root user line in /etc/passwd
<grep_root_command>

# Step 2: Print username (1), UID (3), and login shell ($7) from /etc/passwd
<awk_passwd_command>

# Step 3: View the first 5 lines of /etc/group
<head_group_command>
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `grep '^root:' /etc/passwd`.
- Use `awk -F: '{print 1, 3, $7}' /etc/passwd`.
- Use `head -n 5 /etc/group`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Match the root user line in /etc/passwd
grep '^root:' /etc/passwd

# Step 2: Print username (1), UID (3), and login shell ($7) from /etc/passwd
awk -F: '{print 1, 3, $7}' /etc/passwd

# Step 3: View the first 5 lines of /etc/group
head -n 5 /etc/group
```

#### Expected Console / Query Output:
```text
root:x:0:0:Super User:/root:/bin/bash

root 0 /bin/bash
bin 1 /usr/sbin/nologin
daemon 2 /usr/sbin/nologin
openeuler 1000 /bin/bash

root:x:0:
bin:x:1:
daemon:x:2:
sys:x:3:
adm:x:4:
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In openEuler, what are the standard UID ranges for the Superuser, Virtual (system) users, and Common (regular) users respectively?**

- A. Superuser: 1; Virtual users: 2–500; Common users: 501–10000
- B. Superuser: 0; Virtual users: 1–999; Common users: 1000–60000
- C. Superuser: 0; Virtual users: 1000–1999; Common users: 2000–65535
- D. Superuser: 1000; Virtual users: 0–999; Common users: 1001+

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p.160), the Superuser (root) has UID 0, Virtual (system) users have UIDs ranging from 1 to 999, and Common (normal/regular) users have UIDs ranging from 1000 to 60000.
</details>

### Question 2 [Single-Choice]
**In the `/etc/passwd` file, what do the 3rd, 4th, 6th, and 7th colon-separated columns represent?**

- A. UID, GID, User home directory, User login shell
- B. Password hash, UID, User description, Mailbox path
- C. GID, UID, Login shell, Home directory
- D. Username, Password placeholder, Home directory, Group list

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Per Ch.04 (p.161), the 7 columns of `/etc/passwd` are: (1) username, (2) password placeholder, (3) UID, (4) GID, (5) user description, (6) user home directory, and (7) user login shell.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about user groups and `/etc/group` are TRUE?**

- A. Each user has only one private (primary) group, but can belong to multiple public (additional) groups.
- B. Actual encrypted user passwords are stored in `/etc/shadow`, while group passwords are in `/etc/gshadow`.
- C. If a user appears in the 4th column of `/etc/group`, that group serves as a supplementary (additional) group for the user.
- D. If a group is a user's private group, the user's name does NOT appear in the 4th column of `/etc/group`.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.04 (pp.161–162), all four statements are explicitly documented in the official material.
</details>
