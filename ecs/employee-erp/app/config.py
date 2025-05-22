import boto3
import json
import os

class Config:
    SECRET_NAME = os.getenv("AWS_SECRET_NAME")
    REGION_NAME = os.getenv("AWS_REGION", "us-east-1")

    try:
        secret = boto3.client("secretsmanager", region_name=REGION_NAME).get_secret_value(
            SecretId=SECRET_NAME
        )
        creds = json.loads(secret["SecretString"])
    except:
        creds = {
            "username": os.getenv("DB_USER", "postgres"),
            "password": os.getenv("DB_PASS", "password"),
            "host": os.getenv("DB_HOST", "localhost"),
            "port": os.getenv("DB_PORT", "5432"),
            "dbname": os.getenv("DB_NAME", "erpdb")
        }

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{creds['username']}:{creds['password']}@"
        f"{creds['host']}:{creds['port']}/{creds['dbname']}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
