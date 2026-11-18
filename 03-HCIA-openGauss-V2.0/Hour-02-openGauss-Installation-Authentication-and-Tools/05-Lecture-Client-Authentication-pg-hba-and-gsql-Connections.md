# Client Authentication (`pg_hba.conf`), `postgresql.conf` & `gsql` Connections

**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Schedule Block:** Hour 02 — openGauss Installation, Authentication & O&M Tools (Sprint 3 of 4)  
**Format:** Bite-Sized Lecture (7 mins) → Followed immediately by `06-Exercise-pg-hba-Auth-and-gsql-Connection-Lab` (8 mins)  
**Official Material Reference:** `HCIA-openGauss V2.0 Training Material.pdf` — Ch.02, pp. 95–100

---

## Learning Objectives
- Configure client authentication policies in `pg_hba.conf` using `gs_guc set` and `gs_guc reload`
- Distinguish `HOSTTYPE` (`local`, `host`, `hostssl`, `hostnossl`) and `AUTHMETHOD` (`sha256`, `md5`, `trust`, `reject`, `cert`, `gss`)
- Inspect node IP and port (`gs_om -t status --detail`, `postgresql.conf`) and connect via `gsql`

---

### 1. Setting Client Authentication Policies in `pg_hba.conf` (p. 96, 118)
By default, parameters in `pg_hba.conf` and `postgresql.conf` are configured for standalone local access. Use **`gs_guc`** (as user `omm`) to modify parameters or host-based authentication policies:
```bash
gs_guc [ set | reload ] [-N NODE-NAME] [-I INSTANCE-NAME | -D DATADIR] \
  -h "HOSTTYPE DATABASE USERNAME IPADDR-WITH-IPMASK AUTHMETHOD [authentication-options]"
```
- **`set` vs. `reload`**:
  - **`set`**: Modifies **only** the parameter in the configuration file (requires restart or reload later).
  - **`reload`**: Modifies the parameter in the configuration file **AND sends semaphores (signals) to the database process** to reload the configuration file immediately without restarting!
  - *Removing a policy*: Omit `AUTHMETHOD`/`authentication-options` in `gs_guc ... -h "..."` to comment out an existing line in `pg_hba.conf`.

| Parameter | Supported Values & Technical Meaning |
| :--- | :--- |
| **`HOSTTYPE`** | **`local`** (Unix domain socket), **`host`** (plain or SSL TCP/IP socket), **`hostssl`** (SSL-encrypted TCP/IP socket only), **`hostnossl`** (non-SSL TCP/IP socket only). |
| **`AUTHMETHOD`** | **`sha256`** (SHA-256 password hash, **recommended**), **`md5`** (MD5 hash, not supported by default), **`trust`** (no password check; **remote hosts are NOT allowed to use `trust`**), **`reject`** (unconditionally reject connection), **`cert`** (SSL client certificate), **`gss`** (Kerberos authentication). |

---

### 2. Confirming Connection Info & Connecting with `gsql` (pp. 97–99)
1. **Query Primary Node IP & Data Directory**:
   ```bash
   gs_om -t status --detail
   ```
2. **Check Port in `postgresql.conf`**:
   ```bash
   cat /srv/BigData/gaussdb/data1/dbnode/postgresql.conf | grep port
   # port = 8000 (or 5432 in simpleInstall)
   ```
3. **Connect Locally or Remotely with `gsql`**:
   ```bash
   gsql -d postgres -p 8000
   # Remote connection: gsql -h 192.168.0.11 -d postgres -p 8000 -U jack -W Bigdata@123
   ```
   - **Prompt Indicator**: Logging in as administrator `omm` displays **`postgres=#`** (`#` = superuser/admin); logging in as a common user displays **`postgres=>`** (`>` = normal user).
   - **Timeouts**:
     - **`session_timeout`**: Automatically disconnects an idle client session (set `session_timeout = 0` to disable idle timeouts).
     - **`gsql` connection timeout**: Fixed at **5 minutes** when establishing a connection and authenticating.
   - **Change Password & Exit**:
     ```sql
     ALTER ROLE omm IDENTIFIED BY 'NewPass@2026' REPLACE 'OldPass@2012';
     \q
     ```

---

## Key Takeaways
- **`gs_guc set` only writes to the config file, whereas `gs_guc reload` writes to the config file AND signals the database process to reload immediately.**
- **In `pg_hba.conf`, `sha256` is the recommended authentication method; `trust` is only allowed for local connections (remote hosts cannot use `trust`).**
- **In `gsql`, `DBNAME=#` indicates an administrator (`omm`) prompt, whereas `DBNAME=>` indicates a common user prompt.**

## Huawei ICT Competition National Stage Exam Traps
> [!WARNING]
> EXAM TRAP: Remote hosts are NOT allowed to access openGauss using `trust` mode in `pg_hba.conf`! Remote connections must use `sha256` (recommended), `cert`, or `gss`.

> [!WARNING]
> EXAM TRAP: System catalogs store structured metadata of openGauss. Never manually add, delete, or modify system catalogs, as doing so causes metadata inconsistency or database unavailability (Ch.02 p. 100).

---

### Next Step: Immediate Hands-On Exercise
Proceed immediately to **[`06-Exercise-pg-hba-Auth-and-gsql-Connection-Lab.html`](./06-Exercise-pg-hba-Auth-and-gsql-Connection-Lab.html)** (or [`06-Exercise-pg-hba-Auth-and-gsql-Connection-Lab.md`](./06-Exercise-pg-hba-Auth-and-gsql-Connection-Lab.md)) to apply this concept in an interactive lab workbench!
