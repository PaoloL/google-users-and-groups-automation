# Gmail Group Automation Script

## Overview
This Python script automates the creation of Gmail groups and adds users to these groups using the Gmail API. It is designed for administrators who need to manage group memberships efficiently. The script reads user details from a CSV file and creates groups with specific naming conventions, then adds the users to the corresponding groups.

## Features
- **Automated Group Creation**: Automatically creates Gmail groups based on user details.
- **Adding Users to Groups**: Adds users to the created groups based on the information provided in a CSV file.
- **Customizable Group Naming**: Groups are named using a predefined structure, which can be easily modified in the script.

## Prerequisites
- Python 3.x
- Google account with administrative privileges
- Google Cloud project with Gmail API enabled
- `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, and `google-api-python-client` libraries installed

## Installation
1. Clone the repository or download the script.
2. Install the required Python libraries:
   ```
   pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

## Setup
1. Enable the Gmail API in your Google Cloud project.
2. Create OAuth 2.0 credentials (type: Desktop app) in the Google Cloud Console.
3. Download the credentials JSON file and save it as `credentials.json` in the same directory as the script.
4. Create a CSV file named `User_List.csv` with user details. Format: `first_name;last_name;email`.

## Usage
1. Run the script:
   ```
   python CeateAndAdd.py
   ```
2. Follow the prompts to authorize the application with your Google account.
3. The script will read users from the CSV file and prompt you to proceed with group creation.

## Important Notes
- The script requires a `token.json` file for storing access tokens. It will be created automatically upon the first successful authentication.
- Modify `EMAIL_DOMAIN` and `GROUP_SUFFIX` variables in the script to match your domain and desired group suffix.
- The CSV file should not contain headers and should be formatted as `first_name;last_name;email`.
- Handle any exceptions and errors appropriately for your use case.

## Disclaimer
This script is provided as-is, and it is recommended to test it in a controlled environment before using it in production. The author is not responsible for any unintended consequences of using this script.

## License
This script is released under the MIT License. See the LICENSE file for more details.

---