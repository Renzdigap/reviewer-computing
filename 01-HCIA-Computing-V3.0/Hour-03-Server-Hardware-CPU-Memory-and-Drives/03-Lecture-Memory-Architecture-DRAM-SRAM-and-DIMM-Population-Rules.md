# Memory Architecture, DRAM/SRAM/ROM & DIMM Installation Rules

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 03 — Server Hardware Architecture: CPU, Memory, Mainboard & Storage Drives (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (8 mins) - Followed immediately by `04-Exercise-DIMM-Channel-Balance-and-SPD-Verification-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.03, pp. 142–148, 224–225

---

## Learning Objectives
- Identify the components of a memory module including the 8-pin 256-byte SPD EEPROM (24LC01B) and timing calibration register
- Contrast DRAM (capacitor, periodic refresh, main memory) vs. SRAM (transistor latch, no refresh, CPU cache) vs. ROM/Flash
- Master TaiShan 200 (2280) 32-slot (8-channel × 2 DPC) DDR4 DIMM installation and channel-balance rules

---

### 1. Memory Module Structure & SPD Chip (pp. 142–143, 224)
Memory (internal/main memory) acts as the communication bridge between external storage (drives) and the CPU.
- **Physical Components of a Memory Module (p. 143)**: Memory chip, Register (used for **timing calibration**), Edge connector, Resistor/Capacitor, Specification mark, Anti-counterfeit mark, and **SPD & TSOD**.
- **Serial Presence Detect (SPD, pp. 143, 224)**:
  - An **8-pin SOIC-encapsulated (3 mm × 4 mm) electrically erasable programmable read-only memory (EEPROM)** with a capacity of **256 bytes** (main model: **24LC01B**, located on the right side of the front of a DIMM).
  - Stores memory capacity, chip/module manufacturer, operating speed, voltage, and row/column address bandwidth. During boot, the mainboard automatically reads the SPD to configure memory working parameters.

---

### 2. Memory Categories: DRAM vs. SRAM vs. ROM & SIMM/DIMM (pp. 144–146, 225)
| Memory Type | Storage Element & Refresh | Integration / Speed / Power | Primary Application |
| :--- | :--- | :--- | :--- |
| **DRAM (Dynamic RAM)** | **Capacitor** + components (charge level = 0 or 1); **requires periodic refresh** due to leakage | Simple architecture, **high integration**, lower cost | **Main memory modules (DIMMs)** |
| **SRAM (Static RAM)** | **Transistor latch**; **does NOT require refreshing** | Low integration, **high speed**, high power consumption | **Small-capacity, high-efficiency CPU Caches (L1/L2/L3)** |
| **ROM / Flash** | Nonvolatile (retains data when powered off) | Includes traditional ROM, **EPROM, EEPROM, and Flash memory** | **BIOS ROM** (stored in Flash ROM), SSDs, USB flash drives |

- **Memory Parameters (p. 146)**:
  - **Memory Frequency**: Measured in **MT/s** (*millions of transfers/times per second*, e.g., 2666, 2933, 3000, 3200, 3600 MT/s).
  - **SIMM vs. DIMM**: A Single Inline Memory Module (**SIMM**) provides a **32-bit** data channel (4 Bytes); a Dual Inline Memory Module (**DIMM**) provides a **64-bit** data channel (**8 Bytes**).
  - **Theoretical Memory Bandwidth Formula**: Bandwidth = Memory Frequency (MT/s) × 8 Bytes (64 bits) × Number of Channels.

---

### 3. TaiShan 200 (2280) DIMM Slots & Installation Rules (pp. 147–148)
- **Slot Topology (p. 147)**: Equipped with two Kunpeng 920 processors (e.g., 7260 or 5250), a TaiShan 200 (2280) provides up to **32 DDR4 DIMM slots**:
  - Each processor supports **8 DIMM channels**, and each channel supports **2 DIMMs** (2 CPUs × 8 channels × 2 DIMMs/channel = 32 DIMMs).
- **Mandatory DIMM Installation Rules (p. 148)**:
  1. **At least one DIMM must be configured in slots supported by CPU 1**.
  2. **All DIMMs on a server must have the exact same specifications** (capacity, bit width, rank, height) — i.e., **the same part number (P/N code)**.
  3. **Balanced Configuration Principle**: Optimal performance requires both CPUs to have the **same number of DIMMs** (processor balance) and DIMMs to be **evenly distributed across the 8 memory channels** (channel balance: **1, 2, 4, 6, 8, or 16 DIMMs per CPU**, though 6 is partially populated, **3, 5, 7, 9, 10, 11, 12, 13, 14, or 15 DIMMs on a single CPU** are explicitly listed on p. 148 as **unbalanced channel configurations**!).

---

## Key Takeaways
- **SPD (Serial Presence Detect, model 24LC01B) is an 8-pin, 256-byte EEPROM on a DIMM that stores speed, capacity, voltage, and manufacturer metadata read during startup.**
- **DRAM uses capacitors and requires periodic refreshing (used for main memory); SRAM uses transistor latches, needs no refreshing, and is used for CPU L1/L2/L3 caches.**
- **SIMM has a 32-bit data channel; DIMM has a 64-bit (8-byte) data channel.**
- **TaiShan 200 (2280) has 32 DIMM slots (2 CPUs × 8 channels × 2 DIMMs/channel). All DIMMs must share the same P/N code, at least 1 DIMM must be on CPU 1, and configuring 3, 5, 7, 9, 10, 11, 12, 13, 14, or 15 DIMMs per CPU causes an unbalanced channel configuration.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse DRAM and SRAM! DRAM uses capacitors (needs periodic refresh -> main memory), while SRAM uses transistor latches (no refresh needed -> CPU cache).

> [!WARNING]
> EXAM TRAP: On a Kunpeng 920 CPU (8 memory channels), installing 12 DIMMs per CPU is an UNBALANCED channel configuration (12 is not divisible by 8); balanced full/half channel counts per CPU are 1, 2, 4, 8, or 16 DIMMs!

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-DIMM-Channel-Balance-and-SPD-Verification-Lab.html`](./04-Exercise-DIMM-Channel-Balance-and-SPD-Verification-Lab.html)** (or [`04-Exercise-DIMM-Channel-Balance-and-SPD-Verification-Lab.md`](./04-Exercise-DIMM-Channel-Balance-and-SPD-Verification-Lab.md)) to apply this concept in an interactive lab workbench!
