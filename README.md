# Oracle_CPU_API_CVE_to_Excel-Automation (v1.0)
[![Download Oracle_CPU_API_CVE_to_Excel-Automation.zip](https://img.shields.io/badge/download-Oracle_CPU_API_CVE_to_Excel_Automation.zip-blue?style=flat-square&color=yellow)](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/releases/download/Oracle_CPU_API_CVE_to_Excel-Automation_v1.0/Oracle_CPU_API_CVE_to_Excel-Automation_v1.0.zip)
[![Release Version](https://img.shields.io/github/v/release/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation.svg)](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/releases/tag/Oracle_CPU_API_CVE_to_Excel-Automation_v1.0)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue)](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/blob/main/LICENSE)

# About the tool:
I implemented this project to streamlines vulnerability management by automating Oracle CVE data collection and analysis. The tool leverages Oracle's API to extract CVE details and CVSS metrics, exporting them into structured Excel formats for enterprise security ticketing system workflows.

This project enhances vulnerability assessment procedures by automating critical tasks for the University. The tool makes requests to Oracle's API to pull their CPU (Critical Patch Update) vulnerability database and collects specific data from the unstructured JSON formatting. This includes details such as CVE, Product Name, Component, Protocol, Remote Exploit, Base Score, Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality, Integrity, Availability, Supported Versions Affected, and Reference Link values. Upon collecting these values, it exports the data to an Excel sheet in an organized, structured way, making it ready for integration with the university's ticketing system workflows. This enables automatic ticket creation with the concerned internal departments who own the affected servers, allowing them to patch these vulnerabilities.

# Challenges - Manual Oracle Vulnerability Assessment
During my internship with the Information Security team at the University of Delaware, I identified a significant operational challenge in their vulnerability management process. Since the team could not use commercial vulnerability scanning tools like Tenable for their critical servers, which were hosted on Oracle applications, they manually extracted values from unstructured vulnerability data from the Oracle CPU database and added those values to an Excel sheet. Once the Excel sheet report was ready, they uploaded it to the ticketing system to automatically generate tickets for the respective departments responsible for patching vulnerabilities on those servers. This manual process required significant effort, consumed many hours and introduces the risk of human error.

 **Below is an example how the raw unstructured JSON formatting CVE vulnerability data appears in Oracle CPU database:**

**Select the Month/Year for which you would like to see data for:
 ![Oracle_CPU_vulnerability_database_snapshot](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/blob/main/images/Oracle_CPU_database_Release.png)

 **View of the raw unstructured JSON formatting data:
![Oracle_CPU_raw_database_snapshot](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/blob/main/images/oracle_raw_json_data.png)

Step 3: Cross-referencing this data against the university's inventory of Oracle products and versions
Identifying applicable vulnerabilities from a database of over 10,000 entries
Creating tickets for relevant internal departments to address identified vulnerabilities

This manual process was highly inefficient, typically requiring several hours to complete and introducing the risk of human error. The team needed a more streamlined approach to effectively manage Oracle vulnerabilities while maintaining their security standards.

# Why use this tool?
By using this tool, it automates the manual work do the same work in just 2 seconds.


Univerties had several Oracle servers which 

## Key Features:
- Automated CVE data retrieval via Oracle API
- Structured Excel export of vulnerability data
- Capable of generating vulnerability reports for any time period (year or month) as long as the Oracle database has the source data for it."
- Cross-reference functionality for version matching
- Streamlined patch management workflow

Designed to support enhance security operations by enabling rapid vulnerability identification, assessment, and remediation through automated processes.

## Oracle CPU API data integration Link:
https://www.oracle.com/security-alerts/#CriticalPatchUpdates

## Citation:
If you found this repository helpful, please cite my Github repository link & name in your post :)
```bash
Repository Link: https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/
Author name:Himanshu Kumar
Author LinkedIn Profile: https://www.linkedin.com/in/himanshuk8
```

## Demo:
![oracle_CPU_automation_report.gif](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/blob/main/video/oracle_CPU_automation_report.gif)

## Future Scope:
I am currently engaged in an independent project aimed at enhancing the autonomy and convenience of the aforementioned system. The goal is to enable users to identify vulnerabilities associated with all software installed across their organization's network without the need for conventional vulnerability scanning tools. Given that such tools rely on CVE data from entities like NIST, there is often a delay in updating their databases, which can impact the accuracy and timeliness of vulnerability assessments. By directly importing data from NIST and comparing it with the current software versions installed in your organization, we aim to expedite the vulnerability assessment process while minimizing network traffic load and reducing the likelihood of false positive detections by SIEM tools.
