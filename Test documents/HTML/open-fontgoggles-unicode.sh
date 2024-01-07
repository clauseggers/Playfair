#!/bin/zsh

# Exit if not on MacOS
os=$(uname -s)
if [ "$os" != "Darwin" ]; then
  echo "This script requires FontGoggles which is only available for MacOS"
  exit 0
fi

# Check if the user provided a four-character argument with only letters and numbers
if [[ $# -ne 1 || ${#1} -ne 4 || ! "$1" =~ ^[[:alnum:]]+$ ]]; then
  echo "Pass a four character Unicode hex value to this script as an argument."
  exit 1
fi

# Store the argument in a variable
search_term=$1

# Search for files in child directories with the provided argument using ripgrep
#files=$(rg "\\\u$search_term" --glob '*.gggls' --null | awk -v RS='\0' '{print $1}')
files=$(find . -type f -name "*.gggls" -exec rg -l --null "$search_term" {} + | tr '\n' '\0')

# Check if any matching files were found
if [[ -z "$files" ]]; then
  echo "No matching files found."
  exit 0
fi

# Output the filenames of all the found files
echo "$files" | tr '\0' '\n'

# Open all the matching files using the MacOS `open` command
echo "$files" | xargs -0 -I{} sh -c 'test -f "{}" && open "{}"'

# EOF
