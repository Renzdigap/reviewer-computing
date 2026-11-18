# 💻 Hands-On Lab: S920X00 Mainboard & Enterprise Drive Spec Classifier

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 03 — Server Hardware Architecture: CPU, Memory, Mainboard & Storage Drives (Sprint 3 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `05-Lecture-Server-Chassis-Mainboard-and-Hard-Disk-Mechanics`  
**Interactive Workbench:** Open **[`06-Exercise-Mainboard-S920X00-and-Drive-MTBF-DWPD-Lab.html`](./06-Exercise-Mainboard-S920X00-and-Drive-MTBF-DWPD-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Complete the hardware specification file for the Kunpeng S920X00 mainboard and classify enterprise HDD/SSD drive parameters.

### 📋 Step-by-Step Instructions
1. Set `mainboard_model` to `'S920X00'`, `bmc_management_chip` to `'Hi1710'`, and `pcie_4_slots` to `8`.
2. Set `sas_mtbf_hours` to `1600000` and `ssd_mtbf_hours` to `2000000`.
3. Set `read_intensive_dwpd_max` to `3` and `write_intensive_dwpd_min` to `10`.

### 📝 Starter Workspace (`hw-eng@taishan-2280:~#`)
```bash
# S920X00 Mainboard & Drive Classification Spec
mainboard:
  mainboard_model: "___"
  bmc_management_chip: "___"
  ddr4_2933_slots: 32
  pcie_4_slots: ___

drive_specs:
  sata_nlsas_mtbf_hours: 1200000
  sas_mtbf_hours: ___
  ssd_mtbf_hours: ___
  read_intensive_dwpd_max: ___
  write_intensive_dwpd_min: ___
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- The Kunpeng server mainboard model on page 149 is S920X00 with the Hi1710 chip and 8 PCIe 4.0 slots.
- SAS MTBF is 1,600,000 hours; SSD MTBF is 2,000,000 hours; DWPD thresholds are < 3, 3–10, and > 10.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# S920X00 Mainboard & Drive Classification Spec
mainboard:
  mainboard_model: "S920X00"
  bmc_management_chip: "Hi1710"
  ddr4_2933_slots: 32
  pcie_4_slots: 8

drive_specs:
  sata_nlsas_mtbf_hours: 1200000
  sas_mtbf_hours: 1600000
  ssd_mtbf_hours: 2000000
  read_intensive_dwpd_max: 3
  write_intensive_dwpd_min: 10
```

#### Expected Console / Query Output:
```text
[OK] S920X00 Mainboard & Drive Specs Validated:
- Mainboard: S920X00 (2 x Kunpeng 920 + Hi1710 BMC + 32 DDR4-2933 + 8 PCIe 4.0)
- MTBF: SATA/NL-SAS = 1.2M h | SAS = 1.6M h | SSD = 2.0M h
- SSD DWPD: Read-Intensive (<3) | Mixed (3-10) | Write-Intensive (>10).
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**What are the rotational speed, interface type, and MTBF of an NL-SAS hard disk drive?**

- A. 15,000 RPM, SATA interface, 1,600,000 hours MTBF
- B. 7,200 RPM, enterprise SATA drive with SAS interface, 1,200,000 hours MTBF
- C. 10,000 RPM, PCIe interface, 2,000,000 hours MTBF
- D. 5,400 RPM, parallel ATA interface, 800,000 hours MTBF

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.03 p.153, NL-SAS drives are 7,200 RPM enterprise-class SATA drives with SAS ports, an MTBF of 1,200,000 hours, and an annual failure rate of about 2%.
</details>

### Question 2 [Single-Choice]
**How are enterprise SSDs classified based on Drive Writes Per Day (DWPD)?**

- A. Read-intensive: DWPD < 1; Mixed: DWPD 1–3; Write-intensive: DWPD > 3
- B. Read-intensive: DWPD < 3; Mixed: DWPD 3–10; Write-intensive: DWPD > 10
- C. Read-intensive: DWPD < 5; Mixed: DWPD 5–15; Write-intensive: DWPD > 15
- D. Read-intensive: DWPD < 10; Mixed: DWPD 10–50; Write-intensive: DWPD > 50

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.03 p.154, Read-intensive SSDs have DWPD < 3, Mixed read/write SSDs have DWPD between 3 and 10, and Write-intensive SSDs have DWPD > 10.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following specifications are true regarding the Kunpeng server mainboard (model S920X00)?**

- A. It is equipped with two Kunpeng 920 processors and the Hi1710 intelligent management chip.
- B. It supports up to 32 DDR4-2933 memory slots.
- C. It provides eight PCIe 4.0 slots.
- D. It is compatible with 2U or 4U rack servers.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** All four statements are explicitly stated on Ch.03 p.149 for the Kunpeng server mainboard (model S920X00).
</details>
