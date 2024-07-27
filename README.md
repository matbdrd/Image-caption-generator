# Image Caption Generator

This project is an Image Caption Generator that uses the BLIP2 (Bootstrapping Language-Image Pre-training) model to generate descriptive captions for images. It supports various image formats, including RAW and PSD files, and is optimized for different hardware configurations, including Apple Silicon.

## Features

- Supports multiple image formats: PNG, JPEG, TIFF, PSD, and various RAW formats (NEF, CR2, ARW, DNG)
- Utilizes the BLIP2 model for accurate image captioning
- Optimized for different hardware: CUDA GPUs, Apple Silicon (M1/M2/M3), and CPU
- Batch processing of multiple images
- Automatically saves captions as text files alongside the original images
- Copies all generated captions to the clipboard for easy sharing

## Requirements

- Python 3.9+
- PyTorch
- Transformers
- Pillow
- tkinter
- pyperclip
- rawpy
- psd-tools

For a complete list of dependencies, see the `requirements.txt` file.

## Disk space
You'll need around 16 Go of disk space to install the models.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/image-caption-generator.git
   cd image-caption-generator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script using Python:

```
python main.py
```

The program will guide you through the following steps:

1. It will print version information and set up the model.
2. A file dialog will open, allowing you to select one or more image files.
3. For each selected image, the program will:
   - Generate a caption
   - Save the caption to a .txt file next to the original image
   - Display the caption in the console
4. All generated captions will be copied to your clipboard.
5. The program will then allow you to select more images or exit.

## Supported Image Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)
- TIFF (.tif, .tiff)
- PSD (.psd)
- RAW formats:
  - Nikon (.nef)
  - Canon (.cr2)
  - Sony (.ARW)
  - Adobe Digital Negative (.dng)

## Hardware Optimization

The script automatically detects your hardware configuration and optimizes accordingly:

- For NVIDIA GPUs, it uses CUDA acceleration.
- For Apple Silicon (M1/M2/M3), it uses Metal Performance Shaders (MPS) if available.
- If no compatible GPU is found, it falls back to CPU processing.

## Troubleshooting

- If you encounter memory issues with large images, the script already sets `Image.MAX_IMAGE_PIXELS = None`. However, be cautious when processing extremely large images, as this can consume a lot of memory.
- Ensure you have the latest version of PyTorch installed, especially if you're using Apple Silicon.
- For RAW file support, make sure you have the necessary system libraries installed for rawpy.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

