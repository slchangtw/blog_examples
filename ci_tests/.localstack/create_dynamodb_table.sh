#!/bin/bash
awslocal dynamodb create-table \
   --table-name reverted_texts \
   --attribute-definitions AttributeName=text,AttributeType=S  AttributeName=updated_at,AttributeType=S\
   --key-schema AttributeName=text,KeyType=HASH AttributeName=updated_at,KeyType=RANGE \
   --billing-mode PAY_PER_REQUEST \
   --region us-east-1