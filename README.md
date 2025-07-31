# 🖼️ GIF to PNG Frame Extractor

A simple and efficient Python script that extracts every frame from an animated GIF and saves each one as a separate, sequentially-named PNG file.

---
## 🚀 Demo

![GIF Maker Demo](https://raw.githubusercontent.com/Bhuvan-kio/GIF-Maker/refs/heads/main/Output.gif) --> (https://raw.githubusercontent.com/Bhuvan-kio/GIF-to-PNG-Converter/refs/heads/main/PNGs/frame_000.png)

---
## ✨ Features

-   **Frame Extraction**: Converts any animated GIF into a full sequence of PNG images.
-   **Automated Folder Creation**: Automatically creates the output directory if it doesn't already exist.
-   **Sequential Naming**: Saves frames with clear, padded filenames (e.g., `frame_000.png`, `frame_001.png`) for easy sorting.
-   **Minimal Dependencies**: Relies only on the standard and powerful **Pillow** library.

---

## 🛠️ Prerequisites

Before you begin, ensure you have Python 3 and the Pillow library installed on your system.

1.  **Python 3**: If you don't have it, [download it here](https://www.python.org/downloads/).
2.  **Pillow Library**: Install it using pip with the following command in your terminal:
    ```bash
    pip install Pillow
    ```

---

## 🚀 How to Use

1.  **Place Your GIF**: Have your input GIF file ready (e.g., `my_animation.gif`).

2.  **Configure the Script**: Open the Python script (`gif_to_png_converter.py` or similar) and edit the configuration variables at the bottom of the file:

    ```python
    # --- Configuration ---
    # ❗️ EDIT THESE VALUES

    # Set the path to your input GIF file.
    input_gif = "path/to/your/animation.gif"

    # Set the path to the folder where you want to save the PNG frames.
    output_png_folder = "path/to/your/output_frames"
    # --------------------
    ```

3.  **Run the Script**: Execute the script from your terminal.
    ```bash
    python your_script_name.py
    ```

The script will create the specified output folder and populate it with all the frames from your GIF, saved as individual PNG files.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
