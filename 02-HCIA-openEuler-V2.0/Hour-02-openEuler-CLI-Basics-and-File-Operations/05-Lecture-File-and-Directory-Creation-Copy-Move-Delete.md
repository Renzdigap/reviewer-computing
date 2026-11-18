# 📖 File & Directory Creation, Copying, Moving & Deletion (`mkdir`, `touch`, `cp`, `mv`, `rm`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 02 — openEuler CLI Basics & File Operations (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-File-Lifecycle-Operations-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.03, pp. 88–95

---

## 🎯 Learning Objectives
- Create single, multiple, and nested parent directories with `mkdir [-p] [-v]` and manage file timestamps with `touch [-a|-m|-t|-d]`
- Copy files and directories while preserving attributes or creating links with `cp [-a|-p|-r|-l|-s|-i]`
- Move/rename files with `mv [-b|-f|-i|-u]` and safely remove files/directories with `rm [-r|-f|-i|-v]`

---

### 1. Creating Directories (`mkdir`) and Files/Timestamps (`touch`)
* **`mkdir [OPTION]... DIRECTORY...` (Make Directory):**
  * Creates one (`mkdir dir1`) or multiple directories (`mkdir dir1 dir2`).
  * **`-p` (Parents):** Creates non-existent parent directories automatically (`mkdir -p dir1/dir2/dir3`) and **suppresses errors** if the directory already exists.
  * **`-v` (Verbose):** Displays a message for each created directory (`mkdir -pv dir1/dir2`).
* **`touch [OPTION]... FILE...`:**
  * Creates an empty file if it does not exist, or updates its timestamps if it already exists:
    * **`touch file`:** Updates all timestamps to the current system time.
    * **`touch -a file`:** Changes **only the access time (atime)**.
    * **`touch -m file`:** Changes **only the modification time (mtime)**.
    * **`touch -d "2020-01-17 17:14:10" file`:** Sets the timestamp using a date string.
    * **`touch -t 202001020304.05 file`:** Sets the timestamp using `[[CC]YY]MMDDhhmm[.ss]` format.

---

### 2. Copying Files and Directories (`cp`)
* **Syntax:** `cp [OPTION]... SOURCE... DIRECTORY` or `cp [OPTION]... [-T] SOURCE DEST`
* **Key Options:**
  * **`-r`:** Recursively copies directories and all subdirectories/files.
  * **`-p`:** Preserves file content, modification time, ownership, and access permissions.
  * **`-a` (Archive):** Retains links, file attributes, and copies block/character devices and pipe files intact (`-dpR`).
  * **`-l` vs. `-s`:** **`-l`** creates a **hard link** instead of copying data; **`-s`** creates a **symbolic (soft) link** (`cp -s /etc/passwd passwd_link`).
  * **`-t DIRECTORY SOURCE...`:** Specifies target directory first (ideal with `xargs`: `find -name "*.html" | xargs cp -t /data/html/`).
  * **Root Alias Note:** In openEuler's default root shell, `cp`, `mv`, and `rm` are aliased with **`-i` (interactive prompt)** to prevent accidental overwriting. Note that in `cp`, `-f` deletes an unopenable destination file and retries, rather than bypassing the `cp -i` alias prompt.

---

### 3. Moving/Renaming (`mv`) and Deleting (`rm`)
* **`mv [option] source target` (Move / Rename):**
  * Moves files/directories across directories, or **renames** a file if source and target are in the same parent directory (`mv test02.log test03.log`).
  * **`-f`:** Forcibly overwrites target without prompting.
  * **`-i`:** Prompts for user consent before overwriting. (**Rule:** If both `-i` and `-f` are specified on `mv` or `rm`, **the option on the right (last option) takes effect**!)
  * **`-b`:** Backs up the target file before overwriting.
  * **`-u`:** Updates the target file **only when the source file is newer** than the target.
* **`rm [OPTION] file_or_dir` (Remove):**
  * **Irreversible Deletion:** Linux `rm` does **not** move files to a recycle bin; deleted files cannot be restored easily.
  * **`-r` / `-R` / `--recursive`:** Recursively deletes directories and all contents.
  * **`-f` / `--force`:** Ignores non-existent files and deletes without prompting (`rm -rf dir1`).
  * **`-i`:** Interactive confirmation before each deletion.

---

## 🔑 Key Takeaways
- **mkdir -p automatically creates missing parent directories and reports no error if the target directory already exists.**
- **cp -a preserves all attributes, symlinks, and special device files; cp -p preserves mode, ownership, and timestamps; cp -s creates a symbolic link.**
- **In mv and rm, the shell aliases include -i by default; if both -i and -f are passed on the command line, the rightmost option takes effect.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: To copy or delete a directory, you MUST include '-r' (or '-a' for cp). Running 'cp dir1 dir2' or 'rm dir1' without '-r' fails!

> [!WARNING]
> EXAM TRAP: 'touch -a' updates only the access time, whereas 'touch -m' updates only the modification time.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-File-Lifecycle-Operations-Lab.html`](./06-Exercise-File-Lifecycle-Operations-Lab.html)** (or [`06-Exercise-File-Lifecycle-Operations-Lab.md`](./06-Exercise-File-Lifecycle-Operations-Lab.md)) to apply this concept in an interactive lab workbench!
