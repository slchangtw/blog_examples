import os
from datetime import datetime
from typing import Optional

import boto3
from boto3.dynamodb.conditions import Key

DYNAMODB_TABLE = "reverted_texts"


class TextReverter:
    def __init__(self):
        self._dynamodb_table = self._get_dynamodb_table()

    def _get_dynamodb_table(self) -> boto3.resource:
        region = os.environ.get("AWS_REGION")
        end_point_url = os.environ.get("AWS_ENDPOINT_URL")

        dynamodb = boto3.resource(
            "dynamodb", region_name=region, endpoint_url=end_point_url
        )
        return dynamodb.Table(DYNAMODB_TABLE)

    def _revert_text(self, text: str) -> str:
        return text[::-1]

    def query_dynamodb(self, text: str) -> Optional[str]:
        response = self._dynamodb_table.query(
            KeyConditionExpression=Key("text").eq(text),
            ScanIndexForward=False,
            Limit=1,
        )

        if response["Count"] != 0:
            return response["Items"][0]["reverted_text"]

        return None

    def write_dynamodb(self, text: int, reverted_text: str) -> None:
        self._dynamodb_table.put_item(
            Item={
                "text": text,
                "updated_at": datetime.now().isoformat(),
                "reverted_text": reverted_text,
            }
        )

    def revert(self, text: str) -> str:
        if reverted_text := self.query_dynamodb(text):
            return reverted_text

        reverted_text = self._revert_text(text)
        self.write_dynamodb(text, reverted_text)

        return reverted_text
