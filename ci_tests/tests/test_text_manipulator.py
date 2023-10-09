import os

import boto3

from src.text_manipulator import TextManipulator


def create_table() -> None:
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=os.environ.get("AWS_REGION"),
        endpoint_url=os.environ.get("AWS_ENDPOINT_URL"),
    )
    dynamodb.create_table(
        TableName="reversed_texts",
        KeySchema=[
            {"AttributeName": "text", "KeyType": "HASH"},  # Partition_key
            {"AttributeName": "updated_at", "KeyType": "RANGE"},  # Sort_key
        ],
        AttributeDefinitions=[
            {"AttributeName": "text", "AttributeType": "S"},
            {"AttributeName": "updated_at", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 1},
    )


def delete_table() -> None:
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=os.environ.get("AWS_REGION"),
        endpoint_url=os.environ.get("AWS_ENDPOINT_URL"),
    )
    dynamodb.Table("reversed_texts").delete()


def test_text_manipulator():
    try:
        create_table()

        text_manipulator = TextManipulator()

        assert text_manipulator.query_dynamodb("grandpa") is None

        assert text_manipulator.reverse("grandpa") == "apdnarg"
        assert text_manipulator.query_dynamodb("grandpa") == "apdnarg"

        text_manipulator.write_dynamodb("grandpa", "grandson")
        assert text_manipulator.query_dynamodb("grandpa") == "grandson"
    finally:
        delete_table()
