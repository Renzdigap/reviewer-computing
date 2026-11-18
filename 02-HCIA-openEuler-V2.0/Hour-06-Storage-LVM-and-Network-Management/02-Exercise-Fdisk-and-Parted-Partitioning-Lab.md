# Hands-On Lab: Inspecting File Systems (`lsblk -f`, `fdisk -l`) and Non-Interactive GPT Partitioning (`parted`)

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 06 — openEuler Disk Partitioning, LVM & Network Management (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-Storage-File-Systems-and-Disk-Partitioning`  
**Interactive Workbench:** Open **[`02-Exercise-Fdisk-and-Parted-Partitioning-Lab.html`](./02-Exercise-Fdisk-and-Parted-Partitioning-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You have attached a new 4 TB disk `/dev/sdb` to an openEuler server. Because it exceeds 2 TB, you must inspect existing disks with `fdisk -l` and `lsblk -f`, and then use `parted` in non-interactive mode to initialize `/dev/sdb` with a `gpt` partition table and create a primary partition.

### Step-by-Step Instructions
1. Step 1: View all disks and partitions using `fdisk -l` and check file system types using `lsblk -f`.
2. Step 2: Use `parted` in non-interactive mode to convert `/dev/sdb` to a GPT partition table (`parted /dev/sdb mklabel gpt`).
3. Step 3: Use `parted` in non-interactive mode to create a 1000 MB partition on `/dev/sdb` (`parted /dev/sdb mkpart primary 0 1000`).

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: List all disks/partitions and check file system types
<fdisk_list_command>
<lsblk_fs_command>

# Step 2: Change /dev/sdb partition table format to GPT using parted
<parted_mklabel_command>

# Step 3: Create a partition from 0 to 1000 MB on /dev/sdb using parted
<parted_mkpart_command>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `fdisk -l` and `lsblk -f`.
- Use `parted /dev/sdb mklabel gpt` (exact command from Ch.05 p.276).
- Use `parted /dev/sdb mkpart primary 0 1000` (exact command from Ch.05 p.276).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: List all disks/partitions and check file system types
fdisk -l
lsblk -f

# Step 2: Change /dev/sdb partition table format to GPT using parted
parted /dev/sdb mklabel gpt

# Step 3: Create a partition from 0 to 1000 MB on /dev/sdb using parted
parted /dev/sdb mkpart primary 0 1000
```

#### Expected Console / Query Output:
```text
Disk /dev/vda: 40 GiB, 42949672960 bytes, 83886080 sectors
Disklabel type: gpt
NAME               FSTYPE      MOUNTPOINT
vda1               vfat        /boot/efi
vda2               ext4        /boot
└─openeuler-root   ext4        /

Information: You may need to update /etc/fstab.
Model: Virtio Block Device (virtblk)
Disk /dev/sdb: 4000GB
Partition Table: gpt
Number  Start   End     Size    File system  Name     Flags
 1      1049kB  1000MB  999MB                primary
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**What is the default file system on openEuler, and what does the device name `/dev/sdb6` represent?**

- A. `xfs`; the 6th primary partition on the 2nd SATA disk
- B. `ext4`; the 2nd logical partition on the 2nd SCSI/SATA disk
- C. `btrfs`; the 6th logical partition on the 1st IDE disk
- D. `vfat`; the 1st extended partition on the 2nd virtio disk

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.05 (p.259 & p.268), the default file system on openEuler is `ext4`. In `/dev/xxyN`, primary/extended partitions are numbered 1 to 4 and logical partitions start from 5, so `/dev/sdb6` is the second logical partition on the second SCSI disk.
</details>

### Question 2 [Single-Choice]
**What is the maximum disk/partition size supported by the MBR partitioning scheme (`fdisk`), and how many partitions per disk are supported by GPT (`parted`)?**

- A. MBR max: 512 GB; GPT max: 64 partitions
- B. MBR max: 2 TB; GPT max: 128 partitions (up to 18 EB)
- C. MBR max: 18 EB; GPT max: 4 primary partitions
- D. MBR max: 4 TB; GPT max: 15 partitions

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.05 (pp.269–273), MBR uses 32-bit values and cannot exceed 2 TB, whereas GPT uses 64-bit LBA (up to 18 EB) and supports up to 128 partitions per disk.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following commands can be used in openEuler to check the file system type of a partition?**

- A. `lsblk -f`
- B. `blkid`
- C. `df -T`
- D. `pwd -P`

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.05 (p.260), the three commands used to check the file system type of a partition in Linux are `lsblk -f`, `blkid`, and `df -T`.
</details>
