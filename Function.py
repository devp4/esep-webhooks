import json
import os
import urllib.request
from urllib.request import Request

def lambda_handler(event, context):
    issue_url = event['issue']['html_url']
    text = {'text': f"Issue Created: {issue_url}"}
    jsontext = json.dumps(text).encode('utf-8')
    
    slack_url = os.environ.get('SLACK_URL')
    request = Request(slack_url, data=jsontext, headers={'Content-Type': 'application/json'})
    
    with urllib.request.urlopen(request) as response:
        statusCode = response.statusCode
        response_data = response.read().decode('utf-8')

    return {
        'statusCode': statusCode,
        'body': response_data,
    }
