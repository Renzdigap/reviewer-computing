# Hands-On Lab: Pulling, Tagging, Inspecting & Removing Images with `isula`

**Pillar:** HCIA-openEuler V2.0 (Operating System & Cloud-Native iSula)  
**Schedule Block:** Hour 08 — openEuler Native Container Engine iSula (iSulad) (Sprint 4 of 4)  
**Format:** Immediate Hands-On Exercise (8 mins) — Paired with `07-Lecture-Container-Image-Architecture-and-Management`  
**Interactive Workbench:** Open **[`08-Exercise-iSula-Image-Pull-Tag-Inspect-Rmi-Lab.html`](./08-Exercise-iSula-Image-Pull-Tag-Inspect-Rmi-Lab.html)** or **[`../index.html`](../index.html)** for live execution & auto-grading!

---

## Part A: Practical Lab Scenario
You are managing container images on an openEuler host (following Ch.07 pp. 435–438). Pull `openeuler/busybox:latest`, re-tag it as `busybox:test`, list all local images to verify they share the same `IMAGE ID`, and then remove the `busybox:test` tag using `isula rmi`.

### Step-by-Step Instructions
1. Step 1: Pull the `openeuler/busybox:latest` image using `isula pull openeuler/busybox:latest`.
2. Step 2: Tag `openeuler/busybox:latest` as `busybox:test` using `isula tag openeuler/busybox:latest busybox:test` and list local images with `isula images`.
3. Step 3: Delete the `busybox:test` image reference using `isula rmi busybox:test`.

### Starter Workspace (`root@openEuler:~#`)
```bash
# Step 1: Pull openeuler/busybox:latest from registry
<isula_pull_command>

# Step 2: Tag openeuler/busybox:latest as busybox:test and list images
<isula_tag_command>
<isula_images_command>

# Step 3: Remove the busybox:test image
<isula_rmi_command>
```

<details>
<summary><strong>Click to View Hints</strong></summary>

- Use `isula pull openeuler/busybox:latest` (Ch.07 p.436).
- Use `isula tag openeuler/busybox:latest busybox:test` and `isula images` (Ch.07 p.437).
- Use `isula rmi busybox:test` (Ch.07 p.438).

</details>

<details>
<summary><strong>Click to Reveal Full Working Solution & Expected Output</strong></summary>

#### Solution Code / Commands:
```bash
# Step 1: Pull openeuler/busybox:latest from registry
isula pull openeuler/busybox:latest

# Step 2: Tag openeuler/busybox:latest as busybox:test and list images
isula tag openeuler/busybox:latest busybox:test
isula images

# Step 3: Remove the busybox:test image
isula rmi busybox:test
```

#### Expected Console / Query Output:
```text
Image "openeuler/busybox:latest" pulled

REPOSITORY          TAG      IMAGE ID       CREATED               SIZE
busybox             test     81968c526c7a   2026-05-21 17:17:32   517.291MB
openeuler/busybox   latest   81968c526c7a   2026-05-21 17:17:32   517.291MB

Image "busybox:test" removed
```
</details>

---

## Part B: National Stage Exam Verification Drill

### Question 1 [Single-Choice]
**What is the maximum number of layers a container image can have, and what Happens when a file inside a read-only image layer (`lowerdir`) is deleted inside a running container?**

- A. Max 32 layers; the file is physically erased from `lowerdir` on the host disk
- B. Max 128 layers; UnionFS (AUFS/OverlayFS) creates a `whiteout` file in the R/W container layer (`upperdir`) to hide the deleted file
- C. Max 1024 layers; the host kernel is recompiled
- D. Max 4 layers; the container immediately crashes

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 1)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.07 (p.428 & p.430–433), an image is immutable and cannot exceed 128 layers. When a file is deleted in a container, UnionFS creates a whiteout file at the R/W container layer (`upperdir`) to block/hide the file without altering the read-only image layer.
</details>

### Question 2 [Single-Choice]
**Which four directories are used by `OverlayFS` to construct a union file system, and which one is invisible to users?**

- A. `bootfs`, `rootfs`, `procfs`, `sysfs` (`procfs` is invisible)
- B. `lowerdir`, `upperdir`, `merged`, `workdir` (`workdir` is invisible to users)
- C. `diff`, `mnt`, `layers`, `tmp` (`mnt` is invisible)
- D. `bin`, `sbin`, `usr`, `var` (`var` is invisible)

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 2)</strong></summary>

- **Correct Answer:** `B`
- **Explanation:** Per Ch.07 (p.433), OverlayFS is constructed and implemented using the `lowerdir`, `upperdir`, `merged`, and `workdir` directories, where `workdir` is invisible to users.
</details>

### Question 3 [Multiple-Choice (Select ALL)]
**Which of the following statements about container image naming and `isula` image commands are TRUE?**

- A. In `[registry/][path/]<imagename>[:tag]`, if `:tag` is not specified, `latest` is used by default.
- B. `isula` supports the `isula pull` command to download images, and does NOT support the `push` command.
- C. `isula tag openeuler/busybox:latest busybox:test` modifies/adds image tag information.
- D. `isula rmi <image>` deletes an image on the host.

<details>
<summary>[PASS] <strong>Check Answer & Explanation (Question 3)</strong></summary>

- **Correct Answer:** `ABCD`
- **Explanation:** Per Ch.07 (pp.434–438), all four statements are explicitly documented in the official Huawei training material.
</details>
