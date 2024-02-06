#!/bin/bash

main_folder="/mnt/d/a"
marker_file="/mnt/d/marker_file.txt"
destination_path="/mnt/d/abhi"
csv_file="/mnt/d/file_mapping.csv"

# Function to get the first letter of each word
get_first_letters() {
    echo "$1" | awk '{for(i=1;i<=NF;i++) print toupper(substr($i,1,1))}' | tr -d '\n'
}

rename_files() {
  while IFS= read -r -d '' file; do
    if [ -f "$file" ]; then
      folder_path=$(dirname "$file")
      relative_path=${folder_path#$main_folder/}  # Remove the leading main_folder part
      folder_names=$(echo "$relative_path" | tr '/' '_')
      new_file_name="${folder_names}_$(basename "$file")"

      # Append path and new filename to the CSV file
      echo "$file,$new_file_name" >> "$csv_file"

      mv "$file" "$folder_path/$new_file_name"
      cp "$folder_path/$new_file_name" "$destination_path"
    fi
  done < <(find "$main_folder" -type f -print0)
}

copy_files() {
  while IFS= read -r -d '' file; do
    if [ -f "$file" ]; then
      # Append path and filename to the CSV file
      echo "$file,$(basename "$file")" >> "$csv_file"

      cp "$file" "$destination_path"
    fi
  done < <(find "$main_folder" -type f -print0)
}

# Check if the main folder exists
if [ ! -d "$main_folder" ]; then
  echo "Main folder does not exist: $main_folder"
  exit 1
fi

# Check if the marker file exists
if [ -e "$marker_file" ]; then
  echo "Files have already been processed. Skipping."
else
  # Check if the first path length is equal to the lengths of the subsequent paths
  first_path_length=$(echo "$main_folder" | awk '{print length}')
  other_paths_length=$(find "$main_folder" -mindepth 1 -type d -exec echo {} \; | awk '{print length}' | uniq)

  if [ $(echo "$other_paths_length" | wc -l) -eq 1 ] && [ "$first_path_length" -eq "$(echo "$other_paths_length" | head -n 1)" ]; then
    rename_files
  else
    copy_files
  fi

  touch "$marker_file"
  echo "Files processed successfully."
fi
