import json
import boto3
import logging
import os
from openai import OpenAI
# Configure logging
logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    try:
        # Get prompt from event
        prompt = event['prompt']
        # Diagnose API Key accessibility
        api_key = <your-open-ai-key>> # First element of the list is the API key

        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables.")
        question = event['prompt']
        client = OpenAI(api_key=api_key)
        # Create chat 
        messages = [{"role": "user", "content": question}]
        completion = client.chat.completions.create(model="gpt-4",messages=messages ,max_tokens=250)
        response = completion.choices[0].message.content

        return {
            "statusCode": 200,
            "body": json.dumps({"response": response})}

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }


