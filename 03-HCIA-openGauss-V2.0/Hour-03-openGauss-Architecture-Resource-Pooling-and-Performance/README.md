# Hour 03: openGauss Architecture, Resource Pooling & High Performance
**Pillar:** HCIA-openGauss V2.0 (Enterprise Relational Database & GaussDB)  
**Official Material Reference:** Chapter 03 Part 1 (pp. 131–198)  
**Pacing:** 60 Minutes (4 × 15-Minute Active Learning Sprints)

Explore the internal memory, multi-threading, and directory architecture of openGauss, master the 3-layer Resource Pooling architecture (DMS + DSS), compare CBO vs. ABO optimizers and Row-Store vs. Column-Store tables, and configure Partitioned Tables, Kunpeng NUMA optimizations, SMP intra-query parallelism, Primary/Standby Switchover/Failover, and Ultimate RTO.

---

## Strict Alternating Lecture & Exercise Sequence

| Order | Type | Duration | Interactive HTML | Study Sheet (.md) |
| :--- | :--- | :--- | :--- | :--- |
| **01** | Lecture | 7 mins | **[`01-Lecture-Instance-Memory-Threads-and-Directory-Layout.html`](./01-Lecture-Instance-Memory-Threads-and-Directory-Layout.html)** | [`01-Lecture-Instance-Memory-Threads-and-Directory-Layout.md`](./01-Lecture-Instance-Memory-Threads-and-Directory-Layout.md) |
| **02** | Exercise | 8 mins | **[`02-Exercise-Memory-Threads-and-Data-Directory-Lab.html`](./02-Exercise-Memory-Threads-and-Data-Directory-Lab.html)** | [`02-Exercise-Memory-Threads-and-Data-Directory-Lab.md`](./02-Exercise-Memory-Threads-and-Data-Directory-Lab.md) |
| **03** | Lecture | 7 mins | **[`03-Lecture-Resource-Pooling-Architecture-DMS-and-DSS.html`](./03-Lecture-Resource-Pooling-Architecture-DMS-and-DSS.html)** | [`03-Lecture-Resource-Pooling-Architecture-DMS-and-DSS.md`](./03-Lecture-Resource-Pooling-Architecture-DMS-and-DSS.md) |
| **04** | Exercise | 8 mins | **[`04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab.html`](./04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab.html)** | [`04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab.md`](./04-Exercise-Resource-Pooling-DMS-DSS-Architecture-Lab.md) |
| **05** | Lecture | 7 mins | **[`05-Lecture-Optimizers-CBO-ABO-Statistics-and-Row-vs-Column-Store.html`](./05-Lecture-Optimizers-CBO-ABO-Statistics-and-Row-vs-Column-Store.html)** | [`05-Lecture-Optimizers-CBO-ABO-Statistics-and-Row-vs-Column-Store.md`](./05-Lecture-Optimizers-CBO-ABO-Statistics-and-Row-vs-Column-Store.md) |
| **06** | Exercise | 8 mins | **[`06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab.html`](./06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab.html)** | [`06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab.md`](./06-Exercise-ANALYZE-Statistics-and-Column-Store-Lab.md) |
| **07** | Lecture | 7 mins | **[`07-Lecture-Partitioning-Kunpeng-NUMA-SMP-and-HA-Ultimate-RTO.html`](./07-Lecture-Partitioning-Kunpeng-NUMA-SMP-and-HA-Ultimate-RTO.html)** | [`07-Lecture-Partitioning-Kunpeng-NUMA-SMP-and-HA-Ultimate-RTO.md`](./07-Lecture-Partitioning-Kunpeng-NUMA-SMP-and-HA-Ultimate-RTO.md) |
| **08** | Exercise | 8 mins | **[`08-Exercise-Partitioning-SMP-Switchover-and-RTO-Lab.html`](./08-Exercise-Partitioning-SMP-Switchover-and-RTO-Lab.html)** | [`08-Exercise-Partitioning-SMP-Switchover-and-RTO-Lab.md`](./08-Exercise-Partitioning-SMP-Switchover-and-RTO-Lab.md) |