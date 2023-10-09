import os
from datetime import datetime
from typing import Optional

import boto3
from boto3.dynamodb.conditions import Key

DYNAMODB_TABLE = "reversed_texts"


class TextManipulator:
    def __init__(self):
        self._dynamodb_table = self._get_dynamodb_table()

    def _get_dynamodb_table(self) -> boto3.resource:
        region = os.environ.get("AWS_REGION")
        end_point_url = os.environ.get("AWS_ENDPOINT_URL")

        dynamodb = boto3.resource(
            "dynamodb", region_name=region, endpoint_url=end_point_url
        )
        return dynamodb.Table(DYNAMODB_TABLE)

    def _reverse_text(self, text: str) -> str:
        return text[::-1]

    def query_dynamodb(self, text: str) -> Optional[str]:
        response = self._dynamodb_table.query(
            KeyConditionExpression=Key("text").eq(text),
            ScanIndexForward=False,
            Limit=1,
        )

        if response["Count"] != 0:
            return response["Items"][0]["reversed_text"]

        return None

    def write_dynamodb(self, text: int, reversed_text: str) -> None:
        self._dynamodb_table.put_item(
            Item={
                "text": text,
                "updated_at": datetime.now().isoformat(),
                "reversed_text": reversed_text,
            }
        )

    def reverse(self, text: str) -> str:
        if reversed_text := self.query_dynamodb(text):
            return reversed_text

        reversed_text = self._reverse_text(text)
        self.write_dynamodb(text, reversed_text)

        return reversed_text
