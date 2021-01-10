import base64
import boto3
import json
import requests
import time
import uuid

StreamName = 'StreamingProject'

kinesis_client = boto3.client('kinesis')
partition_key = str(uuid.uuid4())



rec_count = 0
while True:
    time.sleep(0.8)
    print(f"Putting record: {rec_count}")
    results = requests.get('https://randomuser.me/api/?exc=login', headers={"Content-Type": "application/json"})
    try:
        results = results.json()
        resp = kinesis_client.put_record(
                StreamName=StreamName,
                Data=json.dumps(results).encode(),
                PartitionKey=partition_key
        )
        print(results)
        print(resp)
        rec_count += 1
    except Exception as e:
        print(e)
        print(results.text)
