# Hands-On Lab: Data Center Site Survey & Power-On Specification Check

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 06 — Computing Product Deployment: Equipment Room, iBMC, BIOS & RAID Configuration (Sprint 1 of 4)  
**Format:** Immediate Hands-On Exercise (7 mins) — Paired with `01-Lecture-Equipment-Room-Layouts-ESD-and-Physical-Installation`  
**Interactive Workbench:** Open **[`02-Exercise-Equipment-Room-Environment-and-Power-On-Checklist-Lab.html`](./02-Exercise-Equipment-Room-Environment-and-Power-On-Checklist-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Complete the pre-installation site survey checklist for deploying TaiShan 200 (model 2280) servers in a customer equipment room.

### Step-by-Step Instructions
1. Set `optimal_cooling_layout` to `'In-row air conditioners with contained aisles'` and `cabinet_standard` to `'IEC 297'`.
2. Set `min_cabinet_depth_mm` to `1000` and `front_rear_clearance_mm` to `800`.
3. Set `ac_breaker_amps` to `32`, `dc_breaker_amps` to `63`, and `default_state_upon_power` to `'Power on'`.

### Starter Workspace (`site-eng@dc-survey:~#`)
```bash
# Data Center Site Survey Checklist (TaiShan 200 2280)
facility_requirements:
  optimal_cooling_layout: "___"
  cabinet_standard: "___"
  min_cabinet_depth_mm: ___
  front_rear_clearance_mm: ___
  temp_range_celsius: "5 to 40"
  humidity_range_rh: "8% to 90%"

electrical_and_power:
  ac_breaker_amps: ___
  dc_breaker_amps: ___
  default_state_upon_power: "___"
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- In-row air conditioners with contained aisles is the best layout; cabinets conform to IEC 297 (>1000 mm depth) with 800 mm clearance.
- Circuit breakers are 32 A AC or 63 A DC, and the default state upon power supply is 'Power on'.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Data Center Site Survey Checklist (TaiShan 200 2280)
facility_requirements:
  optimal_cooling_layout: "In-row air conditioners with contained aisles"
  cabinet_standard: "IEC 297"
  min_cabinet_depth_mm: 1000
  front_rear_clearance_mm: 800
  temp_range_celsius: "5 to 40"
  humidity_range_rh: "8% to 90%"

electrical_and_power:
  ac_breaker_amps: 32
  dc_breaker_amps: 63
  default_state_upon_power: "Power on"
```

#### Expected Console / Query Output:
```text
[PASS] Equipment Room & Electrical Readiness Verified:
- Layout: In-row air conditioners with contained aisles (Optimal PUE)
- Cabinet: 19-inch IEC 297 (>1000 mm depth, 800 mm front/rear clearance, 5-40C, 8-90% RH)
- Power: 32 A AC / 63 A DC breaker | Default System State Upon Power Supply: Power on.
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**Among the three common equipment room air-conditioning and aisle layouts, which option is the BEST for optimizing resource utilization, power density per rack, PUE, and safety?**

- A. In-room air conditioners with open aisles
- B. In-room air conditioners with contained aisles
- C. In-row air conditioners with contained aisles
- D. Natural convection without air conditioners or aisles

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** According to Ch.05 p.289, in-row air conditioners with contained aisles are the best option, followed by in-room air conditioners with contained aisles, while in-room air conditioners with open aisles are the least optimal.
</details>

### Question 2 [Single-Choice]
**What are the required cabinet depth, front/rear clearance, and external circuit breaker current ratings for installing a TaiShan 200 (model 2280) server?**

- A. Depth > 600 mm; clearance 400 mm; breaker 10 A AC or 16 A DC
- B. Depth > 1,000 mm (IEC 297); clearance 800 mm; breaker 32 A AC or 63 A DC
- C. Depth > 1,500 mm; clearance 1,200 mm; breaker 100 A AC or 100 A DC
- D. Depth > 800 mm; clearance 500 mm; breaker 16 A AC or 32 A DC

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 pp. 291 and 295, cabinets must conform to IEC 297 and exceed 1,000 mm in depth, with 800 mm clearance at front and rear, and external circuit breakers rated at 32 A AC or 63 A DC.
</details>

### Question 3 [True / False]
**By default, the 'System State Upon Power Supply' parameter of a TaiShan 200 (model 2280) server is set to 'Power on', meaning the server automatically powers on when power is supplied to the PSUs.**

- A. True
- B. False

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** True. According to Ch.05 p.295, the server is powered on together with the PSUs by default ('System State Upon Power Supply' = 'Power on', configurable under iBMC WebUI Power > Power Control).
</details>
