import sys
import boto3

print(sys.path)

client=boto3.client("s3")
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
