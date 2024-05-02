import winreg
import google.generativeai as genai
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.font as tkFont
from collections import Counter
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.image_processing import detect_blood_cell
import glob

reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")

downloads_path = winreg.QueryValueEx(reg_key, "{374DE290-123F-4565-9164-39C4925E467B}")[0]

winreg.CloseKey(reg_key)

GOOGLE_API_KEY  = (os.environ.get('GOOGLE_API_KEY_FILE'))

def count_blood_cells(text):
    blood_counts = {}

    # Split the text by newline character
    lines = text.split('\n')

    for line in lines:
        # Split each line by colon
        parts = line.split(':')
        if len(parts) == 2:
            blood_cell_type = parts[0].strip().replace('-', '')  # Replace dash with underscore
            count_info = parts[1].strip().split('(')
            blood_count = int(count_info[0].replace(',', ''))  # Remove commas from count
            blood_counts[blood_cell_type] = blood_count

            if len(count_info) > 1:
                percentage = float(count_info[1].strip('%)'))
                blood_counts[f'{blood_cell_type}_percentage'] = percentage

    return blood_counts

# Global variable to hold the original image
original_image = None

def open_image(root, image_label):
    global original_image

    input_path = filedialog.askopenfilename()
    detect_blood_cell(input_path, downloads_path)
    file_path = glob.glob(os.path.join(downloads_path, "processed_image/", '*.jpg'))[0]

    if file_path:
        original_image = Image.open(file_path)
        thumbnail = original_image.copy()
        thumbnail.thumbnail((1050, 1050))  # Resize the image for display
        photo = ImageTk.PhotoImage(thumbnail)
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection

def analyze_image(image_label, right_frame, right_bg_color):
    global original_image
    genai.configure(api_key=GOOGLE_API_KEY)

    # Check if an image has been loaded
    if original_image is None:
        messagebox.showinfo("No Image", "Please upload an image first.")
        return

    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(["Count the number of blood cells based on this example format -RBC: 78\n-WBCs: 2\n-platelets: 0", original_image], stream=True)
    response.resolve()
    msg = response.text
    print(msg)
    
                
    # Count the blood cells.
    cell_counts = count_blood_cells(response.text)
    print(cell_counts)
    #cell_counts = {"Type1": 30, "Type2": 45, "Type3": 25}
    # Create a new dataframe with the cell counts.
    df = pd.DataFrame.from_dict(cell_counts, orient='index', columns=['Count'])

    # Set the color palette and create the pie chart.
    colors = sns.color_palette('Reds_d', len(df))
    fig = Figure(figsize=(4, 2.5), facecolor=right_bg_color)  # Set the facecolor to right_bg_color
    ax = fig.add_subplot(111)
    textprops = {"color": "white"}
    print(df)
    ax.pie(df['Count'], labels=df.index, autopct='%1.1f%%', colors=colors, startangle=90, pctdistance=0.85, textprops=textprops)
    ax.text(0, 0, "Complete Blood Count", fontsize=16, ha='center', va='center', color='white')  # Add the text in the middle with white color
    # Draw a circle at the center of pie to create a donut chart
    
    centre_circle = plt.Circle((0,0),0.70,fc=right_bg_color)
    fig.gca().add_artist(centre_circle)
    #ax.set_title('Blood Count Chart')
    ax.axis('equal')

    # Embedding the plot into Tkinter
    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas_widget = canvas.get_tk_widget()
    #canvas_widget.pack(side='top', fill='both', expand=True)
    canvas_widget.pack(side='top', fill='both', expand=True, pady=2)

    message_label = tk.Label(right_frame, text=msg, bg=right_bg_color, fg='white')
    message_label.pack(pady=2)  # Place the label below the image