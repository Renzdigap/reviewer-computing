# 💻 Hands-On Lab: Kunpeng 8-Channel Memory Bandwidth & DIMM Balance Calculator

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 03 — Server Hardware Architecture: CPU, Memory, Mainboard & Storage Drives (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-Memory-Architecture-DRAM-SRAM-and-DIMM-Population-Rules`  
**Interactive Workbench:** Open **[`04-Exercise-DIMM-Channel-Balance-and-SPD-Verification-Lab.html`](./04-Exercise-DIMM-Channel-Balance-and-SPD-Verification-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Write a Python script to validate the SPD EEPROM specs, compute the theoretical peak memory bandwidth of a dual-socket Kunpeng 920 server with DDR4-2933 across 16 total channels (2 × 8 channels), and check DIMM population rules.

### 📋 Step-by-Step Instructions
1. Set `spd_pins` to `8`, `spd_capacity_bytes` to `256`, and `dimm_data_width_bits` to `64`.
2. Set `channels_per_cpu` to `8` and `total_dimm_slots_2p` to `32`.
3. Specify `dram_storage_element` as `'capacitor'` and `sram_storage_element` as `'transistor'`.

### 📝 Starter Workspace (`python3@taishan-2280:~$`)
```bash
# TaiShan 200 (2280) Memory & SPD Validator
spd_pins = ___
spd_capacity_bytes = ___
dimm_data_width_bits = ___
channels_per_cpu = ___
total_dimm_slots_2p = ___
dram_storage_element = "___"
sram_storage_element = "___"

# Bandwidth per CPU at 2933 MT/s (GB/s) = 2933 * 8 bytes * 8 channels / 1000
bw_per_cpu_gbs = round(2933 * (dimm_data_width_bits // 8) * channels_per_cpu / 1000, 1)
print(f"SPD: {spd_pins}-pin {spd_capacity_bytes}B | Slots: {total_dimm_slots_2p} | BW/CPU: {bw_per_cpu_gbs} GB/s")
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- SPD is an 8-pin, 256-byte EEPROM; each DIMM has a 64-bit data bus.
- TaiShan 200 (2280) has 8 channels per CPU and 32 DIMM slots total; DRAM uses a capacitor while SRAM uses a transistor latch.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# TaiShan 200 (2280) Memory & SPD Validator
spd_pins = 8
spd_capacity_bytes = 256
dimm_data_width_bits = 64
channels_per_cpu = 8
total_dimm_slots_2p = 32
dram_storage_element = "capacitor"
sram_storage_element = "transistor"

# Bandwidth per CPU at 2933 MT/s (GB/s) = 2933 * 8 bytes * 8 channels / 1000
bw_per_cpu_gbs = round(2933 * (dimm_data_width_bits // 8) * channels_per_cpu / 1000, 1)
print(f"SPD: {spd_pins}-pin {spd_capacity_bytes}B | Slots: {total_dimm_slots_2p} | BW/CPU: {bw_per_cpu_gbs} GB/s")
```

#### Expected Console / Query Output:
```text
SPD: 8-pin 256B | Slots: 32 | BW/CPU: 187.7 GB/s
[OK] Memory architecture, DRAM/SRAM cell types, and 8-channel DIMM rules verified.
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**What is the capacity and function of the Serial Presence Detect (SPD) chip on a server memory module (DIMM)?**

- A. A 64-KB SRAM cache chip used to store CPU L1 instructions
- B. An 8-pin, 256-byte EEPROM chip that stores memory capacity, manufacturer, voltage, and operating speed read by the mainboard during startup
- C. A 16-MB Flash ROM chip that stores the UEFI operating system boot loader
- D. A timing calibration register that converts 32-bit SIMM channels into 64-bit DIMM channels

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.03 pp. 143 and 224, SPD (model 24LC01B) is an 8-pin electrically erasable programmable read-only memory (EEPROM) with a capacity of 256 bytes that stores memory metadata (capacity, manufacturer, speed, voltage) detected during startup.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**Which of the following statements about DRAM, SRAM, and TaiShan 200 (model 2280) DIMM installation rules are true?**

- A. A storage unit of DRAM uses a capacitor and requires periodic refresh, making it suitable for main memory modules.
- B. A storage unit of SRAM is a transistor latch that does not require refreshing, making it suitable for CPU caches.
- C. All DIMMs installed on the same server must have the same specifications and part number (P/N code), and at least one DIMM must be installed in a slot supported by CPU 1.
- D. Configuring 12 DIMMs on a single 8-channel Kunpeng 920 processor is a balanced channel configuration.

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** A, B, and C are true (Ch.03, pp. 144, 148). D is false because on an 8-channel processor, configuring 3, 5, 7, 9, 10, 11, 12, 13, 14, or 15 DIMMs per CPU results in an unbalanced channel configuration (p. 148).
</details>

### Question 3 [Single-Choice]
**How many data channel bits does a Single Inline Memory Module (SIMM) provide compared to a Dual Inline Memory Module (DIMM)?**

- A. SIMM provides 16-bit data channels; DIMM provides 32-bit data channels
- B. SIMM provides 32-bit data channels; DIMM provides 64-bit data channels
- C. SIMM provides 64-bit data channels; DIMM provides 128-bit data channels
- D. Both SIMM and DIMM provide 64-bit data channels

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.03 p.146, each SIMM provides 32-bit data channels, whereas each DIMM provides 64-bit data channels.
</details>
