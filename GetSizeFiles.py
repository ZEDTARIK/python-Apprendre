import os
import time

def calculate_folder_size(folder_path):
    """
    Calculate the total size of files within a specified folder.

    Args:
        folder_path (str): Path to the folder.

    Returns:
        int: Total size of files in bytes, or None if folder does not exist.
    """
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        return None  # Return None if folder does not exist or is not a directory

    total_size = 0
    try:
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
    except OSError:
        return None  # Return None if there's an error accessing files within the folder

    return total_size

def update_folder_sizes_in_file(file_path):
    """
    Update the file with folder sizes appended after each folder path.

    Args:
        file_path (str): Path to the text file containing folder paths.
    """
    # Read existing folder paths from the file
    with open(file_path, 'r') as file:
        folder_paths = [line.strip() for line in file.readlines() if line.strip()]

    # Calculate folder sizes and generate updated lines
    updated_lines = []
    start_time = time.time()  # Start timing

    for folder_path in folder_paths:
        size = calculate_folder_size(folder_path)
        size_str = "Folder not found" if size is None else f"{size} bytes"
        updated_lines.append(f"{folder_path} ; {size_str}")

    end_time = time.time()  # End timing
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

    # Write updated lines back to the file
    with open(file_path, 'w') as file:
        file.write("\n".join(updated_lines) + "\n")

# Main entry point
if __name__ == "__main__":
    file_path = input("Enter the path to the file containing folder paths (e.g., file.txt): ")
    update_folder_sizes_in_file(file_path)
