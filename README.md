# Smart QR Code Generator

## Project Overview

Smart QR Code Generator is a Python desktop application that generates a QR code from a website URL entered by the user. The application provides a simple graphical user interface where users can enter a URL, generate a QR code, preview it, and save the generated QR code as a PNG image.

The project demonstrates the use of Python GUI development, QR code generation, input validation, file handling, and error handling.

## Features

* Simple graphical user interface
* Accepts website URLs from the user
* Validates the entered URL
* Generates QR codes dynamically
* Displays the generated QR code inside the application
* Allows users to save the QR code as a PNG file
* Automatically creates a unique filename using date and time
* Clear option to reset the application
* Displays error messages for invalid or empty URLs
* Supports both HTTP and HTTPS URLs

## Technologies Used

* Python 3
* Tkinter
* qrcode
* Pillow (PIL)
* Visual Studio Code
* Git
* GitHub

## Project Structure

```text
SmartQRGenerator/
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    └── qr_generator_output.png
```

## Installation

Clone or download the project and open the project directory.

Install the required Python libraries:

```bash
python3 -m pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
qrcode[pil]
Pillow
```

## Running the Application

Run the application using:

```bash
python3 app.py
```

The Smart QR Code Generator window will open.

## How to Use

1. Enter a valid website URL beginning with `http://` or `https://`.
2. Click **Generate QR Code**.
3. The generated QR code will appear in the application.
4. Scan the QR code to verify that it opens the correct website.
5. Click **Save QR Code** to save it as a PNG image.
6. Click **Clear** to reset the application and generate another QR code.

## Example

Example URL:

```text
https://www.bioxsystems.com/
```

The application generates a QR code containing this URL. When the QR code is scanned, the user is directed to the corresponding website.

## Input Validation

The application checks whether the URL is empty or invalid before generating a QR code. A valid URL must use either the HTTP or HTTPS protocol and contain a website address.

This validation helps prevent QR codes from being generated from incorrect input.

## Application Output

A screenshot of the working application is available in the `screenshots` directory.

## Conclusion

The Smart QR Code Generator demonstrates how Python can be used to build a practical desktop application. The project combines Tkinter for the graphical user interface, the qrcode library for QR code generation, and Pillow for image processing and preview functionality.

The application provides an easy way to convert website URLs into machine-readable QR codes and save them for future use.
