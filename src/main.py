import json


def lambda_handler(event, context):
    print(f"Body recebido: {event.get('body')}")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": "ok"}),
    }
