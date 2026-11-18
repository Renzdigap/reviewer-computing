# Hour 05: Software Packages, systemd Services, Processes & Scheduled Tasks
**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Official Material Reference:** Chapter 04 Part 2 (pp. 194–251)  
**Pacing:** 60 Minutes (4 × 15-Minute Active Learning Sprints)

Master RPM package operations (`rpm -ivh/-Uvh/-Fvh/-e/-qa/-ql/-qf/-qc`), configure local and remote DNF repositories (`/etc/dnf/dnf.conf`, `/etc/yum.repos.d/*.repo`, `createrepo`, `dnf config-manager`), manage `systemd` unit files (`systemctl`) and `journald` logs (`journalctl`), control processes and priorities (`ps`, `top`, `nice`, `renice`, `kill`), and automate one-off (`at`) and periodic (`crontab`) tasks.

---

## Strict Alternating Lecture & Exercise Sequence

| Order | Type | Duration | Interactive HTML | Study Sheet (.md) |
| :--- | :--- | :--- | :--- | :--- |
| **01** | Lecture | 7 mins | **[`01-Lecture-RPM-Package-Management-and-DNF-Repositories.html`](./01-Lecture-RPM-Package-Management-and-DNF-Repositories.html)** | [`01-Lecture-RPM-Package-Management-and-DNF-Repositories.md`](./01-Lecture-RPM-Package-Management-and-DNF-Repositories.md) |
| **02** | Exercise | 8 mins | **[`02-Exercise-RPM-Queries-and-Local-Repo-Creation-Lab.html`](./02-Exercise-RPM-Queries-and-Local-Repo-Creation-Lab.html)** | [`02-Exercise-RPM-Queries-and-Local-Repo-Creation-Lab.md`](./02-Exercise-RPM-Queries-and-Local-Repo-Creation-Lab.md) |
| **03** | Lecture | 7 mins | **[`03-Lecture-DNF-Package-and-Group-Management.html`](./03-Lecture-DNF-Package-and-Group-Management.html)** | [`03-Lecture-DNF-Package-and-Group-Management.md`](./03-Lecture-DNF-Package-and-Group-Management.md) |
| **04** | Exercise | 8 mins | **[`04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab.html`](./04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab.html)** | [`04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab.md`](./04-Exercise-DNF-Config-Manager-and-Package-Ops-Lab.md) |
| **05** | Lecture | 7 mins | **[`05-Lecture-systemd-Service-and-Journald-Log-Management.html`](./05-Lecture-systemd-Service-and-Journald-Log-Management.html)** | [`05-Lecture-systemd-Service-and-Journald-Log-Management.md`](./05-Lecture-systemd-Service-and-Journald-Log-Management.md) |
| **06** | Exercise | 8 mins | **[`06-Exercise-Systemctl-and-Journalctl-Service-Lab.html`](./06-Exercise-Systemctl-and-Journalctl-Service-Lab.html)** | [`06-Exercise-Systemctl-and-Journalctl-Service-Lab.md`](./06-Exercise-Systemctl-and-Journalctl-Service-Lab.md) |
| **07** | Lecture | 7 mins | **[`07-Lecture-Process-Management-and-Scheduled-Tasks.html`](./07-Lecture-Process-Management-and-Scheduled-Tasks.html)** | [`07-Lecture-Process-Management-and-Scheduled-Tasks.md`](./07-Lecture-Process-Management-and-Scheduled-Tasks.md) |
| **08** | Exercise | 8 mins | **[`08-Exercise-Top-Nice-Kill-At-and-Crontab-Lab.html`](./08-Exercise-Top-Nice-Kill-At-and-Crontab-Lab.html)** | [`08-Exercise-Top-Nice-Kill-At-and-Crontab-Lab.md`](./08-Exercise-Top-Nice-Kill-At-and-Crontab-Lab.md) |