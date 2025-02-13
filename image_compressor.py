from PIL import Image
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

def get_directory(prompt):
    """Open file dialog to select a directory"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory = filedialog.askdirectory(title=prompt)
    return directory

def get_target_size():
    """Get target file size from user input"""
    while True:
        try:
            size = float(input("Enter target size in MB (e.g., 0.5 for 500KB): "))
            if size > 0:
                return size
            print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")

def compress_images(input_dir, output_dir, max_size_mb=1.0, quality_start=95):
    """
    Compress all images in a directory.
    
    Args:
        input_dir (str): Input directory containing images
        output_dir (str): Output directory for compressed images
        max_size_mb (float): Target maximum file size in megabytes
        quality_start (int): Initial quality setting (1-95)
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Supported image formats
    supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
    
    # Convert max_size to bytes
    max_bytes = max_size_mb * 1024 * 1024
    
    # Count total files to process
    total_files = sum(1 for f in os.listdir(input_dir) 
                     if Path(f).suffix.lower() in supported_formats)
    processed_files = 0
    
    print(f"\nFound {total_files} images to process\n")
    
    # Process all files in the directory
    for filename in os.listdir(input_dir):
        file_extension = Path(filename).suffix.lower()
        
        if file_extension in supported_formats:
            input_path = os.path.join(input_dir, filename)
            
            # Create output filename (preserve original extension)
            output_filename = f'compressed_{filename}'
            output_path = os.path.join(output_dir, output_filename)
            
            try:
                # Open and process image
                with Image.open(input_path) as img:
                    # Convert to RGB if necessary
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')
                    
                    # Start with initial quality
                    quality = quality_start
                    
                    while True:
                        # Save with current quality setting
                        img.save(output_path, 'JPEG', quality=quality)
                        
                        # Check if size is within target
                        file_size = os.path.getsize(output_path)
                        
                        if file_size <= max_bytes or quality <= 5:
                            break
                            
                        # Reduce quality and try again
                        quality -= 5
                
                # Calculate compression ratio
                original_size = os.path.getsize(input_path)
                compressed_size = os.path.getsize(output_path)
                ratio = (1 - compressed_size / original_size) * 100
                
                processed_files += 1
                print(f'Processed {processed_files}/{total_files}: {filename}')
                print(f'  Original size: {original_size / 1024:.1f}KB')
                print(f'  Compressed size: {compressed_size / 1024:.1f}KB')
                print(f'  Compression ratio: {ratio:.1f}%')
                print(f'  Final quality setting: {quality}')
                print('---')
                
            except Exception as e:
                print(f'Error processing {filename}: {str(e)}')
                print('---')

def main():
    print("Image Compression Tool")
    print("=====================")
    
    # Get input directory from user
    print("\nSelect the INPUT directory containing images to compress...")
    input_dir = get_directory("Select Input Directory")
    if not input_dir:
        print("No input directory selected. Exiting...")
        return
    
    # Get output directory from user
    print("\nSelect the OUTPUT directory for compressed images...")
    output_dir = get_directory("Select Output Directory")
    if not output_dir:
        print("No output directory selected. Exiting...")
        return
    
    # Get target file size
    target_mb = get_target_size()
    
    print("\nStarting compression...")
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Target size per image: {target_mb}MB")
    
    # Run compression
    compress_images(
        input_dir=input_dir,
        output_dir=output_dir,
        max_size_mb=target_mb,
        quality_start=95
    )
    
    print("\nCompression complete!")
    print(f"Compressed images have been saved to: {output_dir}")
    
    # Keep terminal window open
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
