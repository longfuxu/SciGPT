# SciGPT

## How to start

Windows, MacOS and Ubuntu systems should be fine;

python version is best 3.9, other versixons should not have any problems

1. Copy `apikey.example` and rename it as `apikey.ini`; fill in your openai key in apikey.ini. Note that this code is a pure local project, your key is very safe!

2. The process must ensure global proxy! 

3. Install dependencies:
``` bash
pip install -r requirements.txt
```
4. Run chat_paper.py, for example:

```python
python chat_paper.py --pdf_path "pdf_path.pdf"
```
## Use cases: Batch Download PDFs from Plaintext References and Analyze with ChatPaper
This manual will guide you through the process of converting a list of plaintext references into a .bib file, batch downloading the corresponding PDFs using Zotero, copying the PDFs to a separate folder, analyzing the documents using ChatPaper, and compiling a PDF file with key messages.
### Step 1: Convert Citations to a .bib File and Batch Download PDFs with Zotero
1. Convert your citations to a .bib or .ris file: Use an online citation converter tool like AnyStyle (https://anystyle.io/) to convert your list of citations into a BibTeX (.bib) or RIS (.ris) format file. Copy and paste your list of citations into the text box and click "Parse." Once the parsing is complete, click "Download" and choose either the BibTeX or RIS format. Make sure to carefully check each parsed reference in AnyStyle, as each line will be recognized as a separate file.

2. Import the .bib or .ris file into Zotero: Open Zotero and create a new collection to store your references. Go to "File" > "Import," select the .bib or .ris file you downloaded, and choose the collection you created. Zotero will import the references into the collection.

3. Download the articles using the DOI: In Zotero, use the Digital Object Identifier (DOI) to find and download the articles. If the DOI is already included in the imported reference, follow these steps:

- Select the items in the collection you want to download.
- Right-click the selection and choose "Find Available PDFs." Zotero will search for the PDF files online using the DOI.
- If Zotero finds a PDF file, it will automatically download and attach the file to the corresponding reference in your library. This process may take some time, depending on the number of references you have.

Note that the success of this method depends on the availability of the articles through your university's subscriptions, open access, or the compatibility of Zotero with specific publisher websites or databases. If Zotero doesn't work for some articles, you may need to download them manually from the publisher's website or your university's library website.

### Step 2:Copy Selected PDFs to a Separate Folder
1. Install Python: If you don't have Python installed, download it from https://www.python.org/downloads/ and install it on your computer.

2. Export the citations from Zotero: In Zotero, select the items you want to copy to a separate folder. Right-click the selection and choose "Export Items..." Export the selected items in CSV format and save the file to a convenient location.

3. Create a Python script: Open your favorite text editor or integrated development environment (IDE) and create a new Python script file (e.g., `copy_pdf_files.py`). Copy and paste the following code into the script file:
```python
import os
import shutil
import csv

# Set your destination folder and CSV file path
destination_folder = "/path/to/destination/folder"
csv_file = "/path/to/exported/csv/file.csv"

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

uncopied_files = []

# Read the CSV file and copy the PDF files
with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pdf_paths = row['File Attachments'].strip(';').split(';')
        for pdf_path in pdf_paths:
            pdf_path = pdf_path.strip()
            if pdf_path.lower().endswith('.pdf'):
                pdf_filename = pdf_path.split('/')[-1]
                pdf_destination_path = os.path.join(destination_folder, pdf_filename)
                try:
                    shutil.copy2(pdf_path, pdf_destination_path)
                except FileNotFoundError as e:
                    print(f"Error: {e}")
                    uncopied_files.append(pdf_filename)

print("PDF files copied successfully!")

if uncopied_files:
    print("\nThe following files could not be copied:")
    for file in uncopied_files:
        print(file)


```
4. Configure the script: Replace `/path/to/destination/folder` with the path to the folder where you want to copy the selected PDF files. Replace `/path/to/exported/csv/file.csv` with the path to the CSV file you exported in step 2.

5. Run the script: Save the script file and run it using a Python interpreter. The script will read the CSV file, locate the PDF files in your Zotero storage folder, and copy them to the destination folder.

### Step 3:Run ChatPaper Analysis
Follow above instructions on How to Use

### Step 4: Combine Multiple Markdown Files into a Single PDF
1. To combine multiple Markdown files into a single PDF, use a tool called Pandoc, which is a universal document converter.

2. Navigate to the folder where you have all the markdown files.
Run the following code:
```bash
pandoc -s *.md -o output.pdf --pdf-engine=xelatex
```

This command will combine all the Markdown files in the folder into a single PDF file called output.pdf.

### Enjoy Science
## Credit
This repo is modified based on repo(https://github.com/kaixindelele/ChatPaper). 