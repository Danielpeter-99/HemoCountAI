# HemoCountAI
HemoCountAI for Microsoft Generative AI Hackathon

## App POC:
![image](https://github.com/Danielpeter-99/HemoCountAI/assets/38712706/7730907b-5617-45ba-a292-f99951188380)

**This application, coded in Python with Tkinter for the GUI, appears to be a blood cell counting tool named "HemoCountAI". The key features and functionalities are as follows:**

**Login System: It has a simple login system where users can enter a username and password. The login is verified against preset credentials (in this case, 'admin' and 'password'). After successful login, the user is directed to the main window of the application.

**Image Upload and Display: Users can upload an image, likely of a blood sample. The uploaded image is then displayed in the GUI.

**Image Analysis: The core feature of the application is analyzing the uploaded image to count different types of blood cells. It uses a generative AI model from Google (Google's Gemini Pro Vision API) to process the image and extract text information about the count and percentages of various blood cells.

**Data Visualization: After analysis, the application generates a pie chart showing the count and percentages of different blood cell types using matplotlib. The pie chart is displayed in the GUI.

**Interactive GUI Components: The GUI includes interactive elements like buttons for uploading images, analyzing them, and closing the application. These buttons change color when hovered over, enhancing user experience.

**Styling and Layout: The application has a left frame for image and message display, and a right frame for other controls and displays. It uses custom styling for buttons and other GUI components.

**API Integration: The application integrates with Google's generative AI API for image analysis, demonstrating how external APIs can be used to enhance the functionality of an application.

## Back-end Installation

```bash 
  cd HemoCountAi/
  pip install -r requirements.txt
  python test-genimi-api.py
```

## Front-end installation

```bash
  cd HemoCountAi/frontend
  npm install
  npm run dev
```

## Environment Variables

`GOOGLE_API_KEY_FILE`