# app/utils/cognito_auth.py

import boto3
from jose import jwt
import os

COGNITO_POOL_ID = os.getenv("COGNITO_USER_POOL_ID")
COGNITO_CLIENT_ID = os.getenv("COGNITO_APP_CLIENT_ID")
AWS_REGION = os.getenv("AWS_REGION")

cognito = boto3.client('cognito-idp', region_name=AWS_REGION)

def verify_token(token: str):
    try:
        decoded = jwt.get_unverified_claims(token)
        return decoded
    except Exception as e:
        print("Token error:", e)
        return None

def get_user_info(token: str):
    claims = verify_token(token)
    if claims:
        return {
            "username": claims.get("cognito:username"),
            "email": claims.get("email")
        }
    return None
