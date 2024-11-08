Instructions for generating HTML specimen from corpora

Clone or download this repository of corpora
https://github.com/unicode-org/unilex

The files we need are in unilex/data/frequency
https://github.com/unicode-org/unilex/tree/main/data/frequency

Take all these TXT files and put them in a sub-directory (to this file) called 'languages'

Copy the `GF_SSA_alphabets.csv` file from this repo (one level up from here) to this directory

Execute the Python script `1_filter_languages.py`
# python 1_filter_languages.py

This will copy all the TXT-files that also have entries in the CSV-file into a sub-directory called `ssa_languages`

Now run the Python script `2_format.py`
# python 2_format.py

This will format the file as one string.

Now run the Python script `3_clean.py`

This will purify and sanctify our precious bodily fluids.

Finally we generate the HTML-documents from the template by running the final Python script `4_generate.py`
# python 4_generate.py

The terminal will now output the HTML test documents for which there was an entry in the CSV-file and a matching TXT-file into a sub-directory called `output_html_docs`. The script will also output a list of all the rows that did not have a matching TXT-file.

You now have to move the HTML-files to a directory of your choice, but remember to add the CSS- and WOFF2-files to that directory.

NOTE! The quality of the `unilex` source is not perfect. There are eg. errors of confusables[1], eg. using LATIN SMALL LETTER REVERSED C (u2184) instead of the correct LATIN SMALL LETTER OPEN O (u0254).

[1] https://util.unicode.org/UnicodeJsps/confusables.jsp?a=ↄ&r=None
