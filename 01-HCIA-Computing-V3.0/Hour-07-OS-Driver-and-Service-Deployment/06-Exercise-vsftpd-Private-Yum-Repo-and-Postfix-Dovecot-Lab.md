# Hands-On Lab: Deploying FTP-Based Private Yum Repo & Postfix/Dovecot Mail Stack

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 07 — OS Compatibility, openEuler 22.03 LTS Installation, Drivers/Firmware & Service Deployment (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Deploying-Enterprise-Services-FTP-Yum-and-Mail-Server`  
**Interactive Workbench:** Open **[`06-Exercise-vsftpd-Private-Yum-Repo-and-Postfix-Dovecot-Lab.html`](./06-Exercise-vsftpd-Private-Yum-Repo-and-Postfix-Dovecot-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Configure an FTP-based private Yum repository using `vsftpd` on openEuler 22.03 LTS and verify the Postfix (SMTP) and Dovecot (POP3/IMAP) mail server protocol bindings.

### Step-by-Step Instructions
1. Enable and start the `vsftpd` service using `systemctl enable --now vsftpd`.
2. Set `FTP_JAIL_TECH` to `'chroot'`, `MTA_SMTP_SERVER` to `'Postfix'`, and `MDA_POP3_IMAP_SERVER` to `'Dovecot'`.
3. Set `HEADER_ON_DEMAND_SYNC_PROTOCOL` to `'IMAP'`.

### Starter Workspace (`root@openeuler-services:~#`)
```bash
# 1. Enable and start the vsftpd service:
systemctl enable --now ___

# 2. Verify FTP chroot and Mail Server protocol roles:
FTP_JAIL_TECH="___"
FTP_LOG_DIR="/var/log/"
MTA_SMTP_SERVER="___"
MDA_POP3_IMAP_SERVER="___"
HEADER_ON_DEMAND_SYNC_PROTOCOL="___"
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- The FTP daemon is `vsftpd` and its directory restriction mechanism is `chroot`.
- Postfix provides SMTP, Dovecot provides POP3 and IMAP, and IMAP fetches subjects first and synchronizes status.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# 1. Enable and start the vsftpd service:
systemctl enable --now vsftpd

# 2. Verify FTP chroot and Mail Server protocol roles:
FTP_JAIL_TECH="chroot"
FTP_LOG_DIR="/var/log/"
MTA_SMTP_SERVER="Postfix"
MDA_POP3_IMAP_SERVER="Dovecot"
HEADER_ON_DEMAND_SYNC_PROTOCOL="IMAP"
```

#### Expected Console / Query Output:
```text
Created symlink /etc/systemd/system/multi-user.target.wants/vsftpd.service -> /usr/lib/systemd/system/vsftpd.service.
[OK] vsftpd (chroot, anonymous read-only Yum repo) and Postfix (SMTP) + Dovecot (POP3/IMAP) verified.
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In an FTP server (`vsftpd`), what is the restricted environment called that confines a logged-in FTP user to their home directory and prevents access to sensitive system directories like `/etc` and `/usr/local`?**

- A. SELinux enforcing mode
- B. changed root (chroot)
- C. syslogd
- D. JBOD passthrough

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 pp. 337–338, restricting an FTP user to their home directory is called a changed root, or chroot for short.
</details>

### Question 2 [Single-Choice]
**In a Linux mail server built with the Postfix + Dovecot combination, which protocols do Postfix and Dovecot provide, respectively, and how does IMAP differ from POP3?**

- A. Postfix provides POP3/IMAP; Dovecot provides SMTP; POP3 syncs actions on the server
- B. Postfix provides SMTP; Dovecot provides POP3 and IMAP; IMAP fetches key details (like subjects) first, downloads full content on demand, and synchronizes read/delete status on the server
- C. Both Postfix and Dovecot only provide FTP and HTTP protocols
- D. Postfix provides SNMP; Dovecot provides Redfish

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 pp. 340 and 342, Postfix provides SMTP (for sending/relaying), while Dovecot provides POP3 and IMAP. POP3 downloads entire emails and disconnects, whereas IMAP fetches subjects first, downloads on demand, and mirrors read/delete actions on the server.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following are valid steps in deploying an FTP-based private Yum repository on openEuler (Ch.05, p. 339)?**

- A. Create a Yum repository on the local host and install/enable the FTP service upon system startup.
- B. Modify the vsftpd configuration file to allow anonymous access and disable write permissions.
- C. Disable the firewall and SELinux.
- D. Set automatic mounting and test the FTP service.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** All four options match the exact 6-step procedure on Ch.05 p.339 for deploying an FTP-based private Yum repository.
</details>
