# 💻 Hands-On Lab: Repository Management (`dnf config-manager`), Dependency Download & Group Installation

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 05 — Software Packages, systemd Services, Processes & Scheduled Tasks (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-DNF-Package-and-Group-Management`  
**Interactive Workbench:** Open **[`04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab.html`](./04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
You are configuring software packages on an openEuler node. Add the local repository `file:///mnt/local_repo` using `dnf config-manager`, download the `httpd` package along with its uninstalled dependencies, and list all available DNF package groups.

### 📋 Step-by-Step Instructions
1. Step 1: Add the repository `file:///mnt/local_repo` using `dnf config-manager --add-repo file:///mnt/local_repo`.
2. Step 2: Download the `httpd` RPM package and all its uninstalled dependencies using `dnf download --resolve httpd`.
3. Step 3: List all installed and available software package groups using `dnf group list`.

### 📝 Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Add local repository file:///mnt/local_repo
<dnf_add_repo_command>

# Step 2: Download httpd package and its uninstalled dependencies
<dnf_download_command>

# Step 3: List all software package groups
<dnf_group_list_command>
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- Use `dnf config-manager --add-repo file:///mnt/local_repo`.
- Use `dnf download --resolve httpd` (Ch.04 p.212).
- Use `dnf group list` (Ch.04 p.213).

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Add local repository file:///mnt/local_repo
dnf config-manager --add-repo file:///mnt/local_repo

# Step 2: Download httpd package and its uninstalled dependencies
dnf download --resolve httpd

# Step 3: List all software package groups
dnf group list
```

#### Expected Console / Query Output:
```text
Adding repo from: file:///mnt/local_repo

Last metadata expiration check: 0:00:05 ago.
(1/3): apr-1.7.4-1.oe2403.aarch64.rpm          125 kB/s | 108 kB     00:00
(2/3): apr-util-1.6.3-1.oe2403.aarch64.rpm     110 kB/s |  92 kB     00:00
(3/3): httpd-2.4.58-1.oe2403.aarch64.rpm       1.2 MB/s | 1.4 MB     00:01

Available Environment Groups:
   Minimal Install
   Server
Available Groups:
   Development Tools
   System Tools
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Which command generates a new `.repo` configuration file in `/etc/yum.repos.d/` from a specified repository URL?**

- A. `dnf repolist --create repository_url`
- B. `dnf config-manager --add-repo repository_url`
- C. `createrepo --url repository_url`
- D. `rpm -ivh repository_url`

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p.207), running `dnf config-manager --add-repo repository_url` as user `root` automatically generates the corresponding `.repo` file in `/etc/yum.repos.d/`.
</details>

### Question 2 [Single-Choice]
**When using `dnf download package_name` to download an RPM file without installing it, which option must be added to also download any uninstalled dependencies?**

- A. --nodeps
- B. --resolve
- C. --allmatches
- D. --database

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p.212), if you need to download a dependency that is not installed, add `--resolve` (`dnf download --resolve package_name`).
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following DNF commands are valid for managing software repositories and package groups in openEuler?**

- A. `dnf config-manager --set-enable repository`
- B. `dnf config-manager --set-disable repository`
- C. `dnf groups summary` and `dnf group list`
- D. `dnf group install group_name/groupid` and `dnf group remove group_name/groupid`

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.04 (pp.208, 213–214), all four command sets are standard DNF operations in openEuler.
</details>
