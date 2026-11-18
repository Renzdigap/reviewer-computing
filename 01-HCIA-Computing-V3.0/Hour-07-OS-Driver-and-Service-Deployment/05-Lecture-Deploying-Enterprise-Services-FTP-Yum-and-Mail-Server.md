# Deploying Enterprise Services on openEuler: FTP (`vsftpd`), Private Yum & Mail Server

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 07 — OS Compatibility, openEuler 22.03 LTS Installation, Drivers/Firmware & Service Deployment (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (8 mins) - Followed immediately by `06-Exercise-vsftpd-Private-Yum-Repo-and-Postfix-Dovecot-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.05, pp. 336–342

---

## Learning Objectives
- Understand FTP user classifications (real, guest, anonymous), syslogd logging (`/var/log/`), `chroot` access restriction, and `vsftpd` security mechanisms
- Execute the 6-step deployment of an FTP-based private Yum repository
- Master Linux Mail Server architecture (`Postfix` SMTP + `Dovecot` POP3/IMAP), real vs. virtual users, and POP3 vs. IMAP synchronization

---

### 1. FTP Server & `vsftpd` Security Architecture (pp. 337–338)
- **Three Key FTP Server Functions (p. 337)**:
  1. **User classification**: Classifies users into **real**, **guest**, and **anonymous** users with different permissions (e.g., anonymous users can only download resources, whereas real users have broader permissions).
  2. **Command and file logs**: Uses the **`syslogd`** service to log command history and data transfer details (transfer time, file size) in **`/var/log/`**.
  3. **Access restriction (`chroot`)**: Restricts a user to their home directory (**changed root / `chroot`**) so they cannot access sensitive system directories like `/etc`, `/home`, or `/usr/local`.
- **Why `vsftpd` (*very secure FTP daemon*, p. 338)**: Standard FTP does **not** encrypt data during transmission. `vsftpd` enhances security in 3 ways:
  1. Runs as an **unprivileged user** and enforces **`chroot`** environments.
  2. Any command requiring elevated privileges is controlled by a **parent process running with the least privileges required**.
  3. Integrates common Linux commands (`dir`, `ls`, `cd`) internally to reduce reliance on external binaries.

---

### 2. Six-Step FTP-Based Private Yum Repository Deployment (p. 339)
1. **Step 1**: Create a Yum repository on the local host (e.g., using `createrepo` and configuring `.repo` files).
2. **Step 2**: Install the FTP service (`vsftpd`) and enable it to start upon system startup (`systemctl enable --now vsftpd`).
3. **Step 3**: Modify the `vsftpd` configuration file (`/etc/vsftpd/vsftpd.conf`) to **allow anonymous access and disable write permissions**.
4. **Step 4**: **Disable the firewall and SELinux** (`systemctl stop firewalld`, `setenforce 0`).
5. **Step 5**: Set automatic mounting (`/etc/fstab`).
6. **Step 6**: Test the FTP service and Yum repository (`yum makecache`).

---

### 3. Linux Mail Server: Postfix (SMTP) + Dovecot (POP3/IMAP) (pp. 340–342)
- **Mainstream Combination**: **Postfix + Dovecot** (often backed by MySQL, storing mail in `/var/mail/mydomain.com/myuser`):
  - **Postfix**: Open-source Mail Transfer Agent providing the **SMTP (Simple Mail Transfer Protocol)** service for sending and relaying emails between mail servers (e.g., `me@huawei.com` \rightarrow `smtp.huawei.com` \rightarrow `smtp.gmail.com`, which saves the email to disk).
  - **Dovecot**: Famous **POP3** and **IMAP** server implementation responsible **only for the path between the recipient's mail server and the recipient's email client (user agent)**.
- **POP3 vs. IMAP (pp. 340, 342)**:
  - **POP3 (Post Office Protocol v3)**: Downloads **entire emails** to the client device and then disconnects; actions on the client do not sync back to the server.
  - **IMAP (Internet Message Access Protocol)**: Fetches **only key details (such as subjects/headers)** first and downloads full content **on demand**; **synchronizes actions** (deletion, marking as read) with the mail server so status is consistent across webmail and clients.
- **Two Working Modes of a Postfix Email System (p. 341)**:
  1. **Local Linux users** (`root@example.com`, limited by allowed number of OS users).
  2. **Virtual users** (not associated with real Linux users; each has separate drive space; overcomes OS user count limits, enhances security, suitable for multi-user scenarios).

---

## Key Takeaways
- **FTP classifies users into real, guest, and anonymous; logs via syslogd to /var/log/; and isolates users to their home directory using chroot.**
- **Six steps for an FTP-based private Yum repo: (1) Create local Yum repo -> (2) Install & enable FTP -> (3) Modify vsftpd config (allow anonymous, disable write) -> (4) Disable firewall & SELinux -> (5) Set automatic mounting -> (6) Test FTP.**
- **In a Linux mail server, Postfix provides SMTP (client-to-server and server-to-server sending/relaying), while Dovecot provides POP3/IMAP (server-to-recipient client retrieval).**
- **POP3 downloads entire emails and disconnects; IMAP fetches headers/subjects first, downloads full content on demand, and synchronizes read/delete state on the server.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: POP3/IMAP (Dovecot) is ONLY responsible for retrieving mail from the recipient's mail server to the recipient's email client; sending mail from the client and relaying between mail servers (`smtp.huawei.com` -> `smtp.gmail.com`) both use SMTP (Postfix)!

> [!WARNING]
> EXAM TRAP: In Step 3 of deploying an FTP-based private Yum repository (p. 339), you modify the vsftpd config file to ALLOW anonymous access and DISABLE write permissions!

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-vsftpd-Private-Yum-Repo-and-Postfix-Dovecot-Lab.html`](./06-Exercise-vsftpd-Private-Yum-Repo-and-Postfix-Dovecot-Lab.html)** (or [`06-Exercise-vsftpd-Private-Yum-Repo-and-Postfix-Dovecot-Lab.md`](./06-Exercise-vsftpd-Private-Yum-Repo-and-Postfix-Dovecot-Lab.md)) to apply this concept in an interactive lab workbench!
