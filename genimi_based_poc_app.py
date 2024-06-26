import tkinter as tk
import os
import sys
from tkinter import ttk
from PIL import Image, ImageTk
from utils.blood_count_analysis import open_image, analyze_image
from utils.lab_report_analysis import upload_pdf, analyze_pdf, download_sample_pdf
from tkinter import messagebox

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def verify_login(username, password, login_top_level, root):
    # Dummy authentication logic (replace with your own logic)
    if username == "admin" and password == "password":
        login_top_level.destroy()  # Close login window
        root.deiconify()  # Show the main window
    else:
        messagebox.showwarning("Login Failed", "Incorrect username or password")

def login_window(root):
    """
    Creates a top-level window for the login.

    Args:
        root: The root window of the application.

    Returns:
        None
    """
    # Create a top-level window for the login
    login_top_level = tk.Toplevel(root)
    login_top_level.title("Login")
    login_top_level.geometry("300x150")
    login_top_level.grab_set()  # Makes the login window modal

    # Username Entry
    tk.Label(login_top_level, text="Username:").pack(pady=5)
    username_entry = tk.Entry(login_top_level)
    username_entry.pack()

    # Password Entry
    tk.Label(login_top_level, text="Password:").pack(pady=5)
    password_entry = tk.Entry(login_top_level, show="*")
    password_entry.pack()

    # Login Button
    login_button = tk.Button(login_top_level, text="Login", command=lambda: verify_login(username_entry.get(), password_entry.get(), login_top_level, root))
    login_button.pack(pady=10)

def close_app(root):
    # Implement closing application functionality
    root.destroy()

def on_enter(event, widget, color):
    widget.config(bg=color)

def on_leave(event, widget, color):
    widget.config(bg=color)

def create_buttons_tab1(root, left_frame, button_bg, button_fg, hover_color, right_frame, right_bg_color):
    """
    Create buttons for Tab 1.

    Args:
        root: The root window.
        left_frame: The frame where the buttons will be placed.
        button_bg: The background color of the buttons.
        button_fg: The foreground color of the buttons.
        hover_color: The color when the mouse hovers over the buttons.
        right_frame: The frame where the image label will be placed.
        right_bg_color: The background color of the right frame.
    """

    # Styling options
    button_font = ('Helvetica', 12, 'bold')

    # Create a frame for the buttons
    button_frame = tk.Frame(left_frame)
    button_frame.pack(pady=5)

    # Upload Button
    upload_button = tk.Button(button_frame, text="Upload", font=button_font, bg=button_bg, fg=button_fg, relief="raised", borderwidth=2, command=lambda: open_image(image_label))
    upload_button.pack(side="left", padx=5)
    upload_button.bind("<Enter>", lambda e: on_enter(e, upload_button, hover_color))
    upload_button.bind("<Leave>", lambda e: on_leave(e, upload_button, button_bg))

    # Analyze Button
    analyze_button = tk.Button(button_frame, text="Analyze", font=button_font, bg=button_bg, fg=button_fg, relief="raised", borderwidth=2, command=lambda: analyze_image(right_frame, right_bg_color))
    analyze_button.pack(side="left", padx=5)
    analyze_button.bind("<Enter>", lambda e: on_enter(e, analyze_button, hover_color))
    analyze_button.bind("<Leave>", lambda e: on_leave(e, analyze_button, button_bg))

    # Close Button
    close_button = tk.Button(button_frame, text="Close", font=button_font, bg=button_bg, fg=button_fg, relief="raised", borderwidth=2, command=lambda: close_app(root))
    close_button.pack(side="left", padx=5)
    close_button.bind("<Enter>", lambda e: on_enter(e, close_button, hover_color))
    close_button.bind("<Leave>", lambda e: on_leave(e, close_button, button_bg))

    # Label for the uploaded image
    image_label = tk.Label(left_frame)
    image_label.pack(pady=20)

def create_buttons_tab2(root, left_frame, button_bg, button_fg, hover_color, right_frame):
    """
    Create buttons for the second tab.

    Args:
        root (tkinter.Tk): The root window of the application.
        left_frame (tkinter.Frame): The frame where the buttons will be placed.
        button_bg (str): The background color of the buttons.
        button_fg (str): The foreground color (text color) of the buttons.
        hover_color (str): The color of the buttons when hovered.
        right_frame (tkinter.Frame): The frame where the right-side content will be displayed.
    """

    # Styling options
    button_font = ('Helvetica', 12, 'bold')

    # Create a frame for the buttons
    button_frame = tk.Frame(left_frame)
    button_frame.pack(pady=5)

    # Upload Button
    upload_button = tk.Button(button_frame, text="Upload", font=button_font, bg=button_bg, fg=button_fg, relief="raised", borderwidth=2, command=lambda: upload_pdf(right_frame))
    upload_button.pack(side="left", padx=5)
    upload_button.bind("<Enter>", lambda e: on_enter(e, upload_button, hover_color))
    upload_button.bind("<Leave>", lambda e: on_leave(e, upload_button, button_bg))

    # Analyze Button
    analyze_button = tk.Button(button_frame, text="Analyze", font=button_font, bg=button_bg, fg=button_fg, relief="raised", borderwidth=2, command=lambda: analyze_pdf(left_frame))
    analyze_button.pack(side="left", padx=5)
    analyze_button.bind("<Enter>", lambda e: on_enter(e, analyze_button, hover_color))
    analyze_button.bind("<Leave>", lambda e: on_leave(e, analyze_button, button_bg))

    # Close Button
    close_button = tk.Button(button_frame, text="Close", font=button_font, bg=button_bg, fg=button_fg, relief="raised", borderwidth=2, command=lambda: close_app(root))
    close_button.pack(side="left", padx=5)
    close_button.bind("<Enter>", lambda e: on_enter(e, close_button, hover_color))
    close_button.bind("<Leave>", lambda e: on_leave(e, close_button, button_bg))

    # Create a frame for the download button
    download_frame = tk.Frame(left_frame)
    download_frame.pack(side="bottom", pady=(0, 20))  # Pack it to the bottom of the left_frame

    # Download Button
    download_button = tk.Button(download_frame, text="Download Interpreted Lab Report", font=button_font, bg=button_bg, fg=button_fg, relief="raised", borderwidth=2, command=download_sample_pdf)
    download_button.pack(side="bottom", padx=5)  # Pack it to the bottom of download_frame
    download_button.bind("<Enter>", lambda e: on_enter(e, download_button, hover_color))
    download_button.bind("<Leave>", lambda e: on_leave(e, download_button, button_bg))

def main():
    try:
        root = tk.Tk()
        root.title("HemoCountAI")
        root.geometry("800x600")

    # Initialize the login window
        login_window(root)
        
        # Create a Notebook
        notebook = ttk.Notebook(root)
        notebook.pack(fill='both', expand=True)

        # First tab - Existing functionality
        existing_tab = ttk.Frame(notebook)
        notebook.add(existing_tab, text='Blood Count')

    

        # Styling options
        button_fg =  '#ffffff'
        hover_color = "#FFA500" #'#36648b'
        right_bg_color = '#333333'

        # Create a frame for the left side elements (Image and Message)
        left_frame = tk.Frame(existing_tab)
        left_frame.pack(side="left", fill="both", expand=True)

        # Create a frame for the right side elements (Logo and Buttons)
        right_frame = tk.Frame(existing_tab, bg=right_bg_color)
        right_frame.pack(side="right", fill="both", expand=True)

        # Get the dominant color from the logo
        #dominant_color = get_dominant_color(logo_path)
        button_bg = "#FFA500" #'#36648b' #'#{:02x}{:02x}{:02x}'.format(*dominant_color)  # Convert RGB to hex

        # Load the logo
        logo_image = Image.open(resource_path("logo.png"))
        logo_image.thumbnail((200, 200))  # Resize if necessary
        logo_photo = ImageTk.PhotoImage(logo_image)

        # Display the logo
        logo_label = tk.Label(left_frame, image=logo_photo)
        logo_label.image = logo_photo
        logo_label.pack(pady=10)

        # Label for the final message
        message_label = tk.Label(left_frame, text="Upload a thin blood smear image to count the number of blood cells")
        message_label.pack(pady=10)


        # Create buttons for the first tab
        create_buttons_tab1(root, left_frame, button_bg, button_fg, hover_color, right_frame, right_bg_color)

        # Second tab - Exactly like the first tab
        existing_tab_2 = ttk.Frame(notebook)
        notebook.add(existing_tab_2, text='Lab Report')

        # Create a frame for the left side elements (Image and Message)
        left_frame_2 = tk.Frame(existing_tab_2)
        left_frame_2.pack(side="left", fill="both", expand=True)

        # Create a frame for the right side elements (Logo and Buttons)
        right_frame_2 = tk.Frame(existing_tab_2, bg=right_bg_color)
        right_frame_2.pack(side="right", fill="both", expand=True)

        # Display the logo
        logo_label_2 = tk.Label(left_frame_2, image=logo_photo)
        logo_label_2.image = logo_photo
        logo_label_2.pack(pady=10)

        # Label for the final message
        message_label_2 = tk.Label(left_frame_2, text="Upload a pdf of lab report to analyze")
        message_label_2.pack(pady=5)


        # Create buttons for the second tab
        create_buttons_tab2(root, left_frame_2, button_bg, button_fg, hover_color, right_frame_2)

        root.mainloop()
    except Exception as e:
        messagebox.showwarning("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()
