"""
file_rename.py

This script renames all files in a given folder using a simple numbering format.
It keeps the original file extensions and applies a clean, consistent file name.
The script is created for basic automation practice.
"""
import os


def rename_files(folder_path):
    """
    Renames all files in the given folder using a numbered format.
    Example: file_1.txt, file_2.jpg
    """

    files = os.listdir(folder_path)
    count = 1

    for file_name in files:
        old_path = os.path.join(folder_path, file_name)

        if os.path.isfile(old_path):
            name, extension = os.path.splitext(file_name)
            new_name = f"file_{count}{extension}"
            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)
            count += 1


if __name__ == "__main__":
    folder = input("Enter the folder path: ")
    rename_files(folder)
    print("File renaming completed.")
