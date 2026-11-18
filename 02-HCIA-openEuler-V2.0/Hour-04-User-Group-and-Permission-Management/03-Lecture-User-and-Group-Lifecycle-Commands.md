# User, Group & Password Lifecycle Commands (`useradd`, `usermod`, `userdel`, `passwd`, `chage`, `gpasswd`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 04 — User, Group & File Permission Management (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `04-Exercise-User-Group-and-Password-Aging-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.04, pp. 163–168

---

## Learning Objectives
- Create, modify, and delete users and groups with `useradd`, `usermod`, `userdel`, `groupadd`, `groupmod`, and `groupdel`
- Manage user passwords and account locks with `passwd` (`-n`, `-x`, `-w`, `-i`, `-d`, `-S`, `-l`, `-u`, `-e`) and password aging with `chage` (`-l`, `-M`, `-m`, `-w`, `-d`, `-I`)
- Manage group memberships safely without overwriting existing supplementary groups using `gpasswd` (`-a`, `-d`, `-M`, `-A`) vs. `usermod -G`

---

### 1. Creating, Modifying & Deleting Users and Groups
| Command | Key Options & Exam Rules |
| :--- | :--- |
| **`useradd [options] user`** | **`-u`** (specify UID), **`-o`** (used with `-u` to allow duplicate UIDs), **`-g`** (specify basic/primary group name or GID), **`-d`** (specify and create home directory), **`-s`** (specify default login shell), **`-D`** (display/change default config). |
| **`usermod [options] user`** | **`-u`** (modify UID), **`-g`** (modify primary group), **`-G`** (specify supplementary group—**overwrites previous supplementary groups** unless `-a` is combined or `gpasswd -a` is used!), **`-l`** (modify login username), **`-d`** (modify home directory), **`-s`** (modify default shell). |
| **`userdel [options] user`** | Without options, deletes only the account entry (leaves home/mail files). **`-r`** recursively deletes the user **and their home directory/mail files**. **`-f`** forcibly deletes a user even if currently logged in. |
| **`groupadd [options] grp`** | **`-g`** (assign GID), **`-o`** (allow duplicate GID), **`-r`** (create system group), **`-f`** (exit successfully if group exists), **`-p`** (encrypted password). |
| **`groupmod [options] grp`** | **`-g`** (set new GID), **`-n`** (set new group name), **`-o`** (allow duplicate GID), **`-p`** (modify password). |
| **`groupdel [options] grp`** | Deletes a group. **Rule:** If a group is the primary group of an existing user, delete the user first (or use **`-f`** to force). |

---

### 2. Password Management (`passwd`) & Password Aging (`chage`)
* **`passwd [OPTION...] user_name`:** (Root can change any user's password; common users can change only their own.)
  * **`-l` / `-u`:** **Locks (`-l`)** or **unlocks (`-u`)** a user's password.
  * **`-d`:** Deletes a user's password. **`-e`:** Forces immediate password expiration on next login. **`-S`:** Displays password status.
  * **`-n <min>` / `-x <max>` / `-w <warn>` / `-i <inactive>`:** Sets min days, max days, warning days, and grace days before disabling an expired account.
* **`chage [OPTION...] user_name` (Change Age):**
  * **`-l`:** Lists password expiration details for a user.
  * **`-M <days>`:** Maximum password validity period.
  * **`-m <days>`:** Minimum password validity period.
  * **`-w <days>`:** Warning days before password expires.
  * **`-I <days>`:** Inactive days after password expiration before account is locked.
  * **`-d <date/0>`:** Sets last password change date (`-d 0` forces change on next login).

---

### 3. Group Association (`gpasswd`) & `chroot`
* **Why `gpasswd` instead of `usermod -G`?** Running `usermod -G group_name user_name` adds the user to `group_name` **but removes the user from any previous supplementary groups!** To add a user to a group while retaining existing supplementary groups, use **`gpasswd`**.
* **`gpasswd [option] group_name`:**
  * **`-a <user>`:** Adds a user to the group.
  * **`-d <user>`:** Deletes (removes) a user from the group.
  * **`-M <u1,u2>`:** Defines the complete list of group members.
  * **`-A <user>`:** Sets group administrator(s); **`-r`** removes group password; **`-R`** restricts access to members only; **`-Q`** specifies a `chroot` directory.
* **`chroot`:** Changes the apparent root directory (`/`) for a process, enhancing security, isolating development environments, and aiding bootloader/system recovery.

---

## Key Takeaways
- **userdel without options keeps the home directory; 'userdel -r username' deletes both the user account and their home/mail directories.**
- **chage -l lists password aging policy, chage -M sets maximum validity days, and passwd -l / -u locks or unlocks an account.**
- **gpasswd -a user group adds a user to a group while keeping existing supplementary groups, whereas 'usermod -G group user' overwrites previous supplementary groups.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse chage options with passwd options! For maximum password validity days, chage uses uppercase '-M' (chage -M 90 user), whereas passwd uses lowercase '-x' (passwd -x 90 user).

> [!WARNING]
> EXAM TRAP: To rename a group, groupmod uses '-n' (groupmod -n newname oldname), whereas to rename a user, usermod uses '-l' (usermod -l newname oldname).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-User-Group-and-Password-Aging-Lab.html`](./04-Exercise-User-Group-and-Password-Aging-Lab.html)** (or [`04-Exercise-User-Group-and-Password-Aging-Lab.md`](./04-Exercise-User-Group-and-Password-Aging-Lab.md)) to apply this concept in an interactive lab workbench!
