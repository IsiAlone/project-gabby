import gcp.storage
import gcp.config as gcp_c

def main():
    # gcp.storage.upload_blob(gcp_c.bucket_name, gcp_c.source_file_name, gcp_c.destination_blob_name)
    gcp.storage.download_blob(gcp_c.bucket_name, gcp_c.source_blob_name, gcp_c.destination_file_name)

if __name__== '__main__':
    main()