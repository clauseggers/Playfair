#!/bin/zsh

# Check if the user provided a four-character argument with only letters and numbers
if [[ $# -ne 1 || ${#1} -ne 4 || ! "$1" =~ ^[[:alnum:]]+$ ]]; then
  echo "Usage: $0 <four-character>"
  exit 1
fi

# Store the argument in a variable
search_term=$1

# Search for files in child directories with the provided argument using ripgrep
files=$(rg "$search_term" --glob '*.gggls' --null | awk -v RS='\0' '{print $1}')

# Echo the found files
echo "$files"

# Check if any matching files were found
if [[ -z "$files" ]]; then
  echo "No matching files found."
  exit 0
fi

# Open the matching files using the MacOS `open` command
while IFS= read -r file; do
  open "$file"
done <<< "$files"

# EOF