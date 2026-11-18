# Sticky Bit, Access Control Lists (`getfacl`, `setfacl`, `chacl`) & Privilege Escalation (`su`, `sudo`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 04 — User, Group & File Permission Management (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `08-Exercise-ACL-and-Sudo-Configuration-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.04, pp. 184–193

---

## Learning Objectives
- Explain how the Sticky Bit (`drwxrwxrwt`) protects shared directories like `/tmp` and `/share` from unauthorized file deletion
- Configure fine-grained Access Control Lists using `getfacl`, `setfacl` (`-m`, `-x`, `-b`, `-k`, `-R`, `-d`), and `chacl` (`-b`, `-d`, `-R`, `-D`, `-B`, `-l`, `-r`)
- Compare `su`, `su -`, and `sudo`, and author `/etc/sudoers` and `/etc/sudoers.d/username` rules using `visudo`

---

### 1. Sticky Bit (`t`) & Access Control Lists (ACL)
* **Sticky Bit (`drwxrwxrwt`, octal prefix `1`, `chmod o+t`):**
  * Special permission set on shared directories (such as `/tmp` or `/share`).
  * **Rule:** When the Sticky Bit is enabled on a directory, **only the file owner, the directory owner, or the `root` user can rename or remove files within that directory**—even if all users have `rwx` (`777`) permissions on the directory and files!
* **Access Control Lists (ACL):**
  * Solves the limitation of traditional `ugo` (`rwx`) permissions by granting fine-grained permissions to specific individual users or groups.
  * **Indicator:** In `ls -l`, a **plus sign (`+`)** at the end of the permission string (`-rw-rw-r--+`) indicates the file has an ACL configured!
  * **3 ACL Commands:**
    1. **`getfacl [-aceEsRLPtpndvh] file...`:** Obtains ACLs (`-a` file ACL only, `-d` default ACL only, `-c` omit header, `-R` recursive, `-n` numeric UIDs/GIDs).
    2. **`setfacl [-bkndRLP] {-m|-M|-x|-X} file...`:** Sets ACLs:
       * **`-m`:** Modifies/adds an ACL entry (e.g., `setfacl -m u:user1:rwx test`; cannot be combined with `-x`).
       * **`-x`:** Deletes specified ACL entries.
       * **`-b`:** **Deletes ALL extended ACL entries**.
       * **`-k`:** Removes default/preset directory ACL entries; **`-d`** presets default directory ACLs; **`-R`** recursive.
    3. **`chacl`:** Changes file/directory ACLs (`-b` modify file & default dir ACLs, `-d` set default dir ACL, `-R` delete file ACLs only, `-D` delete dir ACLs only, **`-B` delete all ACLs**, `-l` list ACLs, `-r` recursive).

---

### 2. Comparing `su` (`su -`) vs. `sudo`
| Dimension | `su` (substitute user) | `sudo` (superuser do) |
| :--- | :--- | :--- |
| **Basic Function** | Switches user identity (`su` keeps current shell env; **`su -`** switches to target user's login shell env). |Temporarily executes a single command as another user (usually `root`). |
| **Password Required** | **Target user's password** (e.g., `root`'s password). | **Current user's own password** (cached for **5 minutes** by default; unless `NOPASSWD` is set). |
| **Security & Auditing** | Low security: shares root password, broad permissions, **commands are NOT audited/recorded**. | High security: fine-grained command control in `/etc/sudoers`, **every command is logged by default**. |

---

### 3. Configuring `/etc/sudoers` and `/etc/sudoers.d/`
* **Best Practice:** Use **`visudo`** (which automatically checks syntax) to edit `/etc/sudoers`, or create a drop-in file **`/etc/sudoers.d/username`** (can be revoked simply by deleting the file).
* **Syntax Breakdown:**
  ```text
  test   openeuler.com=(root)   NOPASSWD:/usr/bin/touch
  %wheel ALL=(ALL)              ALL
  ```
  * **`test` / `%wheel`:** User or **group (prefixed with `%`)** granted privileges.
  * **`openeuler.com` / `ALL`:** Hostname where the rule applies.
  * **`(root)` / `(ALL)`:** Target user identity for privilege escalation.
  * **`NOPASSWD:/usr/bin/touch`:** Optional `NOPASSWD:` tag (skips password prompt) + comma-separated list of allowed absolute command paths.
* **Key `sudo` Options:** **`-l`** (list current user's allowed `sudo` permissions), **`-k`** (invalidate cached credentials, forcing password on next run), **`-v`** (extend password timeout by 5 mins), **`-u user/#uid`** (run as specific user), **`-b`** (run in background).

---

## Key Takeaways
- **When the Sticky Bit ('drwxrwxrwt') is set on a directory, only the file owner, directory owner, or root can delete or rename files inside it.**
- **A '+' at the end of 'ls -l' permissions (-rw-rw-r--+) indicates an ACL is active; manage ACLs with getfacl, setfacl (-m modify, -x delete entry, -b remove all), and chacl.**
- **su requires the target user's password and does not log commands; sudo requires the current user's password, checks /etc/sudoers (or /etc/sudoers.d/<user>), and logs all executed commands.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: 'su username' switches the user identity WITHOUT changing the current shell environment variables, whereas 'su - username' starts a full login shell with the target user's environment!

> [!WARNING]
> EXAM TRAP: In /etc/sudoers, a percent sign ('%') before a name (e.g., '%wheel') indicates a user group rather than an individual user.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-ACL-and-Sudo-Configuration-Lab.html`](./08-Exercise-ACL-and-Sudo-Configuration-Lab.html)** (or [`08-Exercise-ACL-and-Sudo-Configuration-Lab.md`](./08-Exercise-ACL-and-Sudo-Configuration-Lab.md)) to apply this concept in an interactive lab workbench!
