# Hands-On Lab: Searching Stale Logs, Packing `.tar.gz` Archives & Testing Links

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 02 — openEuler CLI Basics & File Operations (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Search-Compression-and-Links`  
**Interactive Workbench:** Open **[`08-Exercise-Find-Tar-and-Links-Lab.html`](./08-Exercise-Find-Tar-and-Links-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You need to locate all regular files in `/var/log/anaconda/` modified more than 7 days ago, pack all `.log` files in the current directory into `log.tar.gz` and extract them into `./log/`, and create both a hard link (`link_h_password`) and a soft link (`link_s_password`) to `passwd`.

### Step-by-Step Instructions
1. Step 1: Search `/var/log/anaconda/` for regular files (`-type f`) with modification time earlier than 7 days (`-mtime +7`) using `find`.
2. Step 2: Pack and compress `*.log` into `log.tar.gz` using `tar -zcf log.tar.gz *.log` and extract it to `./log/` using `tar -zxf log.tar.gz -C ./log/`.
3. Step 3: Create a hard link `ln passwd link_h_password` and a soft link `ln -s passwd link_s_password`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Find regular files in /var/log/anaconda/ modified more than 7 days ago
<find_command>

# Step 2: Compress *.log into log.tar.gz and extract to ./log/
<tar_create_command>
mkdir -p ./log
<tar_extract_command>

# Step 3: Create hard link and soft link to passwd
<ln_hard_command>
<ln_soft_command>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `find /var/log/anaconda/ -type f -mtime +7`.
- Use `tar -zcf log.tar.gz *.log` and `tar -zxf log.tar.gz -C ./log/`.
- Use `ln passwd link_h_password` (no flags for hard link) and `ln -s passwd link_s_password` (`-s` for soft link).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Find regular files in /var/log/anaconda/ modified more than 7 days ago
find /var/log/anaconda/ -type f -mtime +7

# Step 2: Compress *.log into log.tar.gz and extract to ./log/
tar -zcf log.tar.gz *.log
mkdir -p ./log
tar -zxf log.tar.gz -C ./log/

# Step 3: Create hard link and soft link to passwd
ln passwd link_h_password
ln -s passwd link_s_password
```

#### Expected Console / Query Output:
```text
/var/log/anaconda/anaconda.log
/var/log/anaconda/syslog
/var/log/anaconda/storage.log

[root@openEuler ~]# ls ./log
test01.log  test02.log

[root@openEuler ~]# ls -l *password*
-rw-------. 2 root root 2546 Nov 17 09:35 link_h_password
lrwxrwxrwx. 1 root root    6 Nov 17 09:35 link_s_password -> passwd
-rw-------. 2 root root 2546 Nov 17 09:35 passwd
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**When you run `locate filename` on openEuler and receive the error `locate: can not open '/var/lib/mlocate/mlocate.db': No such file or directory`, which command should you run first to generate or update the index database?**

- A. finddb
- B. updatedb
- C. mandb
- D. mkindex

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (pp.108–109), before running `locate` (or if `/var/lib/mlocate/mlocate.db` does not exist), you must run the `updatedb` command to generate/update the database.
</details>

### Question 2 [Single-Choice]
**Which `tar` option is used to specify the target directory when extracting an archive, and which compression options correspond to `gzip`, `bzip2`, and `xz` respectively?**

- A. -d for directory; -g, -b, -x for compression
- B. -C for directory; -z (gzip), -j (bzip2), -J (xz)
- C. -o for directory; -z (bzip2), -j (gzip), -J (xz)
- D. -p for directory; -c, -x, -t for compression

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p.113), `tar xf ball.tar -C /tmp` extracts to `/tmp`, and options `-z`, `-j`, and `-J` correspond to `gzip`, `bzip2`, and `xz` compression tools respectively.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements accurately compare soft links (`ln -s`) and hard links (`ln`) on Linux?**

- A. If the `ln` command is executed without any option, a hard link is created by default.
- B. Deleting the source file invalidates a soft link, but has no impact on accessing data through a hard link.
- C. Soft links support linking to directories and cross-file system linking.
- D. Hard links support cross-file system linking by default.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.03 (pp.115–116), A, B, and C are true. Option D is false because hard links share an inode within a single file system and do NOT support cross-file system linking.
</details>
