import os

import boto3

from src.text_reverter import TextReverter


def create_table() -> None:
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=os.environ.get("AWS_REGION"),
        endpoint_url=os.environ.get("AWS_ENDPOINT_URL"),
    )
    dynamodb.create_table(
        TableName="reverted_texts",
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
    dynamodb.Table("reverted_texts").delete()


def test_text_reverter():
    try:
        create_table()

        text_reverter = TextReverter()

        assert text_reverter.query_dynamodb("grandpa") is None

        assert text_reverter.revert("grandpa") == "apdnarg"
        assert text_reverter.query_dynamodb("grandpa") == "apdnarg"

        text_reverter.write_dynamodb("grandpa", "grandson")
        assert text_reverter.query_dynamodb("grandpa") == "grandson"
    finally:
        delete_table()
