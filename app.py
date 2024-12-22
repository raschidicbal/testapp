from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import boto3
import os
from botocore.exceptions import NoCredentialsError

S3_BUCKET = os.getenv('S3_BUCKET')
REGION = os.getenv('REGION')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# Validate that all required environment variables are set
if not all([S3_BUCKET, REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY]):
    raise ValueError("Missing required environment variables for AWS S3 configuration")

# Specifically print the AWS-related environment variables
print("\nAWS Environment Variables:")
print(f"S3_BUCKET: {os.getenv('S3_BUCKET')}")
print(f"REGION: {os.getenv('REGION')}")
print(f"AWS_ACCESS_KEY_ID: {os.getenv('AWS_ACCESS_KEY_ID')}")
print(f"AWS_SECRET_ACCESS_KEY: {os.getenv('AWS_SECRET_ACCESS_KEY')}")

# Update Boto client configuration here
s3 = boto3.client(
    's3',
    region_name=REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

# User Model
class Users(db.Model):
    __tablename__ = 'appusers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

@app.route('/')
def get_home():
    return 'Hello World Adios.ai'

@app.route('/users')
def get_users():
    users = Users.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        s3.upload_fileobj(file, S3_BUCKET, file.filename)
        return jsonify({"message": f"File '{file.filename}' uploaded successfully to S3!"})
    except NoCredentialsError:
        return jsonify({"error": "Credentials not available"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
