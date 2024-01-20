import os.path
import csv

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.group']
EMAIL_DOMAIN = 'recube.it'
GROUP_SUFFIX = 'tag'

def initialize_credentials():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            credentials = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(credentials.to_json())
    return credentials

def get_users_from_csv():
    csv_file_path = 'User_List.csv'
    user_list = []

    # Open the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=';')

        # Skip the header if your CSV has one
        next(csv_reader, None)

        # Loop over the rows in the CSV
        for row in csv_reader:
            # Append each row to the list
            user_list.append(row)

        return user_list

def create_gmail_group(email, name, description):
  try:
    # Call the Gmail API
    creds = initialize_credentials()
    service = build('admin', 'directory_v1', credentials=creds)

    group_info = {
        'email': group_email,
        'name': group_name,
        'description': group_description
    }

    group = service.groups().insert(body=group_info).execute()

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

def add_user_to_gmail_group(email, group_email):
    member_info = {
        'email': email,
        'role': 'MEMBER' 
    }
    creds = initialize_credentials()
    service = build('admin', 'directory_v1', credentials=creds)
    try:
        service.members().insert(groupKey=group_email, body=member_info).execute()
    except Exception as e:
        return e
    

if __name__ == "__main__":
    users = get_users_from_csv()
    proceed = input('I got ' + str(len(users)) + ' users, do you want to proceed with group creation ? (Y/N): ').strip().upper()
    if proceed == "Y":
        for user in users:
            if user[0].startswith('ᐧ'):
                break  # Stop reading further
            group_email = user[0] + '.' + user[1] + '.' + GROUP_SUFFIX + '@' + EMAIL_DOMAIN
            group_name = "Skill Builder User" + " " + user[0].capitalize() + " " + user[1].capitalize()
            group_description = "Skill Builder User for TAG Devop & Cloud Master - PO-2024-ITA-00120"
            print("I'm creating the group " + group_name)
            create_gmail_group(group_email, group_name, group_description)
            print("I'm adding the email " + user[2] + " in the group " + group_name)
            add_user_to_gmail_group(user[2],group_email)
    elif proceed == "N":
        print("Group creation cancelled!")
    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")


