from urllib import response
from flask import Flask, render_template, request, send_from_directory, make_response
app = Flask(__name__, "", static_folder="templates")
import pytesseract 
from PIL import Image
import fitz
import io

@app.route("/ocr", methods=["POST"])
def ocr():
    im_file = request.files['filename']
    # no_noise = "temp/no_noise.jpg"
    im = Image.open(im_file)
    ocr_result = pytesseract.image_to_string(im)
    return ocr_result

@app.route("/pdftxt", methods=['POST'])
def pdftxt():
    im_file = request.files['filename']
    search_text = request.form['txt']
    print(search_text)
    stream=im_file.read()
    doc = fitz.open(stream=stream, filetype="pdf")
    txt = ""
    for page in doc:
        txt += page.get_text()
    
    response = make_response(txt)
    response.headers.set('Content-Type', "text/plain")
    response.headers.set('Content-Disposition', 'attachment', filename="pdf_txt.txt")
    return response

@app.route("/search", methods=['POST'])
def search():
    im_file = request.files['filename']
    search_text = request.form['query']
    print(search_text)
    stream=im_file.read()
    doc = fitz.open(stream=stream, filetype="pdf")
    for page in doc:
        for inst in page.search_for(search_text):
            highlight = page.add_highlight_annot(inst)
            highlight.update()
    
    response = make_response(doc.write())
    response.headers.set('Content-Type', "application/pdf")
    response.headers.set('Content-Disposition', 'attachment', filename="search.pdf")
    return response

@app.route("/", methods=["GET"])
def index():
    return render_template('MainNav.html')
if __name__ == '__main__':
    app.run(port = "5000", debug = True)
