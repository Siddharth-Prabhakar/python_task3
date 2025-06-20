import os
import shutil
import sys

# Define default folder names (relative to script location)
default_source = 'source_folder'
default_destination = 'destination_folder'

# Allow user to specify full paths via command line arguments
if len(sys.argv) > 2:
    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]
else:
    # Use defaults relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_dir, default_source)
    destination_folder = os.path.join(script_dir, default_destination)

# Error handling: Check if source folder exists
if not os.path.exists(source_folder):
    print(f"Error: Source folder '{source_folder}' does not exist.")
    sys.exit(1)

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Counter for moved files
moved_count = 0

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    # Check if file ends with .jpg or .JPG (case-insensitive)
    if filename.lower().endswith('.jpg'):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        try:
            shutil.move(src_path, dst_path)
            moved_count += 1
        except Exception as e:
            print(f"Failed to move {filename}: {e}")

# Print summary
print(f"Moved {moved_count} .jpg file(s) from '{source_folder}' to '{destination_folder}'.") 