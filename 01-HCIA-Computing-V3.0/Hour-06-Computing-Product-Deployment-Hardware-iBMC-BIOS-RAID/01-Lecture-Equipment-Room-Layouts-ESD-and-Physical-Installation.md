# 📖 Equipment Room Layouts, Environment/ESD Standards & Server Installation

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 06 — Computing Product Deployment: Equipment Room, iBMC, BIOS & RAID Configuration (Sprint 1 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `02-Exercise-Equipment-Room-Environment-and-Power-On-Checklist-Lab` (7 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.05, pp. 288–295

---

## 🎯 Learning Objectives
- Rank the 3 equipment room cooling/aisle layouts by resource utilization, rack power density, PUE, and safety
- Memorize cabinet standards (IEC 297, >1000 mm depth), ambient temperature/humidity, 800 mm clearance, and ESD rules
- Understand the TaiShan 200 (2280) installation workflow, 32 A AC / 63 A DC circuit breaker ratings, and default Power-On state

---

### 1. Equipment Room Layouts Ranked by Efficiency & PUE (pp. 288–289)
Equipment rooms can use **air-cooled** or **water-cooled** layouts across three aisle configurations. Ranked from **BEST (most optimal)** to **LEAST optimal** in terms of resource utilization, power density per rack, Power Usage Effectiveness (**PUE**), and safety:
1. **Best Option**: **In-row air conditioners with contained aisles** (water-cooled or air-cooled).
2. **Second Best**: **In-room air conditioners with contained aisles**.
3. **Least Optimal**: **In-room air conditioners with open aisles**.

---

### 2. Cabinet, Ambient Environment & ESD Prevention Specifications (pp. 291–292)
| Requirement Category | Official Specification (pp. 291–292) |
| :--- | :--- |
| **Cabinet Standard** | General **19-inch** cabinets, **exceeding 1,000 mm in depth**, conforming to **IEC 297** standard; air filters on front, AC power supplied from rear. |
| **Ambient Temperature** | **5°C to 40°C** (41°F to 104°F) |
| **Ambient Humidity** | **8% RH to 90% RH** (non-condensing) — Note: heating decreases indoor humidity and **increases static electricity**! |
| **Space & Airflow** | **800 mm clearance** reserved at the **front and rear** of cabinets; front = **cool air intake**, rear = **hot air exhaust**. |
| **ESD Prevention** | Lay ESD floors, use ESD chairs/mats/bags; ground all metal frames/chassis; remove conductive objects (watches, jewelry); wear **ESD clothing, ESD gloves, and ESD wrist strap** (one end contacts **bare skin**, the other plugged into the **ESD jack on the cabinet/chassis**); never touch pins, welding points, or exposed circuits. |

---

### 3. TaiShan 200 (2280) Installation Workflow & Power-On Specs (pp. 293–295)
- **Five High-Level Deployment Phases (p. 293)**:
  `Hardware installation` $\rightarrow$ `Power-on` $\rightarrow$ `Initialization` (Query mgmt IP $\rightarrow$ Log in to iBMC WebUI $\rightarrow$ Check server $\rightarrow$ Change initial password) $\rightarrow$ `Configuring the BIOS` $\rightarrow$ `Configuring RAID` $\rightarrow$ `Installing the OS` $\rightarrow$ `Driver installation`.
- **Physical Mounting (p. 294)**: Support the server from the **bottom center of both sides**, place it onto the guide rails, slide it into the cabinet, align the mounting ears with the cabinet mounting bars, and tighten the **captive screws**.
- **Power-On & Circuit Breaker Specifications (p. 295)**:
  - External power circuit breaker current rating connected to the server: **32 A AC** or **63 A DC**.
  - **Default Power-On Behavior**: The default value of *System State Upon Power Supply* is **Power on** — the server **automatically powers on as soon as power is supplied to the PSUs**! To change this, log in to the iBMC WebUI and choose **Power > Power Control**.

---

## 🔑 Key Takeaways
- **Equipment room layout ranking: In-row air conditioners with contained aisles (Best PUE/density) > In-room with contained aisles (2nd) > In-room with open aisles (Least optimal).**
- **Environment specs: 19-inch IEC 297 cabinet > 1,000 mm deep, 800 mm front/rear clearance, 5°C–40°C temperature, 8%–90% RH non-condensing humidity.**
- **External circuit breaker rating for TaiShan 200 (2280): 32 A AC or 63 A DC. By default, the server powers on automatically when PSUs receive power (configurable under iBMC Power > Power Control).**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Heating an equipment room DECREASES indoor relative humidity and INCREASES static electricity (ESD risk) (p. 292)!

> [!WARNING]
> EXAM TRAP: By default, a TaiShan 200 (2280) server powers on AUTOMATICALLY when power is supplied to its PSUs ('System State Upon Power Supply' = 'Power on').

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`02-Exercise-Equipment-Room-Environment-and-Power-On-Checklist-Lab.html`](./02-Exercise-Equipment-Room-Environment-and-Power-On-Checklist-Lab.html)** (or [`02-Exercise-Equipment-Room-Environment-and-Power-On-Checklist-Lab.md`](./02-Exercise-Equipment-Room-Environment-and-Power-On-Checklist-Lab.md)) to apply this concept in an interactive lab workbench!
