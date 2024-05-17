import boto3
import json

bedrock = boto3.client(
  service_name='bedrock-runtime', 
  region_name="us-east-1"
)

def cal_embedding(text:str) -> list:

    body = json.dumps(
        {
            "inputText": text
        }
    )

    modelId = 'amazon.titan-embed-text-v1'
    accept = '*/*'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())
    return response_body['embedding']

if __name__ == '__main__':
    print(cal_embedding("bye"))