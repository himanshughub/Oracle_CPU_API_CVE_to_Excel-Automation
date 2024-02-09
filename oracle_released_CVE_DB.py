###############################################################################
# ORACLE CVE DATABASE - Code written by Himanshu Kumar ########################
# Follow me on LinkedIn: https://www.linkedin.com/in/himanshu-kumar-60b790114 #
###############################################################################

#INSTRUCTIONS:-
#Make sure to install library:openpyxl in order for python to do converstion data in excel format
#You may install using this command:$sudo pip3 install openpyxl

import subprocess
import re
import pandas as pd
import os

def save_cve_data_to_file(url):
    # Run the command and save the output to a file
    command_output = subprocess.check_output(f"curl -s {url} | jq -r '.vulnerabilities[] | {{cve: .cve, text: (.notes[] | select(.text | startswith(\"Vulnerability in the Oracle\")).text), known_affected: .product_status.known_affected}}' | jq -c '.' | jq -c -r 'to_entries | map(.key + \": \" + (.value | tojson + \"\\n\")) | join(\"\")'", shell=True, text=True)
    with open("processing_data.txt", "w") as output_file:
        output_file.write(command_output)

def parse_cve_data(input_file):
    with open(input_file, 'r') as f:
        cve_data = f.read()

    cve_entries = re.split(r'\ncve:', cve_data)
    
    # Initialize lists to store data
    cve_list = []
    product_list = []
    component_list = []
    protocol_list = []
    remote_exploit_list = []
    base_score_list = []
    attack_vector_list = []
    attack_complex_list = []
    privs_required_list = []
    user_interact_list = []
    scope_list = []
    confidentiality_list = []
    integrity_list = []
    availability_list = []
    supported_versions_affected_list = []

    for entry in cve_entries:
        if entry.strip():
            # Parse CVE ID
            cve_match = re.search(r'CVE-\d{4}-\d{1,10}', entry)
            cve_id = cve_match.group() if cve_match else None

            # Parse text description
            text_match = re.search(r'text: "(.*?)"', entry, re.DOTALL)
            text = text_match.group(1) if text_match else ''
            
            # Extract the product name from the text
            product_match = re.search(r'Vulnerability in the (.*?) (product|component) of', text)
            product = product_match.group(1).strip() if product_match else None

            # Extract Component from the text
            component_match = re.search(r'\(component: (.*?)\)\.', text)
            component = component_match.group(1).strip() if component_match else None

            # If the component value is not found, check for the alternative pattern
            if component is None:
               alternative_component_match = re.search(r'component of (.*?)\.', text)
               component = alternative_component_match.group(1).strip() if alternative_component_match else None

            # Extract Protocol from the text
            protocol_match = re.search(r'network access via (.*?) to compromise', text)
            protocol = protocol_match.group(1).strip() if protocol_match else None

            # Extract CVSS Vector from the text
            cvss_vector_match = re.search(r'CVSS Vector: (.*?\))', entry)
            cvss_vector = cvss_vector_match.group(1).strip() if cvss_vector_match else None

            # Determine Remote Exploit based on AV:N condition
            remote_exploit = "Yes" if "AV:N" in cvss_vector else "No"

            # Extract Base Score from the text
            base_score_match = re.search(r'Base Score (.*?) \(', entry)
            base_score = base_score_match.group(1).strip() if base_score_match else None

            # Determine Attack Vector based on AV value in CVSS Vector
            if "AV:N" in cvss_vector:
                attack_vector = "Network"
            elif "AV:L" in cvss_vector:
                attack_vector = "Local"
            elif "AV:P" in cvss_vector:
                attack_vector = "Physical"
            elif "AV:A" in cvss_vector:
                attack_vector = "Adjacent Network"
            else:
                attack_vector = "Unknown"

            # Determine Attack Complex based on AC value in CVSS Vector
            if "AC:L" in cvss_vector:
                attack_complex = "Low"
            elif "AC:M" in cvss_vector:
                attack_complex = "Medium"
            elif "AC:H" in cvss_vector:
                attack_complex = "High"
            else:
                attack_complex = "Unknown"

            # Determine Privs Req'd based on PR value in CVSS Vector
            if "PR:N" in cvss_vector:
                privs_required = "None"
            elif "PR:L" in cvss_vector:
                privs_required = "Low"
            elif "PR:H" in cvss_vector:
                privs_required = "High"
            else:
                privs_required = "Unknown"

            # Determine User Interact based on UI value in CVSS Vector
            if "UI:N" in cvss_vector:
                user_interact = "None"
            elif "UI:R" in cvss_vector:
                user_interact = "Required"
            else:
                user_interact = "Unknown"

            # Determine Scope based on S value in CVSS Vector
            if "S:U" in cvss_vector:
                scope = "Unchanged"
            elif "S:C" in cvss_vector:
                scope = "Changed"
            else:
                scope = "Unknown"

            # Determine Confidentiality based on C value in CVSS Vector
            if "C:N" in cvss_vector:
                confidentiality = "None"
            elif "C:L" in cvss_vector:
                confidentiality = "Low"
            elif "C:H" in cvss_vector:
                confidentiality = "High"
            else:
                confidentiality = "Unknown"

            # Determine Integrity based on I value in CVSS Vector, correctly checking for "/I:"
            if re.search(r"/I:N", cvss_vector):
                integrity = "None"
            elif re.search(r"/I:L", cvss_vector):
                integrity = "Low"
            elif re.search(r"/I:H", cvss_vector):
                integrity = "High"
            else:
                integrity = "Unknown"
            
            # Determine Availability based on A value in CVSS Vector, correctly checking for "/A:"
            if re.search(r"/A:N", cvss_vector):
                availability = "None"
            elif re.search(r"/A:L", cvss_vector):
                availability = "Low"
            elif re.search(r"/A:H", cvss_vector):
                availability = "High"
            else:
                availability = "Unknown"
                 
            # Parse known affected
            known_affected_match = re.search(r'known_affected: (\[.*?\])', entry)
            known_affected_str = known_affected_match.group(1) if known_affected_match else '[]'
            known_affected = eval(known_affected_str)

            # Format known affected with single quotes and square brackets
            array_of_known_affected = [f"{item}" for item in known_affected]
            array_of_known_affected_str = ', '.join(array_of_known_affected)

            # Parse affected versions
            affected_versions_match = re.search(r'affected (?:are|is)(.*?)\b(?:Difficult|Medium|Easily)', entry, re.DOTALL)
            affected_versions = affected_versions_match.group(1) if affected_versions_match else ''

            # Format actual affected versions with square brackets
            Supported_Versions_Affected = []
            for item in affected_versions.split(';'):
                parts = item.strip().split(':')
                if len(parts) > 1:  # Handle cases with product names
                    product_name = parts[0].strip()
                    versions = re.split(r', | and ', parts[1])  # Split on commas or "and"
                    versions_str = ', '.join(f"{product_name}:{version.strip()}" for version in versions)
                    Supported_Versions_Affected.append(versions_str)
                else:  # Handle cases without product names
                    Supported_Versions_Affected.append(item.strip())

            # Remove the trailing period if present
            Supported_Versions_Affected = ', '.join(Supported_Versions_Affected).rstrip('.')

            # Replace "and" with ","
            Supported_Versions_Affected = Supported_Versions_Affected.replace(" and ", ", ")

            # Remove extra space after the colon
            Supported_Versions_Affected = Supported_Versions_Affected.replace(": ", ":")

            # Append data to lists
            cve_list.append(cve_id)
            product_list.append(product)
            component_list.append(component)
            protocol_list.append(protocol)
            remote_exploit_list.append(remote_exploit)
            base_score_list.append(base_score)
            attack_vector_list.append(attack_vector)
            attack_complex_list.append(attack_complex)
            privs_required_list.append(privs_required)
            user_interact_list.append(user_interact)
            scope_list.append(scope)
            confidentiality_list.append(confidentiality)
            integrity_list.append(integrity)
            availability_list.append(availability)
            supported_versions_affected_list.append(Supported_Versions_Affected)

            # Replace "None" with the string "None" in protocol_list
            protocol_list = ['None' if protocol is None else protocol for protocol in protocol_list]

    # Create a DataFrame
    df = pd.DataFrame({
        "CVE#": cve_list,
        "Product": product_list,
        "Component": component_list,
        "Protocol": protocol_list,
        "Remote Exploit": remote_exploit_list,
        "Base Score": base_score_list,
        "Attack Vector": attack_vector_list,
        "Attack Complex": attack_complex_list,
        "Privs Req'd": privs_required_list,
        "User Interact": user_interact_list,
        "Scope": scope_list,
        "Confidentiality": confidentiality_list,
        "Integrity": integrity_list,
        "Availability": availability_list,
        "Supported Versions Affected": supported_versions_affected_list
    })

    # Create a new column "Reference Link" and populate it with NVD links
    df['Reference Link'] = "https://nvd.nist.gov/vuln/detail/" + df['CVE#']

    # Export DataFrame to Excel
    file_name = f"Oracle_{selected_month}_{selected_year}_DB.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Data exported to '{file_name}' successfully.")

    # Remove the processing_data.txt file
    os.remove("processing_data.txt")

# Prompt the user for month and year
print("\033[93m" + """
##################################
##  LIST OF O R A C L E CVE DB  ##
##################################

""" + "\033[0m")

month_options = ["jan", "apr", "jul", "oct"]
selected_month = input(f"Select a month from {', '.join(month_options)} (case-sensitive): ")

# Ensure a valid month is selected
while selected_month not in month_options:
    print("Invalid month. Please select from the provided options.")
    selected_month = input(f"Select a month from {', '.join(month_options)} (case-sensitive): ")

# Prompt the user for the year
year_input = input("Enter the year (format reference: 20XX): ")
while not (year_input.isdigit() and len(year_input) == 4):
    print("Invalid year format. Please enter a 4-digit year.")
    year_input = input("Enter the year (format reference: 20XX): ")

# Generate the URL based on user input
selected_year = year_input
url = f"https://www.oracle.com/docs/tech/security-alerts/cpu{selected_month}{selected_year}csaf.json"

# Save the command output to the file using the dynamically generated URL
save_cve_data_to_file(url)

# Replace with your actual input file name:
parse_cve_data('processing_data.txt')
