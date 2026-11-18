# Hands-On Lab: Kickstart & Partitioning Specification for openEuler 24.03 LTS

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 01 — OS for the AI Era & Getting Started with openEuler (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Installing-openEuler-OS-and-Partitioning`  
**Interactive Workbench:** Open **[`06-Exercise-openEuler-Installation-and-Partition-Plan-Lab.html`](./06-Exercise-openEuler-Installation-and-Partition-Plan-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are preparing an automated Kickstart configuration (`anaconda-ks.cfg`) for a batch of openEuler 24.03 LTS UEFI servers with 4 GB RAM. Complete the partition and environment rules.

### Step-by-Step Instructions
1. Step 1: Specify the automated batch installation tool name (`Kickstart`) in the header comment.
2. Step 2: Define the four recommended partitions: `/boot`, `/boot/efi`, `swap` (sized at 2x RAM = `8192` MB), and `/`.
3. Step 3: Select one of the three official software base environments (`Minimum installation`, `Server`, or `Hypervisor`).

### Starter Workspace (`root@openEuler:~#`)
```bash
# Batch Automation Tool: <tool_name>
part /boot --fstype="ext4" --size=1024
part <efi_mount_point> --fstype="efi" --size=200
part <swap_partition> --fstype="swap" --size=8192
part <root_mount_point> --fstype="ext4" --grow
ENVIRONMENT="<Minimum installation | Server | Hypervisor>"
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- The automated installation tool in openEuler/RedHat Anaconda is `Kickstart`.
- UEFI boot partitions mount at `/boot/efi`, virtual memory is `swap`, and the root partition is `/`.
- Choose `Minimum installation`, `Server`, or `Hypervisor` for `ENVIRONMENT`.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Batch Automation Tool: Kickstart
part /boot --fstype="ext4" --size=1024
part /boot/efi --fstype="efi" --size=200
part swap --fstype="swap" --size=8192
part / --fstype="ext4" --grow
ENVIRONMENT="Server"
```

#### Expected Console / Query Output:
```text
[Kickstart Validator] Parsing anaconda-ks.cfg...
 -> Tool: Kickstart (Full Automation Mode)
 -> Partition 1: /boot (1024 MB, ext4)
 -> Partition 2: /boot/efi (200 MB, EFI System Partition)
 -> Partition 3: swap (8192 MB = 2x 4GB RAM)
 -> Partition 4: / (Root partition, ext4, remaining capacity)
 -> Software Selection: Server Environment
[OK] Kickstart configuration is valid for openEuler 24.03 LTS.
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [True / False]
**[Official Ch.02 Quiz Q1] You do not need to specify the password of the root user during the openEuler OS installation. However, you must specify the password of the root user when logging in to the OS after the installation.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** Official Ch.02 Quiz Q1 (p.52): Marked as A (True) in the official Huawei training material answer key.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**Which of the following software installation options are supported on the 'Software Selection' screen of openEuler 24.03 LTS?**

- A. Minimum installation
- B. Server
- C. Hypervisor
- D. Windows Subsystem

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** Per Ch.02 (p.44), openEuler 24.03 LTS supports three software installation base options: Minimum installation, Server, and Hypervisor.
</details>

### Question 3 [Single-Choice]
**Which tool is recommended in the openEuler documentation for batch automated OS installations?**

- A. Anaconda GUI
- B. Kickstart
- C. fdisk
- D. PuTTY

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.02 (p.39), you can use the Kickstart tool to automatically install openEuler in semi-automatic or full automation mode for batch installations.
</details>
