import os

def remove_header(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Find the index of the first occurrence of two space characters
    index = content.find("  ")

    if index != -1:
        # Remove everything up to and including the first occurrence of two space characters
        modified_content = content[index + 2:]
    else:
        # If two space characters are not found, keep the original content
        modified_content = content

    # Save the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

def process_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            remove_header(file_path)

if __name__ == "__main__":
    # Replace 'your_directory_path' with the path to your directory containing TXT files
    your_directory_path = 'ssa_languages'
    
    process_files(your_directory_path)
    print("Header removal complete.")
