import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode
from urllib.parse import urlparse
from datetime import datetime
import os


class QRCodeGeneratorApp:
    """
    Desktop application for generating QR codes from website URLs.
    """

    def __init__(self, root):
        """Initialize the QR Code Generator application."""

        self.root = root
        self.root.title("Smart QR Code Generator")
        self.root.geometry("600x750")
        self.root.resizable(False, False)

        # Stores the currently generated QR image.
        self.qr_image = None

        # Stores the Tkinter-compatible preview image.
        self.preview_image = None

        # Create all application components.
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange all GUI components."""

        # Main heading
        title_label = tk.Label(
            self.root,
            text="Smart QR Code Generator",
            font=("Arial", 24, "bold")
        )
        title_label.pack(pady=(30, 5))

        # Description
        description_label = tk.Label(
            self.root,
            text="Enter a website URL and generate a QR code instantly.",
            font=("Arial", 11)
        )
        description_label.pack(pady=(0, 25))

        # URL input section
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        url_label = tk.Label(
            input_frame,
            text="Website URL:",
            font=("Arial", 12, "bold")
        )
        url_label.pack(anchor="w")

        self.url_entry = tk.Entry(
            input_frame,
            width=55,
            font=("Arial", 12)
        )
        self.url_entry.pack(pady=8, ipady=6)

        # Example URL
        example_label = tk.Label(
            input_frame,
            text="Example: https://www.bioxsystems.com/",
            font=("Arial", 9)
        )
        example_label.pack(anchor="w")

        # Generate button
        generate_button = tk.Button(
            self.root,
            text="Generate QR Code",
            font=("Arial", 12, "bold"),
            width=22,
            height=2,
            command=self.generate_qr
        )
        generate_button.pack(pady=20)

        # QR preview area
        self.preview_frame = tk.Frame(
            self.root,
            width=300,
            height=300,
            relief="solid",
            borderwidth=1
        )
        self.preview_frame.pack(pady=10)
        self.preview_frame.pack_propagate(False)

        self.qr_label = tk.Label(
            self.preview_frame,
            text="Your QR Code\nwill appear here",
            font=("Arial", 13)
        )
        self.qr_label.pack(expand=True)

        # Status message
        self.status_label = tk.Label(
            self.root,
            text="Ready to generate QR code",
            font=("Arial", 10)
        )
        self.status_label.pack(pady=10)

        # Bottom buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        self.save_button = tk.Button(
            button_frame,
            text="Save QR Code",
            width=16,
            height=2,
            command=self.save_qr,
            state="disabled"
        )
        self.save_button.grid(row=0, column=0, padx=8)

        clear_button = tk.Button(
            button_frame,
            text="Clear",
            width=16,
            height=2,
            command=self.clear_form
        )
        clear_button.grid(row=0, column=1, padx=8)

        # Footer
        footer_label = tk.Label(
            self.root,
            text="Python QR Code Generator",
            font=("Arial", 9)
        )
        footer_label.pack(side="bottom", pady=15)

        # Put cursor directly in URL box.
        self.url_entry.focus()

        # Pressing Enter also generates QR code.
        self.root.bind("<Return>", lambda event: self.generate_qr())

    @staticmethod
    def is_valid_url(url):
        """
        Validate the URL.

        A valid URL must contain:
        - http:// or https://
        - a website/domain
        """

        try:
            parsed_url = urlparse(url)

            return (
                parsed_url.scheme in ("http", "https")
                and bool(parsed_url.netloc)
            )

        except ValueError:
            return False

    def generate_qr(self):
        """Generate a QR code using the URL entered by the user."""

        url = self.url_entry.get().strip()

        # Check for empty input.
        if not url:
            messagebox.showwarning(
                "Missing URL",
                "Please enter a website URL."
            )
            return

        # Validate URL before creating the QR code.
        if not self.is_valid_url(url):
            messagebox.showerror(
                "Invalid URL",
                "Please enter a valid URL starting with "
                "http:// or https://"
            )
            return

        try:
            # Create QRCode configuration.
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4
            )

            # Add URL information to QR code.
            qr.add_data(url)

            # Automatically calculate required QR size.
            qr.make(fit=True)

            # Create black-and-white QR image.
            self.qr_image = qr.make_image(
                fill_color="black",
                back_color="white"
            ).convert("RGB")

            # Create a copy for the application preview.
            preview = self.qr_image.copy()

            # Resize preview without changing the original image.
            preview.thumbnail((270, 270))

            # Convert PIL image so Tkinter can display it.
            self.preview_image = ImageTk.PhotoImage(preview)

            # Display QR code.
            self.qr_label.config(
                image=self.preview_image,
                text=""
            )

            # Enable Save button.
            self.save_button.config(state="normal")

            self.status_label.config(
                text="QR Code generated successfully!"
            )

        except Exception as error:
            messagebox.showerror(
                "Generation Error",
                f"Unable to generate QR code.\n\n{error}"
            )

    def save_qr(self):
        """Save the generated QR code to the user's computer."""

        if self.qr_image is None:
            messagebox.showwarning(
                "No QR Code",
                "Please generate a QR code first."
            )
            return

        # Create a unique filename using date and time.
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        default_filename = f"qr_code_{timestamp}.png"

        # Let the user choose the save location.
        file_path = filedialog.asksaveasfilename(
            title="Save QR Code",
            defaultextension=".png",
            initialfile=default_filename,
            filetypes=[
                ("PNG Image", "*.png"),
                ("All Files", "*.*")
            ]
        )

        # User may cancel the Save dialog.
        if not file_path:
            return

        try:
            self.qr_image.save(file_path)

            self.status_label.config(
                text=f"Saved: {os.path.basename(file_path)}"
            )

            messagebox.showinfo(
                "Saved Successfully",
                "Your QR code has been saved successfully."
            )

        except OSError as error:
            messagebox.showerror(
                "Save Error",
                f"Unable to save the QR code.\n\n{error}"
            )

    def clear_form(self):
        """Clear URL, QR preview, and status information."""

        self.url_entry.delete(0, tk.END)

        self.qr_label.config(
            image="",
            text="Your QR Code\nwill appear here"
        )

        self.qr_image = None
        self.preview_image = None

        self.save_button.config(state="disabled")

        self.status_label.config(
            text="Ready to generate QR code"
        )

        self.url_entry.focus()


def main():
    """Start the QR Code Generator application."""

    root = tk.Tk()

    QRCodeGeneratorApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()