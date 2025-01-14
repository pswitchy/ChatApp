import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    file_content = event.get('file_content')
    file_name = event.get('file_name')
    bucket_name = event.get('bucket_name')
    
    if file_content is None or file_name is None or bucket_name is None:
        return {
            'statusCode': 400,
            'body': json.dumps('file_content, file_name, and bucket_name are required')
        }
    
    file_content = base64.b64decode(file_content)
    
    try:
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        return {
            'statusCode': 200,
            'body': json.dumps('File uploaded successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading file: {str(e)}')
        }