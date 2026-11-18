# 💻 Hands-On Lab: TaiShan 200 Portfolio & KAE Subsystem Configuration

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 05 — Huawei Kunpeng Processors, TaiShan Servers, openEuler/openGauss & HPC (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (7 mins) — Paired with `03-Lecture-Kunpeng-Accelerator-Engine-KAE-and-TaiShan-200-Servers`  
**Interactive Workbench:** Open **[`04-Exercise-TaiShan-Server-Portfolio-and-KAE-Architecture-Lab.html`](./04-Exercise-TaiShan-Server-Portfolio-and-KAE-Architecture-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## 🛠️ Part A: Practical Lab Scenario
Complete the TaiShan 200 hardware specification and KAE subsystem mapping for a Kunpeng data center deployment.

### 📋 Step-by-Step Instructions
1. Set `kae_app_libraries` to `'OpenSSL/zlib'`, `kae_license_manager` to `'BMC'`, and `kae_acpi_reporter` to `'BIOS'`.
2. Set `taishan_cpu_replaceable_separately` to `False`.
3. Map the TaiShan 200 models: `balanced_2u2p` -> `'2280'`, `storage_4u2p` -> `'5280'`, and `high_perf_2u4p` -> `'2480'`.

### 📝 Starter Workspace (`admin@taishan-cluster:~#`)
```bash
# KAE & TaiShan 200 Portfolio Configuration
kae_architecture:
  kae_app_libraries: "___"
  kae_license_manager: "___"
  kae_acpi_reporter: "___"
  supported_chinese_crypto: "SM3/SM4"

taishan_200_series:
  taishan_cpu_replaceable_separately: ___
  balanced_2u2p: "___"
  storage_4u2p: "___"
  high_perf_2u4p: "___"
  storage_5280_max_3_5_drives: 40
```

<details>
<summary>💡 <strong>Click to View Hints</strong></summary>

- KAE application libraries are OpenSSL/zlib; BMC manages licenses and BIOS reports the ACPI table.
- TaiShan CPUs are soldered on the mainboard (False); 2280 is 2U2P balanced, 5280 is 4U2P storage, and 2480 is 2U4P high-performance.

</details>

<details>
<summary>🔑 <strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# KAE & TaiShan 200 Portfolio Configuration
kae_architecture:
  kae_app_libraries: "OpenSSL/zlib"
  kae_license_manager: "BMC"
  kae_acpi_reporter: "BIOS"
  supported_chinese_crypto: "SM3/SM4"

taishan_200_series:
  taishan_cpu_replaceable_separately: False
  balanced_2u2p: "2280"
  storage_4u2p: "5280"
  high_perf_2u4p: "2480"
  storage_5280_max_3_5_drives: 40
```

#### Expected Console / Query Output:
```text
[OK] KAE & TaiShan 200 Series Configuration Validated:
- KAE: On-chip encryption (SM3/SM4) + compression | BMC (License) + BIOS (ACPI) + OpenSSL/zlib
- TaiShan 200 Models: 1280 (1U2P), 2280 (2U2P Balanced), 2280E (Edge), 2480 (2U4P), 5280 (4U 40-drive Storage), 5290 (72-slot)
- CPU Integration: Soldered on mainboard (not separately replaceable).
```
</details>

---

## 📝 Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**In the logical architecture of the Kunpeng Accelerator Engine (KAE), which subsystem manages accelerator licenses for servers, and which standard application library interfaces are provided to upper-layer applications?**

- A. BIOS subsystem manages licenses; JDBC and ODBC interfaces are provided
- B. BMC subsystem manages licenses; OpenSSL and zlib interfaces are provided
- C. iBMA manages licenses; POSIX and Win32 interfaces are provided
- D. RAID controller manages licenses; MPI and KML interfaces are provided

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** According to Ch.04 pp. 241–242, the BMC subsystem manages accelerator licenses, the BIOS subsystem reports the ACPI table to the kernel, and the application library subsystem provides standard OpenSSL and zlib interfaces.
</details>

### Question 2 [True / False]
**Like traditional x86 rack servers, the Kunpeng 920 CPUs in a TaiShan 200 (model 2280) server are installed in standard socket latches and can be replaced separately without replacing the motherboard.**

- A. True
- B. False

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.04 p.250, unlike x86 servers, the CPUs of a TaiShan server are integrated on the motherboard and cannot be replaced separately (3 types of motherboards are available).
</details>

### Question 3 [Single-Choice]
**Which TaiShan 200 server model is a 4U 2-socket storage server supporting up to forty 3.5-inch drives (560 TB local storage) and sharing the same motherboard as the TaiShan 2280?**

- A. TaiShan 1280
- B. TaiShan 2480
- C. TaiShan 5280
- D. TaiShan 2280E

<details>
<summary>✅ <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** According to Ch.04 pp. 247 and 252, the TaiShan 5280 is a 4U 2-socket storage server supporting up to 40 × 3.5-inch drives (560 TB) and 4 × 2.5-inch NVMe SSDs, sharing the same motherboard as the 2U TaiShan 2280.
</details>
