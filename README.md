# Image Compression Tool
A Python-based tool for batch compressing images while maintaining reasonable quality. This tool provides a user-friendly interface with GUI directory selection and customizable compression settings.

## Features
- GUI file dialogs for selecting input and output directories
- Customizable target file size
- Supports multiple image formats (JPG, JPEG, PNG, BMP, WebP)
- Preserves original file names (adds 'compressed_' prefix)
- Progress tracking and detailed compression statistics
- Error handling for corrupt or unsupported files
- Automatic conversion from RGBA to RGB when needed
- Progressive quality reduction to maintain optimal quality while meeting size requirements

## Installation
1. Clone the repository:
```bash
git clone https://github.com/6ogo/image-compression-tool.git
cd image-compression-tool
```

2. Install the required dependency:
```bash
pip install Pillow
```

## Usage

1. Run the script:
```bash
python image_compressor.py
```

2. Follow the interactive prompts:
   - Select the input directory containing your images when the first file dialog opens
   - Select the output directory for compressed images when the second file dialog opens
   - Enter your desired target file size in MB (e.g., 0.5 for 500KB) in the terminal

3. The script will process all supported images and display:
   - Progress (X/Y files processed)
   - Original file size
   - Compressed file size
   - Compression ratio
   - Final quality setting used

4. Press Enter when finished to close the program

## Example Output
```
Image Compression Tool
=====================

Select the INPUT directory containing images to compress...
Select the OUTPUT directory for compressed images...
Enter target size in MB (e.g., 0.5 for 500KB): 0.5

Starting compression...
Input directory: C:/Users/YourName/Pictures
Output directory: C:/Users/YourName/Pictures/Compressed
Target size per image: 0.5MB

Found 3 images to process

Processed 1/3: vacation.jpg
  Original size: 2048.0KB
  Compressed size: 498.2KB
  Compression ratio: 75.7%
  Final quality setting: 65
---
```

## Supported Image Formats
- JPG/JPEG
- PNG
- BMP
- WebP

## Requirements
- Python 3.6 or higher
- Pillow (PIL) library

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgments
- PIL (Python Imaging Library) for image processing capabilities
- tkinter for the GUI file dialog implementation
