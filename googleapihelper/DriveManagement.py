from __future__ import print_function

import google.auth, os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

class GoogleDrive():
    def __init__(self, creds):
        self.creds = creds
        self.service = build('drive', 'v3', credentials=self.creds)
    
    def uploadFile(self, file_path):
        file_name = os.path.basename(file_path)
        file_metadata = {'name': file_name}
        
        try:
            media = MediaFileUpload(file_path, mimetype='image/png')
        except Exception as e:
            print("Couldn't find the file. Error " + e)
            return None
        
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        return file.get("id")

if __name__ == '__main__':
    from Credentials import Account
    creds = Account().getAuthToken()
    
    drive = GoogleDrive(creds)
    drive.uploadFile(r'C:\Users\dulea\OneDrive\Desktop\marcel ciolacu.png')
    