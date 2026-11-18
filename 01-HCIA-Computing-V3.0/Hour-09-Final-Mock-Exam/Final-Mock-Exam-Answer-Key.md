# Official Answer Key & Explanations — HCIA-Computing V3.0 — National Stage Final Mock Exam

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Total Questions:** 60 (1000 Points)

---

### Q1 (Ch.01 History of Computing) — [15 pts]
- **Question:** (Official Ch.01 Quiz Q1) Which of the following is not a basic element of AI applications?
- **Correct Answer:** `D`
- **Explanation:** According to Ch.01 pp. 48, 51, and p. 62 Quiz Q1, Data, Algorithms, Computing power, and Scenarios are the four basic elements of AI applications. Talent is not a basic element.

### Q2 (Ch.01 History of Computing) — [15 pts]
- **Question:** In 1946, a research team led by John Mauchly at the University of Pennsylvania developed the second electronic computer and the world's first general-purpose programmable electronic computer. What was its name and speed?
- **Correct Answer:** `B`
- **Explanation:** According to Ch.01 p.23, ENIAC (1946) is the second electronic computer (after ABC in 1937) and the first general-purpose computer, capable of up to 5,000 additions or 400 multiplications per second using 17,000+ electron tubes.

### Q3 (Ch.01 History of Computing) — [15 pts]
- **Question:** In the Hadoop big data ecosystem (Ch.01, p. 44), which component acts as the unified resource allocator, and which acts as the distributed coordination service?
- **Correct Answer:** `B`
- **Explanation:** According to Ch.01 p.44, YARN is the unified resource allocator, ZooKeeper is the distributed coordination service, Ambari is the installation/deployment tool, and Oozie is the workflow scheduling system.

### Q4 (Ch.02 Computing System Overview) — [15 pts]
- **Question:** (Official Ch.02 Quiz Q2 / p. 98) According to the database model definitions in Chapter 02 (p. 98), which database model allows more than one node to have no parent and allows a node to have more than one parent?
- **Correct Answer:** `B`
- **Explanation:** On Ch.02 p.98, the Network model is explicitly defined as: 'Allows more than one node to have no parent. A node can have more than one parent.' (Whereas the Hierarchical model has only one root node and each non-root node has only one parent).

### Q5 (Ch.02 Computing System Overview) — [15 pts]
- **Question:** When comparing Windows Server 2022 Standard edition with Datacenter edition (Ch.02, p. 88), how many Virtual Machines (VMs) does each Standard edition license permit?
- **Correct Answer:** `B`
- **Explanation:** According to Ch.02 p.88, each Windows Server 2022 Datacenter license allows an unlimited number of VMs and one Hyper-V host (plus SDN, Storage Spaces Direct, and Network Controller), whereas each Standard edition license permits only two VMs and one Hyper-V host.

### Q6 (Ch.02 Computing System Overview) — [15 pts]
- **Question:** To deploy Huawei FusionCompute on physical servers (Ch.02, p. 115), what are the minimum system drive capacities required for the VRM node and each compute node, respectively?
- **Correct Answer:** `B`
- **Explanation:** According to Ch.02 p.115, the system drive on the Virtual Resource Manager (VRM) node must be >= 270 GB, and the system drive on each compute node must be >= 150 GB.

### Q7 (Ch.03 Server Architecture Overview) — [15 pts]
- **Question:** In a server CPU's Control Unit (Ch.03, pp. 138, 224), which component decodes an instruction into an operation code and an address code, and which component generates micro-operation control signals?
- **Correct Answer:** `B`
- **Explanation:** According to Ch.03 pp. 138 and 224, the Instruction Decoder (ID) decodes instructions into operation codes and address codes, while the Operation Controller (OC) generates operation control signals according to predetermined timing.

### Q8 (Ch.03 Server Architecture Overview) — [15 pts]
- **Question:** On a TaiShan 200 (model 2280) server equipped with two Kunpeng 920 processors (Ch.03, pp. 147–148), which of the following DIMM counts installed on a SINGLE CPU results in an UNBALANCED memory channel configuration?
- **Correct Answer:** `C`
- **Explanation:** According to Ch.03 p.148, each Kunpeng 920 CPU has 8 memory channels (2 DIMMs per channel = 16 slots per CPU). If a single CPU is configured with 3, 5, 7, 9, 10, 11, 12, 13, 14, or 15 DIMMs, the memory configuration between channels is unbalanced.

### Q9 (Ch.03 Server Architecture Overview) — [15 pts]
- **Question:** According to the drive benchmark table in Chapter 03 (p. 158), what are the typical 4 KB Random Write IOPS and 128 KB Sequential Read Bandwidth of an NVMe SSD?
- **Correct Answer:** `D`
- **Explanation:** According to Ch.03 p.158: SATA HDD = 330 IOPS / 200 MB/s; SAS 10K = 350 / 195 MB/s; SAS 15K = 450 / 290 MB/s; SATA SSD = 30–60K / 540 MB/s; SAS SSD = 155K / 1000 MB/s; NVMe SSD = 300K IOPS / 3500 MB/s.

### Q10 (Ch.03 Server Architecture Overview) — [15 pts]
- **Question:** Which RAID level uses two independent distributed parity codes (P and Q, where P uses XOR and Q uses Galois field multiplication) so that data accessibility remains unaffected even if two disks fail simultaneously?
- **Correct Answer:** `C`
- **Explanation:** According to Ch.03 p.161, RAID 6 uses two independent distributed parity codes: P0 = D0 xor D1 and Q0 = (D0*K0) xor (D1*K1), tolerating up to two simultaneous disk failures.

### Q11 (Ch.03 Server Architecture Overview) — [15 pts]
- **Question:** What are the total pin count and total physical length of a PCIe x16 slot, and what is its bandwidth under PCIe 3.0 vs. PCIe 4.0 (Ch.03, p. 173)?
- **Correct Answer:** `C`
- **Explanation:** According to Ch.03 p.173, a PCIe x16 slot has 164 total pins (142 in main port area), a total length of 89 mm (71.65 mm main port area), and delivers 15.8 GB/s in PCIe 3.0 (8.0 GT/s) and 31.5 GB/s in PCIe 4.0 (16.0 GT/s).

### Q12 (Ch.03 Server Architecture Overview) — [15 pts]
- **Question:** In computing power measurement (Ch.03, p. 185), how many floating-point operations per second do PFLOPS and EFLOPS represent, and which metric focuses on integer computing power?
- **Correct Answer:** `B`
- **Explanation:** According to Ch.03 p.185: MFLOPS = 10^6, GFLOPS = 10^9, TFLOPS = 10^12, PFLOPS = 10^15, EFLOPS = 10^18; TOPS (teraOPS) measures trillions of operations per second focusing on integer computing power.

### Q13 (Ch.04 Huawei Computing Industry) — [15 pts]
- **Question:** Which bus technology in the Huawei Kunpeng 920 processor provides coherent memory access across cores, devices, and clusters with up to 480 Gbit/s inter-chip bandwidth and supports up to four sockets (256 physical cores)?
- **Correct Answer:** `C`
- **Explanation:** According to Ch.04 p.237, the Huawei Cache Coherence System (HCCS) bus provides coherent access to system memory with up to 480 Gbit/s inter-chip bandwidth, allowing interconnection of up to four Kunpeng 920 processors (256 physical cores).

### Q14 (Ch.04 Huawei Computing Industry) — [15 pts]
- **Question:** In Software-Defined Storage (SDS) scenarios (Ch.04, p. 256), by how much does the Kunpeng 920 processor's built-in compression engine reduce data compression time and increase IOPS compared to traditional processor algorithms?
- **Correct Answer:** `B`
- **Explanation:** According to Ch.04 p.256, in SDS scenarios, the Kunpeng processor uses a built-in data compression engine and multi-core parallel computing to reduce compression time by 66% and increase IOPS performance by more than 20%.

### Q15 (Ch.05 Computing Product Deployment) — [15 pts]
- **Question:** (Official Ch.05 Quiz Q1) To install the OS using the openEuler-22.03-LTS-aarch64-dvd.iso file, which of the following boot options needs to be used?
- **Correct Answer:** `B`
- **Explanation:** According to Ch.05 p.329 and p.346 Quiz Q1, when installing the OS using the mounted `openEuler-22.03-LTS-aarch64-dvd.iso` file on the remote virtual console, the boot option must be set to DVD-ROM drive.

### Q16 (Ch.05 Computing Product Deployment) — [15 pts]
- **Question:** What are the default user name and password for the 'Default iBMC login user' (distinct from the WebUI/CLI `Administrator` account) on a TaiShan 200 (model 2280) server (Ch.05, p. 297)?
- **Correct Answer:** `A`
- **Explanation:** According to the table on Ch.05 p.297: Default iBMC login user = `root` / `Huawei12#$`; iBMC WebUI or CLI login = `Administrator` / `Admin@9000`; iBMC U-Boot data default password = `Admin@9000`.

### Q17 (Ch.05 Computing Product Deployment) — [15 pts]
- **Question:** When installing a device driver and firmware on a server (Ch.05, p. 335), what is the correct sequence for 'Overwrite installation' (upgrading a device that already has driver and firmware installed)?
- **Correct Answer:** `B`
- **Explanation:** According to the flowchart on Ch.05 p.335: Initial installation installs the driver first and then the firmware; Overwrite installation installs the firmware first and then the driver.

### Q18 (Ch.06 Basic O&M of Computing Products) — [15 pts]
- **Question:** In Huawei computing products (such as X6800 and E9000), which control unit complies with IPMI 2.0 specifications and supplements the server node iBMC by managing chassis power supplies, fan speed adjustment, asset collection, and network convergence (Ch.06, pp. 358, 442)?
- **Correct Answer:** `B`
- **Explanation:** According to Ch.06 pp. 358 and 442, the Hyper Management Module (HMM) is a controller designed for power supply and fan management that complies with IPMI 2.0 and supplements the iBMC of a server node.

### Q19 (Ch.06 Basic O&M of Computing Products) — [15 pts]
- **Question:** In Huawei FusionDirector's Automatic Go-Online Planning (Ch.06, p. 385), which component is used to obtain the rack U marks of servers in location-based planning, and what happens when location planning is enabled?
- **Correct Answer:** `A`
- **Explanation:** According to Ch.06 p.385, installation planning by location uses iRM to obtain the U marks of servers deployed in a rack. When location planning is enabled, the activation switch based on SN/MAC planning is automatically disabled (and vice versa).

### Q20 (Ch.06 Basic O&M of Computing Products) — [15 pts]
- **Question:** In Huawei eSight Device Power-On and Power-Off Management (Ch.06, p. 411), how are task execution priorities numbered and ordered?
- **Correct Answer:** `B`
- **Explanation:** According to Ch.06 p.411, there are intervals at which commands are executed for devices with different priorities (1 to 10 in descending order), and devices with higher priorities are powered on or off first.

### Q21 (Ch.01 History of Computing) — [20 pts]
- **Question:** (Official Ch.01 Quiz Q2) Which of the following places can be represented in the knot counting method of the Inca people?
- **Correct Answer:** `ABD`
- **Explanation:** According to Ch.01 p.10 and p.62 Official Quiz Q2, Inca Quipu knots represent Ones, Tens, Hundreds (A), Thousands (D), and Tens of thousands ('Tens of hundreds', B). 'Hundreds of thousands' (C) cannot be represented.

### Q22 (Ch.01 History of Computing) — [20 pts]
- **Question:** Which of the following statements about early and mechanical computing tools in Chapter 01 are true?
- **Correct Answer:** `ABCD`
- **Explanation:** All four statements are exact facts from Ch.01 pp. 11, 13, 17, and 18.

### Q23 (Ch.01 History of Computing) — [20 pts]
- **Question:** With cloud transformation, enterprise data centers are transformed in which five ways according to Chapter 01 (p. 35)?
- **Correct Answer:** `ABCD`
- **Explanation:** All five transformations are listed on Ch.01 p.35.

### Q24 (Ch.01 History of Computing) — [20 pts]
- **Question:** Which of the following statements about emerging computing trends in Chapter 01 (pp. 56–58) are true?
- **Correct Answer:** `ABCD`
- **Explanation:** All four statements come directly from Ch.01 pp. 56 and 58.

### Q25 (Ch.02 Computing System Overview) — [20 pts]
- **Question:** (Official Ch.02 Quiz Q3) Which of the following statements are true about computing system solutions?
- **Correct Answer:** `ACD`
- **Explanation:** According to Ch.02 p.125 Official Quiz Q3, A, C, and D are true. B is false because more than 80% of applications in education and scientific research are open-source (Ch.02, pp. 119, 122).

### Q26 (Ch.02 Computing System Overview) — [20 pts]
- **Question:** Which of the following are the five core features of a server (RASUM) defined in Chapter 02 (p. 75)?
- **Correct Answer:** `ABCD`
- **Explanation:** Reliability, Availability, Scalability, Usability, and Manageability are the five server features defined on Ch.02 p.75.

### Q27 (Ch.02 Computing System Overview) — [20 pts]
- **Question:** Which of the following statements accurately compare Tower, Blade, and Rack servers (Ch.02, pp. 78–80)?
- **Correct Answer:** `ABC`
- **Explanation:** A, B, and C are true (Ch.02, pp. 78–80). D is false because each blade is an independent server and runs its own OS (p. 79).

### Q28 (Ch.02 Computing System Overview) — [20 pts]
- **Question:** To achieve optimal performance when deploying openGauss 5.0.0+ on a 4-socket Kunpeng server running openEuler 20.03 LTS (Ch.02, p. 101), which hardware specifications are recommended by Huawei?
- **Correct Answer:** `ABCD`
- **Explanation:** All four specifications are listed verbatim in the slide notes on Ch.02 p.101.

### Q29 (Ch.03 Server Architecture Overview) — [20 pts]
- **Question:** (Official Ch.03 Quiz Q1) Which of the following statements are true about NICs of Huawei servers?
- **Correct Answer:** `AB`
- **Explanation:** According to Ch.03 p.177 and p.220 Official Quiz Q1, A and B are true. C is false (FlexIO cards are pluggable rear-panel cards for Huawei rack servers) and D is false (Mezzanine cards are only for Huawei E9000 blade server compute nodes).

### Q30 (Ch.03 Server Architecture Overview) — [20 pts]
- **Question:** Which of the following features are supported by Huawei's third-generation intelligent converged network chip Hi1822 / IN200 iNIC (Ch.03, pp. 179–180)?
- **Correct Answer:** `ABCD`
- **Explanation:** All four sets of features are explicitly listed on Ch.03 pp. 179–180 for the Hi1822 chip and IN200 iNIC.

### Q31 (Ch.03 Server Architecture Overview) — [20 pts]
- **Question:** Which of the following statements about GPUs and NPUs in Chapter 03 (pp. 181–183) are true?
- **Correct Answer:** `ABCD`
- **Explanation:** All four statements come directly from Ch.03 pp. 181–183.

### Q32 (Ch.03 Server Architecture Overview) — [20 pts]
- **Question:** Trace the evolution of the Intelligent Platform Management Interface (IPMI) specification (Ch.03, p. 193). Which of the following statements are true?
- **Correct Answer:** `ABC`
- **Explanation:** A, B, and C are true (Ch.03, p.193). D is false because IPMI exchanges information via the BMC using entry-level intelligent hardware rather than the OS.

### Q33 (Ch.04 Huawei Computing Industry) — [20 pts]
- **Question:** (Official Ch.04 Quiz Q1) Which of the following statements are true about the Huawei Kunpeng 920 processor?
- **Correct Answer:** `ABCD`
- **Explanation:** All four options (ABCD) are true and match the official Chapter 04 Quiz Q1 on p. 279.

### Q34 (Ch.04 Huawei Computing Industry) — [20 pts]
- **Question:** Which of the following statements about the Kunpeng Accelerator Engine (KAE) on Kunpeng 920 / TaiShan 200 servers are true (Ch.04, pp. 240–242)?
- **Correct Answer:** `ABCD`
- **Explanation:** All four statements come directly from Ch.04 pp. 240–242.

### Q35 (Ch.04 Huawei Computing Industry) — [20 pts]
- **Question:** What are the four pillars of Huawei's Kunpeng computing industry ecosystem strategy (Ch.04, p. 258)?
- **Correct Answer:** `ABCD`
- **Explanation:** According to Ch.04 p.258, Huawei promotes Kunpeng industry development by adhering to the strategy of 'open hardware, open source software, partner enablement, and talent cultivation'.

### Q36 (Ch.05 Computing Product Deployment) — [20 pts]
- **Question:** Which of the following ESD (Electrostatic Discharge) prevention precautions must be observed when installing or maintaining server hardware in an equipment room (Ch.05, p. 292)?
- **Correct Answer:** `ABC`
- **Explanation:** A, B, and C are mandatory ESD rules on Ch.05 p.292. D is strictly forbidden ('Do not touch welding points, pins, or exposed circuits').

### Q37 (Ch.05 Computing Product Deployment) — [20 pts]
- **Question:** Which of the following statements about `vsftpd` security features and Postfix mail server working modes are true (Ch.05, pp. 338, 341)?
- **Correct Answer:** `ABCD`
- **Explanation:** All four statements come directly from Ch.05 pp. 338 and 341.

### Q38 (Ch.06 Basic O&M of Computing Products) — [20 pts]
- **Question:** (Official Ch.06 Quiz Q1) A batch of TaiShan 200 2280 balanced servers are purchased, but they do not have pre-integrated software. During project delivery, engineers need to configure RAIDs for these servers and install OSs. Which of the following computing management software can be used to configure RAIDs for these servers?
- **Correct Answer:** `ABC`
- **Explanation:** According to Ch.06 p.438 Official Quiz Q1, Smart Provisioning (A), SmartKit (B), and iBMC (C) can configure RAIDs on bare-metal TaiShan 200 2280 servers; eService (D) is for remote O&M and cannot configure RAID.

### Q39 (Ch.06 Basic O&M of Computing Products) — [20 pts]
- **Question:** In Huawei FusionDirector's Intelligent Energy Efficiency Management (Ch.06, p. 399), which four optimization analysis functions are provided?
- **Correct Answer:** `ABCD`
- **Explanation:** All four optimization analysis functions are listed in the table on Ch.06 p.399.

### Q40 (Ch.06 Basic O&M of Computing Products) — [20 pts]
- **Question:** In Huawei SmartKit Batch Distribution and Configuration Check functions (Ch.06, pp. 428, 432), which of the following capabilities are supported?
- **Correct Answer:** `ABCD`
- **Explanation:** All four capabilities are explicitly described on Ch.06 pp. 428 and 432.

### Q41 (Ch.02 Computing System Overview) — [10 pts]
- **Question:** (Official Ch.02 Quiz Q1) Servers are developed from midrange computers to general-purpose servers and then to mainframe servers.
- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.02 p.76 and p.124 Official Quiz Q1, servers evolved from Mainframes (1940s–1950s) -> Midrange computers (1960s–1970s) -> Microcomputers (1970s–1980s) -> General-purpose servers (1980s–1990s).

### Q42 (Ch.03 Server Architecture Overview) — [10 pts]
- **Question:** (Official Ch.03 Quiz Q2) The baseboard management controller (BMC) complies with the Intelligent Platform Management Interface (IPMI) specification. It collects, processes, and stores sensor signals, and monitors the operating status of components.
- **Correct Answer:** `A`
- **Explanation:** True. This is the exact statement from Ch.03 p.201 and p.220 Official Quiz Q2.

### Q43 (Ch.01 History of Computing) — [10 pts]
- **Question:** In 1983, Apple Lisa was launched and became the world's first personal computer that uses both a graphical user interface (GUI) and a mouse device.
- **Correct Answer:** `A`
- **Explanation:** True. According to Ch.01 p.27, Apple II (1977) displayed color graphics, and Apple Lisa (1983) became the world's first PC to use both a GUI and a mouse device.

### Q44 (Ch.02 Computing System Overview) — [10 pts]
- **Question:** Apache Tomcat is a lightweight open-source web application server that complies with Servlet and JSP specifications and natively supports Enterprise JavaBeans (EJB).
- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.02 p.91, Tomcat complies with Servlet and JSP specifications, but it does NOT support EJB (JBoss can be used instead if open-source EJB support is required).

### Q45 (Ch.03 Server Architecture Overview) — [10 pts]
- **Question:** In RAID 01, data is striped first (RAID 0) and then mirrored (RAID 1); therefore, the failure of a single disk causes the loss of an entire mirrored stripe and transitions the system into a non-redundant RAID 0 array.
- **Correct Answer:** `A`
- **Explanation:** True. According to Ch.03 p.160, RAID 01 stripes first and then mirrors, so losing one disk loses the entire mirrored stripe and degrades the array to RAID 0 (making RAID 10 more reliable than RAID 01).

### Q46 (Ch.03 Server Architecture Overview) — [10 pts]
- **Question:** On a Linux operating system, `/media` is used as a temporary manual mount point by administrators, whereas `/mnt` is where removable USB flash drives are automatically mounted by the system.
- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.03 p.219, `/media` is where removable devices (USB drives, CD-ROMs) are automatically identified and mounted by Linux, while `/mnt` is the temporary mount point for manual mounting.

### Q47 (Ch.04 Huawei Computing Industry) — [10 pts]
- **Question:** On the rear panel of a TaiShan 200 (model 2280) server, I/O modules 1, 2, and 3 can all be interchangeably configured with the exact same 3.5-inch drive module or riser module.
- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.04 p.249, I/O modules 1 and 2 on the rear panel can be configured with the same drive module or riser module, while I/O module 3 cannot.

### Q48 (Ch.05 Computing Product Deployment) — [10 pts]
- **Question:** If a RAID controller card does not support the JBOD (drive passthrough) feature, an operating system can only be installed on virtual drives (RAID volumes) configured under the controller card.
- **Correct Answer:** `A`
- **Explanation:** True. According to Ch.05 p.321, if the controller card does not support the passthrough (JBOD) feature, you can install the OS only on the virtual drives configured under the controller card.

### Q49 (Ch.06 Basic O&M of Computing Products) — [10 pts]
- **Question:** As computing O&M software evolves toward intelligence, enterprises can skip the tool-based and automated phases and jump directly from manual configuration to intelligent O&M.
- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.06 p.355 ('Does this imply that intelligence is our ultimate aim and that the tool-based and automated phases can be skipped? The answer is obviously not.'), single-node interfaces, batch tools, and automated centralized management are all essential foundations.

### Q50 (Ch.06 Basic O&M of Computing Products) — [10 pts]
- **Question:** In Huawei FusionDirector, backup Server Profiles exported from one FusionDirector instance can be freely imported into a different or reinstalled FusionDirector instance.
- **Correct Answer:** `B`
- **Explanation:** False. According to Ch.06 p.383, profile import/export cannot be performed on a different FusionDirector or a reinstalled FusionDirector.

### Q51 (Ch.02 Computing System Overview) — [20 pts]
- **Question:** Lab 1 (FusionCompute Cluster Disk Sizing): Complete the configuration snippet specifying the minimum required system drive capacities (in GB) for a FusionCompute VRM node and a CNA compute node.
- **Correct Answer:** `vrm_system_drive_min_gb: 270
cna_compute_drive_min_gb: 150`
- **Explanation:** According to Ch.02 p.115, the system drive on the VRM node must be >= 270 GB, and the system drive on each compute node must be >= 150 GB.

### Q52 (Ch.03 Server Architecture Overview) — [20 pts]
- **Question:** Lab 2 (Kunpeng Mainboard & BMC Chip Identification): Specify the official Kunpeng server mainboard model illustrated in Ch.03 and its onboard Huawei intelligent management chip model.
- **Correct Answer:** `MAINBOARD_MODEL="S920X00"
MANAGEMENT_CHIP="Hi1710"`
- **Explanation:** According to Ch.03 p.149, the Kunpeng server mainboard model is S920X00, equipped with two Kunpeng 920 processors and the Hi1710 intelligent management chip.

### Q53 (Ch.03 Server Architecture Overview) — [20 pts]
- **Question:** Lab 3 (RAID 6 Galois Parity & Utilization): For an 8-disk RAID 6 array (N=8), write the number of parity disks and the drive space utilization percentage.
- **Correct Answer:** `raid6_parity_disks: 2
raid6_utilization_8disks: "75%"`
- **Explanation:** RAID 6 uses 2 independent parity blocks (P and Q) with utilization (N-2)/N = 6/8 = 75% (Ch.03, pp. 161, 163).

### Q54 (Ch.03 Server Architecture Overview) — [20 pts]
- **Question:** Lab 4 (iBMC Black Box Diagnostic Tools): Specify the name of the iBMC black box feature and its companion parsing tool from Ch.03 p. 202.
- **Correct Answer:** `ibmc_black_box: "Kbox"
ibmc_parsing_tool: "HWKbox"`
- **Explanation:** According to Ch.03 p.202, iBMC diagnosis assistance provides the Black box (`Kbox`) and Parsing tool (`HWKbox`).

### Q55 (Ch.04 Huawei Computing Industry) — [20 pts]
- **Question:** Lab 5 (Kunpeng 920 Die & Interconnect Specs): Specify the number of CPU dies, number of I/O dies, and HCCS inter-chip bandwidth (in Gbit/s) for the Kunpeng 920 processor.
- **Correct Answer:** `kunpeng920_cpu_dies = 2
kunpeng920_io_dies = 1
hccs_bandwidth_gbps = 480`
- **Explanation:** According to Ch.04 pp. 234 and 237, Kunpeng 920 encapsulates 2 CPU dies + 1 I/O die (3 dies total) and interconnects via the HCCS bus at up to 480 Gbit/s.

### Q56 (Ch.04 Huawei Computing Industry) — [20 pts]
- **Question:** Lab 6 (openEuler & openGauss Core Technologies): Specify openEuler's AI-driven tuning system, openEuler's C/C++ lightweight container engine, and openGauss's open-source license.
- **Correct Answer:** `openeuler_ai_tuner: "A-Tune"
openeuler_container_engine: "iSulad"
opengauss_license: "Mulan PSL v2"`
- **Explanation:** According to Ch.04 pp. 261, 262, and 266, openEuler features A-Tune and iSulad, and openGauss is licensed under the Mulan Permissive Software License v2 (Mulan PSL v2).

### Q57 (Ch.05 Computing Product Deployment) — [20 pts]
- **Question:** Lab 7 (TaiShan 200 2280 Default iBMC Access): Complete the command/config variables with the factory-default iBMC management port IP, default WebUI/CLI username, and default WebUI/CLI password.
- **Correct Answer:** `IBMC_DEFAULT_IP="192.168.2.100"
IBMC_WEB_USER="Administrator"
IBMC_WEB_PASS="Admin@9000"`
- **Explanation:** According to Ch.05 p.297, the default iBMC IP is 192.168.2.100 (mask 255.255.255.0) and the default WebUI/CLI account is Administrator / Admin@9000.

### Q58 (Ch.05 Computing Product Deployment) — [20 pts]
- **Question:** Lab 8 (openGauss Cluster Deployment CLI): Fill in the two openGauss installation utilities: the environment pre-check/initialization utility (run as root) and the database installation utility (run as omm).
- **Correct Answer:** `# Step 1: Initialize installation environment
gs_preinstall -U omm -G dbgrp -X /opt/software/openGauss/cluster_config.xml
# Step 2: Perform database installation
su - omm -c "gs_install -X /opt/software/openGauss/cluster_config.xml"`
- **Explanation:** According to Ch.05 p.345, `gs_preinstall` prepares and initializes the installation environment, and `gs_install` performs the openGauss installation.

### Q59 (Ch.06 Basic O&M of Computing Products) — [20 pts]
- **Question:** Lab 9 (iBMA BOB CLI & Online Update Platform): Specify the CLI command used to start/stop/restart the BOB forwarding service and the 4-letter acronym for the Huawei Online Update Platform.
- **Correct Answer:** `BOB_CLI_TOOL="bobCmd"
ONLINE_UPDATE_REPO="HOUP"`
- **Explanation:** According to Ch.06 pp. 361 and 391, BOB provides the `bobCmd` CLI to manage BOB forwarding services, and HOUP is the Huawei Online Update Platform.

### Q60 (Ch.06 Basic O&M of Computing Products) — [20 pts]
- **Question:** Lab 10 (SmartKit Burn-In Test & eService Automatic Fault Reporting): Specify the burn-in stress test ISO mounted on V3 servers, the burn-in engine used on TaiShan 200/V5 servers, and the eService automatic alarm-to-ticket feature.
- **Correct Answer:** `v3_burn_in_image: "FTK.iso"
ts200_burn_in_engine: "Smart Provisioning"
eservice_auto_ticket_feature: "Call Home"`
- **Explanation:** According to Ch.06 pp. 429 and 437, SmartKit Burn-in Test mounts `FTK.iso` on V3 servers and uses `Smart Provisioning` on V5/TaiShan 200 servers; eService uses `Call Home` to automatically report alarms to Huawei support and create trouble tickets.
