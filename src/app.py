from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from module import *

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_PATH'] = 'src/static'

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        gambar = request.files['gambar']
        data = request.files['dataset']
        gambar.save(os.path.join(app.config['UPLOAD_PATH'],'basis.png'))
        data.save(os.path.join(app.config['UPLOAD_PATH'],'1.png'))

        metode = request.form['metode']
        if metode == "no":
            gambar = cv2.imread('static/basis.png')
            data = cv2.imread('static/1.png')
            kemiripan = bandingTekstur(gambar,data)
        return render_template('home.html')
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)