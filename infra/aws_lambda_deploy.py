import boto3
import zipfile
import os

class LambdaPackager:
    def __init__(self):
        self.lambda_client = boto3.client('lambda')
    
    def create_deployment_package(self):
        with zipfile.ZipFile('lambda_package.zip', 'w') as z:
            for root, _, files in os.walk('src'):
                for file in files:
                    z.write(os.path.join(root, file))
            z.write('config.json')
    
    def deploy_function(self, function_name):
        with open('lambda_package.zip', 'rb') as f:
            self.lambda_client.update_function_code(
                FunctionName=function_name,
                ZipFile=f.read()
            )