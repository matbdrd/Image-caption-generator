# Image Captioning Tool

## Overview

This Image Captioning Tool is a Python-based application that generates textual descriptions for images using advanced AI models. It supports a wide range of image formats, including RAW files from various camera manufacturers, and provides an easy-to-use interface for batch processing multiple images.

## Features

- Support for multiple image formats: PNG, JPEG, TIFF, PSD, DNG, NEF (Nikon), CR2 (Canon), ARW (Sony)
- Utilizes the BLIP2 (Salesforce/blip2-opt-2.7b) model for high-quality image captioning
- GPU acceleration support for faster processing
- Batch processing of multiple images
- Automatic saving of captions as text files alongside the original images
- Clipboard integration for easy access to generated captions
- Cross-platform compatibility (Windows, macOS, Linux)

## Requirements

- Python 3.7+
- PyTorch
- Transformers library
- Pillow (PIL)
- tkinter
- pyperclip
- rawpy
- psd-tools

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/image-captioning-tool.git
   cd image-captioning-tool
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install torch transformers Pillow tkinter pyperclip rawpy psd-tools
   ```

## Usage

1. Run the script:
   ```
   python main.py
   ```

2. The application will initialize and load the necessary models. This may take a few moments.

3. A file dialog will open, allowing you to select one or multiple images for captioning.

4. The tool will process each image, generating captions and saving them as text files in the same directory as the original images.

5. All generated captions will be copied to your clipboard for easy access.

6. The process will repeat, allowing you to select more images or exit the application.

## How It Works

1. The tool uses the BLIP2 model, a state-of-the-art AI for image captioning.
2. Images are loaded and preprocessed to be compatible with the model.
3. The model generates a textual description for each image.
4. Captions are saved as text files and copied to the clipboard.

## Customization

You can modify the `main.py` script to adjust various parameters:

- Change the model by updating the `setup_model()` function.
- Adjust the maximum caption length by modifying the `max_new_tokens` parameter in the `generate_caption()` function.
- Add support for additional image formats in the `select_image_files()` and `load_image()` functions.

## Troubleshooting

- If you encounter memory issues with large images, try adjusting the `Image.MAX_IMAGE_PIXELS` value.
- For GPU-related issues, ensure you have the correct CUDA version installed for your PyTorch installation.

## Contributing

Contributions to improve the Image Captioning Tool are welcome. Please feel free to submit pull requests or open issues to discuss proposed changes.

## License

[Specify your license here, e.g., MIT, GPL, etc.]

## Acknowledgments

- This project uses the BLIP2 model developed by Salesforce Research.
- Thanks to the open-source community for the various libraries used in this project.
