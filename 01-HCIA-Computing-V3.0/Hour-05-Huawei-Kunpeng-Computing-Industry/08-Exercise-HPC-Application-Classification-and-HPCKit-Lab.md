# Hands-On Lab: HPC Workload Classifier & HPCKit Toolchain Config

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 05 — Huawei Kunpeng Processors, TaiShan Servers, openEuler/openGauss & HPC (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Kunpeng-HPC-Solution-and-HPCKit`  
**Interactive Workbench:** Open **[`08-Exercise-HPC-Application-Classification-and-HPCKit-Lab.html`](./08-Exercise-HPC-Application-Classification-and-HPCKit-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
Classify scientific workloads into the four official HPC categories and configure the HPCKit toolchain manifest.

### Step-by-Step Instructions
1. Map the workloads: `numerical_calculation` -> `'Memory-constrained'`, `meteorology_and_aerospace` -> `'Computing-intensive'`, `animation_and_gene_analysis` -> `'I/O-intensive'`, and `cae_simulation` -> `'Network-intensive'`.
2. Set `bisheng_compiler_base` to `'LLVM'` and `hyper_mpi_standard` to `'MPI-3.1'`.
3. Set `infiniband_100g_latency_us` to `1.5`.

### Starter Workspace (`hpc-user@kunpeng-cluster:~#`)
```bash
# HPC Workload & HPCKit Toolchain Configuration
hpc_workload_classes:
  numerical_calculation: "___"
  meteorology_and_aerospace: "___"
  animation_and_gene_analysis: "___"
  cae_simulation: "___"

hpckit_toolchain:
  bisheng_compiler_base: "___"
  bisheng_auto_tuning_feature: "Autotuner"
  hyper_mpi_standard: "___"
  math_library: "KML"
  infiniband_100g_latency_us: ___
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Numerical calculation is Memory-constrained, Meteorology/Aerospace is Computing-intensive, Animation/Gene analysis is I/O-intensive, and CAE simulation is Network-intensive.
- BiSheng Compiler is based on LLVM; Hyper MPI supports MPI-3.1; 100G InfiniBand latency is 1.5 microseconds.

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# HPC Workload & HPCKit Toolchain Configuration
hpc_workload_classes:
  numerical_calculation: "Memory-constrained"
  meteorology_and_aerospace: "Computing-intensive"
  animation_and_gene_analysis: "I/O-intensive"
  cae_simulation: "Network-intensive"

hpckit_toolchain:
  bisheng_compiler_base: "LLVM"
  bisheng_auto_tuning_feature: "Autotuner"
  hyper_mpi_standard: "MPI-3.1"
  math_library: "KML"
  infiniband_100g_latency_us: 1.5
```

#### Expected Console / Query Output:
```text
[OK] Kunpeng HPC Workload Classification & HPCKit Manifest Verified:
- Workloads: Memory-constrained (Numerical) | Computing-intensive (Meteorology) | I/O-intensive (Gene/Animation) | Network-intensive (CAE)
- HPCKit: BiSheng Compiler (LLVM + Fortran + Autotuner) + Hyper MPI (Open MPI 4.1.1 / UCX 1.10.1 / MPI-3.1) + KML
- Cloud HPC: PFS (Object + POSIX, -20% TCO) | 100G IB (1.5 us latency).
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**According to Chapter 04 (p. 273), how are 'animation rendering and gene analysis' and 'CAE simulation' classified among HPC application types?**

- A. Animation/gene analysis is I/O-intensive; CAE simulation is Network-intensive
- B. Animation/gene analysis is Network-intensive; CAE simulation is Memory-constrained
- C. Animation/gene analysis is Computing-intensive; CAE simulation is I/O-intensive
- D. Both are classified exclusively as Memory-constrained

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** According to Ch.04 p.273: Numerical calculation is Memory-constrained; Meteorology, earthquake, and aerospace are Computing-intensive; Animation rendering and gene analysis are I/O-intensive; and CAE simulation is Network-intensive.
</details>

### Question 2 [Multiple-Choice (Select ALL)]
**Which of the following statements about the components of Huawei's HPCKit are true?**

- A. Hyper MPI is based on Open MPI 4.1.1 and Open UCX 1.10.1 and supports the MPI-3.1 standard.
- B. The Kunpeng Math Library (KML) accelerates FFT, matrix calculation, vectorization, and trigonometric/logarithmic functions.
- C. The BiSheng Compiler is developed based on LLVM, supports the Fortran front-end, and integrates the Autotuner feature.
- D. HPCKit only runs on x86 CISC processors and does not support Arm processors.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `ABC`
- **Explanation:** A, B, and C are true (Ch.04, p.276). D is false because HPCKit is specifically optimized for Huawei Kunpeng (Arm) processors.
</details>

### Question 3 [Single-Choice]
**In the Kunpeng Cloud HPC solution, which storage technology supports both object storage and POSIX interfaces without requiring data copy operations, reducing TCO by 20%?**

- A. Parallel File System (PFS)
- B. FAT32
- C. NTFS
- D. Local SATA RAID 0

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `A`
- **Explanation:** According to Ch.04 p.277, Huawei's unique Parallel File System (PFS) supports both object storage and POSIX interfaces without data copy operations, reducing TCO by 20%.
</details>
