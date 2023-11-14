from flask import Flask, render_template, request, redirect, url_for
import os
from zipfile import ZipFile
from werkzeug.utils import secure_filename
from CBIR_Tekstur import *

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_PATH'] = 'src/static/upload'

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        gambar = request.files['gambar']
        data = request.files['dataset']
        gambar.save(os.path.join(app.config['UPLOAD_PATH'],'basis.png'))
        data.save(os.path.join(app.config['UPLOAD_PATH'],'dataset.zip'))
        with ZipFile('src/static/upload/dataset.zip', 'r') as f :
            f.extractall('src/static/upload/dir')
        metode = request.form['metode']
        if metode == "no":
            gambar = 'src/static/upload/basis.png'
            data = os.listdir('src/static/upload/dir')
            ar_cos = texture(gambar,data)
            gambar = '../static/upload/basis.png'
        return render_template('home.html',gambar=gambar, ar_cos=ar_cos)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)