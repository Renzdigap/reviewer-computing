# 💻 Hands-On Lab: Provisioning Accounts, Group Memberships (`gpasswd`) & Password Aging (`chage`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 04 — User, Group & File Permission Management (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-User-and-Group-Lifecycle-Commands`  
**Interactive Workbench:** Open **[`04-Exercise-User-Group-and-Password-Aging-Lab.html`](./04-Exercise-User-Group-and-Password-Aging-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are onboarding a developer account `dev01` with UID `1500` and a custom group `devops` with GID `2000`. Create the group and user, add `dev01` to `devops` using `gpasswd -a`, set the maximum password validity period to 90 days using `chage -M 90 dev01`, and remove a temporary account `tempuser` along with its home directory.

### 📋 Step-by-Step Instructions
1. Step 1: Create the group `devops` with GID `2000` (`groupadd -g 2000 devops`) and create user `dev01` with UID `1500` (`useradd -u 1500 dev01`).
2. Step 2: Add `dev01` to the `devops` group using `gpasswd -a dev01 devops` and set `dev01`'s maximum password validity period to 90 days using `chage -M 90 dev01`.
3. Step 3: Delete user `tempuser` and all of its home directory files recursively using `userdel -r tempuser`.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Create group devops (GID 2000) and user dev01 (UID 1500)
<groupadd_command>
<useradd_command>

# Step 2: Add dev01 to devops using gpasswd and set max password age to 90 days
<gpasswd_command>
<chage_command>

# Step 3: Delete tempuser and its home directory
<userdel_command>
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `groupadd -g 2000 devops` and `useradd -u 1500 dev01`.
- Use `gpasswd -a dev01 devops` and `chage -M 90 dev01`.
- Use `userdel -r tempuser` so the home directory is also removed.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Create group devops (GID 2000) and user dev01 (UID 1500)
groupadd -g 2000 devops
useradd -u 1500 dev01

# Step 2: Add dev01 to devops using gpasswd and set max password age to 90 days
gpasswd -a dev01 devops
chage -M 90 dev01

# Step 3: Delete tempuser and its home directory
userdel -r tempuser
```

#### Expected Console / Query Output:
```text
Adding user dev01 to group devops
[root@openEuler ~]# id dev01
uid=1500(dev01) gid=1500(dev01) groups=1500(dev01),2000(devops)
[root@openEuler ~]# chage -l dev01 | grep Maximum
Maximum number of days between password change		: 90
[root@openEuler ~]# userdel -r tempuser
[OK] tempuser and /home/tempuser removed.
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Which command and option should be used to delete a user account `Test` along with their home directory and all files inside it?**

- A. userdel Test
- B. userdel -r Test
- C. userdel -h Test
- D. groupdel -f Test

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p.165), if you do not add any options to `userdel`, only the user account is deleted. To delete the user's home directory and all contents recursively, run `userdel -r Test`.
</details>

### Question 2 [Single-Choice]
**Why does the official openEuler documentation recommend `gpasswd -a user_name group_name` over `usermod -G group_name user_name` when adding a user to a supplementary group?**

- A. Because `usermod -G` cannot be run by the root user.
- B. Because `usermod -G group_name user_name` removes the user from any previous supplementary groups, whereas `gpasswd -a` retains previous groups.
- C. Because `gpasswd` automatically changes the user's UID to 0.
- D. Because `usermod -G` deletes `/etc/group`.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p.168), `usermod -G group_name user_name` adds a user to a specified group, but removes the user from any previous groups. `gpasswd -a` adds the user while retaining previous groups.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about `passwd` and `chage` are TRUE?**

- A. Only the `root` user can change any user's password, while common users can change only their own passwords.
- B. `passwd -l` locks a user password so the locked user cannot log in to the system, while `passwd -u` unlocks it.
- C. `chage -l user_name` checks the password expiration information of a specified user.
- D. `chage -M` sets the maximum validity period of a password.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.04 (pp.166–167), all four statements accurately describe `passwd` and `chage`.
</details>
