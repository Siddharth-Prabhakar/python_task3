# Move JPG Files Utility

**Author:** Siddharth Prabhakar

## Overview
This project is a simple Python utility to move all `.jpg` files from a source folder to a destination folder. It is useful for organizing images by automatically transferring them from one directory to another.

## Features
- Moves all `.jpg` files from the specified source folder to the destination folder.
- Prints the number of files moved and the source/destination paths.
- Easy to use and modify for similar file operations.

## Requirements
- Python 3.x
- Standard Python libraries (`os`, `shutil`)

## How It Works
1. Place your `.jpg` files in the `source_folder` directory.
2. Run the script `move_jpg_files.py` using Python.
3. The script will move all `.jpg` files from `source_folder` to `destination_folder`.
4. After execution, you will see a message indicating how many files were moved and the involved directories.

## Usage
```bash
python move_jpg_files.py
```

## Example Output
```
Moved 3 .jpg file(s) from 'c:\Users\Parbhakar\OneDrive\Desktop\task-3\source_folder' to 'c:\Users\Parbhakar\OneDrive\Desktop\task-3\destination_folder'.
```

## Project Structure
- `move_jpg_files.py` : The main script to move `.jpg` files.
- `source_folder/` : Place your `.jpg` files here.
- `destination_folder/` : Files will be moved here.

## License
See [LICENSE](LICENSE) for details. 
