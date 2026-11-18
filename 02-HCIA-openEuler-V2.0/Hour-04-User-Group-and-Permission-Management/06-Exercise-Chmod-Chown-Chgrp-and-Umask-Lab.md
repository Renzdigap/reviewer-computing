# 💻 Hands-On Lab: Modifying Permissions (`chmod`), Dual Ownership (`chown`) & `umask`

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 04 — User, Group & File Permission Management (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-File-Permissions-Ownership-and-umask`  
**Interactive Workbench:** Open **[`06-Exercise-Chmod-Chown-Chgrp-and-Umask-Lab.html`](./06-Exercise-Chmod-Chown-Chgrp-and-Umask-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are securing the directory `usertxt` on openEuler (following the exact official lab on pp. 177–183). Set its permissions to `644`, change both its owner and group to `user:usergroup` using `chown`, change its group to `usergroup01` using `chgrp`, and set the system `umask` to `022`.

### 📋 Step-by-Step Instructions
1. Step 1: Modify the permissions of `usertxt` to `644` using `chmod 644 usertxt`.
2. Step 2: Change both the owner and group of `usertxt` to `user:usergroup` using `chown user:usergroup usertxt`, then change its group to `usergroup01` using `chgrp usergroup01 usertxt`.
3. Step 3: Set the preset permission mask to `022` using `umask 022`.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Set permissions of usertxt to 644
<chmod_command>

# Step 2: Change owner and group to user:usergroup, then group to usergroup01
<chown_command>
<chgrp_command>

# Step 3: Set permission mask to 022
<umask_command>
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `chmod 644 usertxt`.
- Use `chown user:usergroup usertxt` and `chgrp usergroup01 usertxt` (exact commands from Ch.04 pp.179, 181).
- Use `umask 022`.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Set permissions of usertxt to 644
chmod 644 usertxt

# Step 2: Change owner and group to user:usergroup, then group to usergroup01
chown user:usergroup usertxt
chgrp usergroup01 usertxt

# Step 3: Set permission mask to 022
umask 022
```

#### Expected Console / Query Output:
```text
[root@openEuler ~]# ls -ld usertxt
drw-r--r--. 2 user usergroup01 4096 Jun  8 11:10 usertxt
[root@openEuler ~]# umask
0022
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In the output of `ls -l`, what does the first character `c` vs. `b` represent in the file type and permission string?**

- A. `c` = compressed file; `b` = binary executable
- B. `c` = character device file (e.g., keyboard/mouse); `b` = block device file (random access storage)
- C. `c` = configuration file; `b` = boot loader file
- D. `c` = socket file; `b` = named pipe file

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p.172), `b` indicates a block device file (random access device) and `c` indicates a character device file (one-time read device such as keyboard and mouse).
</details>

### Question 2 [Single-Choice]
**According to the openEuler `umask` table, if the `umask` value is set to `027`, what are the default permissions for newly created files and directories respectively?**

- A. File: 644; Directory: 755
- B. File: 640; Directory: 750
- C. File: 664; Directory: 775
- D. File: 660; Directory: 770

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p.182), when `umask` is `027`, the default file permission is `640` and the default directory permission is `750`.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about directory permissions (`r`, `w`, `x`) and ownership commands are TRUE?**

- A. Having `w` (write) permission on a directory allows a user to create, delete, or move files within that directory.
- B. Having `x` (execute) permission on a directory allows a user to access (`cd` into) that directory.
- C. `chown user:usergroup file` modifies both the file owner and the file owner group at the same time.
- D. Any common user can run `chown` to transfer ownership of their files to `root`.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.04 (pp.174–179), A, B, and C are true. Option D is false because the usage permission for `chown` is restricted to the administrator (`root`).
</details>
