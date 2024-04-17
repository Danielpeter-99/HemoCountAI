import google.generativeai as genai
import os
import PIL.Image
import re
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def count_blood_cells(text):
  # Use a regular expression to extract the counts for each type of blood cell.
  counts = re.findall(r'(\d+)\s+(\w+)', text)

  # Create a dictionary to store the counts.
  cell_counts = {}
  for count, cell_type in counts:
    cell_counts[cell_type] = int(count)

  # Return the dictionary of cell counts.
  return cell_counts

def plot_pie_chart(cell_counts):
    # prompt: make the pie chart look better with different shades of reds and the text within the chart white
    # Create a new dataframe with the cell counts.
    df = pd.DataFrame.from_dict(cell_counts, orient='index', columns=['Count'])

    # Set the color palette.
    colors = sns.color_palette('Reds_d', len(df))

    # Create the pie chart.
    plt.figure(figsize=(10, 6))
    plt.pie(df['Count'], labels=df.index, autopct='%1.1f%%', colors=colors)

    # Add a white circle in the center.
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Equal aspect ratio ensures a circular pie chart.
    plt.axis('equal')

    # Set the title.
    plt.title('Blood Count Chart')

    # Improve the aesthetics.
    plt.tight_layout()

    # Show the plot.
    plt.show()
  
def main():

    GOOGLE_API_KEY  = (os.environ.get('GOOGLE_API_KEY_FILE'))
    genai.configure(api_key=GOOGLE_API_KEY)

    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    model = genai.GenerativeModel('gemini-pro-vision')
    img = PIL.Image.open('data/HRI001.jpg')
    response = model.generate_content(["Count the number of blood cells, and how many of each types", img], stream=True)
    response.resolve()
    text = response.text

    # Count the blood cells.
    cell_counts = count_blood_cells(text)
    print(cell_counts)

    # Plot pie chart of the cell counts.
    plot_pie_chart(cell_counts)

if __name__ == "__main__":
    main()

