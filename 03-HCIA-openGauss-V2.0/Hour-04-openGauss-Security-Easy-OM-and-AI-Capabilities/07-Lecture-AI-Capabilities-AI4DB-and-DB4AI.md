# 📖 AI Capabilities — AI4DB (`X-Tuner`, `SQLdiag`, `Index-advisor`) & DB4AI (`DeepSQL`, Native DB4AI)

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 04 — openGauss High Security, Easy O&M & AI Capabilities (DBMind) (Sprint 4 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `08-Exercise-Index-Advisor-Virtual-Index-and-DB4AI-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.03, pp. 243–267

---

## 🎯 Learning Objectives
- Distinguish the two sub-pillars of DBMind: AI4DB (X-Tuner, SQLdiag, Index-advisor, Anomaly-detection) and DB4AI (DeepSQL, Native DB4AI)
- Operate X-Tuner (`recommend`, `train`, `tune`), SQLdiag (`train`, `predict`), and Index-advisor (`gs_index_advise`, `hypopg_create_index`, `index_advisor_workload.py`)
- Describe DeepSQL (60+ ML/graph algorithms) and Native DB4AI (`CREATE MODEL`, `PREDICT BY`)

---

### 1. openGauss AI Architecture (`DBMind`: `AI4DB` + `DB4AI`, p. 244)
- **AI4DB (AI for Database)**: Uses AI to make the database self-tuning, self-diagnosing, self-healing, and self-securing. Includes **`X-Tuner`**, **`SQLdiag`**, **`Index-advisor`**, and **`Anomaly-detection`**.
- **DB4AI (Database for AI)**: Runs machine learning and deep learning directly inside the database engine using SQL-like syntax without moving data across platforms. Includes **`DeepSQL`** and the **`Native DB4AI Engine`**.

---

### 2. AI4DB Tools: `X-Tuner`, `SQLdiag` & `Index-advisor` (pp. 245–263)

#### A. `X-Tuner` (Knob Parameter Tuning Tool, pp. 245–249)
- Uses **Deep Reinforcement Learning (DRL, e.g., DDPG)** and **Global Search Algorithms (Bayesian optimization, Particle Swarm Optimization / PSO)**. Can be run from source (`python main.py`) or installed via `python setup.py install` (`gs_xtuner`).
- **3 Running Modes (p. 247)**:
  1. **`recommend`**: Inspects current workload features and generates a parameter recommendation report **in seconds without restarting the database**.
  2. **`train`**: Iteratively modifies knobs and runs benchmarks to train a DRL model (may restart DB repeatedly).
  3. **`tune`**: Tunes parameters using either a trained DRL model (requires `train` first with identical knob list/min/max) or a Global Search algorithm (no pre-training required).

#### B. `SQLdiag` (SQL Execution Time Prediction, pp. 250–253)
- Predicts execution duration of unknown SQL queries using **SQL vectorization and template-based similarity** against historical execution logs **without collecting execution plans** (zero impact on DB performance; works for both OLTP and OLAP!).
- Requires GUC `log_statement = all` and `log_statement_stats = on`.
- Usage: `python main.py -m train -f data/train.csv` and `python main.py -m predict -f data/predict.csv`.

#### C. `Index-advisor` (3 Index Recommendation Functions, pp. 254–263)
1. **Single-Query Index Recommendation**:
   ```sql
   SELECT * FROM gs_index_advise('SELECT name, age, sex FROM t1 WHERE age >= 18 AND age < 35 AND sex = ''f'';');
   -- Supports ONLY a single SELECT statement on standard row-store tables!
   ```
2. **Virtual (Hypothetical) Index Recommendation**:
   - Simulates an index in the optimizer without physical creation time/space overhead:
   ```sql
   SELECT * FROM hypopg_create_index('CREATE INDEX ON bmsql_customer(c_w_id)');
   SET enable_hypo_index = on;               -- Default is off!
   EXPLAIN SELECT c_discount FROM bmsql_customer WHERE c_w_id = 10;
   -- Companion functions: hypopg_display_index(), hypopg_drop_index(oid), hypopg_reset_index(), hypopg_estimate_size(oid)
   ```
3. **Workload-Level Index Recommendation**:
   ```bash
   python index_advisor_workload.py 6001 postgres tpcc_log.txt --max_index_num 10 --multi_iter_mode
   ```

---

### 3. DB4AI: `DeepSQL` & Native DB4AI Engine (pp. 264–267)
- **`DeepSQL`**: Encapsulates **60+ machine learning & graph algorithms** (Linear/Logistic Regression, Random Forest, KNN, K-Means, PCA, shortest path, graph diameter, Pearson correlation) into SQL statements (requires Python 2.7.12+ and `PL/Python`).
- **Native DB4AI Engine**: Integrates native AI operators and execution planning directly into the openGauss kernel with SQL-like syntax (**`CREATE MODEL ...`** and **`PREDICT BY ...`**), eliminating external Python/platform data transfers.

---

## 🔑 Key Takeaways
- **X-Tuner runs in 3 modes: `recommend` (completes in seconds without DB restart), `train` (trains DRL model), and `tune` (uses DRL or global search algorithms).**
- **SQLdiag predicts SQL execution time from historical logs using SQL vectorization and templates WITHOUT needing SQL execution plans.**
- **Index-advisor provides 3 levels: `gs_index_advise('SELECT ...')` (single query), `hypopg_create_index(...)` with `SET enable_hypo_index = on` (virtual index), and `index_advisor_workload.py` (workload-level).**

## ⚠️ Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: After creating a virtual index with `hypopg_create_index()`, the optimizer will NOT use it in `EXPLAIN` unless you set `SET enable_hypo_index = on;` (default is `off`, Ch.03 p. 258)!

> [!WARNING]
> EXAM TRAP: `gs_index_advise()` supports ONLY a single `SELECT` statement and does NOT support column-store tables, views, materialized views, global temp tables, or encrypted databases (Ch.03 p. 255).

---

### 🚀 Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`08-Exercise-Index-Advisor-Virtual-Index-and-DB4AI-Lab.html`](./08-Exercise-Index-Advisor-Virtual-Index-and-DB4AI-Lab.html)** (or [`08-Exercise-Index-Advisor-Virtual-Index-and-DB4AI-Lab.md`](./08-Exercise-Index-Advisor-Virtual-Index-and-DB4AI-Lab.md)) to apply this concept in an interactive lab workbench!
