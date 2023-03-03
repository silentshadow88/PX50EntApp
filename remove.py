import zipfile
import os
import glob

# Path to the directory containing APK files
apk_dir_path = "/home/kali/Desktop/app"

# Path to the output directory
output_dir_path = "/home/kali/Desktop"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir_path):
    os.mkdir(output_dir_path)

# Iterate over the APK files in the directory and extract their .so files
for apk_file_path in glob.glob(os.path.join(apk_dir_path, "*.apk")):
    # Extract the APK file to a temporary directory
    with zipfile.ZipFile(apk_file_path, "r") as apk_file:
        apk_file.extractall("temp_dir")

    # Path to the directory containing .so files
    lib_dir_path = os.path.join("temp_dir", "lib", "arm64-v8a")

    # Create an empty list to store the names of the .so files
    so_file_names = []

    # Iterate over the .so files in the lib directory and save their names to a list
    for file_name in os.listdir(lib_dir_path):
        if file_name.endswith(".so"):
            # Add the "rm /system/app" command to the name of the .so file
            name = "rm /system/lib64/" + file_name
            so_file_names.append(name)

    # Write the names of the .so files with "rm /system/app" command to a text file in the output directory
    apk_name = os.path.splitext(os.path.basename(apk_file_path))[0]
    with open(os.path.join(output_dir_path, apk_name + ".txt"), "w") as name_file:
        for name in so_file_names:
            name_file.write(name + "\n")

    # Delete the temporary directory
    os.system("rm -r temp_dir")