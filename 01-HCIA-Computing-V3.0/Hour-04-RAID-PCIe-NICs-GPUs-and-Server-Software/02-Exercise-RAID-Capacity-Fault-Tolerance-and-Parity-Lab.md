# 💻 Hands-On Lab: Enterprise RAID Capacity & Fault Tolerance Calculator

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 04 — RAID Arrays, PCIe Bus, NICs/iNICs, GPU/NPU, Power/Cooling & Server Software (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `01-Lecture-RAID-Levels-Parity-and-Hardware-vs-Software-RAID`  
**Interactive Workbench:** Open **[`02-Exercise-RAID-Capacity-Fault-Tolerance-and-Parity-Lab.html`](./02-Exercise-RAID-Capacity-Fault-Tolerance-and-Parity-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Write a Python script to compute usable capacities for a server with 8 × 4 TB drives across RAID 5, RAID 6, RAID 10, and RAID 60 (with M=2 spans), and verify minimum disk counts.

### 📋 Step-by-Step Instructions
1. Set `raid5_min_disks` to `3`, `raid50_min_disks` to `6`, and `raid60_min_disks` to `8`.
2. For `N = 8` disks of `4` TB each (total raw = 32 TB, `M = 2` spans): set `usable_tb_raid5` to `28` ($(8-1)\times 4$), `usable_tb_raid6` to `24` ($(8-2)\times 4$), and `usable_tb_raid60` to `16` ($(8 - 2\times 2)\times 4$).
3. Set `software_raid_supports_bootable_array` to `False`.

### 📝 Starter Workspace (`python3@taishan-raid:~$`)
```bash
# RAID Capacity & Fault Tolerance Calculator (8 x 4 TB Drives, M = 2 Spans)
raid5_min_disks = ___
raid50_min_disks = ___
raid60_min_disks = ___

usable_tb_raid5 = ___
usable_tb_raid6 = ___
usable_tb_raid60 = ___
software_raid_supports_bootable_array = ___

print(f"Min Disks (R5/R50/R60): {raid5_min_disks}/{raid50_min_disks}/{raid60_min_disks}")
print(f"Usable TB (R5/R6/R60): {usable_tb_raid5}T / {usable_tb_raid6}T / {usable_tb_raid60}T")
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- RAID 5 requires >= 3 disks, RAID 50 requires >= 6 disks, and RAID 60 requires >= 8 disks (Ch.03, pp. 161–162).
- With 8 × 4 TB drives: RAID 5 usable = 7 × 4 = 28 TB; RAID 6 usable = 6 × 4 = 24 TB; RAID 60 (2 spans) usable = (8 - 4) × 4 = 16 TB.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# RAID Capacity & Fault Tolerance Calculator (8 x 4 TB Drives, M = 2 Spans)
raid5_min_disks = 3
raid50_min_disks = 6
raid60_min_disks = 8

usable_tb_raid5 = 28
usable_tb_raid6 = 24
usable_tb_raid60 = 16
software_raid_supports_bootable_array = False

print(f"Min Disks (R5/R50/R60): {raid5_min_disks}/{raid50_min_disks}/{raid60_min_disks}")
print(f"Usable TB (R5/R6/R60): {usable_tb_raid5}T / {usable_tb_raid6}T / {usable_tb_raid60}T")
```

#### Expected Console / Query Output:
```text
Min Disks (R5/R50/R60): 3/6/8
Usable TB (R5/R6/R60): 28T / 24T / 16T
[OK] RAID utilization formulas and Software RAID limitations verified.
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**If a server is configured with N member drives arranged in M spans in a RAID 60 array, what is the drive utilization formula, and what is the theoretical minimum number of drives required to construct RAID 60?**

- A. (N - M)/N; at least 6 drives
- B. (N - M * 2)/N; at least 8 drives
- C. (N - 2)/N; at least 4 drives
- D. 50%; at least 4 drives

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.03 pp. 161–163, RAID 60 sets up RAID 6 (at least 4 drives per span) first and then RAID 0 across M spans, requiring at least 8 drives with drive utilization (N - M × 2)/N.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**Which of the following functions are NOT provided by Software RAID according to Chapter 03 (p. 167)?**

- A. Hot swap and hot spare of hard disks
- B. Remote array management
- C. Bootable arrays
- D. S.M.A.R.T. for disks

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** According to Ch.03 p.167, Software RAID does not support hot swap of hard disks, hot spare of hard disks, remote array management, bootable arrays, array configuration on hard disks, or S.M.A.R.T. for disks.
</details>

### Question 3 [True / False]
**Because RAID 6 uses two independent distributed parity codes (P and Q) and can tolerate two simultaneous drive failures, configuring RAID 6 eliminates the need for data backup and disaster recovery.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.03 p.165, RAID cannot be used as an alternative to data backup because it cannot prevent data loss caused by non-disk faults such as viruses, man-made damage, or accidental deletion.
</details>
