import google.generativeai as genai
import os
import PIL.Image
import re
from flask_cors import CORS
from flask import Flask, jsonify, request

# Load the API key from an environment variable.
GOOGLE_API_KEY  = (os.environ.get('GOOGLE_API_KEY_FILE'))
app = Flask(__name__)
CORS(app)


# Configure the API key & start model instance
genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

    model = genai.GenerativeModel('gemini-pro-vision')

@app.route('/get_blood_cells', methods=['POST'])
def get_blood_cells():
  """
  Retrieves the count of blood cells using the main function and returns it as a JSON response.

  Returns:
    A JSON response containing the count of blood cells.
  """
  if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

  file = request.files['file']

  # Ensure the file is an image (you can add more checks as needed)
  if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
      # Process the file here (e.g., count blood cells in the image)
      # Replace the main() function call with your actual processing code
      cell_count = main(file)

  # cell_count = main()
      return jsonify(cell_count)
  else:
        return jsonify({'error': 'Invalid file format, please upload an image'}), 400

def count_blood_cells(text):
  # Use a regular expression to extract the counts for each type of blood cell.
  counts = re.findall(r'(\d+)\s+(\w+)', text)

  # Create a dictionary to store the counts.
  cell_counts = {}
  for count, cell_type in counts:
    cell_counts[cell_type] = int(count)

  # Return the dictionary of cell counts.
  print(cell_counts)
  return cell_counts
      
def main(file):

    
    img = PIL.Image.open(file)
    response = model.generate_content(["Count the number of blood cells based on this example format: 'RBC: 78\neosinophils: 2\nbasophils: 2\nlymphocytes: 2\nplatelets: 0'", img], stream=True)
    response.resolve()
    text = response.text
    print(text)

    # Count the blood cells.
    cell_counts = count_blood_cells(text)
    return cell_counts
    


if __name__ == "__main__":
    app.run(debug=True)

