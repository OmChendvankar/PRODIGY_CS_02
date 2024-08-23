# Pixel Manipulation Tool for Image Encryption

## Introduction

The **Pixel Manipulation Tool** is a Python application developed using PySide6 that allows users to encrypt and decrypt images. The tool provides two primary encryption methods: pixel value addition and pixel swapping. Users can easily select input and output image files, specify encryption keys, and apply encryption or decryption operations through a graphical user interface (GUI).

## Features

- **Image Encryption & Decryption**: Supports encryption and decryption of images using pixel manipulation techniques.
- **Encryption Methods**:
  - **Add Value**: Adds a specified integer value to each pixel's RGB values.
  - **Swap Pixels**: Swaps pixels in a grid pattern to obscure the image.
- **File Selection**: Users can choose input and output image files through file dialogs.
- **Image Display**: Displays the selected and processed images within the application window.
- **Error Handling**: Provides user feedback in case of invalid inputs or processing errors.

## Usage

1. **Run the Application**:
   - Execute the Python script to start the application window.

2. **Select Input Image**:
   - Click the "Input Image" button to open a file dialog and select the image you want to encrypt or decrypt.
   - The path of the selected image will be displayed next to the button.

3. **Select Output Image**:
   - Click the "Output Image" button to open a file dialog and specify where to save the processed image.
   - The path of the selected save location will be displayed next to the button.

4. **Enter Encryption Key**:
   - Input an integer key into the provided text field. This key will be used for encryption and decryption.

5. **Choose Encryption Method**:
   - Select one of the two methods:
     - **Add Value**: Encrypts or decrypts by adding or subtracting the key value to pixel RGB values.
     - **Swap Pixels**: Encrypts or decrypts by swapping pixels in a grid pattern.

6. **Encrypt or Decrypt Image**:
   - Click the "Encrypt Image" button to apply the selected encryption method to the input image and save it to the specified output location.
   - Click the "Decrypt Image" button to apply the selected decryption method to the input image and save it to the specified output location.

7. **View Processed Image**:
   - The processed image will be displayed in the application window.

## Error Handling

- **No Input Image Selected**: If you try to encrypt or decrypt without selecting an input image, a warning message will be displayed.
- **No Output Location Specified**: If you try to encrypt or decrypt without specifying an output location, a warning message will be displayed.
- **Invalid Key**: If the key is not a valid integer, an error message will be shown.
- **Processing Errors**: Any errors during image processing will be reported with a descriptive error message.

## Requirements

To run this application, you need the following:

- **Python 3.x**: Make sure you have Python installed on your system.
- **PySide6**: This is the Python module used to create the GUI. You can install it using pip:

  ```bash
  pip install PySide6