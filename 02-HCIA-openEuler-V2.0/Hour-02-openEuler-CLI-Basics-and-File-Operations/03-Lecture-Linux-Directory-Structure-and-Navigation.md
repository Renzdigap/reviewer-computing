# 📖 Linux File Directory Structure (FHS) & Path Navigation (`pwd`, `cd`, `ls`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 02 — openEuler CLI Basics & File Operations (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `04-Exercise-FHS-and-Directory-Navigation-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.03, pp. 79–87

---

## 🎯 Learning Objectives
- Apply the Linux philosophy 'Everything is a file' and identify the purpose of every standard root subdirectory (`/bin`, `/sbin`, `/etc`, `/proc`, `/var`, `/dev`, `/usr`, `/opt`, etc.)
- Differentiate absolute paths vs. relative paths and logical (`pwd -L`) vs. physical (`pwd -P`) working directories
- Use `cd` (`~`, `-`, `..`, `.`) and `ls` (`-a`, `-A`, `-l`, `-h`, `-t`, `-S`, `-r`, `-d`, `-R`) with precision

---

### 1. "Everything is a File" & Linux Directory Tree (`/`)
In Linux, **everything is a file**—regular files, directories, character/block devices, sockets, pipes, and processes can all be read/written via `fopen()`, `fclose()`, `fwrite()`, and `fread()`. All directories branch from the single **root directory (`/`)**:

| Directory | Purpose & Key Characteristics |
| :--- | :--- |
| **`/bin` & `/sbin`** | `/bin` stores frequently used binary commands for all users; `/sbin` (`s` = superuser) stores system management programs for `root`. |
| **`/boot`** | Core files for starting the Linux OS (kernel images, bootloader, initramfs). |
| **`/dev`** | External hardware device files (disks, terminals) accessed just like files. |
| **`/etc`** | All system and service configuration files and subdirectories. |
| **`/home` & `/root`** | `/home` contains regular users' home directories (`/home/username`); `/root` is the superuser's home directory. |
| **`/lib` & `/lib64`** | Essential dynamic link libraries (similar to Windows `.dll` files) and 64-bit shared libraries. |
| **`/media` & `/mnt`** | `/media` auto-mounts removable media (USB drives, CD-ROMs); `/mnt` is for temporary manual mounts. |
| **`/opt`** | Optional/additional third-party application software (empty by default). |
| **`/proc`** | **Virtual directory that is a mapping of system memory (RAM).** Access it directly to obtain real-time kernel/process information. |
| **`/run`** | Temporary file system storing runtime data since boot (cleared on reboot; `/var/run` points to `/run`). |
| **`/srv` & `/sys`** | `/srv` stores service data; `/sys` mounts `sysfs` (introduced in Linux 2.6 kernel for hardware/kernel objects). |
| **`/tmp` & `/var`** | `/tmp` stores temporary files; `/var` stores constantly expanding variable files such as **logs (`/var/log`)**. |
| **`/usr`** | User applications and files (similar to Windows `Program Files`). |

---

### 2. Paths, `pwd`, and `cd`
* **Absolute Path:** Always starts from the root slash **`/`** (e.g., `/var/log/messages`).
* **Relative Path:** Relative to the current working directory (e.g., `../lib` or `./script.sh`).
* **`pwd` (Print Working Directory):**
  * **`pwd -L` (Default):** Prints the **logical** path (preserves symbolic link names from `$PWD`).
  * **`pwd -P`:** Prints the **physical** directory path, resolving all symbolic links!
* **`cd` (Change Directory):**
  * `cd` or `cd ~`: Goes to the current user's home directory.
  * `cd ..`: Moves to the upper-level (parent) directory.
  * `cd .`: Stays in the current directory.
  * **`cd -`**: Switches back to the **previous working directory** (fast toggle between two directories).

---

### 3. Listing Files and Directories with `ls`
* **`-l`**: Long format (file type, permissions, hard links, owner, group, size, timestamp, name).
* **`-a` vs. `-A`**: **`-a`** shows all hidden files (starting with `.`) **including `.` and `..`**; **`-A`** shows hidden files **excluding `.` and `..`**.
* **`-h`**: Human-readable sizes (`4.0K`, `12M`, `2G`).
* **`-d`**: Displays information about the **directory itself** (`ls -ld /etc`) rather than its contents.
* **Sorting flags:** **`-t`** (sort by modification/creation time), **`-S`** (sort by size), **`-X`** (sort by extension), **`-r`** (reverse sort order), **`-R`** (recursive listing).

---

## 🔑 Key Takeaways
- **/proc is a virtual directory that maps system memory (RAM); /var stores constantly growing files like logs; /etc stores configuration files.**
- **pwd -L (default) prints the logical symlink path, whereas pwd -P resolves symlinks and prints the true physical directory path.**
- **ls -a includes '.' and '..', whereas ls -A excludes them; ls -ld <dir> inspects the directory itself rather than listing its contents.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse /root (the home directory of the superuser) with / (the root directory of the entire Linux filesystem tree)!

> [!WARNING]
> EXAM TRAP: If /tmp/link3 points to /tmp/d1 and you run 'cd /tmp/link3', 'pwd' (or 'pwd -L') outputs '/tmp/link3', whereas 'pwd -P' outputs '/tmp/d1'.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-FHS-and-Directory-Navigation-Lab.html`](./04-Exercise-FHS-and-Directory-Navigation-Lab.html)** (or [`04-Exercise-FHS-and-Directory-Navigation-Lab.md`](./04-Exercise-FHS-and-Directory-Navigation-Lab.md)) to apply this concept in an interactive lab workbench!
