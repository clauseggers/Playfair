import os

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process each line in the file
    processed_lines = [line.split('\t')[0].strip() for line in lines]

    # Join the processed lines with a space
    result = ' '.join(processed_lines)

    # Write the result back to the file
    with open(file_path, 'w') as file:
        file.write(result)

def process_files_in_directory(directory):
    # List all files in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    # Process each file in the directory
    for file in files:
        file_path = os.path.join(directory, file)
        process_file(file_path)
        print(f"Processed: {file}")

if __name__ == "__main__":
    # Replace 'your_directory_path' with the actual path to your directory containing the txt files
    directory_path = 'ssa_languages'

    process_files_in_directory(directory_path)
