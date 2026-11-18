# 💻 Hands-On Lab: Configuring Fine-Grained ACLs (`setfacl`/`getfacl`) and Passwordless `sudo`

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 04 — User, Group & File Permission Management (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Sticky-Bit-ACL-and-Privilege-Escalation`  
**Interactive Workbench:** Open **[`08-Exercise-ACL-and-Sudo-Configuration-Lab.html`](./08-Exercise-ACL-and-Sudo-Configuration-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You need to grant user `test` read-write (`rw`) access to `/root/report.txt` without changing its owner or group by using `setfacl`, verify the ACL with `getfacl`, and configure a drop-in `/etc/sudoers.d/test` rule allowing user `test` to run `/usr/bin/touch` as `root` without a password.

### 📋 Step-by-Step Instructions
1. Step 1: Grant user `test` `rw-` permissions on `/root/report.txt` using `setfacl -m u:test:rw /root/report.txt`.
2. Step 2: Display the ACL entries of `/root/report.txt` using `getfacl /root/report.txt`.
3. Step 3: Write the sudoers rule `test ALL=(root) NOPASSWD:/usr/bin/touch` into `/etc/sudoers.d/test`.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Set ACL granting user 'test' rw permissions on /root/report.txt
<setfacl_command>

# Step 2: Query the ACL of /root/report.txt
<getfacl_command>

# Step 3: Create /etc/sudoers.d/test granting passwordless /usr/bin/touch
echo "<sudoers_rule>" > /etc/sudoers.d/test
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `setfacl -m u:test:rw /root/report.txt`.
- Use `getfacl /root/report.txt`.
- Include `NOPASSWD:/usr/bin/touch` in the `/etc/sudoers.d/test` echo statement.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Set ACL granting user 'test' rw permissions on /root/report.txt
setfacl -m u:test:rw /root/report.txt

# Step 2: Query the ACL of /root/report.txt
getfacl /root/report.txt

# Step 3: Create /etc/sudoers.d/test granting passwordless /usr/bin/touch
echo "test ALL=(root) NOPASSWD:/usr/bin/touch" > /etc/sudoers.d/test
```

#### Expected Console / Query Output:
```text
# file: root/report.txt
# owner: root
# group: root
user::rw-
user:test:rw-
group::r--
mask::rw-
other::r--

[root@openEuler ~]# ls -l /root/report.txt
-rw-rw-r--+ 1 root root 0 Nov 17 10:00 /root/report.txt
[root@openEuler ~]# cat /etc/sudoers.d/test
test ALL=(root) NOPASSWD:/usr/bin/touch
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**When the Sticky Bit (`drwxrwxrwt`) is enabled on a shared directory such as `/share`, who is permitted to rename or remove a file inside `/share`?**

- A. Any user in the system who has read and execute permissions on `/share`
- B. Only the file owner, the directory owner, or the `root` user
- C. Only users with a UID greater than 1000
- D. Nobody, not even `root`, until the Sticky Bit is removed

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p.184), a sticky bit is a special permission set on a directory. When enabled, only the file owner, the directory owner, or the `root` user can rename or remove files within that directory.
</details>

### Question 2 [Single-Choice]
**When `ls -l filename` is executed, what character displayed immediately after the 9 permission bits (e.g., `-rw-rw-r--+`) indicates that the file has an Access Control List (ACL) configured, and which `setfacl` option deletes all ACL parameters?**

- A. `.` (dot); `setfacl -m`
- B. `+` (plus sign); `setfacl -b`
- C. `*` (asterisk); `setfacl -d`
- D. `@` (at sign); `setfacl -R`

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p.185 & p.187), if a plus sign (`+`) is displayed next to the file permission in `ls -l`, the file has an ACL. `setfacl -b` deletes all ACL parameters.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements accurately compare `su` and `sudo` in openEuler?**

- A. `su` requires the password of the target user (e.g., `root`), whereas `sudo` requires the password of the current user.
- B. By default, commands executed via `sudo` are recorded in audit logs, whereas commands executed after `su` are not recorded.
- C. In `/etc/sudoers`, a `%` symbol before a name (such as `%wheel`) indicates privilege escalation for a user group.
- D. `sudo -k` forces the user to enter a password upon the next execution of `sudo`, even within the default 5-minute timeout window.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.04 (pp.190–193), all four statements match the official Huawei training material.
</details>
