import base64
import os

import boto3


def test_case():
    data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdjYGBg+A8AAQQBAHAgZQsAAAAASUVORK5CYII="  # png
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")
    AWS_S3_BUCKET_KEY = os.getenv("AWS_S3_BUCKET_KEY")

    client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    object = client.get_object(Bucket=AWS_S3_BUCKET_NAME, Key=AWS_S3_BUCKET_KEY)

    assert base64.b64encode(object["Body"].read()).decode("utf-8") == data
