from openai import AzureOpenAI

# API credentials and endpoint
api_base = "https://hemocountopenai-westus.openai.azure.com/"
api_key = "1bc3cca309524c44b7849863fcf73827"
deployment_name = 'gpt-35-turbo'
api_version = '2023-03-15-preview'

client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
)

def ask_question(question, context):
    # Define the prompt
    prompt = f"Question: {question}\nContext: {context}\nAnswer:"

    # Set parameters for the completion
    params = {
        "temperature": 0.5,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "stop": ["\n"]
    }

    # Generate the answer
    response = client.chat.completions.create(
        engine="gpt-35-turbo",
        prompt=prompt,
        max_tokens=150,
        **params
    )

    # Extract and return the answer
    answer = response.choices[0].text.strip()
    return answer

# Example context and question
context = "The Amazon rainforest, also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf tropical rainforest in the Amazon biome that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 km2 (2,700,000 sq mi), of which 5,500,000 km2 (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations."
question = "What is the approximate area covered by the Amazon rainforest?"

# Get the answer to the question
answer = ask_question(question, context)
print("Answer:", answer)
