import csv
import json

def generate_gggls_template(language, iso_3, alphabet):
    template = {
        "fonts": [
            {"path": "../PlayfairRomanVF.woff2"},
            {"path": "../PlayfairItalicVF.woff2"}
        ],
        "textSettings": {
            "text": alphabet,  # Change this line
            "textFilePath": None,
            "textFileIndex": 0,
            "shouldApplyBiDi": True,
            "direction": None,
            "script": "latn",
            "language": iso_3,
            "alignment": None,
            "features": {},
            "varLocation": {"opsz": 12, "wght": 400, "wdth": 100},
            "relativeFontSize": 0.7,
            "relativeHBaseline": 0.25,
            "relativeVBaseline": 0.5,
            "relativeMargin": 0.1,
            "enableColor": True
        },
        "uiSettings": {
            "windowPosition": [129.0, 597.0, 2335.0, 500.0],
            "fontListItemSize": 150,
            "fontListShowFontFileName": True,
            "characterListVisible": False,
            "characterListSize": 575.5,
            "glyphListVisible": False,
            "glyphListSize": 226.0,
            "compileOutputVisible": False,
            "compileOutputSize": 80.0,
            "formattingOptionsVisible": True,
            "feaVarTabSelection": "variations",
            "showHiddenAxes": False
        }
    }
    return template

def save_gggls_file(file_path, content):
    with open(file_path, 'w') as file:
        json.dump(content, file, indent=2)

def main():
    input_csv_file = 'GF_SSA_alphabets.csv'  # Replace with the actual path to your CSV file

    with open(input_csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for i, row in enumerate(reader, start=1):  # start=1 as there is no header row
            try:
                language = row[0].strip()
                iso_3 = row[2].strip()
                alphabet = row[3].strip()  # Add this line

                gggls_template = generate_gggls_template(language, iso_3, alphabet)  # Update this line

                filename = f"Playfair_2-2_{language}_{iso_3}.gggls"
                save_gggls_file(filename, gggls_template)
                print(f"Row {i}: File '{filename}' generated successfully.")
            except Exception as e:
                print(f"Row {i}: Error processing row - {e}")

if __name__ == "__main__":
    main()
