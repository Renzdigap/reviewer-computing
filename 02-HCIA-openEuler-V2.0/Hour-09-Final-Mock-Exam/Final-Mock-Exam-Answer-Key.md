# 🔑 Official Answer Key & Explanations — HCIA-openEuler V2.0 — National Stage Final Mock Exam

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Total Questions:** 60 (1000 Points)

---

### Q1 (Ch.02 Getting Started with openEuler) — [15 pts]
- **Question:** (Official Ch.02 Quiz Q2) Which of the following keys can be used in the openEuler Bash shell to quickly supplement (auto-complete) commands, options, and file parameters?
- **Correct Answer:** `C`
- **Explanation:** Per Ch.02 (p. 50 & p. 52), pressing Tab automatically completes commands, parameters, or filenames (pressing Tab twice lists all matching commands).

### Q2 (Ch.02 Getting Started with openEuler) — [15 pts]
- **Question:** In the openEuler source code repository, which directory explicitly declares all open-source licenses in use, and what is China's first open-source license adopted by openEuler?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.02 (p. 29 & p. 35), in the openEuler code repository the `LICENSES` directory declares the open-source licenses in use, and Mulan is China's first open-source license adopted by openEuler.

### Q3 (Ch.03 openEuler CLI Basics) — [15 pts]
- **Question:** (Official Ch.03 Quiz Q1) How many lines of a file are displayed by default when running the `head` command without any `-n` option?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p. 98, p. 141 & p. 151), both `head` and `tail` display 10 lines by default when no line count is specified.

### Q4 (Ch.03 openEuler CLI Basics) — [15 pts]
- **Question:** Which Linux virtual directory is a direct mapping of system kernel and memory state, allowing administrators to read CPU, memory, and process info directly?
- **Correct Answer:** `C`
- **Explanation:** Per Ch.03 (p. 80), `/proc` is a virtual directory mapping system memory; `/etc` holds configuration files, `/var` stores variable logs/spool data, and `/opt` stores third-party optional applications.

### Q5 (Ch.03 openEuler CLI Basics) — [15 pts]
- **Question:** When creating links with `ln`, what happens if you create a symbolic (soft) link with `ln -s target linkname` and later delete the original `target` file?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (pp. 115–116), a soft link points to a file path (different inode) and becomes invalid if the source file is deleted, whereas a hard link (`ln` without `-s`) shares the same inode and keeps the data intact until all hard links are deleted.

### Q6 (Ch.03 openEuler CLI Basics) — [15 pts]
- **Question:** In Vim Command-line (Last-line) mode, which command globally replaces all occurrences of `foo` with `bar` across the entire file?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p. 129), `%` targets all lines in the file and the `g` flag replaces all matches on each line (`:%s/foo/bar/g`).

### Q7 (Ch.04 openEuler System Configuration) — [15 pts]
- **Question:** (Official Ch.04 Quiz Q1) Which of the following commands can be used to dynamically check host resource usage (CPU, memory, load average, and running processes) in real time?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p. 249), `top` dynamically monitors real-time CPU, memory, and process resource usage; `ps` shows a static snapshot, `free` displays memory only, and `lscpu` displays CPU hardware architecture.

### Q8 (Ch.04 openEuler System Configuration) — [15 pts]
- **Question:** If the current shell `umask` is `0022`, what are the default numeric permissions assigned to a newly created regular file and a newly created directory respectively?
- **Correct Answer:** `C`
- **Explanation:** Per Ch.04 (p. 183), default base permissions are `666` for regular files (no execute bit by default) and `777` for directories. Subtracting `022` gives `644` (`rw-r--r--`) for files and `755` (`rwxr-xr-x`) for directories.

### Q9 (Ch.04 openEuler System Configuration) — [15 pts]
- **Question:** In `/etc/passwd`, which two colon-separated columns represent the user's UID and login shell respectively?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p. 161), `/etc/passwd` has 7 fields: `1:username`, `2:password placeholder (x)`, `3:UID`, `4:GID`, `5:description`, `6:home directory`, `7:login shell`.

### Q10 (Ch.04 openEuler System Configuration) — [15 pts]
- **Question:** When sending process termination signals using `kill`, what is the key difference between signal `15 (SIGTERM)` and signal `9 (SIGKILL)`?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p. 234), Signal 15 (`SIGTERM`, default for `kill PID`) allows a process to clean up and exit gracefully, whereas Signal 9 (`SIGKILL`) cannot be caught or ignored and terminates the process unconditionally.

### Q11 (Ch.05 Storage and Network Management) — [15 pts]
- **Question:** (Official Ch.05 Quiz Q2) Which of the following commands correctly formats the `/dev/hdb6` partition with the ext4 file system?
- **Correct Answer:** `A`
- **Explanation:** Per Ch.05 (p. 279 & p. 318), `mkfs -t <fstype> <device>` (or `mkfs.ext4 /dev/hdb6`) formats a partition on openEuler.

### Q12 (Ch.05 Storage and Network Management) — [15 pts]
- **Question:** Under the traditional MBR disk partitioning scheme for a SCSI disk, what are the maximum disk capacity and partition limits?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.05 (pp. 269 & 273), MBR has a 2 TB limit and allows up to 4 primary partitions (or 3 primary + 1 extended containing logical partitions, capped at 15 total partitions on SCSI disks), whereas GPT breaks the 2 TB limit and supports 128 primary partitions.

### Q13 (Ch.05 Storage and Network Management) — [15 pts]
- **Question:** In LVM online expansion of an `xfs` file system after running `lvextend -L +5G /dev/vg01/lv01`, which command grows the XFS file system to occupy the newly added space?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.05 (p. 298), `resize2fs` resizes ext2/ext3/ext4 file systems, while `xfs_growfs <mount_point>` (or `xfs_growfs <lv_device>`) expands mounted XFS file systems online.

### Q14 (Ch.05 Storage and Network Management) — [15 pts]
- **Question:** When shrinking an ext4 Logical Volume (LV) offline, what is the mandatory safe sequence of operations?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.05 (p. 299), you MUST unmount first (`umount`), check the filesystem (`e2fsck -f`), shrink the filesystem (`resize2fs`), shrink the LV (`lvreduce`), and finally remount (`mount`). Shrinking the LV before shrinking the filesystem destroys data!

### Q15 (Ch.06 Shell Scripts) — [15 pts]
- **Question:** (Official Ch.06 Quiz Q1) What is the meaning of the `*` operator in a shell script arithmetic expression such as `$((a * b))`?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.06 (p. 351 & p. 379), `*` performs arithmetic multiplication in shell arithmetic expressions (note: when using `expr`, `*` must be escaped as `\*` to avoid shell glob expansion).

### Q16 (Ch.06 Shell Scripts) — [15 pts]
- **Question:** Which special Bash variable retrieves the exit code of the most recently executed foreground command, and which value indicates success?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.06 (p. 372), `$?` stores the exit status of the previous command, where `0` means success and any non-zero value (1–255) indicates an error.

### Q17 (Ch.06 Shell Scripts) — [15 pts]
- **Question:** Which Bash command-line flag executes a shell script in debugging mode, printing each expanded command prefixed with `+` before executing it?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.06 (pp. 370–371), `bash -x script.sh` enables execution tracing (debugging mode), printing each command and its expanded arguments prior to execution.

### Q18 (Ch.07 Native Container Engine iSula) — [15 pts]
- **Question:** What is the configuration precedence order (highest to lowest priority) for the `iSulad` container daemon?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.07 (p. 401), iSulad configuration priority is strictly: `CLI > configuration file (/etc/isulad/daemon.json) > default configurations in code`. Modifying `OPTIONS` in `/etc/sysconfig/iSulad` is equivalent to CLI configuration.

### Q19 (Ch.07 Native Container Engine iSula) — [15 pts]
- **Question:** In the `OverlayFS` union file system used by container images, which directory acts as an internal scratch directory and is invisible to users?
- **Correct Answer:** `D`
- **Explanation:** Per Ch.07 (p. 433), OverlayFS uses `lowerdir` (read-only image layers), `upperdir` (writable container layer), `merged` (unified mount point), and `workdir` (internal helper directory invisible to users).

### Q20 (Ch.07 Native Container Engine iSula) — [15 pts]
- **Question:** Which southbound OCI container runtime does `iSulad` use by default, and which network mode does `iSula` currently support with CNI?
- **Correct Answer:** `B`
- **Explanation:** Per Ch.07 (p. 394 & p. 420), iSula uses LCR as its default southbound OCI runtime (while also supporting runC/Kata) and currently supports `bridge` mode for CNI networking.

### Q21 (Ch.01 OS for the AI Era) — [20 pts]
- **Question:** Which of the following are core intelligent O&M and AI capabilities provided by the `openEuler Intelligence` platform?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.01 (pp. 8–16), openEuler Intelligence delivers all four capability pillars: Intelligent Q&A, AI Application Development Framework, Intelligent Optimization, Intelligent Diagnosis, and Intelligent Container Images.

### Q22 (Ch.02 Getting Started with openEuler) — [20 pts]
- **Question:** According to Richard Stallman and the Free Software Foundation (FSF), which four essential freedoms define Free Software?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.02 (p. 29), FSF defines four freedoms: run for any purpose (0), learn and modify source code (1), redistribute programs (2), and create/distribute derivatives (3).

### Q23 (Ch.02 Getting Started with openEuler) — [20 pts]
- **Question:** Which of the following statements about openEuler releases and licenses are TRUE?
- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.02 (pp. 29–36), A, B, and C are true. D is reversed: openEuler LTS (Long Term Support) versions are released every 2 years with long-term maintenance, while Innovation versions are released every 6 months with shorter maintenance.

### Q24 (Ch.03 openEuler CLI Basics) — [20 pts]
- **Question:** Which of the following help commands can be used on openEuler to inspect command usage, manuals, or brief one-line descriptions?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.03 (pp. 65–69), `man` queries `/usr/share/man/*.gz` manual pages, `--help` queries external command options, `help` queries shell built-in commands, and `whatis` prints a brief summary from the man database.

### Q25 (Ch.03 openEuler CLI Basics) — [20 pts]
- **Question:** Which of the following statements about `tar` and `gzip` archive/compression operations on openEuler are TRUE?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.03 (pp. 111–114), all four statements accurately describe `gzip` and `tar` flags (`-c` create, `-x` extract, `-t` list, `-z` gzip, `-v` verbose, `-f` archive file, `-C` target directory).

### Q26 (Ch.03 openEuler CLI Basics) — [20 pts]
- **Question:** Which of the following Linux text processing commands and options are matched with their TRUE functions?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.03 (pp. 143–147), all four statements accurately describe `grep`, `cut`, `wc`, `sort`, and `awk`.

### Q27 (Ch.04 openEuler System Configuration) — [20 pts]
- **Question:** Which of the following statements about Linux file types and `chmod`/`chown`/`sticky bit` permissions are TRUE?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.04 (pp. 172, 178–185), all four statements are directly confirmed in the official openEuler System Configuration chapter.

### Q28 (Ch.04 openEuler System Configuration) — [20 pts]
- **Question:** Which of the following statements about RPM and DNF software package management on openEuler are TRUE?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.04 (pp. 195–214), all four statements accurately contrast `rpm` and `dnf` operations on openEuler.

### Q29 (Ch.04 openEuler System Configuration) — [20 pts]
- **Question:** Which of the following `systemctl` and `journald` commands are valid for managing services and inspecting logs on openEuler?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.04 (pp. 216–223), all four statements accurately describe `systemd`, `systemctl`, and `journald`.

### Q30 (Ch.04 openEuler System Configuration) — [20 pts]
- **Question:** Which of the following statements about process scheduling priority (`nice`), background jobs, and scheduled tasks (`at`/`crontab`) are TRUE?
- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.04 (pp. 229–248), A, B, and C are true. D is false because regular users can only lower priority (increase nice value toward +19) for their own processes; only `root` can assign negative nice values.

### Q31 (Ch.05 Storage and Network Management) — [20 pts]
- **Question:** Which of the following statements about persistent storage, `parted`, and `/etc/fstab` are TRUE?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.05 (pp. 257–282), all four statements match the official Storage Management slides.

### Q32 (Ch.05 Storage and Network Management) — [20 pts]
- **Question:** Which of the following statements accurately describe Logical Volume Management (LVM) layers and commands on openEuler?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.05 (pp. 284–297), all four statements correctly describe LVM concepts and commands.

### Q33 (Ch.05 Storage and Network Management) — [20 pts]
- **Question:** Which of the following `nmcli` and network diagnostic commands are valid on openEuler?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.05 (pp. 308–317), all four statements accurately reflect NetworkManager (`nmcli`), `ss`, and `tracepath` usage on openEuler.

### Q34 (Ch.06 Shell Scripts) — [20 pts]
- **Question:** Which of the following statements about Bash I/O redirection, pipes, and quoting are TRUE?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.06 (pp. 338–347), all four statements are true.

### Q35 (Ch.06 Shell Scripts) — [20 pts]
- **Question:** Which of the following statements about Bash variables, test conditions, and loops are TRUE?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.06 (pp. 345–366), all four statements are core Bash scripting fundamentals covered in the training material.

### Q36 (Ch.06 Shell Scripts) — [20 pts]
- **Question:** When comparing a `while` loop and an `until` loop in Bash, which of the following statements are TRUE?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.06 (pp. 353 & 365–367), all four statements are true.

### Q37 (Ch.07 Native Container Engine iSula) — [20 pts]
- **Question:** (Official Ch.07 Quiz Q1) Which of the following are valid container states in `iSula`?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.07 (p. 439), all four (`Created`, `Exited`, `Up`, and `Paused`) are container states displayed by `isula ps -a`.

### Q38 (Ch.07 Native Container Engine iSula) — [20 pts]
- **Question:** Which Linux kernel mechanisms provide container isolation and resource limits, and what makes `iSula` distinct from Docker?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.07 (pp. 390–398), all four statements describe kernel container primitives and `iSula` architectural advantages.

### Q39 (Ch.07 Native Container Engine iSula) — [20 pts]
- **Question:** Which of the following `isula` CLI commands perform the stated container lifecycle operations?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.07 (pp. 405–417), all four `isula` lifecycle commands are valid and follow Docker-compatible CLI semantics.

### Q40 (Ch.07 Native Container Engine iSula) — [20 pts]
- **Question:** Which of the following statements about container image layering and Copy-on-Write (CoW) in `iSula` are TRUE?
- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.07 (pp. 428–438), all four statements accurately describe UnionFS/OverlayFS CoW mechanics and image commands.

### Q41 (Ch.01 OS for the AI Era) — [10 pts]
- **Question:** (Official Ch.01 Quiz Q1) The `openEuler Intelligence` platform currently supports two interaction entries: Web entry and Intelligent Shell entry.
- **Correct Answer:** `A`
- **Explanation:** Per Ch.01 (p. 8 & p. 20), openEuler Intelligence explicitly exposes two interaction entries: Web and Intelligent Shell.

### Q42 (Ch.02 Getting Started with openEuler) — [10 pts]
- **Question:** (Official Ch.02 Quiz Q1) You do not need to specify the password of the `root` user during the openEuler OS installation; however, you must specify the password of the `root` user when logging in to the OS after the installation.
- **Correct Answer:** `A`
- **Explanation:** Per Ch.02 (p. 52), the official quiz states this is True (when root account is skipped or locked/deferred in installer if an admin user is created, or per the official quiz Q1 answer key: True).

### Q43 (Ch.03 openEuler CLI Basics) — [10 pts]
- **Question:** In the openEuler filesystem, `less` allows only forward (downward) page scrolling and cannot scroll backward, whereas `more` supports full bidirectional scrolling.
- **Correct Answer:** `B`
- **Explanation:** Per Ch.03 (p. 104 & pp. 137–139), it is the opposite: `more` only moves forward, while `less` supports both upward and downward scrolling as well as `/` and `?` searching.

### Q44 (Ch.03 openEuler CLI Basics) — [10 pts]
- **Question:** Running `locate myfile.conf` searches an internal file index database (`mlocate.db`), so newly created files may not appear until `updatedb` is executed.
- **Correct Answer:** `A`
- **Explanation:** Per Ch.03 (pp. 108–109), `locate` queries a pre-built database rather than scanning live disks like `find`, so `updatedb` must be run to index newly created files.

### Q45 (Ch.04 openEuler System Configuration) — [10 pts]
- **Question:** The `su root` command switches identity to `root` AND resets all environment variables (including `PATH` and `HOME`) to `root`'s login environment, making it completely identical to `su - root`.
- **Correct Answer:** `B`
- **Explanation:** Per Ch.04 (p. 191), `su` changes the user identity WITHOUT starting a login shell or loading the target user's environment variables, whereas `su -` (or `su -l`) switches to a full login shell with the target user's environment.

### Q46 (Ch.04 openEuler System Configuration) — [10 pts]
- **Question:** Unlike `at`, which uses `cron` daemon configuration files, `crontab -e` edits a user's personal periodic schedule, and modifying it immediately notifies `crond` without requiring a service restart.
- **Correct Answer:** `A`
- **Explanation:** Per Ch.04 (pp. 244–247), editing crontab with `crontab -e` automatically updates and reloads the user's cron schedule in `crond`.

### Q47 (Ch.05 Storage and Network Management) — [10 pts]
- **Question:** (Official Ch.05 Quiz Q1) The `route` command can view or configure host route information, and route entries configured with `route add` remain valid permanently across system reboots.
- **Correct Answer:** `B`
- **Explanation:** Per Ch.05 (p. 318), routes added via the `route` command take effect temporarily in runtime kernel memory and are LOST upon reboot; use `nmcli` or route config files for persistence.

### Q48 (Ch.06 Shell Scripts) — [10 pts]
- **Question:** (Official Ch.06 Quiz Q2) An administrator can run the `name==Tom` command in a Bash script to assign the value `Tom` to the variable `name`.
- **Correct Answer:** `B`
- **Explanation:** Per Ch.06 (p. 346 & p. 379), variable assignment in Bash uses a single `=` with NO spaces around it (`name=Tom`), NOT `==`.

### Q49 (Ch.06 Shell Scripts) — [10 pts]
- **Question:** If a shell script does not have execute (`+x`) permission, it cannot be invoked directly via `./script.sh`, but it can still be executed via `bash script.sh` or `sh script.sh`.
- **Correct Answer:** `A`
- **Explanation:** Per Ch.06 (p. 334), `./script.sh` requires read+execute permission, whereas passing the file to an interpreter (`bash script.sh`) only requires read permission.

### Q50 (Ch.07 Native Container Engine iSula) — [10 pts]
- **Question:** A container started in `iSula` with `-v /root/test2.txt:/tmp/test2.txt:ro` allows processes inside the container to modify `/tmp/test2.txt` and persist those edits to the host.
- **Correct Answer:** `B`
- **Explanation:** Per Ch.07 (p. 426), the `:ro` mount option mounts the host path as **read-only** inside the container; `:rw` is required for read-write persistence.

### Q51 (Ch.03 openEuler CLI Basics) — [20 pts]
- **Question:** Lab 1 (Text Processing Pipeline): Complete the command pipeline to extract all lines from `/etc/passwd` whose login shell ends with `bash`, then print ONLY column 1 (username) and column 7 (shell) using `awk` with `:` as delimiter.
- **Correct Answer:** `grep 'bash' /etc/passwd | awk -F ':' '{print 1, $7}'`
- **Explanation:** Per Ch.03 (pp. 144–145), `grep 'bash' /etc/passwd` matches lines ending with `bash`, and `awk -F ':' '{print 1, $7}'` splits on `:` to display username and shell.

### Q52 (Ch.03 openEuler CLI Basics) — [20 pts]
- **Question:** Lab 2 (Archive & Symbolic Link): Write two commands: (1) create a gzip-compressed tar archive `/tmp/etc_conf.tar.gz` from `/etc/hosts`, and (2) create a symbolic (soft) link `/tmp/hosts.link` pointing to `/etc/hosts`.
- **Correct Answer:** `tar -czvf /tmp/etc_conf.tar.gz /etc/hosts
ln -s /etc/hosts /tmp/hosts.link`
- **Explanation:** Per Ch.03 (pp. 113–117), `tar -czvf` creates a gzip-compressed archive and `ln -s` creates a symbolic link (omitting `-s` would create a hard link).

### Q53 (Ch.04 openEuler System Configuration) — [20 pts]
- **Question:** Lab 3 (User & ACL Permissions): Write two commands: (1) add existing user `alice` to supplementary group `wheel` WITHOUT removing her existing groups, and (2) grant user `alice` read-write-execute (`rwx`) ACL permission on `/opt/app.log`.
- **Correct Answer:** `usermod -aG wheel alice
setfacl -m u:alice:rwx /opt/app.log`
- **Explanation:** Per Ch.04 (pp. 168 & 187), `usermod -aG` appends a supplementary group (`-G` alone overwrites existing supplementary groups), and `setfacl -m u:alice:rwx` modifies the file ACL.

### Q54 (Ch.04 openEuler System Configuration) — [20 pts]
- **Question:** Lab 4 (Systemd & Crontab): Write: (1) the command to enable and immediately start the `httpd` service, and (2) a `crontab` schedule line that runs `/usr/local/bin/backup.sh` every day at 02:30 AM.
- **Correct Answer:** `systemctl enable --now httpd
30 2 * * * /usr/local/bin/backup.sh`
- **Explanation:** Per Ch.04 (pp. 220 & 245–246), `systemctl enable --now` enables boot startup and activates immediately; crontab fields are `minute(30) hour(2) dom(*) month(*) dow(*)`.

### Q55 (Ch.05 Storage and Network Management) — [20 pts]
- **Question:** Lab 5 (LVM Provisioning Workflow): Complete the 4-step LVM creation commands to initialize `/dev/sdb1` as a PV, create Volume Group `vg_data`, create a 20G Logical Volume `lv_app` inside `vg_data`, and format it as `ext4`.
- **Correct Answer:** `pvcreate /dev/sdb1
vgcreate vg_data /dev/sdb1
lvcreate -L 20G -n lv_app vg_data
mkfs -t ext4 /dev/vg_data/lv_app`
- **Explanation:** Per Ch.05 (pp. 288–296), the LVM creation workflow is `pvcreate` -> `vgcreate` -> `lvcreate` -> `mkfs`.

### Q56 (Ch.05 Storage and Network Management) — [20 pts]
- **Question:** Lab 6 (Online LV Expansion & NetworkManager): Complete the commands to: (1) extend `/dev/vg_data/lv_app` by adding 10G and grow its `ext4` file system online, and (2) activate an `nmcli` connection named `Euler`.
- **Correct Answer:** `lvextend -L +10G /dev/vg_data/lv_app
resize2fs /dev/vg_data/lv_app
nmcli con up "Euler"`
- **Explanation:** Per Ch.05 (pp. 298 & 310), `lvextend -L +10G` expands the LV, `resize2fs` grows an `ext4` filesystem online, and `nmcli con up` activates the connection profile.

### Q57 (Ch.06 Shell Scripts) — [20 pts]
- **Question:** Lab 7 (Bash Conditional & Variable Assignment): Fix the variable assignment and complete the `if` statement that checks whether `/etc/isulad/daemon.json` is a regular file (`-f`) and prints `Configured`.
- **Correct Answer:** `#!/bin/bash
CFG="/etc/isulad/daemon.json"
if [ -f "$CFG" ]; then
    echo "Configured"
fi`
- **Explanation:** Per Ch.06 (pp. 346 & 356), Bash variable assignments must not have spaces around `=`, `-f` tests for a regular file, and `if` blocks terminate with `fi`.

### Q58 (Ch.06 Shell Scripts) — [20 pts]
- **Question:** Lab 8 (Bash Loop & Arithmetic): Complete the `for` loop and arithmetic expression to accumulate the sum of odd numbers (`1, 3, 5, ..., 99`) using `seq` or brace expansion and `$(( ... ))`.
- **Correct Answer:** `#!/bin/bash
sum=0
for i in $(seq 1 2 99); do
    sum=$((sum + i))
done
echo $sum`
- **Explanation:** Per Ch.06 (pp. 349 & 361), `for ...; do ... done` iterates over the list and `$((sum + i))` performs integer arithmetic expansion.

### Q59 (Ch.07 Native Container Engine iSula) — [20 pts]
- **Question:** Lab 9 (iSula Container Deployment with Persistent Storage): Write the `isula` command to run an interactive container named `web01` from image `openeuler/nginx:latest`, bind-mounting `/root/html` to `/usr/share/nginx/html` in read-write mode and executing `/bin/bash`.
- **Correct Answer:** `isula run -it -n web01 -v /root/html:/usr/share/nginx/html:rw openeuler/nginx:latest /bin/bash`
- **Explanation:** Per Ch.07 (pp. 407–426), `isula run` creates and starts a container, `-n` specifies the container name, and `-v host:container:rw` mounts persistent storage.

### Q60 (Ch.07 Native Container Engine iSula) — [20 pts]
- **Question:** Lab 10 (iSula Debugging & Image Cleanup): Write two commands: (1) execute `ip addr` inside a running container named `web01`, and (2) remove an unused local container image `busybox:test`.
- **Correct Answer:** `isula exec web01 ip addr
isula rmi busybox:test`
- **Explanation:** Per Ch.07 (pp. 412 & 438), `isula exec` runs a command inside an active container and `isula rmi` removes a local container image.
