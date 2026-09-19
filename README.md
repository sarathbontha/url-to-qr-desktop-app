# URL to QR Maker

## About the Project

URL to QR Maker is a simple desktop application developed using Python. The application converts a website address entered by the user into a QR code.

The user can enter a valid URL, create the QR code, preview the result inside the application, and save the generated QR code as an image. The project provides a simple way to understand how QR code generation works in Python.

## Main Features

* Enter a website address
* Check whether the entered URL is valid
* Generate a QR code from the URL
* Preview the QR code in the application
* Save the generated QR code as a PNG image
* Reset the application to create another QR code
* Show messages when the input is empty or incorrect

## Technologies

This project uses:

* Python 3
* Tkinter for the graphical user interface
* qrcode for creating QR codes
* Pillow for displaying and working with images
* Visual Studio Code for development
* GitHub for sharing the project

## Project Files

```text id="h2sf95"
url-to-qr-desktop-app/
├── main.py
├── requirements.txt
├── README.md
└── output/
    └── qr_output.png
```

## Required Libraries

The following libraries are included in `requirements.txt`:

```text id="urvwh3"
qrcode[pil]
Pillow
```

Install them by running:

```bash id="aegdxq"
python3 -m pip install -r requirements.txt
```

## Running the Program

Open the project folder in the terminal and run:

```bash id="nlqycj"
python3 main.py
```

The URL to QR Maker application window will open.

## Using the Application

Enter a website address beginning with `http://` or `https://`.

For example:

```text id="w43wsl"
https://www.python.org/
```

Click **Create QR** to generate the QR code.

The generated QR code will be displayed inside the application. It can be scanned using a mobile phone to verify that it opens the correct website.

The QR code can also be saved as a PNG image for later use.

## Input Checking

The application checks the information entered by the user before creating the QR code. If the URL field is empty or the website address is not valid, the program displays a message asking the user to correct the input.

This prevents the application from creating a QR code from incorrect information.

## Output

After a valid URL is entered, the application creates and displays the QR code. A screenshot of the completed application is included with the assignment documentation.

## Purpose

The purpose of this project is to practice Python programming by developing a small working application. Through this project, I learned how to accept user input, validate a URL, generate QR codes, display images using Tkinter, and save generated images.

## Conclusion

The URL to QR Maker provides a simple method for converting website addresses into QR codes. The project demonstrates how Python libraries can be combined to create a useful desktop application with a graphical user interface.
