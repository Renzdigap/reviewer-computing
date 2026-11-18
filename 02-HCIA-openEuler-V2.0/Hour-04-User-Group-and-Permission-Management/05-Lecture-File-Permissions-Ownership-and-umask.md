# File Types, Permission Bits (`rwx`), Ownership (`chmod`, `chown`, `chgrp`) & `umask`

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 04 — User, Group & File Permission Management (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-Chmod-Chown-Chgrp-and-Umask-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.04, pp. 169–183

---

## Learning Objectives
- Identify all 7 Linux file types (`-`, `d`, `b`, `c`, `l`, `p`, `s`) and decode the 10-character `ls -l` permission string (Bits 0 to 9)
- Modify permissions and ownership using `chmod` (symbolic & octal), `chown user:group`, and `chgrp`
- Calculate default file and directory permissions from any `umask` value (`022`, `027`, `002`, `006`, `007`)

---

### 1. Seven Linux File Types & 10-Bit Permission Structure (`ls -l`)
In `drwxr-xr-x. 2 root root 4096 Jun 1 14:00 shili`, the 10-character mode string is indexed as **Bits 0 to 9**:
* **Bit 0 (File Type — 7 Types in Linux):**
  1. **`-`**: Regular/general file (files excluding the other 6 types).
  2. **`d`**: Directory.
  3. **`b`**: Block device file (random access storage device, e.g., `/dev/sda`).
  4. **`c`**: Character device file (one-time/serial read device such as keyboard and mouse).
  5. **`l`**: Symbolic link file.
  6. **`p`**: Named pipe (FIFO) file.
  7. **`s`**: Socket file.
* **Bits 1–9 (Three 3-Bit Permission Triads):**
  * **Bits 1–3 (`u` — Owner):** File owner permissions.
  * **Bits 4–6 (`g` — Group):** Owner group permissions.
  * **Bits 7–9 (`o` — Others):** Other users' permissions.

| Permission | Octal Value | Meaning on a Regular File (`-`) | Meaning on a Directory (`d`) |
| :--- | :---: | :--- | :--- |
| **`r` (Read)** | **4** | Read the actual content of the file. | Read the directory structure list (`ls`). |
| **`w` (Write)** | **2** | Edit, add, or modify file content (does **not** allow deleting the file itself!). | **Create, delete, rename, or move files** inside the directory! |
| **`x` (Execute)** | **1** | Execute the file as a program/script. | **Access/enter the directory (`cd`)**. |

---

### 2. Permission & Ownership Commands: `chmod`, `chown`, `chgrp`
* **`chmod [OPTION]... MODE FILE...` (Usable by file owner or `root`):**
  * **Octal mode:** `chmod 644 usertxt` (`rw-r--r--`), `chmod -R 755 dir`.
  * **Symbolic mode:** Objects `u` (owner), `g` (group), `o` (others), `a` (all) + Operators `+` (add), `-` (remove), `=` (set exact) + Permissions `r`, `w`, `x`.
* **`chown [OPTION]... [OWNER][:[GROUP]] FILE...` (Usable by `root` only):**
  * Changes file owner, owner group, or **both simultaneously**: `chown user:usergroup usertxt`.
  * Options: **`-R`** (recursive), **`-h`** (modify symlink itself), **`-c`** (report only when changed), **`-f`** (ignore errors), **`-v`** (verbose).
* **`chgrp [OPTION]... GROUP FILE...` (Usable by `root`):**
  * Modifies the group to which a file/directory belongs (`chgrp usergroup01 usertxt`, `-R`, `--reference=<file>`).

---

### 3. Preset Permission Mask (`umask`)
`umask [-p] [-S] [mode]` defines the permissions **masked out** when creating a new file (base `666`) or directory (base `777`):

| `umask` Value | Default File Permission | Default Directory Permission |
| :---: | :---: | :---: |
| **`022`** | **`644`** (`rw-r--r--`) | **`755`** (`rwxr-xr-x`) |
| **`027`** | **`640`** (`rw-r-----`) | **`750`** (`rwxr-x---`) |
| **`002`** | **`664`** (`rw-rw-r--`) | **`775`** (`rwxrwxr-x`) |
| **`006`** | **`660`** (`rw-rw----`) | **`771`** (`rwxrwx--x`) |
| **`007`** | **`660`** (`rw-rw----`) | **`770`** (`rwxrwx---`) |

---

## Key Takeaways
- **The 7 Linux file types are '-' (regular), 'd' (directory), 'b' (block device), 'c' (character device), 'l' (symlink), 'p' (named pipe), and 's' (socket).**
- **chmod can be run by the file owner or root, whereas chown can only be run by the administrator (root).**
- **With umask 022, new files get 644 and new directories get 755; with umask 027, new files get 640 and new directories get 750.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Write permission ('w') on a file allows editing its content, NOT deleting the file! Deleting or renaming a file is controlled by write ('w') + execute ('x') permissions on the PARENT DIRECTORY.

> [!WARNING]
> EXAM TRAP: Notice 'umask 006' in the official table (Ch.04 p.182): directories get 777 - 006 = 771, while files strip the execute bit to get 660!

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-Chmod-Chown-Chgrp-and-Umask-Lab.html`](./06-Exercise-Chmod-Chown-Chgrp-and-Umask-Lab.html)** (or [`06-Exercise-Chmod-Chown-Chgrp-and-Umask-Lab.md`](./06-Exercise-Chmod-Chown-Chgrp-and-Umask-Lab.md)) to apply this concept in an interactive lab workbench!
