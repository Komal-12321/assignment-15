import json
import boto3
import os

codepipeline = boto3.client('codepipeline')

def lambda_handler(event, context):
    pipeline_name = os.environ['PIPELINE_NAME']

    response = codepipeline.start_pipeline_execution(
        name=pipeline_name
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Pipeline triggered successfully",
            "pipeline": pipeline_name
        })
    }
