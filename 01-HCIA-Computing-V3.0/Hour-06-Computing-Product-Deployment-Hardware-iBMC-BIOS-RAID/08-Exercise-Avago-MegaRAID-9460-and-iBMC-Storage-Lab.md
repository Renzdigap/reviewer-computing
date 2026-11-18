# Hands-On Lab: Avago MegaRAID & iBMC Storage Configuration

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 06 — Computing Product Deployment: Equipment Room, iBMC, BIOS & RAID Configuration (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Querying-and-Configuring-RAID-and-JBOD`  
**Interactive Workbench:** Open **[`08-Exercise-Avago-MegaRAID-9460-and-iBMC-Storage-Lab.html`](./08-Exercise-Avago-MegaRAID-9460-and-iBMC-Storage-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Configure a RAID 5 logical volume named 'Data' across four 8 TB SATA HDDs on a TaiShan 200 (2280) server via iBMC WebUI and verify JBOD and BIOS RAID settings.

### Step-by-Step Instructions
1. Set `ibmc_raid_query_path` to `'System > System Info > Others'` and `ibmc_raid_config_path` to `'System > Storage Management'`.
2. Set `passthrough_mode_name` to `'JBOD'` and `unsupported_raid_level` to `'RAID 00'`.
3. For four 8 TB HDDs (`7.2` TB actual capacity each) in RAID 5, set `single_8tb_actual_tb` to `7.2` and `raid5_usable_tb` to `21.6`.

### Starter Workspace (`storage-admin@ibmc-webui:~#`)
```bash
# TaiShan 2280 Hardware RAID & JBOD Configuration
ibmc_navigation:
  ibmc_raid_query_path: "___"
  ibmc_raid_config_path: "___"

controller_capabilities:
  passthrough_mode_name: "___"
  unsupported_raid_level: "___"
  spanned_array_max_spans: 8
  spanned_array_max_drives: 240

logical_drive_data:
  name: "Data"
  init_state: "Quick Init"
  raid_level: 5
  single_8tb_actual_tb: ___
  raid5_usable_tb: ___
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Query RAID card model at System > System Info > Others; configure RAID at System > Storage Management.
- Drive passthrough is JBOD; RAID 00 is not supported; an 8 TB HDD has ~7.2 TB actual capacity (3 × 7.2 = 21.6 TB in 4-disk RAID 5).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# TaiShan 2280 Hardware RAID & JBOD Configuration
ibmc_navigation:
  ibmc_raid_query_path: "System > System Info > Others"
  ibmc_raid_config_path: "System > Storage Management"

controller_capabilities:
  passthrough_mode_name: "JBOD"
  unsupported_raid_level: "RAID 00"
  spanned_array_max_spans: 8
  spanned_array_max_drives: 240

logical_drive_data:
  name: "Data"
  init_state: "Quick Init"
  raid_level: 5
  single_8tb_actual_tb: 7.2
  raid5_usable_tb: 21.6
```

#### Expected Console / Query Output:
```text
[OK] RAID Controller & Logical Drive Configuration Validated:
- Query Path: System > System Info > Others (Avago MegaRAID SAS 9460-8i)
- Config Path: System > Storage Management -> Logical Drive 'Data' (RAID 5, Quick Init)
- Member Drives: 4 x 8 TB SATA HDD (7.2 TB actual each) -> 21.6 TB Usable Capacity.
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Which feature of a RAID controller card, also known as drive passthrough or transparent transmission, allows commands to be directly transmitted to connected physical drives without creating a RAID virtual drive?**

- A. Hot Spare
- B. JBOD (Just a Bunch of Drives)
- C. Changed Block Tracking (CBT)
- D. Preboot Execution Environment (PXE)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 pp. 321 and 349, JBOD (Just a Bunch of Drives), also known as drive passthrough or transparent transmission, allows user commands to be directly transmitted to connected drives.
</details>

### Question 2 [Single-Choice]
**On the iBMC WebUI of a TaiShan 200 (model 2280) server, where do you view the model of the RAID controller card, and where do you create or manage RAID logical drives?**

- A. View model at System > System Info > Others; configure RAID at System > Storage Management
- B. View model at Services > VNC; configure RAID at User & Security > Local Users
- C. View model at Maintenance > System Logs; configure RAID at iBMC Settings > Network Settings
- D. View model at Home > Virtual Console; configure RAID at Power > Power Control

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** According to Ch.05 pp. 319 and 324, you view the RAID controller card model at System > System Info (Others tab) and configure RAID logical drives at System > Storage Management.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**When configuring a virtual drive in the BIOS Avago MegaRAID Configuration Utility via VNC (Ch.05, pp. 320, 322), which of the following statements are true?**

- A. Under 'Select Drives From', 'Unconfigured Capacity' refers to free drives that are not added to any virtual drives, whereas 'Free Capacity' refers to drive group space not used by any virtual drives.
- B. Virtual drive access policies include Read/Write, Read Only, and Blocked.
- C. Each span of a RAID 10 or RAID 50 array allows for 1 failed drive, while each span of a RAID 60 array allows for 2 failed drives.
- D. Avago MegaRAID SAS 9460-8i natively supports RAID 00 across up to 16 spans.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** A, B, and C are true (Ch.05, pp. 320, 322). D is false because Ch.05 p.320 explicitly notes that RAID 00 is NOT supported and spanned arrays support 2 to 8 spans.
</details>
