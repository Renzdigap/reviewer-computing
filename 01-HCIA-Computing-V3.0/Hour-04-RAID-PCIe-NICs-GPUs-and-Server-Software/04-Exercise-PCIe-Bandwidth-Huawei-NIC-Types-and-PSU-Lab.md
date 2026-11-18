# Hands-On Lab: PCIe Gen 1–5 Bandwidth & Huawei Server NIC Audit

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 04 — RAID Arrays, PCIe Bus, NICs/iNICs, GPU/NPU, Power/Cooling & Server Software (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-PCIe-Bus-NICs-iNICs-GPUs-NPUs-and-Power-Cooling`  
**Interactive Workbench:** Open **[`04-Exercise-PCIe-Bandwidth-Huawei-NIC-Types-and-PSU-Lab.html`](./04-Exercise-PCIe-Bandwidth-Huawei-NIC-Types-and-PSU-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Complete the hardware verification file for PCIe 4.0/5.0 bandwidths, Huawei server NIC form factors, CPU/GPU ALU ratios, and TaiShan PSU dimensions.

### Step-by-Step Instructions
1. Set `pcie4_gt_s` to `16.0`, `pcie4_x16_gbs` to `31.5`, and `pcie5_x16_gbs` to `63.0`.
2. Set `non_replaceable_pch_nic` to `'LOM'` and `blade_only_nic` to `'Mezzanine'`.
3. Set `cpu_alu_area_percent` to `5`, `gpu_alu_area_percent` to `40`, and `taishan_2280_psu_width_mm` to `68.0`.

### Starter Workspace (`hw-architect@taishan-2280:~#`)
```bash
# PCIe, NIC, GPU/NPU & PSU Hardware Audit
pcie_specs:
  pcie3_gt_s: 8.0
  pcie4_gt_s: ___
  pcie4_x16_gbs: ___
  pcie5_x16_gbs: ___

huawei_nics:
  non_replaceable_pch_nic: "___"
  rack_only_nonstandard_nic: "FlexIO"
  blade_only_nic: "___"
  third_gen_inic_chip: "Hi1822"

compute_and_power:
  cpu_alu_area_percent: ___
  gpu_alu_area_percent: ___
  taishan_2280_psu_width_mm: ___
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- PCIe 4.0 runs at 16.0 GT/s (31.5 GB/s for x16); PCIe 5.0 runs at 32.0 GT/s (63.0 GB/s for x16).
- LOM is embedded in the PCH chip; Mezzanine cards are for blade servers only. ALU occupies 5% of CPU vs. 40% of GPU; TaiShan 2280 PSUs are 68.0 mm wide.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# PCIe, NIC, GPU/NPU & PSU Hardware Audit
pcie_specs:
  pcie3_gt_s: 8.0
  pcie4_gt_s: 16.0
  pcie4_x16_gbs: 31.5
  pcie5_x16_gbs: 63.0

huawei_nics:
  non_replaceable_pch_nic: "LOM"
  rack_only_nonstandard_nic: "FlexIO"
  blade_only_nic: "Mezzanine"
  third_gen_inic_chip: "Hi1822"

compute_and_power:
  cpu_alu_area_percent: 5
  gpu_alu_area_percent: 40
  taishan_2280_psu_width_mm: 68.0
```

#### Expected Console / Query Output:
```text
[OK] PCIe, NIC, Accelerator & PSU Specs Validated:
- PCIe 4.0 x16 = 31.5 GB/s (16.0 GT/s) | PCIe 5.0 x16 = 63.0 GB/s (32.0 GT/s)
- NICs: LOM (PCH embedded) | PCIe (Standard) | FlexIO (Rack rear) | Mezzanine (E9000 Blade)
- ALU Area: CPU = 5%, GPU = 40% | TaiShan 2280 PSU Width = 68.0 mm.
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Multiple-Choice (Select ALL)]
**(Official Ch.03 Quiz Q1) Which of the following statements are true about NICs of Huawei servers?**

- A. A LOM is integrated in the PCH chip of the server mainboard and cannot be replaced.
- B. Huawei-developed PCIe cards can be installed in standard PCIe slots.
- C. A FlexIO card is integrated on the server panel for front-end service connection.
- D. Mezzanine cards can be used for Huawei rack servers.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `AB`
- **Explanation:** According to Ch.03 p.177 and p.220 Quiz Q1, A and B are true. C is false (FlexIO cards are pluggable non-standard PCIe cards installed on the rear panel of Huawei rack servers), and D is false (Mezzanine cards can ONLY be used on compute nodes of Huawei E9000 blade servers).
</details>

### Question 2 [Single-Choice]
**What are the transmission rate and x16 bandwidth of PCIe 4.0?**

- A. 8.0 GT/s and 15.8 GB/s
- B. 16.0 GT/s and 31.5 GB/s
- C. 32.0 GT/s and 63.0 GB/s
- D. 5.0 GT/s and 8.0 GB/s

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.03 p.173, PCIe 4.0 (launched in 2017) has an original transmission rate of 16.0 GT/s and a ×16 bandwidth of 31.5 GB/s (×1 = 1969 MB/s, ×4 = 7.88 GB/s, ×8 = 15.75 GB/s).
</details>

### Question 3 [Single-Choice]
**Which of the following liquid cooling solutions is classified as an INDIRECT liquid cooling solution where the coolant does not directly contact electronic components?**

- A. Single-phase immersion liquid cooling
- B. Two-phase immersion liquid cooling
- C. Spray liquid cooling
- D. Cold-plate liquid cooling

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `D`
- **Explanation:** According to Ch.03 p.187, liquid cooling is divided into direct cooling (Immersion and Spray, 100% liquid cooling where coolant directly contacts heating components) and indirect cooling (Cold plate, where deionized water/glycol flows inside closed cold plates).
</details>
