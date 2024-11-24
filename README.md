# OOD_GroupAssignment_1 Evaluating the Impact of Class Size on Software Maintainability: An Empirical Study
This repository contains information Evaluating the Impact of Class Size on Software Maintainability: An Empirical Study

**Project Overview**
This project investigates the relationship between software maintainability and class size using the Chidamber and Kemerer (C&K) metrics suite. The primary objective of the study is to examine how class size, measured in Lines of Code (LoC), affects the internal complexity and cohesion of Java classes, which are key factors in determining maintainability. The study uses Weighted Methods per Class (WMC) and Lack of Cohesion in Methods (LCOM) as metrics to analyze five large-scale, open-source Java projects.

**Project Structure**
1. Introduction: The project’s goals, research questions, and metrics used for evaluating class size and maintainability.
2. Data Set Overview: Details of the Java projects selected, including selection criteria and the description of each project.
3. Framework for Measurement: A discussion on the methodology and tools (such as CKJM) used for collecting and analyzing metrics.
4. Analysis and Results: Results from the analysis of the selected projects, including findings based on the research questions.
5. Conclusion: Final conclusions based on the results and practical recommendations for software developers.
6. References: Cited works and research papers relevant to the study, including the tools and books used to support the analysis.
7. 
**Key Metrics**
Lines of Code (LoC): Measures the physical size of the class.
Weighted Methods per Class (WMC): Measures the internal complexity of a class based on the methods it contains.
Lack of Cohesion in Methods (LCOM): Measures the cohesiveness of methods within a class.

**Data Set**
The data used in this study comes from five open-source Java projects:

Apache Pulsar
TechEmpower Framework Benchmarks
Apache Druid
OpenHAB Add-ons
Teammates

**Analysis Tool**
The primary tool used to gather the metrics is the CKJM (Class-level Java Metrics) tool, which calculates several object-oriented metrics based on the Chidamber and Kemerer (C&K) suite. This tool processes Java bytecode and computes metrics like WMC, LCOM, DIT, CBO, etc., to help analyze software maintainability.

For more information, please visit the official CKJM repository: CKJM Tool on GitHub.

**Data Processing and Visualization**
After extracting the metrics, use a Python script to process the data and create visualizations such as scatter plots, bar graphs, and box plots. This can help visualize the relationship between class size and maintainability.

**Expected Results**
Class Size vs. Maintainability: As the size of the class increases (more LoC), we expect the WMC to increase, indicating higher complexity, and LCOM to decrease, indicating lower cohesion.
Large Classes: Large classes are likely to have higher WMC and lower LCOM, which could make them harder to maintain.
Small and Medium Classes: These might show better maintainability trends, with more balanced WMC and LCOM values.
Conclusion
Impact of Class Size on Maintainability: Larger classes typically exhibit higher complexity and lower cohesion, which can hinder maintainability. Refactoring large classes into smaller, more cohesive units can significantly improve maintainability.
Refactoring Recommendations: The findings highlight the importance of refactoring large classes into smaller, manageable units using design patterns and modularization techniques.
