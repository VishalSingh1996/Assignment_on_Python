import os #for intrecting with file system 
import shutil #for copying files 
import sys #To access folder path 
from datetime import datetime #used for timestamps if a file already exists 

def backup_files(source_dir, destination_dir):
#Copy files from source_folder to backup_folder with timestamp to check the when file backup is done.

# Checking the Source Folder Exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
# Checking the Destination Folder Exists | Means Backup Folder Exits
    if not os.path.exists(destination_dir):
        print(f"Error: Destination directory '{destination_dir}' does not exist.")
        return

    for filename in os.listdir(source_dir): #Checking files in Source Folder
        source_file = os.path.join(source_dir, filename) # join both folder path & file name to get full pathh

        if os.path.isfile(source_file): #Checking file(Folder nhi ho)
            destination_file = os.path.join(destination_dir, filename) #Creating full path where this file will be copied

            # Adding timestamp for checking if file already exits then copy file but with new timestap
            if os.path.exists(destination_file):
                base, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                destination_file = os.path.join(destination_dir, f"{base}_{timestamp}{ext}")

            shutil.copy2(source_file, destination_file) #Copying the file
            print(f"Copied: {filename}")

def main():
    if len(sys.argv) != 3:
        print('Usage: python backup.py "<source_folder>" "<destination_folder>"')
        return

    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]

    backup_files(source_dir, destination_dir) # calling backup function

if __name__ == "__main__":
    main()
