# Book Plan - Ada: Engineering Robust and Reliable Software

This document provides the high-level pedagogical blueprint for the Ada programming book. The canonical chapter order and part assignments reside in `OUTLINE.yaml`.

## Target Audience
- **Undergraduate Computer Science Majors:** Students learning software engineering principles, concurrent programming, and compiler-enforced safety.
- **Transitional Software Engineers:** Professionals moving into defense, aerospace, rail, or medical device industries where high-integrity systems are mandated.
- **Systems Programmers:** Developers familiar with C, C++, or Rust who wish to master Ada's deterministic concurrency, strong typing, and contract-based programming.

## Guiding Pedagogical Principles
1. **Engineering-First Mindset:** Treat software construction as an engineering discipline. Emphasize correctness, readability, and maintainability over rapid prototyping.
2. **Type-Driven Design:** Introduce Ada's sophisticated type system early. Teach domain modeling using constrained subtypes, ranges, and invariants before advancing to algorithmic logic.
3. **Correctness by Construction:** Integrate Ada 2012 contracts (preconditions and postconditions) as standard practice from the beginning. Lay a natural foundation for formal verification via the SPARK subset later in the text.
4. **Concurrency as a Core Construct:** Unlike languages that rely on external libraries (for example, POSIX pthreads), Ada integrates tasking natively. We will teach tasks, rendezvous, and protected objects as fundamental building blocks, culminating in real-time profiles (Ravenscar/Jorvik).
5. **Modern Ecosystem:** Dispel the "legacy language" myth by heavily utilizing modern build orchestrators (GPRbuild), package managers (Alire), and Ada 2022 features (parallel blocks).

## Structural Overview (40 Chapters)
- **Part I: Foundations of the Ada Language:** History, philosophy, toolchain orchestration, lexical elements, and fundamental scalar types.
- **Part II: Data Structures and Memory Management:** Composite types (arrays, records), discriminants, access types, memory pools, and the `Ada.Containers` library.
- **Part III: Modularity and Object-Oriented Programming:** Packages, hierarchical libraries, generics, tagged types, dynamic dispatch, and controlled types (RAII).
- **Part IV: Concurrency and Tasking:** Native tasking, synchronization, protected objects, and real-time scheduling theory.
- **Part V: Design by Contract and Formal Verification:** Exception policies, aspect specifications, and proving the Absence of Run-Time Errors (AoRTE) using SPARK.
- **Part VI: Systems Programming and Interfacing:** Representation clauses, bit-level memory layouts, hardware interfacing, and seamless C interoperability.
- **Part VII: Ecosystem, Advanced Features, and Capstone:** Ada 2022 parallelism, distributed systems (Annex E), unit testing frameworks (AUnit), and a culminating high-integrity Capstone project.
