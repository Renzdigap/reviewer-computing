# Huawei ICT Competition (Computing Track) — National Stage Study Reviewer

Welcome to your **Active Learning & Exam-Ready Study Reviewer** for the **Huawei ICT Competition National Stage (Computing Track)**, built directly from the 3 official Huawei training materials in `C:\Users\RoG\Desktop\huawei`:

1. **[`01-HCIA-Computing-V3.0`](./01-HCIA-Computing-V3.0/index.html)** — *Kunpeng Computing Industry, Server Architecture, Hardware/RAID/BIOS/iBMC Deployment & Enterprise O&M (iBMA, Smart Provisioning, FusionDirector, eSight, SmartKit, eService)*
2. **[`02-HCIA-openEuler-V2.0`](./02-HCIA-openEuler-V2.0/index.html)** — *openEuler Intelligence, CLI Basics, Vim, Text Processing (`grep`/`sed`/`awk`), Users/Permissions/ACLs, RPM/DNF/systemd, Processes/Crontab, Disk/LVM/Network (`nmcli`), Shell Scripting & Native Container Engine `iSula`*
3. **[`03-HCIA-openGauss-V2.0`](./03-HCIA-openGauss-V2.0/index.html)** — *Database Fundamentals, openGauss vs PostgreSQL, Installation & O&M Tools (`gs_om`/`gs_guc`/`gs_checkperf`/`gs_dump`), Memory/Thread/Resource Pooling Architecture, Security/WDR/AI4DB, Storage Engines (Row/Column/MOT), Full SQL (DQL/DML/DDL/DCL/Functions) & GaussDB Distributed Architecture*

---

## Quick Launch & Private Local Progress Tracking

- **Interactive Web Platform via Local Server (Recommended for permanent disk storage on your PC):**
  ```powershell
  py run_reviewer.py
  # Select [0] to launch the local web server and open the master dashboard in your browser
  ```
  - **Fixed Port**: Default `http://127.0.0.1:8080` (retains browser origin across computer restarts).
  - **File-Backed Local Persistence**: Automatically persists your progress in real time to your local `progress.json` file.
  - **Strictly Private & Local (Team-Friendly)**: `progress.json` is completely ignored by Git (`.gitignore`). When teammates clone or pull this repository, they get a fresh, clean reviewer and their progress stays 100% private on their own machine without clashing with yours.
  - **Export / Import Backup (.json)**: One-click download and upload buttons on the dashboard for making personal backups or migrating your progress between your own personal computers (e.g. PC to laptop).

- **Direct Offline Browser Launch:** Double-click **[`index.html`](./index.html)** (or open any Pillar's `index.html`). Works 100% offline with zero external dependencies, saving to `localStorage`.
- **Interactive Terminal / CLI Mode:** Run `py run_reviewer.py` and select `[1]`, `[2]`, or `[3]`, or run `py practice_cli.py` inside any pillar folder. Directly syncs completed units and mock exam scores with your local `progress.json`.

---

## 3-Day × 9-Hour Daily Lock-In Curriculum Architecture

Each of the 3 Pillars is engineered for an intensive **9-Hour Daily Lock-In Schedule**:
- **Hours 01 – 08 (8 Hours of Bite-Sized Active Lessons):**
  - Each Hour is divided into **4 × 15-Minute Sprints**.
  - Each Sprint strictly alternates between:
    1. **7-Minute Bite-Sized Lecture** (`01-Lecture`, `03-Lecture`, `05-Lecture`, `07-Lecture`): High-yield theory, comparison tables, exact command/SQL syntax, and **National Stage Exam Traps**.
    2. **8-Minute Immediate Hands-On Exercise** (`02-Exercise`, `04-Exercise`, `06-Exercise`, `08-Exercise`): Split-screen interactive terminal/SQL/config workbench with automated step verification (`Ctrl+Enter`) + 3 graded Exam Verification Drill questions.
- **Hour 09 (1 Hour Comprehensive Final Mock Exam):**
  - **60-Minute Timed Final Mock Exam (`Final-Mock-Exam.html`)**: 60 exam-ready questions (1000 points total: 20 Single-Choice, 20 strict Multiple-Choice, 10 True/False, and 10 Practical Command/SQL Lab Scenarios).

---

## Directory Structure Overview
```text
C:\Users\RoG\Desktop\huawei\
├── index.html                                  # Master Study Hub & Global Search Portal
├── README.md                                   # Master 3×9-Hour Study Plan & Sync Guide
├── run_reviewer.py                             # Fixed-Port Web Server & Master CLI Launcher
├── sync_engine.js                              # Real-time background sync engine & JSON export/import
├── progress_manager.py                         # File-backed persistence manager (progress.json) & Git sync
├── progress.json                               # Persistent JSON store for units and mock exam scores
├── 01-HCIA-Computing-V3.0\                     # PILLAR 1: Computing & Kunpeng (9 Hours)
│   ├── index.html                              # Pillar 1 Course Player
│   ├── practice_cli.py                         # Pillar 1 Terminal Trainer (synced with progress.json)
│   ├── README.md                               # Pillar 1 Schedule & Syllabus
│   ├── Hour-01-History-of-Computing-and-Trends\ # 01-Lecture .. 08-Exercise (.md + .html)
│   ├── ... (Hours 02 through 08) ...
│   └── Hour-09-Final-Mock-Exam\                # Final-Mock-Exam.html (60 Qs, 60 Mins)
├── 02-HCIA-openEuler-V2.0\                     # PILLAR 2: openEuler OS (9 Hours)
│   ├── index.html                              # Pillar 2 Course Player
│   ├── practice_cli.py                         # Pillar 2 Terminal Trainer (synced with progress.json)
│   ├── README.md                               # Pillar 2 Schedule & Syllabus
│   ├── Hour-01-OS-for-AI-Era-and-Getting-Started\
│   ├── ... (Hours 02 through 08) ...
│   └── Hour-09-Final-Mock-Exam\                # Final-Mock-Exam.html (60 Qs, 60 Mins)
└── 03-HCIA-openGauss-V2.0\                     # PILLAR 3: openGauss & GaussDB (9 Hours)
    ├── index.html                              # Pillar 3 Course Player
    ├── practice_cli.py                         # Pillar 3 Terminal Trainer (synced with progress.json)
    ├── README.md                               # Pillar 3 Schedule & Syllabus
    ├── Hour-01-openGauss-Overview-and-Database-Fundamentals\
    ├── ... (Hours 02 through 08) ...
    └── Hour-09-Final-Mock-Exam\                # Final-Mock-Exam.html (60 Qs, 60 Mins)
```
