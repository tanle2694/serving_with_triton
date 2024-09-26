from src.config.manager import settings


class AsyncStorageClient:
    def __init__(self):
        self.minio_uri = ""
        self.minio_access_key = ""
        self.minio_secret_key = ""
        self.minio_bucket_name = ""
        self.minio_region = ""
        self.minio_endpoint = ""
        self.minio_secure = False
        
        