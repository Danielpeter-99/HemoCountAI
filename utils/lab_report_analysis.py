import google.generativeai as genai
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import Image
import PyPDF2
from tkinter import filedialog
from reportlab.pdfgen import canvas
import io
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader

GOOGLE_API_KEY  = (os.environ.get('GOOGLE_API_KEY_FILE'))


pdf_path = None
pdf_text = None
pdf_image = None
def upload_pdf(root, right_frame):
    global pdf_path
    global pdf_text
    global pdf_image
    pdf_path = filedialog.askopenfilename()
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        pdf_text = text

    file_path = "data/lab-reports/CBC-sample-report-with-notes-scaled.jpg"
    if file_path:
        original_image = Image.open(file_path)
        thumbnail = original_image.copy()
        thumbnail.thumbnail((1050, 1050))  # Resize the image for display
        pdf_image = ImageTk.PhotoImage(thumbnail)

    image_label = tk.Label(right_frame, image=pdf_image)
    image_label.pack(pady=20)

answer = None
def generate_answer(question, text, left_frame):
    global answer
    genai.configure(api_key=GOOGLE_API_KEY)
    
    print(text)
    print(question)
    prompt =  f"Question: {question}\nContext: {text}\nAnswer:" 

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, text], stream=True)
    response.resolve()
    answer = response.text

    print(answer)
    message_label = tk.Label(left_frame, text=answer, fg='black', font=("Times New Roman", 10), wraplength=400)
    message_label.pack(pady=25)  # Place the label below the image

def analyze_pdf(left_frame):
    question = "Highligh abnormal lab results in bullet points. Give brief feedback for the patient (not using you) in bullet points like a 10-year experience doctor."
    print(question)
    if question:
        generate_answer(question, pdf_text, left_frame)


# Function to open the sample PDF file in a web browser
def download_sample_pdf():
    # Open the PDF file in read-binary mode

    # read your existing PDF
    existing_pdf = PdfReader(open(pdf_path, "rb"))
    
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(22 * 72, 11 * 72))
    # Create a canvas with letter size in landscape orientation
    # Calculate the center coordinates of the page
    center_x = letter[1] / 2 + 300
    center_y = letter[0] / 2 + 300
    
    # Split the answer text into lines
    lines = answer.split('\n')

    # Calculate the starting y-coordinate for the text to be centered vertically
    # Adjust y_start based on the number of lines
    line_height = 12  # Adjust as needed
    total_height = len(lines) * line_height
    y_start = center_y + total_height / 2

    # Draw each line of text at the center of the page
    for line in lines:
        text_width = can.stringWidth(line)
        x_start = center_x - (text_width / 2)
        can.drawString(x_start, y_start, line)
        y_start -= line_height  # Move to the next line

    can.save()    
    # move to the beginning of the StringIO buffer
    packet.seek(0)    
    # create a new PDF with Reportlab
    new_pdf = PdfReader(packet)
    output = PdfWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    # Add a blank page to the output PDF
    #output.add_blank_page(width=612, height=792)
    page = new_pdf.pages[-1]
    page.merge_page(new_pdf.pages[-1])
    output.add_page(page)
    output.append_pages_from_reader(existing_pdf)
    # Write the modified PDF to a new file
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialfile="amended_pdf")
    print(output_path)
    with open(output_path, 'wb') as output_file:
        output.write(output_file)
    print("New page added successfully. Modified PDF saved as:", output_path)