import os
import uuid
import boto3
from fastapi import FastAPI
from mangum import Mangum

# Read environment variables
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
TABLE_NAME = os.getenv("DYNAMODB_TABLE", "users")
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")

# Initialize DynamoDB
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

app = FastAPI(title="Serverless FastAPI + DynamoDB")

@app.get("/")
def root():
    return {
        "message": "API running",
        "environment": ENVIRONMENT,
        "table": TABLE_NAME
    }

@app.post("/users")
def create_user(name: str):
    user_id = str(uuid.uuid4())

    table.put_item(
        Item={
            "user_id": user_id,
            "name": name
        }
    )

    return {"user_id": user_id, "name": name}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    response = table.get_item(Key={"user_id": user_id})
    return response.get("Item", {"message": "User not found"})

@app.get("/users")
def get_users():
    response = table.scan()
    return response.get("Items", [])
handler = Mangum(app)
