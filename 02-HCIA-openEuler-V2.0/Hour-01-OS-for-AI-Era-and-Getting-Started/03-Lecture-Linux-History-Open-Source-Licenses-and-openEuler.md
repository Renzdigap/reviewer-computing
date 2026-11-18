# Linux History, GNU/FSF, Open Source Licenses & openEuler Community

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 01 — OS for the AI Era & Getting Started with openEuler (Sprint 2 of 4)  
**Format:** Bite-Sized Lecture (7 mins) - Followed immediately by `04-Exercise-openEuler-Releases-and-Licenses-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openEuler V2.0 Training Material.pdf` — Ch.02, pp. 27–37

---

## Learning Objectives
- Trace OS history from Multics (1965) and Unix (1969/1970 by Ken Thompson) to Minix (1987 by Andrew S. Tanenbaum) and Linux (1991 by Linus Torvalds)
- Compare the 4 freedoms of the Free Software Foundation (FSF) and major open source licenses (Mulan, GPL, LGPL, BSD)
- Distinguish openEuler Innovation releases vs. LTS releases, kernel version numbering, and openEuler community portals

---

### 1. From Multics and Unix to GNU/Linux
* **Multics (1965):** Bell Labs, MIT, and GE jointly developed the **Multiplexed Information and Computing Service** time-sharing multitasking system. Bell Labs withdrew in 1969.
* **Unix (1969–1970):** **Ken Thompson** at Bell Labs wrote a lightweight OS to run his game *Space Travel*, named **Unix** (Uniplexed Information and Computing Service). **1970** is defined as the **Unix Epoch**. Commercial Unix derivatives include **IBM AIX**, **HP-UX**, and **Digital Unix**.
* **GNU & FSF (1984):** **Richard Stallman** launched the Free Software Campaign and founded the **Free Software Foundation (FSF)**, creating open-source Unix utilities and the **GPL**. FSF defines **Four Freedoms**:
  1. Freedom to run programs for any purpose.
  2. Freedom to learn and modify the source code.
  3. Freedom to redistribute programs.
  4. Freedom to create derivatives.
* **Minix (1987) & Linux (1991):** Professor **Andrew S. Tanenbaum** (Vrije University, Amsterdam) wrote **Minix** for teaching. On **September 17, 1991**, **Linus Torvalds** released the free Linux OS online; **Linux kernel 1.0** was officially released in **1994**. Because Linux combines the kernel with GNU utilities, its full name is **GNU/Linux** (`Linux distribution = Linux kernel + utility software`).

---

### 2. Comparison of Open Source Licenses
In the openEuler code repository, the **`LICENSES`** directory declares the open source licenses in use (defaulting to **MulanPSL v2** for community projects).

| License | Key Rules & Commercial/Derivative Requirements |
| :--- | :--- |
| **Mulan** | **China's first open source license.** Covers 5 aspects: copyright license, patent license, non-trademark license, distribution restriction, and disclaimer/liability limitation. Grants a permanent, global, free, non-exclusive, irrevocable copyright license. |
| **GPL** | **General Public License.** Strictly contagious ("copyleft"): any software that references a GPL library, modifies GPL code, or derives from GPL code **must also use the GPL** (open source and free of charge, though charging for distribution/support is permitted). |
| **LGPL** | **Lesser GPL.** Designed for class libraries. Allows **commercial software to link to an LGPL library without open-sourcing the commercial code**. However, direct modifications or derivatives of the LGPL library itself must remain LGPL. |
| **BSD** | **Permissive license.** Allows modification and redistribution as open-source or **proprietary/commercial software**, provided 3 conditions are met: (1) retain original BSD license in source distributions, (2) include BSD license/copyright in binary docs, (3) **do not use the original software/author/institution name for marketing**. |

---

### 3. Linux Kernel Numbering & openEuler Releases
* **Linux Kernel Version (`X.Y.Z`, hosted at `kernel.org`):**
  * **1st digit (`X`):** Major release.
  * **2nd digit (`Y`):** In traditional 3-digit numbering, an **even** number indicates a **stable version**, while an **odd** number indicates a **version under development**.
  * **3rd digit (`Z`):** Number of revisions. (Example: openEuler 20.03 LTS uses kernel `4.19.90`).
* **openEuler Release Cadence:**
  * **Innovation Release** (e.g., openEuler 20.09): Released **every half a year (6 months)** for technical innovation.
  * **Long-Term Support (LTS) Release** (e.g., openEuler 20.03 LTS, 22.03 LTS, 24.03 LTS): Stable enterprise release published **every 2 years**.
* **Community Contribution Workflow & Portals:**
  * Workflow: `Join community -> Sign CLA -> Join SIG -> Assign issues -> Prepare dev. env. -> Submit code -> Review code`.
  * Key Portals: Official website (`www.openeuler.org`), Code hosting (`gitee.com/openeuler`), Docs (`docs.openeuler.org`), Forum (`forum.openeuler.org`), Issue tracker (`quickissue.openeuler.org`).

---

## Key Takeaways
- **Mulan is China's first open source license covering 5 aspects (copyright, patent, non-trademark, distribution restriction, disclaimer). openEuler declares its licenses in the LICENSES directory.**
- **LGPL permits commercial software to link to LGPL libraries without open-sourcing the commercial code, whereas GPL requires any software referencing/modifying GPL code to also be GPL.**
- **openEuler Innovation releases are published every 6 months (half a year); openEuler LTS (Long-Term Support) releases are published every 2 years.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Do not confuse Innovation vs. LTS release cycles! Innovation = every half a year (6 months); LTS = every 2 years.

> [!WARNING]
> EXAM TRAP: In the traditional 3-digit Linux kernel version scheme taught in Ch.02 (p.33), an EVEN second digit denotes a stable version, and an ODD second digit denotes a development version.

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`04-Exercise-openEuler-Releases-and-Licenses-Lab.html`](./04-Exercise-openEuler-Releases-and-Licenses-Lab.html)** (or [`04-Exercise-openEuler-Releases-and-Licenses-Lab.md`](./04-Exercise-openEuler-Releases-and-Licenses-Lab.md)) to apply this concept in an interactive lab workbench!
