from google.cloud import storage

# autentificacion
storage_client = storage.Client.from_service_account_json('credentials/creds.json')


# STORAGE

# subida de archivo local
bucket_name = 'project-gabby-storage'
source_file_name = "C:/Users/Isi/Desktop/project-gabby/data/vgsales.csv"
destination_blob_name = 'vgsales'

# descarga de archivo bucket-local

source_blob_name = 'vgsales'
destination_file_name = 'C:/Users/Isi/Desktop/vgsales.csv'
