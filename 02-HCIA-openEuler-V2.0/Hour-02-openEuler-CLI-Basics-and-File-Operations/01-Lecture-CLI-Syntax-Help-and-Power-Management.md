# 📖 Linux Command Syntax, Help Utilities & Session/Power Management

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 02 — openEuler CLI Basics & File Operations (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-Help-Session-and-Power-Commands-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.03, pp. 60–78

---

## 🎯 Learning Objectives
- Parse standard Linux command syntax (`command [-option] [parameter]`) and distinguish short (`-a`) vs. long (`--all`) options
- Query documentation using `man` (9 manual sections and `coreutils-help` on openEuler), `whatis`, and `help`
- Execute login/session commands (`login`, `last`, `exit`) and safe power management (`shutdown`, `halt`, `reboot`)

---

### 1. Why CLI & Standard Linux Command Syntax
* **Why CLI:** Higher efficiency (keyboard + scripting automation), low resource overhead compared to GUI, and often the only choice for production servers.
* **Standard Syntax:** `command [-option] [parameter]` (e.g., `ls -la /etc`).
  * Multiple short options can be combined after a single hyphen (`-la` = `-l -a`).
  * **Short options** use one hyphen (`-a`); **long options** use two hyphens (`--all`).

---

### 2. Help Utilities: `man`, `whatis`, and `help`
* **`man` (Manual Pages — part of the `man-db` package):**
  * Searches for `.gz` manual files in `/usr/share/man`.
  * **openEuler Streamlining Rule:** On openEuler, command binaries and documentation packages are separated! Installing a command does not automatically install its man pages; you must install **`coreutils-help`** to view detailed manuals for core commands.
  * **9 Manual Sections:**
    * **`1`**: User commands/programs operable in the shell (e.g., `man 1 passwd`).
    * **`2`**: System calls invoked by the kernel.
    * **`3`**: Library functions (e.g., `man 3 sleep`).
    * **`4`**: Device file descriptions (usually in `/dev`).
    * **`5`**: File formats and conventions (e.g., `man 5 passwd` for `/etc/passwd`).
    * **`6`**: Games.
    * **`7`**: Miscellaneous (macros, conventions).
    * **`8`**: System management commands (root/superuser only).
    * **`9`**: Kernel routines (non-standard).
  * Search man pages by keyword: **`man -k KEYWORD`** or `find /usr/share/man -iname "*KEYWORD*"`.
* **`whatis <command>`:** Pulls the `NAME` section from a manual page to display a one-line summary (e.g., `whatis ls` -> `ls (1) - list directory contents`).
* **`help [-d|-s] <builtin>`:** Displays help for Bash built-in commands (e.g., `help pwd`). `-d` prints a brief description; `-s` prints command syntax.

---

### 3. Login/Session & Power Management Commands
* **Login & Session Auditing:**
  * **`login`**: Logs in to the system (applicable to all users).
  * **`last`**: Reads `/var/log/wtmp` to display recent user/terminal logins, reboots, and shutdowns. Options: `-n <num>` (number of records), `-t tty` (specific console), `-y` (display year/month/day), `-x` (shutdowns/logins/logouts), `-f file`, `-i IP`.
  * **`exit`**: Logs out of the current shell session (no options).
* **Power Management (Superuser Only):**
  * **`shutdown`**: Safely shuts down or restarts the system, notifying all logged-in users and freezing `login`.
    * **`-h`**: Powers off after shutdown.
    * **`-r`**: Restarts after shutdown.
    * **`-k`**: Sends warning messages to users **without** actually shutting down.
    * **`-F`**: Forcibly runs filesystem check (`fsck`) on reboot.
    * **`-t <sec>` / `-time`**: Specifies delay before shutdown.
  * **`halt`**: Terminates processes, calls `sync` (writes buffer data to disk), and stops the kernel. Options: `-n` (do not sync system calls—used after repairing root partition with `fsck` so kernel doesn't overwrite repaired superblock), `-w` (only write record to `/var/log/wtmp` without halting), `-d` (do not write record to `wtmp`), `-f` (force halt without calling `shutdown`), `-i` (shut down network interfaces first).
  * **`reboot`**: Restarts the host (`-n`, `-w`, `-d`, `-i`).

---

## 🔑 Key Takeaways
- **man pages are divided into 9 sections: 1 = User commands, 2 = System calls, 3 = C library functions, 4 = /dev devices, 5 = Config file formats, 8 = Root admin commands.**
- **On openEuler, command packages and documentation packages are separated; install 'coreutils-help' to access core command manual pages.**
- **shutdown -k only broadcasts a warning without shutting down; halt -w / reboot -w only writes a record to /var/log/wtmp without halting/rebooting.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: 'man 1 passwd' views the passwd command manual, whereas 'man 5 passwd' views the /etc/passwd configuration file format manual!

> [!WARNING]
> EXAM TRAP: Neither 'shutdown -k', 'halt -w', nor 'reboot -w' actually powers off or restarts the server—'-k' only warns users, and '-w' only writes a test record to /var/log/wtmp.

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Help-Session-and-Power-Commands-Lab.html`](./02-Exercise-Help-Session-and-Power-Commands-Lab.html)** (or [`02-Exercise-Help-Session-and-Power-Commands-Lab.md`](./02-Exercise-Help-Session-and-Power-Commands-Lab.md)) to apply this concept in an interactive lab workbench!
