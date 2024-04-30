import openai, os, requests

openai.api_type = "azure"
# Azure OpenAI on your own data is only supported by the 2023-08-01-preview API version
openai.api_version = "2024-02-15-preview"
# Azure OpenAI setup
openai.api_base = "https://lab-interpreter-2.openai.azure.com/" # Add your endpoint here
openai.api_key = "fda9b2e41f134dcc8dd15767d2fbea52" # Add your OpenAI API key here
deployment_id = "gpt-4" # Add your deployment ID here

message_text = [{"role": "user", "content": "What is the meaning of life?"}]

completion = openai.ChatCompletion.create(
    messages=message_text,
    deployment_id=deployment_id,
)
print(completion)
'''
import PyPDF2
## Upload pdf
# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2. PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

# Function to ask a question using Azure OpenAI's API
def ask_question_about_text(text, question):
    response = openai.Completion.create(
        model="gpt-35-turbo",  # Using the text model for question answering
        question=question,
        documents=[text],  # Providing the extracted text as document
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Path to your PDF file
pdf_path = "../data/Cumulative-sample-report-with-notes-2017_2.pdf"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)
#print(pdf_text)
# Ask a question about the text
question = "Highlight abnormal lab result in bullet points"


answer = ask_question_about_text(pdf_text, question)

print("Answer:", answer)

message_text = [{"role": "user", "content": "Describe the text?"}]

completion = openai.ChatCompletion.create(
    messages=message_text,
    documents=[pdf_text],
    deployment_id=deployment_id,
)
print(completion)
'''