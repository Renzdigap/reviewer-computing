# 📖 System Software: Operating Systems, Middleware & Databases

**Pillar:** HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)  
**Schedule Block:** Hour 02 — Computing System Overview, System Software & Virtualization (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (8 mins) → Followed immediately by `04-Exercise-Database-Models-OLTP-OLAP-and-Sizing-Lab` (7 mins)  
**Official Material Reference:** `HCIA-Computing V3.0 Training Material.pdf` — Ch.02, pp. 84–101

---

## 🎯 Learning Objectives
- Understand OS architecture (System Call Layer + Kernel) and compare Linux vs. Windows Server 2022 Standard and Datacenter editions
- Differentiate JBoss, Tomcat, WebLogic, and WebSphere middleware
- Master DBS components, Hierarchical vs. Network vs. Relational models, OLTP vs. OLAP, and 4-socket Kunpeng openGauss server sizing

---

### 1. Operating Systems: Linux vs. Windows Server 2022 (pp. 85–89)
- **OS Structure**: Consists of the **Kernel** (manages CPU, memory, and drive hardware) and the **System Call Layer** (provides APIs so engineers can develop software without directly accessing/damaging the kernel).
- **Linux**: Open-source OS under **GNU GPL**. Distributions include **openEuler, Red Hat (RHEL), SUSE, and Ubuntu**. Used for **Website servers**, **Key financial/database applications** (openGauss, MySQL, Oracle), and **HPC** (GCC compilation, fluid mechanics).
- **Windows Server**: Offers **LTSC** (Long-Term Servicing Channel, core stability/security) and **AC** (Annual Channel, frequent updates for containers/microservices). Common scenarios: **Domain controller (Active Directory)**, **Remote Desktop Service (RDS)**, and **Network server (DNS, DHCP, network controller)**.
  - **Windows Server 2022 Standard vs. Datacenter (p. 88)**: Datacenter uniquely supports **Software-Defined Networking (SDN)**, **Storage Spaces Direct (S2D)**, **Network Controller**, and **unlimited VMs + 1 Hyper-V host** per license, whereas **Standard permits only 2 VMs + 1 Hyper-V host**.

---

### 2. Middleware & Runtime (pp. 90–91)
Middleware connects system software (OS) and application software across different architectures. **Runtime** refers to the runtime library/environment supporting program execution (e.g., **JRE, C#, Visual Basic .NET**).

| Middleware | License | JEE / EJB Support & Target Scenario |
| :--- | :--- | :--- |
| **JBoss** | Open-source (**LGPL** — free for commercial use) | Complies with **JEE**; supports **EJB 1.1, 2.0, and 3**; SOA enterprise applications. |
| **Tomcat** | Free, open-source (Apache/Sun) | Lightweight web server complying with **Servlet and JSP** specs; **does NOT support EJB**; used in SMEs with low concurrency. |
| **WebLogic / WebSphere** | Closed-source commercial | Full **JEE** middleware with high scalability for large-scale enterprise projects. |

---

### 3. Databases, Data Models, OLTP vs. OLAP & Hardware Sizing (pp. 92–101)
- **Database System (DBS)**: DBS = Database (DB) + DBMS + Database Applications (plus DBA and users). DBMS provides **DDL** (Data Definition Language), **DML** (Data Manipulation Language), operation management (integrity, security, concurrency, fault recovery), and maintenance utilities.
- **Three Classical Database Models (p. 98 — Official Quiz Q2)**:
  - **Hierarchical model** (e.g., IBM **IMS**): Tree structure; **only one root node** has no parent; all other nodes have **only one parent node**.
  - **Network model**: **Allows more than one node to have no parent**, and **a node can have more than one parent**.
  - **Relational model (born 1969)**: Two-dimensional tables (rows/tuples and columns/attributes); relationships must be normalized with indivisible atomic data items.
  *(Exam Note: On Ch.02 p.98, the text explicitly defines **Network model** as allowing >1 node with >1 parent; however, the slide notes on p.124 printed `2. C` as an answer-key typo. Always know both the technical definition of Network model and the official slide text!)*

| Feature | OLTP (On-Line Transaction Processing) | OLAP (On-Line Analytical Processing, Codd 1993) |
| :--- | :--- | :--- |
| **Orientation & Users** | **Transaction** / Clerks, DBAs | **Analysis** / Decision-making personnel |
| **Data & Access** | **Current, detailed** / Read & write (short transactions) | **Historical, consolidated** / Mostly read (complex scans) |
| **Records & Scale** | **Dozens** of records / **100 MB to GB** | **Millions** of records / **100 GB to TB** |
| **Key Bottleneck / Metric** | **Memory efficiency**, TPS, SQL rate, concurrency | **Drive I/O bandwidth**, SQL duration, partitioning |

- **Server Requirements for Databases (p. 101)**: Peak CPU load must **not exceed 85%**. Reference 4-socket Kunpeng openGauss 5.0.0+ configuration on **openEuler 20.03 LTS**: **TaiShan 200 (model 2480)**, **4 × Kunpeng 920 64-core CPUs**, **1 TB RAM**, **Hi1822 NIC (4 × 25GE, latency < 0.1 ms)**, **4 × NVMe SSDs** (V5 sequential write ≥ 2600 MB/s).

---

## 🔑 Key Takeaways
- **Windows Server 2022 Datacenter supports unlimited VMs, SDN, Storage Spaces Direct, and Network Controller; Standard supports only 2 VMs per license.**
- **Tomcat supports Servlet/JSP but does NOT support EJB (use JBoss under LGPL or commercial WebLogic/WebSphere for EJB).**
- **Hierarchical model allows only 1 parent per node; Network model allows a node to have >1 parent and >1 root node.**
- **When selecting a database server CPU, peak CPU load must not exceed 85%.**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP (Ch.02 Quiz Q2): Page 98 explicitly states under 'Network model': 'Allows more than one node to have no parent. A node can have more than one parent.' (Note that p.124 slide notes had a typo listing C; in standard Huawei exams, Network model is the multi-parent graph model).

> [!WARNING]
> EXAM TRAP: Tomcat is lightweight and does NOT support EJB! If an enterprise requires open-source EJB support, choose JBoss (LGPL).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-Database-Models-OLTP-OLAP-and-Sizing-Lab.html`](./04-Exercise-Database-Models-OLTP-OLAP-and-Sizing-Lab.html)** (or [`04-Exercise-Database-Models-OLTP-OLAP-and-Sizing-Lab.md`](./04-Exercise-Database-Models-OLTP-OLAP-and-Sizing-Lab.md)) to apply this concept in an interactive lab workbench!
