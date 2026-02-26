# PowerShell: From Zero to Toolmaker

This folder contains the PowerShell book and its source-of-truth outline.

- `OUTLINE.yaml` is the canonical chapter list and section map.
- `chapters/` contains the actual Markdown chapters.

## Table of contents

### Part I — Foundations

Why PowerShell exists, how to discover commands, basic syntax, flow control, and formatting.

- **01.** [1. Foundations of the Shell and The Monad Manifesto](chapters/01 - 1. Foundations of the Shell and The Monad Manifesto.md) — *stable*
- **02.** [2. The Type System and Variable Scope](chapters/02 - 2. The Type System and Variable Scope.md) — *stable*
- **03.** [3. The Object Pipeline](chapters/03 - 3. The Object Pipeline.md) — *draft*
- **04.** [4. Operators and Expressions](chapters/04 - 4. Operators and Expressions.md) — *draft*
- **05.** [5. Flow Control and Logic](chapters/05 - 5. Flow Control and Logic.md) — *draft*
- **06.** [6. The Formatting System](chapters/06 - 6. The Formatting System.md) — *draft*

### Part II — Data and Platform Integration

Providers, regex/text parsing, structured data formats, management via CIM/WMI, .NET interop, and scripting fundamentals.

- **07.** [7. Providers and Drives](chapters/07 - 7. Providers and Drives.md) — *draft*
- **08.** [8. Regular Expressions and Text Parsing](chapters/08 - 8. Regular Expressions and Text Parsing.md) — *draft*
- **09.** [9. Structured Data Handling](chapters/09 - 9. Structured Data Handling.md) — *draft*
- **10.** [10. CIM and WMI](chapters/10 - 10. CIM and WMI.md) — *draft*
- **11.** [11. .NET Integration and Reflection](chapters/11 - 11. .NET Integration and Reflection.md) — *draft*
- **12.** [12. Scripting Basics](chapters/12 - 12. Scripting Basics.md) — *draft*

### Part III — Toolmaking and Language Power

Advanced functions, pipeline binding, module authoring, and richer object models (custom objects and classes).

- **13.** [13. Advanced Functions: The CmdletBinding Attribute](chapters/13 - 13. Advanced Functions The CmdletBinding Attribute.md) — *draft*
- **14.** [14. Advanced Functions: Pipeline Processing](chapters/14 - 14. Advanced Functions Pipeline Processing.md) — *draft*
- **15.** [15. Module Development - Part 1](chapters/15 - 15. Module Development - Part 1.md) — *draft*
- **16.** [16. Module Development - Part 2](chapters/16 - 16. Module Development - Part 2.md) — *draft*
- **17.** [17. Creating Custom Objects](chapters/17 - 17. Creating Custom Objects.md) — *draft*
- **18.** [18. PowerShell Classes (Class-Based DSL)](chapters/18 - 18. PowerShell Classes (Class-Based DSL).md) — *draft*

### Part IV — Operations and Automation at Scale

Background jobs, multi-threading, remoting, security, debugging, and practical API/reporting workflows.

- **19.** [19. Background Jobs](chapters/19 - 19. Background Jobs.md) — *draft*
- **20.** [20. Multi-threading and Asynchronous Execution](chapters/20 - 20. Multi-threading and Asynchronous Execution.md) — *draft*
- **21.** [21. PowerShell Remoting \- Foundation](chapters/21 - 21. PowerShell Remoting - Foundation.md) — *draft*
- **22.** [22. PowerShell Remoting \- Advanced Configuration](chapters/22 - 22. PowerShell Remoting - Advanced Configuration.md) — *draft*
- **23.** [23. Security and Defensive Coding](chapters/23 - 23. Security and Defensive Coding.md) — *draft*
- **24.** [24. Debugging and Troubleshooting](chapters/24 - 24. Debugging and Troubleshooting.md) — *draft*
- **25.** [25. Regular Expressions \- Applied Workshop](chapters/25 - 25. Regular Expressions - Applied Workshop.md) — *draft*
- **26.** [26. REST API Interaction](chapters/26 - 26. REST API Interaction.md) — *draft*
- **27.** [27. HTML Reporting and Dashboards](chapters/27 - 27. HTML Reporting and Dashboards.md) — *draft*
- **28.** [28. Controller Scripts and Toolmaking Architecture](chapters/28 - 28. Controller Scripts and Toolmaking Architecture.md) — *draft*

### Part V — Configuration, Testing, and Enterprise Automation

DSC, Pester, CI/CD, and common enterprise automation domains (SQL, AD, cloud, GUI, perf).

- **29.** [29. Desired State Configuration (DSC) - Foundations](chapters/29 - 29. Desired State Configuration (DSC) - Foundations.md) — *draft*
- **30.** [30. Desired State Configuration (DSC) - Advanced](chapters/30 - 30. Desired State Configuration (DSC) - Advanced.md) — *draft*
- **31.** [31. Unit Testing with Pester](chapters/31 - 31. Unit Testing with Pester.md) — *draft*
- **32.** [32. Build Pipelines and CI/CD](chapters/32 - 32. Build Pipelines and CICD.md) — *draft*
- **33.** [33. SQL Server Automation](chapters/33 - 33. SQL Server Automation.md) — *draft*
- **34.** [34. Active Directory Management](chapters/34 - 34. Active Directory Management.md) — *draft*
- **35.** [35. Azure Automation (Cloud)](chapters/35 - 35. Azure Automation (Cloud).md) — *draft*
- **36.** [36. Working with Files and Formats (Advanced)](chapters/36 - 36. Working with Files and Formats (Advanced).md) — *draft*
- **37.** [37. User Interface Design (GUI)](chapters/37 - 37. User Interface Design (GUI).md) — *draft*
- **38.** [38. Performance Optimization](chapters/38 - 38. Performance Optimization.md) — *draft*

### Part VI — Platforms, Hardening, and Capstone

Events, Linux/cross-platform, Graph/external APIs, signing/PKI, error patterns, future directions, and a capstone.

- **39.** [39. Event Handling](chapters/39 - 39. Event Handling.md) — *draft*
- **40.** [40. PowerShell Core on Linux](chapters/40 - 40. PowerShell Core on Linux.md) — *draft*
- **41.** [41. Integrating with External APIs (Graph)](chapters/41 - 41. Integrating with External APIs (Graph).md) — *draft*
- **42.** [42. Code Signing and PKI](chapters/42 - 42. Code Signing and PKI.md) — *draft*
- **43.** [43. Error Handling Patterns at Scale](chapters/43 - 43. Error Handling Patterns at Scale.md) — *draft*
- **44.** [44. Future Directions and Community](chapters/44 - 44. Future Directions and Community.md) — *draft*
- **45.** [45. Capstone Project](chapters/45 - 45. Capstone Project.md) — *draft*

### Appendices

Quick references and resources.

- **46.** [46. Appendix A: Syntax and Operator Quick Reference](chapters/46 - 46. Appendix A Syntax and Operator Quick Reference.md) — *draft*
- **47.** [47. Appendix B: Recommended Tools and Ecosystem](chapters/47 - 47. Appendix B Recommended Tools and Ecosystem.md) — *draft*
- **48.** [48. Appendix C: .NET Type Accelerator Reference](chapters/48 - 48. Appendix C .NET Type Accelerator Reference.md) — *draft*
- **49.** [49. Appendix D: Keyboard Shortcuts and Keybindings](chapters/49 - 49. Appendix D Keyboard Shortcuts and Keybindings.md) — *draft*
- **50.** [50. Appendix E: Bibliography and Resources](chapters/50 - 50. Appendix E Bibliography and Resources.md) — *draft*
