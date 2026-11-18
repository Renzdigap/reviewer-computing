# Hands-On Lab: Formatting `/dev/hdb6` (`mkfs -t ext4`), Temporary Mount & `/etc/fstab` Entry

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 06 — openEuler Disk Partitioning, LVM & Network Management (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-Formatting-Mounting-and-fstab`  
**Interactive Workbench:** Open **[`04-Exercise-Mkfs-Mount-and-Fstab-Persistence-Lab.html`](./04-Exercise-Mkfs-Mount-and-Fstab-Persistence-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You have created logical partition `/dev/hdb6` on an openEuler server. Format `/dev/hdb6` with the `ext4` file system using `mkfs -t ext4`, mount it temporarily to `/test`, and append a persistent mount entry to `/etc/fstab`.

### Step-by-Step Instructions
1. Step 1: Format `/dev/hdb6` as `ext4` using `mkfs -t ext4 /dev/hdb6` (exact Ch.05 Quiz Q2 syntax).
2. Step 2: Create mount point `/test` and mount `/dev/hdb6` to `/test` using `mount /dev/hdb6 /test`.
3. Step 3: Append the 6-field persistent entry `/dev/hdb6 /test ext4 defaults 0 2` to `/etc/fstab`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Format /dev/hdb6 with ext4 using mkfs -t
<mkfs_command>

# Step 2: Mount /dev/hdb6 to /test
mkdir -p /test
<mount_command>

# Step 3: Append persistent mount entry to /etc/fstab
echo "<fstab_6_fields>" >> /etc/fstab
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `mkfs -t ext4 /dev/hdb6` (Ch.05 Quiz Q2).
- Use `mount /dev/hdb6 /test`.
- Use `/dev/hdb6 /test ext4 defaults 0 2` inside the echo statement.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Format /dev/hdb6 with ext4 using mkfs -t
mkfs -t ext4 /dev/hdb6

# Step 2: Mount /dev/hdb6 to /test
mkdir -p /test
mount /dev/hdb6 /test

# Step 3: Append persistent mount entry to /etc/fstab
echo "/dev/hdb6 /test ext4 defaults 0 2" >> /etc/fstab
```

#### Expected Console / Query Output:
```text
mke2fs 1.46.5 (30-Dec-2021)
Creating filesystem with 262144 4k blocks and 65536 inodes
Allocating group tables: done
Writing superblocks and filesystem accounting information: done

[root@openEuler ~]# df -Th /test
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/hdb6      ext4  976M  2.6M  907M   1% /test
[root@openEuler ~]# tail -n 1 /etc/fstab
/dev/hdb6 /test ext4 defaults 0 2
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**[Official Ch.05 Quiz Q2] Which of the following commands can be used to format the `/dev/hdb6` partition?**

- A. mkfs -t ext4 /dev/hdb6
- B. format -t ext4 /dev/hdb6
- C. format /dev/hdb6
- D. makefile -t ext4 /dev/hdb6

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Official Ch.05 Quiz Q2 (p.318): A (`mkfs -t ext4 /dev/hdb6`). `mkfs` ('make file system') creates a Linux file system on a partition; `format` and `makefile` are invalid.
</details>

### Question 2 [Single-Choice]
**In `/etc/fstab`, what do the values `0`, `1`, and `2` in the 6th field (`<pass>`) specify?**

- A. Read-only (0), Read-write (1), Swap (2)
- B. The `fsck` check priority: `0` = do not check, `1` = root partition (`/`) checked first, `2` = other devices to be checked
- C. The number of backup copies created by `dump`
- D. The partition type: `0` = primary, `1` = extended, `2` = logical

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.05 (p.282), the `pass` field sets the `fsck` check priority: `1` for the root partition, `2` for other devices that need to be checked, and `0` for devices that will not be checked by `fsck`.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about `mkfs`, `mount`, and `/etc/fstab` are TRUE?**

- A. If `-t fstype` is omitted in the `mkfs` command, the default file system type for Linux `mkfs` is `ext2`.
- B. `mkfs -c` checks the partition for bad blocks before building the file system.
- C. Mounting a partition with `mount /dev/sda5 /test` is temporary and becomes invalid after a system restart.
- D. In `/etc/fstab`, the `noatime` option improves performance by not updating inode access records.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.05 (pp.279–282), all four statements are explicitly documented in the official training material.
</details>
