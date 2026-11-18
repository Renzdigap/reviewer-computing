# Hands-On Lab: Running, Exec-ing, Inspecting & Forcibly Removing `iSula` Containers

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 08 — openEuler Native Container Engine iSula (iSulad) (Sprint 2 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `03-Lecture-iSula-Installation-Config-and-Container-Lifecycle`  
**Interactive Workbench:** Open **[`04-Exercise-iSula-Container-Lifecycle-Lab.html`](./04-Exercise-iSula-Container-Lifecycle-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are deploying an `nginx` web container using `iSula` on openEuler (following Ch.07 pp. 408–417). Start a background container named `test` mapping host port `8081` to container port `80` with environment variable `A=100`, execute `/bin/bash` inside `test` using `isula exec -it`, list the latest 2 containers, and forcibly delete container `test`.

### Step-by-Step Instructions
1. Step 1: Run `nginx` in the background (`-d`) named `test` (`--name test`) with port mapping `-p 8081:80` and environment variable `-e A=100` (`isula run -d --name test -p 8081:80 -e A=100 nginx`).
2. Step 2: Execute an interactive shell in container `test` using `isula exec -it test /bin/bash` and list the latest 2 containers using `isula ps -n 2`.
3. Step 3: Forcibly remove the running container `test` using `isula rm -f test`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Run nginx in background named 'test' with -p 8081:80 and -e A=100
<isula_run_command>

# Step 2: Run interactive /bin/bash via isula exec and list latest 2 containers
<isula_exec_command>
<isula_ps_n2_command>

# Step 3: Forcibly remove running container 'test'
<isula_rm_force_command>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `isula run -d --name test -p 8081:80 -e A=100 nginx`.
- Use `isula exec -it test /bin/bash` and `isula ps -n 2` (Ch.07 pp.412–413).
- Use `isula rm -f test` (Ch.07 p.417).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Run nginx in background named 'test' with -p 8081:80 and -e A=100
isula run -d --name test -p 8081:80 -e A=100 nginx

# Step 2: Run interactive /bin/bash via isula exec and list latest 2 containers
isula exec -it test /bin/bash
isula ps -n 2

# Step 3: Forcibly remove running container 'test'
isula rm -f test
```

#### Expected Console / Query Output:
```text
d306049a6b6af9697a1dab8df72f288137b76a99107e7e26ce8dc4b9ad31e219
root@d306049a6b6a:/# echo $A
100
CONTAINER ID    IMAGE                           COMMAND                  CREATED         STATUS    PORTS                  NAMES
d306049a6b6a    docker.io/library/nginx:latest  "/docker-entrypoint.…"   5 seconds ago   Up        0.0.0.0:8081->80/tcp   test
test
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Multiple-Choice (Select ALL)]
**[Official Ch.07 Quiz Q1] Which of the following are container states?**

- A. Created
- B. Exited
- C. Up
- D. Paused

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Official Ch.07 Quiz Q1 (p.439): ABCD. All four—`Created`, `Exited`, `Up`, and `Paused`—are valid container states in iSula.
</details>

### Question 2 [Single-Choice]
**What is the configuration priority order (from highest to lowest) for the `iSulad` daemon in openEuler?**

- A. Default code configurations > `/etc/isulad/daemon.json` > CLI
- B. `/etc/isulad/daemon.json` > CLI > Default code configurations
- C. CLI (`isulad --xxx`) > Configuration file (`/etc/isulad/daemon.json`) > Default configurations in code
- D. `/etc/fstab` > `/etc/bashrc` > CLI

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `C`
- **Explanation:** Per Ch.07 (p.401), `iSulad` configuration priority from highest to lowest is: CLI > configuration file (`/etc/isulad/daemon.json`) > default configurations in code.
</details>

### Question 3 [Single-Choice]
**When creating a container with `isula run`, which `--restart` policy is used by default if `--restart` is not specified, and which policy restarts a container always EXCEPT when it was already stopped before the `iSulad` daemon started?**

- A. Default: `always`; Exception policy: `on-failure`
- B. Default: `no`; Exception policy: `unless-stopped`
- C. Default: `on-failure`; Exception policy: `no`
- D. Default: `unless-stopped`; Exception policy: `always`

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.07 (p.416), `no` (do not restart when exited) is used by default, and `unless-stopped` always restarts the container when it exits except for containers that were already stopped when the `iSulad` daemon started.
</details>
