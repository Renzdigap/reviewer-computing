# Hour 06: openEuler Disk Partitioning, LVM & Network Management
**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Official Material Reference:** Chapter 05 (pp. 252–320)  
**Pacing:** 60 Minutes (4 × 15-Minute Active Learning Sprints)

Master openEuler file systems (`ext4`, `XFS`) and disk naming (`/dev/sd*`, `/dev/hd*`, `/dev/vd*`), partition disks under MBR (`fdisk`) and GPT (`parted`), format (`mkfs`) and mount file systems temporarily and persistently (`/etc/fstab`), create and dynamically resize LVM volumes (PV, VG, LV), and configure/diagnose networks using `nmcli`, `nmtui`, `ip`, `route`, `ping`, `tracepath`, and `ss`.

---

## Strict Alternating Lecture & Exercise Sequence

| Order | Type | Duration | Interactive HTML | Study Sheet (.md) |
| :--- | :--- | :--- | :--- | :--- |
| **01** | Lecture | 7 mins | **[`01-Lecture-Storage-File-Systems-and-Disk-Partitioning.html`](./01-Lecture-Storage-File-Systems-and-Disk-Partitioning.html)** | [`01-Lecture-Storage-File-Systems-and-Disk-Partitioning.md`](./01-Lecture-Storage-File-Systems-and-Disk-Partitioning.md) |
| **02** | Exercise | 8 mins | **[`02-Exercise-Fdisk-and-Parted-Partitioning-Lab.html`](./02-Exercise-Fdisk-and-Parted-Partitioning-Lab.html)** | [`02-Exercise-Fdisk-and-Parted-Partitioning-Lab.md`](./02-Exercise-Fdisk-and-Parted-Partitioning-Lab.md) |
| **03** | Lecture | 7 mins | **[`03-Lecture-Formatting-Mounting-and-fstab.html`](./03-Lecture-Formatting-Mounting-and-fstab.html)** | [`03-Lecture-Formatting-Mounting-and-fstab.md`](./03-Lecture-Formatting-Mounting-and-fstab.md) |
| **04** | Exercise | 8 mins | **[`04-Exercise-Mkfs-Mount-and-Fstab-Persistence-Lab.html`](./04-Exercise-Mkfs-Mount-and-Fstab-Persistence-Lab.html)** | [`04-Exercise-Mkfs-Mount-and-Fstab-Persistence-Lab.md`](./04-Exercise-Mkfs-Mount-and-Fstab-Persistence-Lab.md) |
| **05** | Lecture | 7 mins | **[`05-Lecture-LVM-Creation-Expansion-and-Reduction.html`](./05-Lecture-LVM-Creation-Expansion-and-Reduction.html)** | [`05-Lecture-LVM-Creation-Expansion-and-Reduction.md`](./05-Lecture-LVM-Creation-Expansion-and-Reduction.md) |
| **06** | Exercise | 8 mins | **[`06-Exercise-LVM-PV-VG-LV-and-Resize-Lab.html`](./06-Exercise-LVM-PV-VG-LV-and-Resize-Lab.html)** | [`06-Exercise-LVM-PV-VG-LV-and-Resize-Lab.md`](./06-Exercise-LVM-PV-VG-LV-and-Resize-Lab.md) |
| **07** | Lecture | 7 mins | **[`07-Lecture-Network-Configuration-and-Diagnosis.html`](./07-Lecture-Network-Configuration-and-Diagnosis.html)** | [`07-Lecture-Network-Configuration-and-Diagnosis.md`](./07-Lecture-Network-Configuration-and-Diagnosis.md) |
| **08** | Exercise | 8 mins | **[`08-Exercise-Nmcli-Hostname-and-Network-Diagnosis-Lab.html`](./08-Exercise-Nmcli-Hostname-and-Network-Diagnosis-Lab.html)** | [`08-Exercise-Nmcli-Hostname-and-Network-Diagnosis-Lab.md`](./08-Exercise-Nmcli-Hostname-and-Network-Diagnosis-Lab.md) |