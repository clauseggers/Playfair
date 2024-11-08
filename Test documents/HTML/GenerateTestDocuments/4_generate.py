import os
import csv

template = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <title>Playfair test document for %LANGUAGE_LONG_NAME%</title>
    <link rel='stylesheet' href='normalize.css'>
    <link rel='stylesheet' href='Playfair2_font-face.css'>
    <link rel='stylesheet' href='Playfair2_style.css'>
  </head>
  <body>
    <p class="headline">The <em>Playfair 2.2</em> typeface family test document for %LANGUAGE_LONG_NAME%</p>
    <div class="%LANGUAGE_LONG_NAME%" lang="%ISO639-3%">
      <p class="abecedarium">%ABECEDARIUM%</p>
      <p class="body">%CORPUS%</p>
      <p class="abecedarium"><em>%ABECEDARIUM%</em></p>
      <p class="body"><em>%CORPUS%</em></p>
    </div>
  </body>
</html>
"""

csv_file_path = "GF_SSA_alphabets.csv"
languages_dir = "ssa_languages"
output_dir = "output_html_docs"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)  # Skip the header row

    for row in reader:
        language_long_name = row[0]
        iso_639_3 = row[2]
        abecedarium = row[3]

        # Check if the text file exists
        text_file_path = os.path.join(languages_dir, f"{row[2]}.txt")
        if not os.path.exists(text_file_path):
            print(f"Skipping row: Text file '{text_file_path}' not found.")
            continue

        # Read the content of the corresponding text file
        with open(text_file_path, 'r', encoding='utf-8') as text_file:
            corpus = text_file.read()

        # Replace placeholders in the template with actual values
        html_content = template.replace('%LANGUAGE_LONG_NAME%', language_long_name) \
            .replace('%ISO639-3%', iso_639_3) \
            .replace('%ABECEDARIUM%', abecedarium) \
            .replace('%CORPUS%', corpus)

        # Write the HTML content to a new file
        output_file_path = os.path.join(output_dir, f"{iso_639_3}_{language_long_name.replace(' ', '_')}_Playfair_2-2_test_document.html")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(html_content)

print("HTML documents generated successfully.")
