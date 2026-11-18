# User & Group Architecture (UID/GID) and Configuration Files

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 04 — User, Group & File Permission Management (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `02-Exercise-Inspecting-Passwd-and-Group-Files-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.04, pp. 158–162

---

## Learning Objectives
- Distinguish the three Linux user types by UID range: Superuser (0), Virtual/System user (1–999), and Common/Regular user (1000–60000)
- Compare Private (primary/owner) groups vs. Public (additional/supplementary) groups
- Parse every colon-delimited field of `/etc/passwd` (7 fields) and `/etc/group` (4 fields) along with `/etc/shadow` and `/etc/gshadow`

---

### 1. Linux User Types (UID) and Group Types (GID)
When a user logs in to Linux, the system identifies the user type by **UID (User ID)**, not by the username!
* **Three User Categories by UID Range (Ch.04, p.160):**
  1. **Superuser (`root`):** **`UID = 0`** (and `GID = 0`). Has full control over the entire OS.
  2. **Virtual user (System user):** **`UID = 1 to 999`**. Used by background services/daemons; cannot log in interactively with a password (typically uses `/sbin/nologin` or `/usr/sbin/nologin`).
  3. **Common user (Normal/Regular user):** **`UID = 1000 to 60000`**. Can modify files in their own home directory (`/home/username`) and access authorized resources.
* **User Group Relationships:**
  * **Private Group (Owner/Primary Group):** Each user has **only one** private group (created with the same name and GID as the user by default). Newly created files belong to this primary group.
  * **Public Group (Additional/Supplementary Group):** A user can belong to **multiple** public groups to inherit shared permissions.

---

### 2. Structure of `/etc/passwd` (7 Fields) and `/etc/group` (4 Fields)
* **`/etc/passwd` (User Configuration File — 7 Colon-Separated Columns):**
  Example: `root:x:0:0:Super User:/root:/bin/bash`
  1. **Username** (`root`)
  2. **Password placeholder** (`x` — indicates password authentication is required; actual encrypted hashes are stored in `/etc/shadow`)
  3. **UID** (`0`)
  4. **Primary GID** (`0`)
  5. **User description / comment** (`Super User`)
  6. **Home directory** (`/root` or `/home/username`)
  7. **Login shell** (`/bin/bash` for interactive login, or `/sbin/nologin` to forbid shell login)
* **`/etc/group` (Group Configuration File — 4 Colon-Separated Columns):**
  Example: `wheel:x:10:openeuler`
  1. **Group name** (`wheel`)
  2. **Password placeholder** (`x`)
  3. **GID** (`10`)
  4. **Supplementary users list** (Comma-separated list of users for whom this group is a **supplementary/additional group**. Note: If a group is a user's **private/primary group**, the username does **not** appear in the 4th column!).

---

### 3. Companion Account Files
* **`/etc/shadow`:** Stores encrypted user passwords and password aging policies (readable only by `root`).
* **`/etc/gshadow`:** Stores encrypted group passwords and group administrators.
* **`/var/spool/mail/username`:** Stores the user's system mailbox.

---

## Key Takeaways
- **Linux identifies users by UID: 0 = Superuser (root), 1–999 = Virtual (system) users, and 1000–60000 = Common (regular) users.**
- **/etc/passwd has 7 colon-separated fields: username : password_placeholder(x) : UID : GID : description : home_dir : login_shell.**
- **/etc/group has 4 colon-separated fields: group_name : password_placeholder(x) : GID : supplementary_users (private group owners do not appear in column 4).**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: The second column 'x' in /etc/passwd is ONLY a password placeholder—the actual encrypted password hash is stored in /etc/shadow!

> [!WARNING]
> EXAM TRAP: Each user can have only ONE private (primary) group, but can belong to MULTIPLE public (additional/supplementary) groups.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Inspecting-Passwd-and-Group-Files-Lab.html`](./02-Exercise-Inspecting-Passwd-and-Group-Files-Lab.html)** (or [`02-Exercise-Inspecting-Passwd-and-Group-Files-Lab.md`](./02-Exercise-Inspecting-Passwd-and-Group-Files-Lab.md)) to apply this concept in an interactive lab workbench!
