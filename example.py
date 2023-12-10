import boto3
import os
from dotenv import load_dotenv
load_dotenv()

# Replace the following variables with your Cognito details
USER_POOL_ID = os.getenv('USER_POOL_ID')
CLIENT_ID = os.getenv('CLIENT_ID')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
REGION_NAME = os.getenv('REGION_NAME')

# Initialize the Cognito client
client = boto3.client('cognito-idp', region_name=REGION_NAME)

# Authenticate the user

response = client.initiate_auth(
    ClientId=CLIENT_ID,
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': USERNAME,
        'PASSWORD': PASSWORD
    }
)

AccessToken = response['AuthenticationResult']['AccessToken']
IdToken = response['AuthenticationResult']['IdToken']
RefreshToken = response['AuthenticationResult']['RefreshToken']

with open('output_tokens.txt', 'w') as f:
    f.write('Access Token: \n')
    f.write(AccessToken)
    f.write('\n')

with open('output_tokens.txt', 'a') as f:
    f.write('ID Token: \n')
    f.write(IdToken)
    f.write('\n')

with open('output_tokens.txt', 'a') as f:
    f.write('Refresh Token: \n')
    f.write(RefreshToken)
    f.write('\n')

