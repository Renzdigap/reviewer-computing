# 🏆 HCIA-openEuler V2.0 — National Stage Final Mock Exam

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Time Limit:** 60 Minutes  
**Total Score:** 1000 Points (Passing / National Finalist Target: 800 Points)  
**Instructions:** 60 Questions in 60 Minutes: 20 Single-Choice (15 pts each), 20 Multiple-Choice (20 pts each, strict all-or-nothing grading), 10 True/False (10 pts each), and 10 Hands-On openEuler/Shell/iSula Labs (20 pts each).

> 💡 **Interactive Timed Mode:** Open **[`Final-Mock-Exam.html`](./Final-Mock-Exam.html)** in your browser for a realistic 60-minute countdown timer, question navigator palette, strict Huawei multi-choice auto-grading, and chapter-by-chapter analytics!

---

### Q1. [Single-Choice — 15 pts] (Ch.02 Getting Started with openEuler)
**(Official Ch.02 Quiz Q2) Which of the following keys can be used in the openEuler Bash shell to quickly supplement (auto-complete) commands, options, and file parameters?**

- [ ] A. Ctrl+L
- [ ] B. Up and Down arrows
- [ ] C. Tab
- [ ] D. Space

### Q2. [Single-Choice — 15 pts] (Ch.02 Getting Started with openEuler)
**In the openEuler source code repository, which directory explicitly declares all open-source licenses in use, and what is China's first open-source license adopted by openEuler?**

- [ ] A. /etc/licenses directory; GPLv2
- [ ] B. LICENSES directory; Mulan PSL (Mulan Permissive Software License)
- [ ] C. /usr/share/doc directory; MIT
- [ ] D. COPYRIGHT directory; BSD 3-Clause

### Q3. [Single-Choice — 15 pts] (Ch.03 openEuler CLI Basics)
**(Official Ch.03 Quiz Q1) How many lines of a file are displayed by default when running the `head` command without any `-n` option?**

- [ ] A. 5
- [ ] B. 10
- [ ] C. 15
- [ ] D. 20

### Q4. [Single-Choice — 15 pts] (Ch.03 openEuler CLI Basics)
**Which Linux virtual directory is a direct mapping of system kernel and memory state, allowing administrators to read CPU, memory, and process info directly?**

- [ ] A. /etc
- [ ] B. /var
- [ ] C. /proc
- [ ] D. /opt

### Q5. [Single-Choice — 15 pts] (Ch.03 openEuler CLI Basics)
**When creating links with `ln`, what happens if you create a symbolic (soft) link with `ln -s target linkname` and later delete the original `target` file?**

- [ ] A. The soft link remains valid and retains a full copy of the original file data
- [ ] B. The soft link becomes a dangling/invalid link because it only stores the path to the target
- [ ] C. The kernel automatically converts the soft link into a hard link
- [ ] D. Both the target and link share the same inode, so data cannot be removed until linkname is deleted

### Q6. [Single-Choice — 15 pts] (Ch.03 openEuler CLI Basics)
**In Vim Command-line (Last-line) mode, which command globally replaces all occurrences of `foo` with `bar` across the entire file?**

- [ ] A. :s/foo/bar
- [ ] B. :%s/foo/bar/g
- [ ] C. :r/foo/bar/all
- [ ] D. /foo/bar/g

### Q7. [Single-Choice — 15 pts] (Ch.04 openEuler System Configuration)
**(Official Ch.04 Quiz Q1) Which of the following commands can be used to dynamically check host resource usage (CPU, memory, load average, and running processes) in real time?**

- [ ] A. ps
- [ ] B. top
- [ ] C. free
- [ ] D. lscpu

### Q8. [Single-Choice — 15 pts] (Ch.04 openEuler System Configuration)
**If the current shell `umask` is `0022`, what are the default numeric permissions assigned to a newly created regular file and a newly created directory respectively?**

- [ ] A. File: 666; Directory: 777
- [ ] B. File: 755; Directory: 644
- [ ] C. File: 644; Directory: 755
- [ ] D. File: 600; Directory: 700

### Q9. [Single-Choice — 15 pts] (Ch.04 openEuler System Configuration)
**In `/etc/passwd`, which two colon-separated columns represent the user's UID and login shell respectively?**

- [ ] A. 2nd column and 6th column
- [ ] B. 3rd column and 7th column
- [ ] C. 4th column and 5th column
- [ ] D. 1st column and 7th column

### Q10. [Single-Choice — 15 pts] (Ch.04 openEuler System Configuration)
**When sending process termination signals using `kill`, what is the key difference between signal `15 (SIGTERM)` and signal `9 (SIGKILL)`?**

- [ ] A. Signal 15 pauses a process; Signal 9 resumes it
- [ ] B. Signal 15 requests graceful termination (can be caught/ignored); Signal 9 forces unconditional immediate termination by the kernel
- [ ] C. Signal 9 reloads configuration files without stopping the PID
- [ ] D. Signal 15 can only be executed by root, while Signal 9 is for regular users

### Q11. [Single-Choice — 15 pts] (Ch.05 Storage and Network Management)
**(Official Ch.05 Quiz Q2) Which of the following commands correctly formats the `/dev/hdb6` partition with the ext4 file system?**

- [ ] A. mkfs -t ext4 /dev/hdb6
- [ ] B. format -t ext4 /dev/hdb6
- [ ] C. format /dev/hdb6
- [ ] D. makefile -t ext4 /dev/hdb6

### Q12. [Single-Choice — 15 pts] (Ch.05 Storage and Network Management)
**Under the traditional MBR disk partitioning scheme for a SCSI disk, what are the maximum disk capacity and partition limits?**

- [ ] A. Max 16 TB; up to 128 primary partitions
- [ ] B. Max 2 TB; up to 4 primary partitions (or 3 primary + 1 extended) and at most 15 partitions total on a SCSI disk
- [ ] C. Max 2 TB; unlimited primary partitions
- [ ] D. Max 4 TB; up to 8 primary partitions

### Q13. [Single-Choice — 15 pts] (Ch.05 Storage and Network Management)
**In LVM online expansion of an `xfs` file system after running `lvextend -L +5G /dev/vg01/lv01`, which command grows the XFS file system to occupy the newly added space?**

- [ ] A. resize2fs /dev/vg01/lv01
- [ ] B. xfs_growfs /mount_point
- [ ] C. e2fsck -f /dev/vg01/lv01
- [ ] D. pvresize /dev/vg01/lv01

### Q14. [Single-Choice — 15 pts] (Ch.05 Storage and Network Management)
**When shrinking an ext4 Logical Volume (LV) offline, what is the mandatory safe sequence of operations?**

- [ ] A. lvreduce -> resize2fs -> e2fsck -f -> umount
- [ ] B. umount -> e2fsck -f -> resize2fs -> lvreduce -> mount
- [ ] C. resize2fs -> lvreduce -> umount -> mount
- [ ] D. umount -> lvreduce -> resize2fs -> mount

### Q15. [Single-Choice — 15 pts] (Ch.06 Shell Scripts)
**(Official Ch.06 Quiz Q1) What is the meaning of the `*` operator in a shell script arithmetic expression such as `$((a * b))`?**

- [ ] A. Summation
- [ ] B. Multiplication
- [ ] C. Subtraction
- [ ] D. Division

### Q16. [Single-Choice — 15 pts] (Ch.06 Shell Scripts)
**Which special Bash variable retrieves the exit code of the most recently executed foreground command, and which value indicates success?**

- [ ] A. `$#`; 1 indicates success
- [ ] B. `$?`; 0 indicates success
- [ ] C. `$$`; 0 indicates success
- [ ] D. `$@`; 255 indicates success

### Q17. [Single-Choice — 15 pts] (Ch.06 Shell Scripts)
**Which Bash command-line flag executes a shell script in debugging mode, printing each expanded command prefixed with `+` before executing it?**

- [ ] A. bash -d script.sh
- [ ] B. bash -x script.sh
- [ ] C. bash -v script.sh
- [ ] D. bash -n script.sh

### Q18. [Single-Choice — 15 pts] (Ch.07 Native Container Engine iSula)
**What is the configuration precedence order (highest to lowest priority) for the `iSulad` container daemon?**

- [ ] A. /etc/isulad/daemon.json > CLI arguments > default code settings
- [ ] B. CLI arguments (or /etc/sysconfig/iSulad OPTIONS) > /etc/isulad/daemon.json > default configurations in code
- [ ] C. Default configurations in code > /etc/isulad/daemon.json > CLI arguments
- [ ] D. Environment variables > /etc/cni/net.d > CLI arguments

### Q19. [Single-Choice — 15 pts] (Ch.07 Native Container Engine iSula)
**In the `OverlayFS` union file system used by container images, which directory acts as an internal scratch directory and is invisible to users?**

- [ ] A. lowerdir
- [ ] B. upperdir
- [ ] C. merged
- [ ] D. workdir

### Q20. [Single-Choice — 15 pts] (Ch.07 Native Container Engine iSula)
**Which southbound OCI container runtime does `iSulad` use by default, and which network mode does `iSula` currently support with CNI?**

- [ ] A. runC; overlay network mode
- [ ] B. LCR (Lightweight Container Runtime); bridge network mode
- [ ] C. containerd; macvlan network mode
- [ ] D. Kata; host-only mode

### Q21. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.01 OS for the AI Era)
**Which of the following are core intelligent O&M and AI capabilities provided by the `openEuler Intelligence` platform?**

- [ ] A. Intelligent Q&A (Natural language interaction, OCR, and knowledge retrieval via RAG)
- [ ] B. AI Application Development Framework (Agents and workflow orchestration)
- [ ] C. Intelligent Optimization (AI-assisted parameter tuning and performance optimization)
- [ ] D. Intelligent Diagnosis & Intelligent Container Image analysis

### Q22. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.02 Getting Started with openEuler)
**According to Richard Stallman and the Free Software Foundation (FSF), which four essential freedoms define Free Software?**

- [ ] A. Freedom to run the program for any purpose
- [ ] B. Freedom to study/learn how the program works and modify the source code
- [ ] C. Freedom to redistribute copies of the program
- [ ] D. Freedom to create and distribute modified derivative versions

### Q23. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.02 Getting Started with openEuler)
**Which of the following statements about openEuler releases and licenses are TRUE?**

- [ ] A. Mulan PSL covers five major aspects: copyright license, patent license, non-trademark license, distribution restriction, and disclaimer/liability limitation.
- [ ] B. BSD permits modifying, redistributing, and developing commercial software based on the open-source code.
- [ ] C. Before contributing code to the openEuler community on Gitee, contributors must sign a Contributor License Agreement (CLA).
- [ ] D. openEuler Innovation releases receive a 6-year enterprise support lifecycle, whereas LTS releases receive only 6 months.

### Q24. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.03 openEuler CLI Basics)
**Which of the following help commands can be used on openEuler to inspect command usage, manuals, or brief one-line descriptions?**

- [ ] A. man <command>
- [ ] B. <command> --help
- [ ] C. help <builtin_command>
- [ ] D. whatis <command>

### Q25. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.03 openEuler CLI Basics)
**Which of the following statements about `tar` and `gzip` archive/compression operations on openEuler are TRUE?**

- [ ] A. `gzip` typically achieves a 60%–70% compression ratio and replaces the original uncompressed file with a `.gz` file by default.
- [ ] B. `tar -czvf backup.tar.gz /etc/hosts` creates a gzip-compressed tar archive.
- [ ] C. `tar -tf backup.tar.gz` lists the contents of an archive without extracting it.
- [ ] D. `tar -xzvf backup.tar.gz -C /tmp` extracts the archive into `/tmp`.

### Q26. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.03 openEuler CLI Basics)
**Which of the following Linux text processing commands and options are matched with their TRUE functions?**

- [ ] A. `grep -i` performs case-insensitive pattern matching; `grep -v` inverts the match (prints non-matching lines).
- [ ] B. `cut -d ':' -f 1,7 /etc/passwd` extracts the 1st and 7th colon-delimited fields.
- [ ] C. `wc -l` counts lines, while `sort -n -r` sorts numerically in descending order.
- [ ] D. `awk -F ':' '{print $1}' /etc/passwd` prints the first field of each line using `:` as the field separator.

### Q27. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.04 openEuler System Configuration)
**Which of the following statements about Linux file types and `chmod`/`chown`/`sticky bit` permissions are TRUE?**

- [ ] A. The 7 Linux file types shown by `ls -l` are `-` (regular), `d` (directory), `l` (symlink), `b` (block), `c` (character), `p` (named pipe), and `s` (socket).
- [ ] B. Setting the sticky bit (`chmod o+t /share` or `chmod 1777 /share`) ensures that only the file owner, directory owner, or root can delete or rename files inside `/share`.
- [ ] C. `chown -R user1:group1 /data` recursively changes both the owner and the owning group of `/data`.
- [ ] D. If `ls -l` displays a `+` sign right after the permission string (e.g., `-rw-r--r--+`), the file has an extended Access Control List (ACL) configured.

### Q28. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.04 openEuler System Configuration)
**Which of the following statements about RPM and DNF software package management on openEuler are TRUE?**

- [ ] A. `rpm -qa` queries all installed RPM packages, while `rpm -qf /usr/bin/vim` queries which package owns that file.
- [ ] B. `/etc/dnf/dnf.conf` is the main global configuration file for DNF, and repository `.repo` files reside in `/etc/yum.repos.d/`.
- [ ] C. Running `rpm -e --nodeps <pkg>` removes a package while ignoring dependencies, which may break dependent software.
- [ ] D. `dnf` resolves package dependencies automatically, whereas `rpm -ivh` requires dependencies to be resolved manually.

### Q29. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.04 openEuler System Configuration)
**Which of the following `systemctl` and `journald` commands are valid for managing services and inspecting logs on openEuler?**

- [ ] A. `systemctl enable --now httpd` enables the service at boot and starts it immediately.
- [ ] B. `systemctl status sshd` displays the running status, PID, and recent log lines of `sshd`.
- [ ] C. `journalctl -u sshd` queries systemd journal logs specifically for the `sshd` unit.
- [ ] D. A standard systemd `.service` unit file contains three main sections: `[Unit]`, `[Service]`, and `[Install]`.

### Q30. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.04 openEuler System Configuration)
**Which of the following statements about process scheduling priority (`nice`), background jobs, and scheduled tasks (`at`/`crontab`) are TRUE?**

- [ ] A. The `nice` value ranges from `-20` (highest priority) to `+19` (lowest priority), and only `root` can assign negative nice values.
- [ ] B. Pressing `Ctrl+Z` suspends a foreground job and puts it in the background in Stopped state; `bg %1` resumes it in the background, and `fg %1` brings it back to the foreground.
- [ ] C. `at` schedules a one-time task (`Ctrl+D` saves the job), while `crontab` schedules recurring periodic tasks using 5 time fields (`min hour dom month dow`).
- [ ] D. Non-root users can execute `renice -n -10 -p <PID>` to increase the priority of any system process.

### Q31. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.05 Storage and Network Management)
**Which of the following statements about persistent storage, `parted`, and `/etc/fstab` are TRUE?**

- [ ] A. On openEuler, `ext4` and `xfs` are common disk file systems; `blkid` and `lsblk -f` inspect block device UUIDs and file system types.
- [ ] B. `parted` supports both MBR and GPT partitioning schemes and can run in both interactive mode and non-interactive script mode.
- [ ] C. In `/etc/fstab`, the 6 columns in order are: Device/UUID, Mount Point, File System Type, Mount Options, Dump backup flag, and fsck Pass order.
- [ ] D. Setting the `noatime` option in `/etc/fstab` disables updating access timestamps on reads and improves file system performance.

### Q32. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.05 Storage and Network Management)
**Which of the following statements accurately describe Logical Volume Management (LVM) layers and commands on openEuler?**

- [ ] A. The LVM hierarchy flows bottom-up: Physical Disk/Partition -> Physical Volume (`pvcreate`) -> Volume Group (`vgcreate`) -> Logical Volume (`lvcreate`) -> File System (`mkfs`).
- [ ] B. A Volume Group (VG) divides storage into fixed-size Physical Extents (PEs), which default to 4 MiB.
- [ ] C. `vgextend vg01 /dev/sdc1` adds a new Physical Volume into an existing Volume Group `vg01`.
- [ ] D. `lvcreate -L 10G -n lv_data vg01` creates a 10 GiB Logical Volume named `lv_data` inside `vg01`.

### Q33. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.05 Storage and Network Management)
**Which of the following `nmcli` and network diagnostic commands are valid on openEuler?**

- [ ] A. `nmcli con add con-name "Euler" type Ethernet ifname enp3s0` creates a new Ethernet connection profile.
- [ ] B. `nmcli con mod "Euler" +ipv4.routes "192.168.10.0/24 10.0.0.1"` appends a persistent static route to the connection.
- [ ] C. `ss -tulnp` inspects listening TCP/UDP sockets along with their owning process PIDs.
- [ ] D. `tracepath <destination>` traces the network hop path and path MTU to a remote host.

### Q34. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.06 Shell Scripts)
**Which of the following statements about Bash I/O redirection, pipes, and quoting are TRUE?**

- [ ] A. File descriptors `0`, `1`, and `2` correspond to Standard Input (stdin), Standard Output (stdout), and Standard Error (stderr).
- [ ] B. `command &> output.log` redirects both stdout and stderr to `output.log` (overwriting its content).
- [ ] C. Single quotes (`'...'`) preserve literal characters and prevent variable/command expansion, whereas double quotes (`"..."`) allow `$var` and `$(cmd)` expansion.
- [ ] D. A pipe (`cmd1 | cmd2`) sends the stdout of `cmd1` directly as the stdin of `cmd2`.

### Q35. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.06 Shell Scripts)
**Which of the following statements about Bash variables, test conditions, and loops are TRUE?**

- [ ] A. `$#` gives the number of positional arguments passed to a script, while `$0` is the script's own name.
- [ ] B. In `[ ... ]` test expressions, `-eq` and `-gt` compare integers, while `=` and `-z` evaluate strings.
- [ ] C. `[ -d /etc/dnf ]` returns exit code 0 (true) if `/etc/dnf` exists and is a directory.
- [ ] D. In loops, `break` exits the entire enclosing loop immediately, whereas `continue` skips the rest of the current iteration and jumps to the next iteration.

### Q36. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.06 Shell Scripts)
**When comparing a `while` loop and an `until` loop in Bash, which of the following statements are TRUE?**

- [ ] A. A `while` loop continues executing as long as its test condition evaluates to TRUE (exit code 0).
- [ ] B. An `until` loop continues executing as long as its test condition evaluates to FALSE (non-zero exit code), and stops once the condition becomes TRUE.
- [ ] C. Both `while` and `until` loops enclose their loop body between `do` and `done`.
- [ ] D. In `i++` (post-increment), the current value of `i` is returned first and then `i` is incremented by 1.

### Q37. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.07 Native Container Engine iSula)
**(Official Ch.07 Quiz Q1) Which of the following are valid container states in `iSula`?**

- [ ] A. Created
- [ ] B. Exited
- [ ] C. Up
- [ ] D. Paused

### Q38. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.07 Native Container Engine iSula)
**Which Linux kernel mechanisms provide container isolation and resource limits, and what makes `iSula` distinct from Docker?**

- [ ] A. Linux `Namespaces` provide isolation (PID, NET, MNT, IPC, UTS, User), while `cgroups` enforce CPU/memory/I/O resource quotas.
- [ ] B. `iSulad` is written in C/C++ (unlike Go-based Docker), giving it a smaller memory footprint and ~35% faster concurrent container startup.
- [ ] C. `iSula` provides northbound CLI and Kubernetes CRI interfaces and southbound OCI interfaces (`LCR`, `runC`, `Kata`).
- [ ] D. `iSula` can manage both lightweight application containers and system containers.

### Q39. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.07 Native Container Engine iSula)
**Which of the following `isula` CLI commands perform the stated container lifecycle operations?**

- [ ] A. `isula exec -it mybox /bin/sh` runs an interactive shell inside a running container named `mybox`.
- [ ] B. `isula logs mybox` retrieves stdout/stderr logs generated by container `mybox`.
- [ ] C. `isula inspect mybox` outputs detailed low-level JSON metadata (IP, mounts, state) for `mybox`.
- [ ] D. `isula rm -f mybox` forcibly deletes a container (even if currently running).

### Q40. [Multiple-Choice (Select ALL Correct) — 20 pts] (Ch.07 Native Container Engine iSula)
**Which of the following statements about container image layering and Copy-on-Write (CoW) in `iSula` are TRUE?**

- [ ] A. A container image consists of read-only image layers (rootfs/app layers), and running a container mounts a thin read-write container layer on top.
- [ ] B. When a container attempts to modify a file located in a read-only `lowerdir`, OverlayFS performs a `copy_up` operation to copy the file into `upperdir` before modifying it.
- [ ] C. Deleting a file that resides in a read-only image layer creates a `whiteout` file in `upperdir` to hide it without modifying the underlying image.
- [ ] D. `isula pull`, `isula tag`, `isula images`, and `isula rmi` manage local container images on the host.

### Q41. [True / False — 10 pts] (Ch.01 OS for the AI Era)
**(Official Ch.01 Quiz Q1) The `openEuler Intelligence` platform currently supports two interaction entries: Web entry and Intelligent Shell entry.**

- [ ] A. True
- [ ] B. False

### Q42. [True / False — 10 pts] (Ch.02 Getting Started with openEuler)
**(Official Ch.02 Quiz Q1) You do not need to specify the password of the `root` user during the openEuler OS installation; however, you must specify the password of the `root` user when logging in to the OS after the installation.**

- [ ] A. True
- [ ] B. False

### Q43. [True / False — 10 pts] (Ch.03 openEuler CLI Basics)
**In the openEuler filesystem, `less` allows only forward (downward) page scrolling and cannot scroll backward, whereas `more` supports full bidirectional scrolling.**

- [ ] A. True
- [ ] B. False

### Q44. [True / False — 10 pts] (Ch.03 openEuler CLI Basics)
**Running `locate myfile.conf` searches an internal file index database (`mlocate.db`), so newly created files may not appear until `updatedb` is executed.**

- [ ] A. True
- [ ] B. False

### Q45. [True / False — 10 pts] (Ch.04 openEuler System Configuration)
**The `su root` command switches identity to `root` AND resets all environment variables (including `$PATH` and `$HOME`) to `root`'s login environment, making it completely identical to `su - root`.**

- [ ] A. True
- [ ] B. False

### Q46. [True / False — 10 pts] (Ch.04 openEuler System Configuration)
**Unlike `at`, which uses `cron` daemon configuration files, `crontab -e` edits a user's personal periodic schedule, and modifying it immediately notifies `crond` without requiring a service restart.**

- [ ] A. True
- [ ] B. False

### Q47. [True / False — 10 pts] (Ch.05 Storage and Network Management)
**(Official Ch.05 Quiz Q1) The `route` command can view or configure host route information, and route entries configured with `route add` remain valid permanently across system reboots.**

- [ ] A. True
- [ ] B. False

### Q48. [True / False — 10 pts] (Ch.06 Shell Scripts)
**(Official Ch.06 Quiz Q2) An administrator can run the `name==Tom` command in a Bash script to assign the value `Tom` to the variable `name`.**

- [ ] A. True
- [ ] B. False

### Q49. [True / False — 10 pts] (Ch.06 Shell Scripts)
**If a shell script does not have execute (`+x`) permission, it cannot be invoked directly via `./script.sh`, but it can still be executed via `bash script.sh` or `sh script.sh`.**

- [ ] A. True
- [ ] B. False

### Q50. [True / False — 10 pts] (Ch.07 Native Container Engine iSula)
**A container started in `iSula` with `-v /root/test2.txt:/tmp/test2.txt:ro` allows processes inside the container to modify `/tmp/test2.txt` and persist those edits to the host.**

- [ ] A. True
- [ ] B. False

### Q51. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.03 openEuler CLI Basics)
**Lab 1 (Text Processing Pipeline): Complete the command pipeline to extract all lines from `/etc/passwd` whose login shell ends with `bash`, then print ONLY column 1 (username) and column 7 (shell) using `awk` with `:` as delimiter.**

```bash
____ 'bash$' /etc/passwd | ____ ____ ':' '{print $1, $7}'
```
*Write your command / SQL / answer below:*
```text

```

### Q52. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.03 openEuler CLI Basics)
**Lab 2 (Archive & Symbolic Link): Write two commands: (1) create a gzip-compressed tar archive `/tmp/etc_conf.tar.gz` from `/etc/hosts`, and (2) create a symbolic (soft) link `/tmp/hosts.link` pointing to `/etc/hosts`.**

```bash
tar ____ /tmp/etc_conf.tar.gz /etc/hosts
ln ____ /etc/hosts /tmp/hosts.link
```
*Write your command / SQL / answer below:*
```text

```

### Q53. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.04 openEuler System Configuration)
**Lab 3 (User & ACL Permissions): Write two commands: (1) add existing user `alice` to supplementary group `wheel` WITHOUT removing her existing groups, and (2) grant user `alice` read-write-execute (`rwx`) ACL permission on `/opt/app.log`.**

```bash
usermod ____ wheel alice
setfacl ____ u:alice:rwx /opt/app.log
```
*Write your command / SQL / answer below:*
```text

```

### Q54. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.04 openEuler System Configuration)
**Lab 4 (Systemd & Crontab): Write: (1) the command to enable and immediately start the `httpd` service, and (2) a `crontab` schedule line that runs `/usr/local/bin/backup.sh` every day at 02:30 AM.**

```bash
systemctl ____ --now httpd
__ __ * * * /usr/local/bin/backup.sh
```
*Write your command / SQL / answer below:*
```text

```

### Q55. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.05 Storage and Network Management)
**Lab 5 (LVM Provisioning Workflow): Complete the 4-step LVM creation commands to initialize `/dev/sdb1` as a PV, create Volume Group `vg_data`, create a 20G Logical Volume `lv_app` inside `vg_data`, and format it as `ext4`.**

```bash
____ /dev/sdb1
____ vg_data /dev/sdb1
____ -L 20G -n lv_app vg_data
mkfs ____ /dev/vg_data/lv_app
```
*Write your command / SQL / answer below:*
```text

```

### Q56. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.05 Storage and Network Management)
**Lab 6 (Online LV Expansion & NetworkManager): Complete the commands to: (1) extend `/dev/vg_data/lv_app` by adding 10G and grow its `ext4` file system online, and (2) activate an `nmcli` connection named `Euler`.**

```bash
____ -L +10G /dev/vg_data/lv_app
____ /dev/vg_data/lv_app
nmcli ____ ____ "Euler"
```
*Write your command / SQL / answer below:*
```text

```

### Q57. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.06 Shell Scripts)
**Lab 7 (Bash Conditional & Variable Assignment): Fix the variable assignment and complete the `if` statement that checks whether `/etc/isulad/daemon.json` is a regular file (`-f`) and prints `Configured`.**

```bash
#!/bin/bash
CFG____"/etc/isulad/daemon.json"
if [ ____ "$CFG" ]; ____
    echo "Configured"
____
```
*Write your command / SQL / answer below:*
```text

```

### Q58. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.06 Shell Scripts)
**Lab 8 (Bash Loop & Arithmetic): Complete the `for` loop and arithmetic expression to accumulate the sum of odd numbers (`1, 3, 5, ..., 99`) using `seq` or brace expansion and `$(( ... ))`.**

```bash
#!/bin/bash
sum=0
for i in $(seq 1 2 99); ____
    sum=____
done
echo $sum
```
*Write your command / SQL / answer below:*
```text

```

### Q59. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.07 Native Container Engine iSula)
**Lab 9 (iSula Container Deployment with Persistent Storage): Write the `isula` command to run an interactive container named `web01` from image `openeuler/nginx:latest`, bind-mounting `/root/html` to `/usr/share/nginx/html` in read-write mode and executing `/bin/bash`.**

```bash
isula ____ -it -n web01 ____ /root/html:/usr/share/nginx/html:rw openeuler/nginx:latest /bin/bash
```
*Write your command / SQL / answer below:*
```text

```

### Q60. [Practical Command / SQL / Scenario Lab — 20 pts] (Ch.07 Native Container Engine iSula)
**Lab 10 (iSula Debugging & Image Cleanup): Write two commands: (1) execute `ip addr` inside a running container named `web01`, and (2) remove an unused local container image `busybox:test`.**

```bash
isula ____ web01 ip addr
isula ____ busybox:test
```
*Write your command / SQL / answer below:*
```text

```
