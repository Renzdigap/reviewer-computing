# DNF Repository, Package & Package Group Management (`dnf`, `dnf config-manager`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 05 — Software Packages, systemd Services, Processes & Scheduled Tasks (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.04, pp. 207–214

---

## Learning Objectives
- Add, list, enable, and disable repositories using `dnf config-manager` (`--add-repo`, `--set-enable`, `--set-disable`) and `dnf repolist`
- Search, list, inspect, download (with dependencies), install, and remove RPM packages using `dnf`
- Query, install, and remove software package groups (`dnf groups summary`, `dnf group list`, `dnf group install`, `dnf group remove`)

---

### 1. Managing Repositories with `dnf config-manager` and `dnf repolist`
Only the **`root`** user can add, enable, or disable `.repo` files in `/etc/yum.repos.d/`:
* **Add a New Repository:**
  ```bash
  dnf config-manager --add-repo repository_url
  ```
  Automatically generates a corresponding `.repo` file inside `/etc/yum.repos.d/`.
* **View Repository IDs:**
  ```bash
  dnf repolist
  ```
* **Enable or Disable a Repository by ID:**
  ```bash
  dnf config-manager --set-enable repository_id
  dnf config-manager --set-disable repository_id
  ```

---

### 2. Searching, Listing, Downloading, Installing & Removing Packages
| Task | DNF Command Syntax & Key Options |
| :--- | :--- |
| **Search by keyword** | **`dnf search term`** (searches package names, abbreviations, and descriptions). |
| **List packages** | **`dnf list all`** (lists all installed and available packages) or **`dnf list glob_expression...`**. |
| **View package details** | **`dnf info package_name...`** |
| **Download RPMs** | **`dnf download package_name`**. To also download uninstalled dependencies, add **`--resolve`**: **`dnf download --resolve package_name`**. |
| **Install packages** | **`dnf install package_name`**. When installing multiple packages simultaneously (`dnf install pkg1 pkg2 --setopt=strict=0` or `strict=False` in `/etc/dnf/dnf.conf`), available packages are still installed even if one package name is unavailable. |
| **Remove packages** | **`dnf remove package_name...`** |

---

### 3. Managing Software Package Groups (`dnf group`)
A **package group** is a curated collection of related software packages (such as `System Tools` or `Development Tools`) identified by both a **group name** and a **group ID**:
* **View Summary of Installed & Available Groups:**
  ```bash
  dnf groups summary
  ```
* **List All Package Groups and Group IDs:**
  ```bash
  dnf group list
  ```
* **Install or Remove a Package Group:**
  ```bash
  dnf group install group_name/groupid
  dnf group remove group_name/groupid
  ```

---

## Key Takeaways
- **Use 'dnf config-manager --add-repo <url>' to add a repository in /etc/yum.repos.d/, 'dnf repolist' to check repo IDs, and '--set-enable' / '--set-disable' to toggle them.**
- **Use 'dnf download --resolve <pkg>' to download an RPM package along with all its uninstalled dependency packages.**
- **Use 'dnf groups summary' and 'dnf group list' to inspect software package groups, and 'dnf group install <name/id>' or 'dnf group remove <name/id>' to manage them.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Only the root user can add a .repo file or run 'dnf config-manager --add-repo' / '--set-enable' / '--set-disable'.

> [!WARNING]
> EXAM TRAP: When installing multiple packages at once with 'dnf install pkg1 pkg2', adding '--setopt=strict=0' (or setting 'strict=False' in /etc/dnf/dnf.conf) allows DNF to skip unavailable packages and continue installing valid ones.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab.html`](./04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab.html)** (or [`04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab.md`](./04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab.md)) to apply this concept in an interactive lab workbench!
