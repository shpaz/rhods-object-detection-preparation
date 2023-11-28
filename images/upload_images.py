from datetime import datetime
from os import environ

from boto3 import client


def upload_results(bucket_name='', data_folder='./'):
    print('Commencing results upload.')

    s3_endpoint_url = environ.get(
        'S3_ENDPOINT_URL', environ.get('AWS_S3_ENDPOINT')
    )
    s3_access_key = environ.get(
        'S3_ACCESS_KEY', environ.get('AWS_ACCESS_KEY_ID')
    )
    s3_secret_key = environ.get(
        'S3_SECRET_KEY', environ.get('AWS_SECRET_ACCESS_KEY')
    )
    s3_bucket_name = environ.get(
        'S3_BUCKET_NAME', environ.get('AWS_S3_BUCKET')
    )

    s3_client = client(
        's3', endpoint_url=s3_endpoint_url,
        aws_access_key_id=s3_access_key, aws_secret_access_key=s3_secret_key
    )

    
    for i in range(1,13): 
      image_name = f'scene{i}.jpg'

      print(f'Uploading scene{i}.jpg to bucket {s3_bucket_name} '
            f'to S3 storage at {s3_endpoint_url}')


      with open(f'{data_folder}/{image_name}', 'rb') as image_file:
          s3_client.upload_fileobj(image_file, s3_bucket_name, image_name)

    print('Finished uploading results.')


if __name__ == '__main__':
    upload_results(data_folder='images/')
