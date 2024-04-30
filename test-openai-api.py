import os
import base64
from openai import AzureOpenAI

# API credentials and endpoint
api_base = "https://hemocountopenai-westus.openai.azure.com/"
api_key = "1bc3cca309524c44b7849863fcf73827"
deployment_name = 'gpt-4'
api_version = '2023-03-15-preview'

client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
)

# Read the image file
image_path = 'data/HRI001.jpg'  # Update with your image path
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": [
            {
                "type": "text",
                "text": "Describe this picture:"
            },
            {
                "type": "image",
                "image": {
                    "base64": encoded_image
                }
            }
        ]}
    ],
    max_tokens=2000
)

print(response)

