# 📖 Kunpeng Accelerator Engine (KAE) & TaiShan 100/200 Server Series

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 05 — Huawei Kunpeng Processors, TaiShan Servers, openEuler/openGauss & HPC (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (8 mins) → Followed immediately by `04-Exercise-TaiShan-Server-Portfolio-and-KAE-Architecture-Lab` (7 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.04, pp. 240–256

---

## 🎯 Learning Objectives
- Understand KAE security advantages (on-chip bus vs. PCIe bus, SM3/SM4 support) and the 4 layers of the KAE logical architecture
- Compare TaiShan 100 (Kunpeng 916) and TaiShan 200 (Kunpeng 920) server portfolios (1280, 2280, 2280E, 2480, 5280, 5290)
- Master the exact hardware differences between TaiShan 2280 (2U balanced) and TaiShan 5280 (4U storage) and x86 servers

---

### 1. Kunpeng Accelerator Engine (KAE) Security & Architecture (pp. 240–243)
- **Why KAE Is More Secure Than Traditional PCIe Encryption Cards (p. 240)**:
  - In traditional servers, plaintext data and keys traverse the **external PCIe bus** to a PCIe encryption card, creating a risk of data leakage.
  - In **Kunpeng 920**, the encryption/decryption engine is **built into the CPU**, keys are stored in an **on-chip security zone** (only specified programs can write keys, and only the CPU can directly read them), and plaintext data travels **only through the on-chip bus**. Supports Chinese national cryptographic algorithms **SM3/SM4** (as well as AES/RSA) and compression (**Gzip/zlib**), without occupying CPU core resources!
- **Four-Layer KAE Logical Architecture (p. 242)**:
  1. **TaiShan Hardware Subsystems**:
     - **Chip accelerator subsystem** (integrated in Kunpeng 920; provides register operations).
     - **BIOS subsystem** (checks license, initializes modules, reports **ACPI table** to kernel).
     - **BMC subsystem** (manages accelerator **licenses** for the server).
  2. **Accelerator driver subsystem**: Core unified driver interface wrap in kernel space.
  3. **Application library subsystem**: Standard **OpenSSL** accelerator engine and **zlib** alternate library (hides hardware details so existing SSL/TLS/compression apps migrate seamlessly).
  4. **Application system**: Upper-layer user applications (Big data stream data, Block data encryption, Smart security video streams, Web service HTTPS handshakes).

---

### 2. TaiShan 100 vs. TaiShan 200 Portfolio (pp. 245–247)
| Feature | TaiShan 100 Server (2016) | TaiShan 200 Server (2019) |
| :--- | :--- | :--- |
| **Processor** | **Kunpeng 916** | **Kunpeng 920** |
| **Memory** | Up to **16 DDR4** DIMMs | Up to **32 DDR4-2933** DIMMs (up to **4 TB**) |
| **PCIe Expansion** | **5 × PCIe 3.0** slots | Up to **8 × PCIe 4.0** slots |
| **Local Drives** | SAS/SATA HDDs and SSDs | **NVMe SSDs**, SAS/SATA HDDs, and SSDs |
| **Onboard LOM** | **GE / 10GE** LOM | **100GE** LOM (flexible 4×GE, 4× 10GE, or 4× 25GE) |
| **Cooling** | Air cooling | **Board-level and full liquid cooling** |

#### TaiShan 200 Model Portfolio (p. 247):
- **2280**: **2U 2-socket balanced model** (max CPU TDP **180 W**, operating temp **5°C–40°C**).
- **5280**: **4U 2-socket 40-drive storage model** (up to **40 × 3.5" drives = 560 TB** + 4 × 2.5" NVMe SSDs; max CPU TDP **200 W**, operating temp **5°C–35°C**).
- **2480**: **2U 4-socket high-performance model** (compute-intensive / core databases).
- **1280**: **1U 2-socket high-density compute model**.
- **5290**: **72-slot high-density storage model**.
- **2280E**: **Edge computing model**.

---

### 3. Structural Differences: TaiShan 2280 vs. 5280 vs. x86 (pp. 248–256)
- **Crucial Structural Difference from x86 (p. 250)**: Unlike x86 servers (which use socketed, replaceable CPUs), **the CPUs of a TaiShan server are integrated (soldered) directly onto the motherboard and CANNOT be replaced separately** (3 motherboard variants are available). TaiShan also delivers higher DIMM density (32 slots vs. 24 on x86 Skylake).
- **Rear I/O Module Rule (p. 249)**: On the rear panel of TaiShan 2280, **I/O modules 1 and 2** can be configured with the same drive module or riser module, while **I/O module 3 cannot** (supports 4× 2.5'' rear drives or 2×PCIe 4.0 x8 FHHL slots).
- **TaiShan 2280 vs. 5280 Internal Structure (pp. 252–254)**: Both share the **same motherboard**, but differ in **drive backplanes**: 5280 holds **24 × 3.5" front drives** + **12 × 3.5" rear lower drives** + **4 × 3.5" rear upper drives** (up to 40 × 3.5" drives) + **4 × 2.5" rear drives**.
- **Kunpeng Application Benchmarks (p. 256)**: Big Data (**+30% performance**), SDS (**+20% IOPS**, compression time **reduced by 66%**).

---

## 🔑 Key Takeaways
- **KAE encrypts/decrypts inside the CPU over the on-chip bus (preventing PCIe bus data leakage), supports SM3/SM4, and exposes standard OpenSSL and zlib interfaces.**
- **In KAE, BMC manages accelerator licenses, while BIOS initializes modules and reports the ACPI table to the kernel.**
- **Unlike x86 servers, TaiShan server CPUs are integrated on the motherboard and CANNOT be replaced separately!**
- **TaiShan 2280 (2U 2P balanced, 5°C–40°C) and TaiShan 5280 (4U 2P storage, up to 40 × 3.5" drives = 560 TB, 5°C–35°C) share the same motherboard but use different drive backplanes.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: If a question asks whether a faulty CPU on a TaiShan 200 (2280) server can be replaced independently of the motherboard, the answer is FALSE — Kunpeng CPUs on TaiShan servers are integrated on the motherboard and cannot be replaced separately (p. 250)!

> [!WARNING]
> EXAM TRAP: In KAE, the BMC subsystem manages accelerator licenses, whereas the BIOS subsystem reports the ACPI table of the accelerator to the OS kernel (p. 242).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-TaiShan-Server-Portfolio-and-KAE-Architecture-Lab.html`](./04-Exercise-TaiShan-Server-Portfolio-and-KAE-Architecture-Lab.html)** (or [`04-Exercise-TaiShan-Server-Portfolio-and-KAE-Architecture-Lab.md`](./04-Exercise-TaiShan-Server-Portfolio-and-KAE-Architecture-Lab.md)) to apply this concept in an interactive lab workbench!
