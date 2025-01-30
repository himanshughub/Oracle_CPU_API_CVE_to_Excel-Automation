# Oracle_CPU_API_CVE_to_Excel-Automation (v1.0)
[![Download Oracle_CPU_API_CVE_to_Excel-Automation.zip](https://img.shields.io/badge/download-Oracle_CPU_API_CVE_to_Excel_Automation.zip-blue?style=flat-square&color=yellow)](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/releases/download/Oracle_CPU_API_CVE_to_Excel-Automation_v1.0/Oracle_CPU_API_CVE_to_Excel-Automation_v1.0.zip)
[![Release Version](https://img.shields.io/github/v/release/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation.svg)](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/releases/tag/Oracle_CPU_API_CVE_to_Excel-Automation_v1.0)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue)](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/blob/main/LICENSE)

# Citation:
If you found this repository helpful, please cite my Github repository link & name in your post :)
```bash
Repository Link: https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/
Author name:Himanshu Kumar
Author LinkedIn Profile: https://www.linkedin.com/in/himanshuk8
```

# About the tool:
I implemented this project to streamlines vulnerability management by automating Oracle CVE data collection and analysis. The tool leverages Oracle's API to extract CVE details and CVSS metrics, exporting them into structured Excel formats for enterprise security ticketing system workflows.

This project enhances vulnerability assessment procedures by automating critical tasks for the University. The tool makes requests to Oracle's API to pull their CPU (Critical Patch Update) vulnerability database and collects specific data from the unstructured JSON formatting. This includes details such as CVE, Product Name, Component, Protocol, Remote Exploit, Base Score, Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality, Integrity, Availability, Supported Versions Affected, and Reference Link values. Upon collecting these values, it exports the data to an Excel sheet in an organized, structured way, making it ready for integration with the university's ticketing system workflows. This enables automatic ticket creation with the concerned internal departments who own the affected servers, allowing them to patch these vulnerabilities.

# Challenges - Manual Oracle Vulnerability Assessment
During my internship with the Information Security team at the University of Delaware, I identified a significant operational challenge in their vulnerability management process. Since the team could not use commercial vulnerability scanning tools like Tenable for their critical servers, which were hosted on Oracle applications, they manually extracted values from unstructured vulnerability data (which has over 10,000+ CVE entries) from the Oracle CPU database and added those values to an Excel sheet. Once the Excel sheet report was ready, they uploaded it to the ticketing system to automatically generate tickets for the respective departments responsible for patching vulnerabilities on those servers. This manual process required significant effort, consumed many hours and introduces the risk of human error.

### In brief points:
- Inability to use commercial vulnerability scanning tools like Tenable for critical servers hosted on Oracle applications.
- Manual extraction of values from unstructured vulnerability data with over 10,000+ CVE entries in the Oracle CPU database.
- Data was manually added to an Excel sheet, which was time-consuming and labor-intensive.
- Uploading the Excel sheet to the ticketing system to generate tickets for departments responsible for patching vulnerabilities.
- High risk of human error in the manual process.
- Significant effort and hours required to complete the process.

 **Below is an example how the raw unstructured JSON formatting CVE vulnerability data appears in Oracle CPU database:**

    • Select the Month/Year for which you would like to see data for:
 ![Oracle_CPU_vulnerability_database_snapshot](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/blob/main/images/Oracle_CPU_database_Release.png)

    • View of the raw unstructured JSON formatting data:
![Oracle_CPU_raw_database_snapshot](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/blob/main/images/oracle_raw_json_data.png)


# Why use this tool?
By using this tool, the manual work is automated, completing the same task in under two seconds and saving hours of manual work with no human error. The script is equipped with an API integration feature that fetches data in real time from the Oracle database, identifies values by analyzing their JSON syntax, and scrapes the data into the Excel sheet in a structured manner. Later, this Excel sheet is fed into the TDX ticketing system workflow to automate ticket creation with the internal department responsible for patching vulnerabilities on those servers.

## 📚 Library Versions used
- jq: jq-1.6
- pandas: 1.3.4

## Oracle CPU API data integration Link:
https://www.oracle.com/security-alerts/#CriticalPatchUpdates

## Demo Video:
![oracle_CPU_automation_report.gif](https://github.com/himanshughub/Oracle_CPU_API_CVE_to_Excel-Automation/blob/main/video/oracle_CPU_automation_report.gif)

## Future Scope:
Most of the renowned vulnerability scanning tools like Tenable and Qualys update their CVE (Common Vulnerability Exposure) databases from sources such as NIST, CISA, Mitre, RedHat, or other open source vulnerability databases. This introduces a delay in updating their databases with the latest exposed vulnerabilities on the internet as they emerge. Additionally, performing scans in an intrusive way to identify vulnerabilities behaves like an attack, which can be disruptive.

I am working independently to develop a cybersecurity vulnerability management tool that addresses these challenges. This tool will operate internally within any organization to perform non-intrusive scans by pulling software version information from workstations or servers. By comparing the software versions with the CVE database for affected versions, the tool will generate a list of vulnerable software in the system and provide recommendations to remediate those vulnerabilities.
