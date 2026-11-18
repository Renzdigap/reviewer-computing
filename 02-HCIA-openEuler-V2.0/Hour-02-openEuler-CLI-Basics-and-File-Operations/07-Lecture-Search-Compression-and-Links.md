# File Search (`find`, `locate`, `which`), Compression (`gzip`, `tar`) & Links (`ln`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 02 — openEuler CLI Basics & File Operations (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `08-Exercise-Find-Tar-and-Links-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.03, pp. 105–117

---

## Learning Objectives
- Search files in real time with `find` (`-name`, `-type`, `-mtime`, `-user`, `-size`, `-empty`, `-exec`), index-based `locate`/`updatedb`, and `$PATH`-based `which`
- Compress and archive files using `gzip` (60–70% compression ratio) and `tar` (`-c`, `-x`, `-t`, `-z`, `-j`, `-J`, `-v`, `-f`, `-C`)
- Compare and create hard links (`ln`) vs. symbolic/soft links (`ln -s`) and trace their behavior when source files are deleted

---

### 1. File Search Utilities: `find`, `locate`, and `which`
* **`find [path...] [expression]` (Real-time directory traversal):**
  * **`-name "pattern"` / `-iname`:** Search by filename (case-sensitive / case-insensitive).
  * **`-type <c>`:** Filter by file type: **`f`** (general file), **`d`** (directory), **`l`** (symbolic link), **`b`** (block device), **`c`** (character device), **`p`** (named pipe).
  * **`-mtime -n / +n`:** By modification time (`-7` = within last 7 days; **`+7` = earlier than 7 days ago**).
  * **`-user <uname>` / `-perm <mode>` / `-size <N>`:** By owner, permission, or size.
  * **`-empty [-delete]`:** Finds (and optionally deletes) empty files/directories.
  * **`-exec cmd {} \;`:** Runs `cmd` on each matched file (e.g., `find -name "*.html" -exec cp {} /data/html/ \;`).
* **`locate [OPTION] PATTERN` (Fast database index search):**
  * Searches the pre-built index database `/var/lib/mlocate/mlocate.db`.
  * **Must run `updatedb` first** if the database does not exist or newly created files are not yet indexed!
* **`which [-a] programname`:** Searches only directories in **`PATH`** to find the absolute path of an executable command (`-a` lists all matches across `PATH`).

---

### 2. Compression & Archiving: `gzip` and `tar`
* **`gzip [option] [file/dir]`:**
  * Compresses files in place with a **60% to 70% compression ratio** for text files, appending **`.gz`** and replacing the original file.
  * Options: **`-d`** (decompress, equivalent to `gunzip`), **`-l`** (list compressed/uncompressed sizes & ratio), **`-r`** (recursively compress files in subdirectories), **`-v`** (verbose), **`-f`** (force).
* **`tar [OPTION...] [FILE]` (Tape Archive — packs multiple files/directories):**
  * **Action flags:** **`-c`** (create archive), **`-x`** (extract archive), **`-t`** (list contents without extracting).
  * **Compression filter flags:**
    * **`-z`:** `gzip` (`.tar.gz` / `.tgz`)
    * **`-j`:** `bzip2` (`.tar.bz2`)
    * **`-J`:** `xz` (`.tar.xz`)
  * **Helper flags:** **`-v`** (verbose), **`-f <archive_name>`** (must immediately precede archive filename), **`-C <target_dir>`** (extract to specified directory instead of current directory).

---

### 3. Hard Links vs. Soft (Symbolic) Links (`ln`)
By default, **`ln Source Target` creates a hard link**; adding **`-s`** (`ln -s Source Target`) creates a **soft (symbolic) link**:

| Feature | Soft Link (`ln -s`) | Hard Link (`ln` default) |
| :--- | :--- | :--- |
| **Nature** | A path shortcut (like a Windows shortcut); has its own new inode (`lrwxrwxrwx`). | A file entry pointing to the **exact same inode/data blocks**; does not occupy extra disk space. |
| **If Source File is Deleted** | **Becomes invalid (broken/dangling link)!** | **No impact!** Data remains accessible via the hard link (`link count` decreases by 1). |
| **Linking to Directories** | **Supported** | **Not supported** (by default; prevents directory loops). |
| **Cross-File System Linking** | **Supported** | **Not supported** (inodes are unique per filesystem). |

---

## Key Takeaways
- **find /var/log/anaconda/ -type f -mtime +7 searches for regular files modified more than 7 days ago; locate requires updatedb to update /var/lib/mlocate/mlocate.db.**
- **tar -zcf packs with gzip (.tar.gz), tar -jcf uses bzip2 (.tar.bz2), tar -Jcf uses xz (.tar.xz), and -C specifies the extraction target directory.**
- **ln creates a hard link by default (survives source file deletion, cannot cross filesystems or link directories); ln -s creates a soft/symbolic link (breaks if source is deleted, can link directories and cross filesystems).**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: If you create a soft link 'ln -s passwd link_s', delete 'passwd', and then copy a new 'passwd' back to the same name, the soft link 'link_s' works again (points by path), whereas a hard link 'link_h' still points to the old inode and is no longer synchronized with the new 'passwd' file (Ch.03 p.117)!

> [!WARNING]
> EXAM TRAP: gzip has a 60%–70% compression ratio for text files and replaces the original file with file.gz.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-Find-Tar-and-Links-Lab.html`](./08-Exercise-Find-Tar-and-Links-Lab.html)** (or [`08-Exercise-Find-Tar-and-Links-Lab.md`](./08-Exercise-Find-Tar-and-Links-Lab.md)) to apply this concept in an interactive lab workbench!
