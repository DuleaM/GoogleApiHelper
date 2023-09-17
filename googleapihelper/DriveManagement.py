import os, io, mimetypes
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

class GoogleDrive():
    def __init__(self, creds):
        self.creds = creds
        self.service = build('drive', 'v3', credentials=self.creds)
    
    def upload_file(self, file_path, file_mimetype=None):
        """Uploads a file to google drive

        Args:
            file_path (str): The path of the file (must be raw)
            file_mimetype (str, optional): If mentioned, it uploads based on the specified mimetype. 
                                           If not, it will try to guess it based on extension.
                                           Defaults to None.

        Returns:
            _type_: Id of the file uploaded to drive
        """
        
        file_name = os.path.basename(file_path)
        
        if file_mimetype == None:
            file_mimetype = mimetypes.guess_type(file_name)[0]

        file_metadata = {'name': file_name}
        
        try:
            media = MediaFileUpload(file_path, mimetype=file_mimetype)
        except Exception as error:
            print(F'An error occurred: {error}')
            return None
        
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        return file.get("id")

    def download_file(self, file_id):
    
        try:
            request = self.service.files().get_media(
                fileId=file_id
            )
            
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(F'Download {int(status.progress() * 100)}.')

        except HttpError as error:
            print(F'An error occurred: {error}')
            return None

        return file.getvalue()
    
if __name__ == '__main__':
    from Credentials import Account
    creds = Account().getAuthToken()
    
    drive = GoogleDrive(creds)
    drive.download_file()    