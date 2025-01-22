import boto3



client = boto3.client('s3')
response = client.list_buckets(
    MaxBuckets=123,
    ContinuationToken='string',
    Prefix='string',
    BucketRegion='string'
)
print(response)