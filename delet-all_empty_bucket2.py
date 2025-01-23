import json
import boto3
# Call S3 to list current buckets
s3 = boto3.client('s3')

def keys(bucket_name, prefix='/', delimiter='/'):
    prefix = prefix[1:] if prefix.startswith(delimiter) else prefix
    bucket = boto3.resource('s3').Bucket(bucket_name)
    return (_.key for _ in bucket.objects.filter(Prefix=prefix))

def delete_all_bucket():
    response = s3.list_buckets()
    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    # Print out the bucket list
    print(f"Bucket List: {buckets}")
    for bucket in buckets:
        _exhausted = object()
        try:
            if next(keys(bucket), _exhausted) == _exhausted:
                print(f"{bucket}: generator is empty")
        except Exception as e:
            print(f"Error: {bucket} - {e}")
            print(json.dumps(f"Scanned {len(buckets)} buckets"))
