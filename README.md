[![Release Version](https://img.shields.io/github/v/release/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation.svg)](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/releases/tag/Oracle_CPU_API_CVE_to_Excel-Automation_v1.0)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue)](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/blob/main/LICENSE)

# Oracle_CPU_API_CVE_to_Excel-Automation (v1.0)
Streamlines vulnerability management by automating Oracle CVE data collection and analysis. The tool leverages Oracle's API to extract CVE details and CVSS metrics, exporting them into structured Excel formats for enterprise security ticketing system workflows.

This project enhances vulnerability assessment procedures by automating critical tasks. Utilizing Oracle API requests, the system efficiently retrieves CVE details and essential CVSS key values, organizing them into an excel sheet with clean, structured data. This exported data can then be utilized to automate further processes based on your organization's structure. For instance, it can be employed to cross-reference vulnerable software versions within your organization's systems. Upon detection of a match, automated ticket generation is triggered, directing the issue to the relevant department for immediate patching. By automating this process, the project expedites the mitigation of potential threats, saving valuable time and bolstering our security measures through timely identification and resolution of vulnerabilities.

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
![oracle_CPU_automation_report.gif](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/blob/main/oracle_CPU_automation_report.gif)

## Future Scope:
I am currently engaged in an independent project aimed at enhancing the autonomy and convenience of the aforementioned system. The goal is to enable users to identify vulnerabilities associated with all software installed across their organization's network without the need for conventional vulnerability scanning tools. Given that such tools rely on CVE data from entities like NIST, there is often a delay in updating their databases, which can impact the accuracy and timeliness of vulnerability assessments. By directly importing data from NIST and comparing it with the current software versions installed in your organization, we aim to expedite the vulnerability assessment process while minimizing network traffic load and reducing the likelihood of false positive detections by SIEM tools.
