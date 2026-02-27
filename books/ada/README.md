# Ada: Engineering Robust and Reliable Software

This directory contains the source-of-truth manuscript and outline for the Ada programming book.

- `OUTLINE.yaml` serves as the canonical map for parts and chapters.
- `chapters/` contains the raw Markdown content for each chapter.

## Table of Contents

### Part I - Foundations of the Ada Language
History, philosophy, toolchain orchestration, syntax, and fundamental scalar types.
- **01.** 1. An Extensive Introduction to Ada
- **02.** 2. Toolchain, Project Layout, and Coding Conventions
- **03.** 3. Language Fundamentals and Lexical Elements
- **04.** 4. Scalar Data Types and Declarations
- **05.** 5. Control Flow and Statements
- **06.** 6. Subprograms: Procedures and Functions

### Part II - Data Structures and Memory Management
Composite types, dynamic memory, safe pointers, and string handling.
- **07.** 7. Composite Types: Arrays and Strings
- **08.** 8. Composite Types: Records and Discriminants
- **09.** 9. Access Types and Safe Pointers
- **10.** 10. Dynamic Memory Management and Storage Pools
- **11.** 11. The Ada.Containers Library
- **12.** 12. Advanced String and Text Handling

### Part III - Modularity and Object-Oriented Programming
Packages, generics, tagged types, interfaces, and dispatching.
- **13.** 13. Packages and Visibility Control
- **14.** 14. Generics and Parametric Polymorphism
- **15.** 15. Object-Oriented Programming: Tagged Types
- **16.** 16. Polymorphism and Dynamic Dispatch
- **17.** 17. Interfaces and Multiple Inheritance
- **18.** 18. Controlled Types and Resource Management

### Part IV - Concurrency and Tasking
Native tasking, rendezvous, protected objects, and the Ravenscar profile.
- **19.** 19. Introduction to Concurrent Programming
- **20.** 20. Task Lifecycle and Simple Synchronization
- **21.** 21. Safe Concurrency with Protected Objects
- **22.** 22. Advanced Tasking and Rendezvous
- **23.** 23. Real-Time Systems and Scheduling
- **24.** 24. The Ravenscar and Jorvik Profiles

### Part V - Design by Contract and Formal Verification
Exceptions, pre/postconditions, type invariants, and the SPARK subset.
- **25.** 25. Exceptions and Predictable Failure Handling
- **26.** 26. Programming by Contract: Pre- and Postconditions
- **27.** 27. Type Invariants and Subtype Predicates
- **28.** 28. Introduction to Formal Verification with SPARK
- **29.** 29. Proving Absence of Run-Time Errors (AoRTE)
- **30.** 30. Advanced SPARK: Ghost Code and Loop Invariants

### Part VI - Systems Programming and Interfacing
Representation clauses, hardware interfacing, C interoperability, and low-level control.
- **31.** 31. Representation Clauses and Data Layout
- **32.** 32. Low-Level Programming and System Attributes
- **33.** 33. Interfacing with C and Other Languages
- **34.** 34. Interrupt Handling and Hardware Interaction
- **35.** 35. Ada.Numerics and Scientific Computing
- **36.** 36. Working with the Operating System and Files

### Part VII - Ecosystem, Advanced Features, and Capstone
Ada 2022 features, parallel constructs, the Alire ecosystem, and a capstone project.
- **37.** 37. Advanced Language Features (Ada 2022 Parallelism)
- **38.** 38. Distributed Systems (Annex E)
- **39.** 39. Testing, QA, and CI/CD for Ada
- **40.** 40. Capstone Project: A High-Integrity Telemetry System
