import argparse
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from get_paper_from_pdf import Paper
from chat_paper import Reader, PaperParams

# Initialize the Flask app and set the upload folder:
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create the uploads folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


# Create a route for the main page that renders an HTML template with a form to upload the PDF file:
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Save the uploaded file
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Create a Reader instance
        reader = Reader(args=argparse.Namespace(pdf_path=file_path, save_image=False, file_format='md', language='en'))

        # Extract the paper information and generate the summary
        paper = Paper(file_path)
        summary_text, conclusion_text, method_text = reader.summary_with_chat([paper])

        # Combine the sections and save them to a file
        if summary_text is not None and conclusion_text is not None and method_text is not None:
            summarized_text = f"{summary_text}\n\n{conclusion_text}\n\n{method_text}"
            
            # Check if the filename contains the expected format
            if " - " in filename:
                first_author, year = filename.split(" - ")[:2]
                summary_filename = f"GPT_Summarized_{first_author}_{year}.md"
            else:
                # Handle the case when the filename format is not as expected
                summary_filename = f"GPT_Summarized_{filename}.md"

            summary_file_path = os.path.join(app.config['UPLOAD_FOLDER'], summary_filename)

            with open(summary_file_path, 'w') as f:
                f.write(summarized_text)

            # Pass the summary_file_path to the render_template function
            return render_template('summary.html', summary=summarized_text, filename=summary_filename, summary_file_path=summary_file_path)

        else:
            # Handle the case when summarized_text is None
            # You can return an error message or redirect to an error page
            return "Error: Summarized text is None"
        
    return render_template('index.html')

# Create a route for the summary page that processes the uploaded PDF file and displays the summary:
@app.route('/summary', methods=['GET', 'POST'])
def summary(filename):
    summary_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(summary_file_path, 'r') as f:
        summarized_text = f.read()
    return render_template('summary.html', summary=summarized_text, filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
