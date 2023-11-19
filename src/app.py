from flask import Flask, render_template, request, url_for
import os
import shutil
from zipfile import ZipFile
from tekstur import *
from warna import *
import time

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_PATH'] = 'src/static/upload'

def tuple_to_dic(item):
    return dict(percentage=item[0], picture=item[1])

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        # Memproses file-file yang diinginkan
        gambar = request.files['gambar']
        data = request.files['dataset']
        gambar.save(os.path.join(app.config['UPLOAD_PATH'],'basis.png'))
        data.save(os.path.join(app.config['UPLOAD_PATH'],'dataset.zip'))
        shutil.rmtree('src/static/upload/dir')
        with ZipFile('src/static/upload/dataset.zip', 'r') as f :
            f.extractall('src/static/upload/dir')
        gambar = 'src/static/upload/basis.png'
        data = os.listdir('src/static/upload/dir')
        metode = request.form['metode']
        
        # Memulai perhitungan cosine simmiliarity
        start = time.time()
        if metode == "no": # metode tekstur
            ar_cos = texture(gambar,data)
            listOfPicture = urutGambar(ar_cos,data)
        else: # metode warna
            ar_cos = color(gambar,data)
            listOfPicture = urutGambarWarna(ar_cos,data)
        end = time.time()

        # Paginasi
        qList = []
        for i in listOfPicture:
            qList.append(tuple_to_dic(i))

        return render_template('home.html',
                               gambar = '../static/upload/basis.png', 
                               data=qList,
                               len = len(listOfPicture), 
                               time = round((end-start),2))
    return render_template('home.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/HowToUse')
def how():
    return render_template('howtouse.html')

@app.route('/Concepts')
def concept():
    return render_template('concept.html')

if __name__ == '__main__':
    app.run()