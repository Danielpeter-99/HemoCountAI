import google.generativeai as genai
import os
import PIL.Image
import re
from flask_cors import CORS
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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
  return cell_counts

# def plot_pie_chart(cell_counts):
#     # prompt: make the pie chart look better with different shades of reds and the text within the chart white
#     # Create a new dataframe with the cell counts.
#     df = pd.DataFrame.from_dict(cell_counts, orient='index', columns=['Count'])
#     print(df)

    # # Set the color palette.
    # colors = sns.color_palette('Reds_d', len(df))

    # # Create the pie chart.
    # plt.figure(figsize=(10, 6))
    # plt.pie(df['Count'], labels=df.index, autopct='%1.1f%%', colors=colors)

    # # Add a white circle in the center.
    # centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    # fig = plt.gcf()
    # fig.gca().add_artist(centre_circle)

    # # Equal aspect ratio ensures a circular pie chart.
    # plt.axis('equal')

    # # Set the title.
    # plt.title('Blood Count Chart')

    # # Improve the aesthetics.
    # plt.tight_layout()

    # # Show the plot.
    # plt.show()
      
def main(file):

    
    img = PIL.Image.open(file)
    response = model.generate_content(["Count the number of blood cells, and how many of each types", img], stream=True)
    response.resolve()
    text = response.text

    # Count the blood cells.
    cell_counts = count_blood_cells(text)
    return cell_counts

    # # Plot pie chart of the cell counts.
    # plot_pie_chart(cell_counts)
    
    serve_image('plot.png')
    


if __name__ == "__main__":
    app.run(debug=True)

