# 📖 Kunpeng HPC Solution, Workload Types & HPCKit Components

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 05 — Huawei Kunpeng Processors, TaiShan Servers, openEuler/openGauss & HPC (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (8 mins) → Followed immediately by `08-Exercise-HPC-Application-Classification-and-HPCKit-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.04, pp. 270–282

---

## 🎯 Learning Objectives
- Understand the 3 paradigms of scientific research and classify HPC workloads into Memory-constrained, Computing-intensive, I/O-intensive, and Network-intensive
- Master the components of HPCKit: Hyper MPI (Open MPI 4.1.1 + Open UCX 1.10.1, MPI-3.1), KML (FFT, matrix/vector), and BiSheng Compiler (LLVM + Fortran + Autotuner)
- Analyze the Kunpeng Cloud HPC solution (PFS, 100G InfiniBand 1.5 us latency) and the petascale university supercomputing case study

---

### 1. HPC Paradigms & Four Workload Categories (pp. 271–275)
- **Three Paradigms in Scientific Research (p. 272)**: **Theoretical science**, **Experimental science**, and **Computing science (HPC)**. HPC reduces new vehicle time-to-market (TTM) from **60 months to 24 months** and drug discovery screening from **5,000 years on common computers to 100 days**.
- **Four Categories of HPC Applications (p. 273 — High-Yield Exam Table!)**:

| HPC Workload Category | Key Hardware Requirement | Representative Applications (p. 273) |
| :--- | :--- | :--- |
| **Memory-constrained** | Large memory capacity & high memory bandwidth | **Numerical calculation**, astrophysics, molecular dynamics simulation |
| **Computing-intensive** | High-speed multi-core CPU | **Meteorology (weather forecasting), earthquake, and aerospace** |
| **I/O-intensive** | High storage bandwidth & large-capacity shared storage | **Animation rendering and gene analysis (DNA sequence alignment/assembly)** |
| **Network-intensive** | High-speed, low-latency node interconnection | **CAE simulation** (automotive, aviation, chip geometric modeling) |

- **Four HPC Industry Challenges (p. 275)**: (1) Ever-increasing demand for computing, (2) Diverse industry applications, (3) Application, deployment, and management complexity/CAPEX, (4) Soaring power costs.

---

### 2. Huawei HPCKit Base Software Components (p. 276)
**HPCKit** provides one-click deployment and collaborative optimization of three core components:
1. **Hyper MPI (Communication Library)**:
   - Built on **Open MPI 4.1.1** and **Open UCX 1.10.1**, supporting the **MPI-3.1 standard** for parallel computing.
   - Provides an optimized collective communication framework and shared memory mechanism between nodes.
2. **KML (Kunpeng Math Library)**:
   - Hardware-accelerated mathematical library optimized for Kunpeng processors, supporting **Fast Fourier Transform (FFT)**, matrix calculation, vectorization, and trigonometric/logarithmic functions.
3. **BiSheng Compiler**:
   - High-performance compiler developed based on **LLVM** and optimized for Kunpeng, adding **Fortran front-end** support, middle-/back-end optimizations, and the **Autotuner** automatic tuning feature.

---

### 3. Kunpeng Cloud HPC, University Case Study & Chapter 04 Acronyms (pp. 277–282)
- **Kunpeng Cloud HPC Highlights (p. 277)**:
  - **30% higher price/performance ratio** than traditional solutions.
  - Unique **Parallel File System (PFS)** supporting both **object storage and POSIX interfaces** without data copy operations, reducing TCO by **20%**.
  - Supports **100G InfiniBand** (latency as low as **1.5 microseconds**) and **RDMA**.
  - On-cloud one-click cluster provisioning improves cluster management efficiency by **90%**.
- **University Petascale Supercomputing Case Study (p. 278)**:
  - Deployed **720 Huawei full liquid-cooled high-density servers** in only **10 cabinets** (saving at least **CNY 170,000/year** in electricity fees), plus **20 TaiShan servers** for bioinformatics and fluid dynamics: **30,480 CPU cores**, **2.52 PFLOPS** peak performance, and **63.95% HPL efficiency** (up to **71%** on some nodes).
- **Key Chapter 04 Acronyms (p. 282)**: **ISV** (*Independent Software Vendor*), **IHV** (*Independent Hardware Vendor*), **C&SI** (*Consulting and Systems Integration*), **SDK** (*Software Development Kit*).

---

## 🔑 Key Takeaways
- **Four HPC workload types (p. 273): Memory-constrained (numerical calculation/molecular dynamics), Computing-intensive (meteorology/earthquake/aerospace), I/O-intensive (animation rendering/gene analysis), and Network-intensive (CAE simulation).**
- **HPCKit consists of Hyper MPI (Open MPI 4.1.1 + Open UCX 1.10.1, MPI-3.1), KML (Kunpeng Math Library: FFT, matrix, vector), and BiSheng Compiler (LLVM-based with Fortran front-end and Autotuner).**
- **Kunpeng Cloud HPC uses Parallel File System (PFS) supporting both Object Storage and POSIX interfaces (-20% TCO) and 100G InfiniBand with 1.5 us latency.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not mix up the 4 HPC workload categories on p. 273: Gene analysis & animation rendering are I/O-INTENSIVE; CAE simulation is NETWORK-INTENSIVE; Meteorology/earthquake/aerospace are COMPUTING-INTENSIVE; Numerical calculation is MEMORY-CONSTRAINED!

> [!WARNING]
> EXAM TRAP: BiSheng Compiler is developed based on LLVM (not GCC) and adds Fortran front-end support and Autotuner (p. 276).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-HPC-Application-Classification-and-HPCKit-Lab.html`](./08-Exercise-HPC-Application-Classification-and-HPCKit-Lab.html)** (or [`08-Exercise-HPC-Application-Classification-and-HPCKit-Lab.md`](./08-Exercise-HPC-Application-Classification-and-HPCKit-Lab.md)) to apply this concept in an interactive lab workbench!
