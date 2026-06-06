import os
import shutil
from datetime import datetime

log_file = "operations_log.txt"

def write_log(message):
    with open(log_file, "a") as file:
        file.write(f"{datetime.now()} - {message}\n")

def organize_files(folder_path):
    try:
        file_types = {
            "Images": [".jpg", ".jpeg", ".png"],
            "Documents": [".pdf", ".txt", ".docx"],
            "Videos": [".mp4"]
        }

        for filename in os.listdir(folder_path):

            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):

                moved = False

                for folder, extensions in file_types.items():

                    if filename.lower().endswith(tuple(extensions)):

                        destination = os.path.join(folder_path, folder)

                        os.makedirs(destination, exist_ok=True)

                        shutil.move(
                            file_path,
                            os.path.join(destination, filename)
                        )

                        write_log(f"Moved {filename} to {folder}")

                        moved = True
                        break

                if not moved:
                    write_log(f"Skipped {filename}")

        print("Files organized successfully!")

    except Exception as e:
        write_log(f"Error: {e}")
        print("Error:", e)

folder = input("Enter folder path: ")

organize_files(folder)