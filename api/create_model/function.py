import os
from pandas import DataFrame
import pandas as pd
import numpy as np
from dateutil.parser import parse
from dotenv import load_dotenv
load_dotenv()

import boto3
import mysql.connector as mysql
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine


s3 = boto3.resource('s3',
        aws_access_key_id=os.environ.get("aws_access_key_id"),
        aws_secret_access_key=os.environ.get("aws_secret_access_key"),
        region_name='ap-northeast-1'
)
s3_client = boto3.client('s3',
        aws_access_key_id=os.environ.get("aws_access_key_id"),
        aws_secret_access_key=os.environ.get("aws_secret_access_key"),
        region_name='ap-northeast-1'
)
BUCKET_NAME = 'newfan-analysis'


# ========================
# Tools
# ========================
def _get_data_s3(uid, table):
    bucket = s3.Bucket(BUCKET_NAME)
    prefix = "UPLOAD_DATA"+"/"+uid
    objects = [obj.key for obj in bucket.objects.filter(Prefix=prefix).all()]
    get_items = [item.split("/")[3] for item in objects if table in item]
    get_items.sort(reverse=True)
    return get_items