from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from module import *

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_PATH'] = 'static/upload'

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        gambar = request.files['gambar']
        data = request.files['dataset']
        gambar.save(os.path.join(app.config['UPLOAD_PATH'],'basis.png'))
        data.save(os.path.join(app.config['UPLOAD_PATH'],'1.png'))

        metode = request.form['metode']
        if metode == "no":
            gambar = 'static/upload/basis.png'
            g1 = cv2.imread(gambar)
            data = 'static/upload/1.png'
            d1 = cv2.imread(data)
            kemiripan = round((bandingTekstur(g1,d1))*100,2)
        return render_template('home.html',gambar=gambar, data=data, kemiripan=kemiripan)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)