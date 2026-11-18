# 📖 RPM Package Management & DNF Repository Configuration (`rpm`, `createrepo`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 05 — Software Packages, systemd Services, Processes & Scheduled Tasks (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-RPM-Queries-and-Local-Repo-Creation-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.04, pp. 194–206

---

## 🎯 Learning Objectives
- Parse the standard RPM package naming format (`name-version-release.arch.rpm`) and execute install, upgrade, uninstall, and query commands (`rpm`)
- Explain why DNF ('next-generation YUM') outperforms YUM using `libsolv` and Python 3 plugins
- Configure `/etc/dnf/dnf.conf`, `/etc/yum.repos.d/*.repo` files, and local software repositories using `createrepo`

---

### 1. RPM Package Naming & Core `rpm` Commands
* **RPM Naming Format:** `name-version-release.arch.rpm` (e.g., `iSulad-2.0.11-1.oe2203.aarch64.rpm`).
* **Installation, Upgrade & Removal:**
  * **`rpm -ivh example.rpm`:** Installs a package (`-i` install, `-v` verbose details, `-h` hash `#` progress bar).
  * **`rpm -Uvh example.rpm`:** Upgrades a package (replaces existing package, or **installs it if not yet installed**).
  * **`rpm -Fvh example.rpm`:** Freshens/upgrades **only if an earlier version is already installed**.
  * **`rpm -e example`:** Uninstalls a package. Force options: **`--nodeps`** (ignore dependencies—use with caution) and **`--allmatches`** (remove all versions); **`--force`** (forcibly install/overwrite files).
* **Query & Validation Options (`rpm -q...`):**
  * **`-q <pkg>`:** Checks if package is installed. **`-qa`:** Lists **all** installed RPM packages.
  * **`-qi <pkg>`:** Displays detailed package description/metadata (`-qpi` for an uninstalled `.rpm` file).
  * **`-ql <pkg>`:** Lists all files and full paths installed by the package (`-qpl` for an uninstalled `.rpm` file).
  * **`-qf <filepath>`:** Queries **which RPM package owns a specific file** on the server.
  * **`-qc <pkg>` / `-qd <pkg>`:** Lists **configuration files (`-qc`)** or **documentation files (`-qd`)**.
  * **`-Va`:** Validates all installed RPM packages to detect missing or modified files.

---

### 2. Evolution from YUM to DNF & `/etc/dnf/dnf.conf`
* **Why DNF?** RPM does not resolve dependencies automatically. **YUM** solved dependency management but suffered from high memory usage and slow dependency resolution on large trees. **DNF (Next-Generation YUM)** maintains CLI compatibility with YUM while using the **`libsolv`** library for fast dependency resolution, lower memory footprint, and a modern **Python 3** plugin architecture.
* **Global Config (`/etc/dnf/dnf.conf` — `[main]` section):**
  * **`cachedir`:** Directory storing downloaded RPMs and database cache.
  * **`best`:** Always attempts to install the latest available version (default: **`True`**).
  * **`installonly_limit`:** Max number of concurrent versions for `installonlypkgs` like kernels (default: **`3`**; do not decrease).
  * **`clean_requirements_on_remove`:** Automatically removes unused dependency packages during `dnf remove` (default: **`True`**).

---

### 3. Configuring `/etc/yum.repos.d/*.repo` & Local Repositories
Repository files reside in **`/etc/yum.repos.d/`** by default:
```ini
[OS]
name=OS
baseurl=https://repo.openeuler.org/openEuler-24.03-LTS-SP1/OS/$basearch/
metalink=https://mirrors.openeuler.org/metalink?repo=$releasever/OS&arch=$basearch
metadata_expire=1h
enabled=1
gpgcheck=1
gpgkey=http://repo.openeuler.org/openEuler-24.03-LTS-SP1/OS/$basearch/RPM-GPG-KEY-openEuler
```
* **`baseurl`** supports three protocols: `http://`, `ftp://`, and **`file:///`** (for local paths).
* **Creating a Local Repository (`createrepo`):**
  1. Install tool as root: `dnf install createrepo`
  2. Place RPM packages in `/mnt/local_repo/`
  3. Generate metadata database: **`createrepo --database /mnt/local_repo`**

---

## 🔑 Key Takeaways
- **rpm -ivh installs, rpm -Uvh upgrades (or installs), rpm -Fvh upgrades only existing packages, rpm -e uninstalls, rpm -qf <file> finds which package owns a file, and rpm -qc lists config files.**
- **DNF ('next-generation YUM') uses the libsolv library and Python 3 plugins; its global config is /etc/dnf/dnf.conf (default installonly_limit=3) and repo files live in /etc/yum.repos.d/.**
- **To build a local repository from a folder of RPMs, install createrepo and run 'createrepo --database /mnt/local_repo'.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse /etc/dnf/dnf.conf (global DNF configuration) with /etc/yum.repos.d/ (default directory for .repo files)!

> [!WARNING]
> EXAM TRAP: To query files inside an UNINSTALLED .rpm package file on disk, you must include the '-p' flag (e.g., 'rpm -qpl pkg.rpm' or 'rpm -qilp pkg.rpm').

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-RPM-Queries-and-Local-Repo-Creation-Lab.html`](./02-Exercise-RPM-Queries-and-Local-Repo-Creation-Lab.html)** (or [`02-Exercise-RPM-Queries-and-Local-Repo-Creation-Lab.md`](./02-Exercise-RPM-Queries-and-Local-Repo-Creation-Lab.md)) to apply this concept in an interactive lab workbench!
