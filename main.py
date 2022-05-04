import boto3
from botocore.exceptions import ClientError
import os

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = os.environ.get('LOCALSTACK_ENDPOINT_URL')

boto3.setup_default_session(profile_name=AWS_PROFILE)

loaclstack_client = boto3.client("s3", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)
#-------------------------------------------------------------------------
# endpoint_url = "http://localhost.localstack.cloud:4566"
# # alternatively, to use HTTPS endpoint on port 443:
# # endpoint_url = "https://localhost.localstack.cloud"

# def main():
#     client = boto3.client("lambda", endpoint_url=endpoint_url)
#     result = client.list_functions()
#     print(result)

# if __name__ == "__main__":
#     main()
#--------------------------------------------------------------------------
