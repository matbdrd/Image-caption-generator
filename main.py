import torch
from transformers import AutoProcessor, Blip2ForConditionalGeneration
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import pyperclip
import rawpy
from psd_tools import PSDImage

# Increase the pixel limit
Image.MAX_IMAGE_PIXELS = None  # This will remove the limit

def print_versions():
    """Print versions of torch and CUDA."""
    print(torch.__version__)
    print(torch.version.cuda)
    print(f"Torch version : {torch.version.cuda}")
    print(f"CUDA avail : {torch.cuda.is_available()}")


def select_image_files():
    """Open a GUI window to select multiple local image files and return their paths."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    file_types = [
        ("All supported formats", "*.png *.jpg *.jpeg *.psd *.nef *.cr2 *.ARW *.tif *.tiff *.dng"),
        ("PNG files", "*.png"),
        ("JPEG files", "*.jpg *.jpeg"),
        ("TIFF files", "*.tif *.tiff"),
        ("PSD files", "*.psd"),
        ("RAW files", "*.nef *.cr2 *.ARW *.dng"),
        ("All files", "*.*")
    ]
    
    try:
        file_paths = filedialog.askopenfilenames(
            title="Select images",
            filetypes=file_types
        )
    except Exception as e:
        print(f"Error in file dialog: {e}")
        file_paths = []
    
    root.destroy()  # Explicitly destroy the root after use
    return file_paths



def load_image(image_path):
    """Load and convert image from the given path."""

    if image_path.lower().endswith('.psd'):
        # Load and convert the .psd file
        psd = PSDImage.open(image_path)
        image = psd.composite()  # This returns a PIL Image
    elif image_path.lower().endswith(('.nef', '.cr2', '.ARW', '.dng')):  # Add other RAW formats as needed
        # Load and convert the RAW file
        with rawpy.imread(image_path) as raw:
            rgb = raw.postprocess()
        image = Image.fromarray(rgb)
    else:
        # For regular image formats like .jpg, .png, .tif
        image = Image.open(image_path).convert('RGB')

    return image


def setup_model():
    """Load the model and processor, and set the device."""
    processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
    model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    return model, processor, device


def generate_caption(model, processor, device, image):
    """Process the image and generate a caption."""
    inputs = processor(image, return_tensors="pt").to(device)
    generated_ids = model.generate(**inputs, max_new_tokens=100)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
    final_caption = generated_text + "" # Add model name
    return final_caption


def save_caption_to_file(image_path, caption):
    """Save the generated caption to a .txt file next to the image."""
    # Derive the base path (without extension) of the image
    base_path = ".".join(image_path.split(".")[:-1])
    # Append .txt to create the filename for the text file
    txt_file_path = base_path + ".txt"

    with open(txt_file_path, 'w') as f:
        f.write(caption)


def main():
    print_versions()
    print("1. Setting up...")
    model, processor, device = setup_model()
    print(f"Using device: {device}")

    accumulated_captions = ""

    while True:
        print("2. Selecting image from local system...")
        image_paths = select_image_files()
        if not image_paths:  # If the user cancels the file dialog, exit the loop.
            break

        for image_path in image_paths:
            image = load_image(image_path)

            print(f"3. Generating caption for {image_path}...")
            caption = generate_caption(model, processor, device, image)
            print("Caption generated:")
            print(caption)

            # Save caption to a .txt file next to the image
            save_caption_to_file(image_path, caption)

            # Accumulate captions
            accumulated_captions += caption + "\n"  # Separate captions with two newlines

        # Copy accumulated captions to clipboard
        pyperclip.copy(accumulated_captions)

        print("Captions copied to clipboard and saved to file. Ready for the next image...")

    # Clear GPU cache
    torch.cuda.empty_cache()



if __name__ == "__main__":
    main()

