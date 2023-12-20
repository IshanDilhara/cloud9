from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import boto3

app = Flask(__name__)

# AWS credentials
AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
AWS_REGION = 'us-east-1'

# S3 bucket configuration
S3_BUCKET_NAME = ''

# Cognito configuration
COGNITO_USER_POOL_ID = 'your-user-pool-id'
COGNITO_CLIENT_ID = 'your-client-id'

# Initialize AWS S3 and Cognito clients
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION)
cognito = boto3.client('cognito-idp', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)

    # Upload file to S3
    s3.upload_fileobj(file, S3_BUCKET_NAME, file.filename)

    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download(filename):
    # Download file from S3
    s3.download_file(S3_BUCKET_NAME, filename, filename)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
