from datetime import datetime
from os import environ

from boto3 import client


def upload_results(bucket_name='', data_folder='models'):
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

    print(f'Uploading models to bucket {s3_bucket_name} '
            f'to S3 storage at {s3_endpoint_url}')


    with open(f'{data_folder}/yolov5n.onnx', 'rb') as model:
          s3_client.upload_fileobj(model, s3_bucket_name, 'yolov5n.onnx')

    with open(f'{data_folder}/model-latest.onnx', 'rb') as model:
          s3_client.upload_fileobj(model, s3_bucket_name, 'model-latest.onnx')

    print('Finished uploading results.')


if __name__ == '__main__':
    upload_results(data_folder='models/')
