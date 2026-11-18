# 📖 Computing System Solutions: Kunpeng HPC, Huawei Cloud MRS & ModelArts

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 02 — Computing System Overview, System Software & Virtualization (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (8 mins) → Followed immediately by `08-Exercise-Kunpeng-HPC-and-Cloud-BigData-Solution-Lab` (8 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.02, pp. 117–128

---

## 🎯 Learning Objectives
- Master the full-stack Kunpeng HPC architecture (Hardware platform, DonauKit, HPCKit, DevKit)
- Distinguish open-source vs. commercial software ecosystems across HPC industries (Ch.02 Quiz Q3 trap!)
- Understand Huawei Cloud Big Data Solution (MRS, DWS, DLI, DataArts Studio, GES, CSS) and ModelArts AI platform

---

### 1. Kunpeng Full-Stack HPC Solution Architecture (pp. 118–122)
Huawei's Kunpeng HPC solution delivers **20% higher computing power**, **80%+ HPL efficiency**, **40% higher energy efficiency**, and **15%+ higher application performance** than competing domestic x86 vendors:
- **Hardware Platform**:
  - **Computing subsystem**: Kunpeng series CPUs across three server forms.
  - **Network subsystem**: Evolution from **RoCE v2 to Lingqu**, fixed and modular switches.
  - **Storage subsystem**: **OceanStor Pacific** and **OceanDisk** high-density storage + homegrown parallel file system **OceanFS**.
- **Software Subsystem**:
  - **DonauKit**: Cluster management (**Donau Portal**) + Job scheduling (**Donau Scheduler**).
  - **HPCKit**: Communication library (**Hyper MPI**), Math library & solver (**KML** — Kunpeng Math Library), and Compilers (**BiSheng Compiler / GCC**).
  - **DevKit**: Performance profiling, code porting, Kunpeng affinity code optimization, I/O optimization.

---

### 2. HPC Industry Software Ecosystems (pp. 119–122 — Official Quiz Q3 Trap!)
Most software in the HPC ecosystem is **open source**, while **commercial closed-source software** is mainly used in **manufacturing, EDA, and oil & gas**:

| HPC Industry Field | Software Ecosystem Characteristic | Typical Applications & Migration Progress |
| :--- | :--- | :--- |
| **Scientific Research / Education** | **Open source software mainly (>80% in physics/chemistry)** | **VASP, Gaussian, GROMACS, LAMMPS, NAMD, CP2K, Amber, Wannier90, Q-Chem**; 400+ projects migrated covering **90%** of compute needs. |
| **Meteorology & Oceanography** | **Open source software mainly (80% open source, 20% in-house)** | **WRF** (most common, fp32 single-precision 180 GFlops, 180 GB/s bandwidth, Bcast small packets), **GRAPES, NEMO, FVCOM, ROMS, CESM, CMAQ**; 30+ apps covering **99%** of ecosystem. |
| **Life Sciences** | **Open source software mainly** | Gene sequencing (**GATK, BWA, BLAST, Bowtie2**), Cryo-EM (**RELION, EMAN**), Drug discovery (**AutoDock, GROMACS**); 1,000+ apps (incl. Bioconda) covering **80%** of compute needs. |
| **Manufacturing Simulation (CAE)** | **Commercial software mainly** | Crash/Structural (**Abaqus, LS-DYNA, ANSYS Mechanical, Radioss, COMSOL**), Fluid (**Fluent, Star-CCM+, CFX, OpenFOAM**), EM (**HFSS, Maxwell**); 3 native + 20+ binary transcoding enablers. |

---

### 3. Huawei Cloud Big Data (MRS) & ModelArts AI Solutions (pp. 123–125)
- **Huawei Cloud Big Data Solution (p. 123)**: Built on an enterprise data lake with storage-compute decoupling (**OBS / HDFS**) and Kunpeng optimization:
  - **MRS (MapReduce Service)**: One-stop big data platform running **HBase, CarbonData, Hive, Spark, SparkSQL, Presto, Flink, Storm, Kafka, Flume, Loader, MapReduce, Tez, MLlib**.
  - **DWS**: Data Warehouse Service; **DLI**: Data Lake Insight; **CSS**: Cloud Search Service; **GES**: Graph Engine Service; **DataArts Studio**: Unified data integration, governance, and development; **DLV**: Data Visualization; **ROMA**: IoT access.
- **ModelArts (p. 125 Quiz Q3)**: Huawei Cloud's one-stop AI development platform enabling developers to quickly create, train, and deploy models.

---

## 🔑 Key Takeaways
- **Kunpeng HPC hardware platform uses OceanStor Pacific / OceanDisk with OceanFS for storage, and RoCE v2 / Lingqu for networking.**
- **DonauKit provides Donau Portal (cluster management) and Donau Scheduler (job scheduling); HPCKit provides Hyper MPI, KML, and BiSheng Compiler.**
- **Education/scientific research, meteorology, and life sciences mainly use OPEN-SOURCE software (>80%), whereas Manufacturing, EDA, and Oil & Gas mainly use COMMERCIAL software!**
- **Huawei Cloud MRS runs open-source big data components (HBase, Kafka, Spark, Hive, Flink), and ModelArts is a one-stop AI development platform.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.02 Quiz Q3): Option B states 'Most applications in the education and scientific research fields are closed-source.' -> FALSE! Over 80% of applications in education/scientific research, meteorology, and life sciences are OPEN-SOURCE. Only manufacturing/EDA/oil & gas are mainly commercial/closed-source!

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-Kunpeng-HPC-and-Cloud-BigData-Solution-Lab.html`](./08-Exercise-Kunpeng-HPC-and-Cloud-BigData-Solution-Lab.html)** (or [`08-Exercise-Kunpeng-HPC-and-Cloud-BigData-Solution-Lab.md`](./08-Exercise-Kunpeng-HPC-and-Cloud-BigData-Solution-Lab.md)) to apply this concept in an interactive lab workbench!
