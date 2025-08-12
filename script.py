from PIL import Image
import os

def gif_to_png(gif_path, output_folder):
    """
    Converts a GIF file into a sequence of PNG images.

    Args:
        gif_path (str): The path to the input GIF file.
        output_folder (str): The folder where the output PNG files will be saved.
    """
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Open the GIF file
        with Image.open(gif_path) as im:
            # Loop through each frame of the GIF
            for i in range(im.n_frames):
                # Seek to the next frame
                im.seek(i)

                # Create the output filename
                output_path = os.path.join(output_folder, f"frame_{i:03d}.png")

                # Save the current frame as a PNG file
                im.save(output_path, "PNG")

        print(f"Successfully converted {im.n_frames} frames from '{gif_path}' to PNGs in '{output_folder}'")

    except FileNotFoundError:
        print(f"Error: The file '{gif_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Configuration ---
# EDIT THESE VALUES
# Set the path to your input GIF file.
input_gif = "path/to/your/animation.gif"

# Set the path to the folder where you want to save the PNG frames.
output_png_folder = "path/to/your/output_frames"
# --------------------

# Run the conversion
gif_to_png(input_gif, output_png_folder)
