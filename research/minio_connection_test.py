from minio import Minio
import os
from pathlib import Path


# Path(output_file_path).parent.mkdir(parents=True, exist_ok=True)
minio_client = Minio("10.98.152.63:9000", access_key="minio", secret_key="minio123", secure=False)

# result = minio_client.fget_object("cicflowmeter", "model_config_rf_cic.json_file", "output.json")
# print(result)
objects = minio_client.list_objects("cicflowmeter", recursive=True)
for obj in objects:
        # print(type(obj.object_name))
        file_name = obj.object_name
        print(file_name)
        # output_file_name = file_name.replace('pcap', 'csv')
        # client.fget_object(bucket, obj.object_name, output_file_name)

buckets = minio_client.list_buckets()
for bucket in buckets:
    print(bucket.name)