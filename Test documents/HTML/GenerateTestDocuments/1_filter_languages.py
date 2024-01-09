import os
import shutil

def copy_files(source_dir, destination_dir, filenames):
    for filename in filenames:
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)
        shutil.copyfile(source_path, destination_path)
        print(f"Copied: {filename}")

def main():
    input_file = "GF_SSA_alphabets.csv"  # Replace with the actual path of your semi-colon separated document
    source_directory = "languages"
    destination_directory = "ssa_languages"

    # Read the semi-colon separated document
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        columns = line.strip().split(';')
        if len(columns) >= 3:
            string_to_match = columns[2].strip()
            filename = f"{string_to_match}.txt"

            # Check if the file exists in the 'languages' directory
            if os.path.exists(os.path.join(source_directory, filename)):
                # Copy the file to the 'ssa_languages' directory
                copy_files(source_directory, destination_directory, [filename])

if __name__ == "__main__":
    main()

