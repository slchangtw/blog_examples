import os


def lambda_handler(event, context):
    try:
        # Read email address from the environment
        email_address = os.environ.get("EMAIL_ADDRESS")

        # Print out the email address
        print(f"Email address is: {email_address}")

        return {"statusCode": 200, "body": f"Email address is: {email_address}"}

    except Exception as e:
        return {"statusCode": 500, "body": f"An error occurred: {str(e)}"}
