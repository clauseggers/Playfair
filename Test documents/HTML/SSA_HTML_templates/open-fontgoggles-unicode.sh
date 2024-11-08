#!/bin/zsh

# Exit if not on MacOS
os=$(uname -s)
if [ "$os" != "Darwin" ]; then
  echo "This script requires FontGoggles which is only available for MacOS"
  exit 1
fi

# Exit if `fd` is not installed
if ! command -v fd &> /dev/null
then
  echo "fd is required"
  exit 1
fi

# Exit if Ripgrep `rg` is not installed
if ! command -v rg &> /dev/null
then
  echo "Ripgrep is required"
  exit 1
fi

# Check if the user provided a four-character argument with only letters and numbers
if [[ $# -ne 1 || ${#1} -ne 4 || ! "$1" =~ ^[[:alnum:]]+$ ]]; then
  echo "Pass a four character Unicode hex value to this script as an argument."
  exit 1
fi

# Store the argument in a variable
unicode_hex=$1

# Search for files in child directories with the provided argument using ripgrep
files=$(fd -e gggls -x rg -l --null "$unicode_hex")

# Check if any matching files were found
if [[ -z "$files" ]]; then
  echo "No matching files found."
  exit 1
fi

# Count the number of files found and wait for user input
number=$(echo -n "$files" | tr -dc '\0' | wc -c)

# Wait for user accept if the number of files is greater than ten
if [ "$number" -gt 10 ]; then

  # Display the message to the user
  echo "$number files found, proceed? (y/n)"

  # read user input
  read -r user_input

  # check if the user input is 'y' or 'y'
  if [ "$user_input" = "y" ] || [ "$user_input" = "y" ]; then
    echo "proceeding...\n"

    # Output the filenames of all the found files
    echo "$files" | tr '\0' '\n'

    # Open all the matching files using the MacOS `open` command
    echo "$files" | xargs -0 -I{} sh -c 'test -f "{}" && open "{}"'
  else
  echo "opening was aborted."
fi

else
  # Output the filenames of all the found files
  echo "$files" | tr '\0' '\n'

  # Open all the matching files using the MacOS `open` command
  echo "$files" | xargs -0 -I{} sh -c 'test -f "{}" && open "{}"'
fi

# EOF
