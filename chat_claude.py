import boto3
import json

bedrock = boto3.client(
  service_name='bedrock-runtime', 
  region_name="us-east-1"
)

def chat(text:str) -> str:

    body = json.dumps(
        {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
            {
                "role": "user",
                "content": [
                {
                    "type": "text",
                    "text": text
                }
                ]
            }
            ]
        }
    )

    modelId = 'anthropic.claude-3-sonnet-20240229-v1:0'
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())
    return response_body['content'][0]['text']

if __name__ == '__main__':
    print(chat("hi"))