import os
from PIL import Image
from rembg import remove

def process_image(image_path, output_folder="."):
    """
    This function takes a path to a PNG image, fills transparent areas with black, 
    converts non-transparent areas to white, and saves the result with a prefix.

    Args:
      image_path: Path to the PNG image.
      output_folder: Folder path to save the output image (default is current directory).

    Returns:
      None
    """
    # Extract filename from path
    filename = os.path.basename(image_path)

    # Create output path with prefix and PNG extension
    output_path = os.path.join(output_folder, f"processed_{filename.split('.')[0]}.png")

    # Open the image
    image = Image.open(image_path).convert("RGBA")

    # Get image dimensions
    width, height = image.size

    # Create a black background image (full size)
    background = Image.new("RGBA", (width, height), (0, 0, 0, 255))

    # Create a white mask image (full size) filled with white (255) alpha channel
    mask = Image.new("L", (width, height), 255)

    # Loop through each pixel and modify based on transparency
    for x in range(width):
        for y in range(height):
            # Get pixel value (RGBA)
            r, g, b, a = image.getpixel((x, y))

            # If pixel is transparent (alpha channel is 0)
            if a == 0:
                # Set corresponding pixel in mask to black (0)
                mask.putpixel((x, y), 0)
            else:
                # Set corresponding pixel in mask to white (255)
                mask.putpixel((x, y), 255)
                # Modify pixel value in the original image (set RGB to white)
                image.putpixel((x, y), (255, 255, 255, a))

    # Paste the original image on the black background, using the mask
    background.paste(image, mask=mask)

    # Save the final image as PNG
    background.save(output_path)

    # Print message indicating the path where the image is saved
    print(f"Processed image saved at: {output_path}")

def extract_and_create_masks(project_path):
    input_folder = os.path.join(project_path, "input")
    mask_folder_path = os.path.join(project_path, "masked_images")
    subject_extraction_path = os.path.join(project_path, "subject_extraction")

    os.makedirs(subject_extraction_path, exist_ok=True)
    os.makedirs(mask_folder_path, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(subject_extraction_path, filename.split('.')[0] + '.png')

            # Perform subject extraction using rembg library
            input_image = Image.open(input_path)
            output_image = remove(input_image)

            # Save subject extraction image
            output_image.save(output_path)

            # Process each subject image
            process_image(output_path, mask_folder_path)

    print("Masks generated successfully.")

if __name__ == "__main__":
    print("Please run main.py to generate masks.")
