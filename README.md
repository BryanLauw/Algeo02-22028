<h1>Tugas Besar 2 IF2123 Aljabar Linear dan Geometri <br>
Aplikasi Aljabar Vektor dalam Sistem Temu Balik Gambar</h1>

<h2>Deskripsi Umum</h2>
<p>
Dalam era digital, jumlah gambar yang dihasilkan dan disimpan semakin meningkat dengan pesat, baik dalam konteks pribadi<br> maupun profesional. Peningkatan ini mencakup berbagai jenis gambar, mulai dari foto pribadi, gambar medis,<br> ilustrasi ilmiah, hingga gambar komersial. Terlepas dari keragaman sumber dan jenis gambar ini, sistem temu balik <br>gambar (image retrieval system) menjadi sangat relevan dan penting dalam menghadapi tantangan ini. Dalam konteks ini, <br>aljabar vektor digunakan untuk menggambarkan dan menganalisis data menggunakan pendekatan klasifikasi berbasis konten <br>(Content-Based Image Retrieval atau CBIR), di mana sistem temu balik gambar bekerja dengan mengidentifikasi gambar <br>berdasarkan konten visualnya, seperti warna dan tekstur.
</p>

<h2>Teknologi</h2>
<ul>
    <li>Python (numpy, math, os, shutil, time, ZipFile)</li>
    <li>HTML</li>
    <li>CSS</li>
</ul>

<h2>Fitur</h2>
<ul>
    <li>CBIR dengan parameter warna</li>
    <li>CBIR dengan parameter tekstur</li>
</ul>

<h2>Struktur</h2>
.
│   README.md
│
├───doc                             # Laporan
│   ├───Algeo02-21026.pdf
├───src                             # Source code
│   ├───Algoritma                   # Algoritma
│   │       faceAlignment.py
│   │       function.py
│   │       getEigenFace.py
│   │       getFolder.py
│   │       gui.py
│   │       main.py
│   │
│   ├───Assets                        # Assets
│   │       cam.png
│   │       detect.png
│   │       dilanbg1.png
│   │       folder1.png
│   │       folder2.png
│   │       icon.ico
│   │       img1.png
│   │       img2.png
│   │       notfound.png
│   │       presentase.png
│   │       result1.png
│   │       result2.png
│   │       train.png
│   │       typex.png
│   │
│   ├───Dataset                        # Dataset   
│   │       Copa.jpg
│   │       Copa1.jpg
│   │       Copa2.jpg
│   │       Copa3.jpg
│   │       Copa4.jpg
│   │       Malik.jpg
│   │       Malik1.jpg
│   │       Malik2.jpg
│   │       Malik3.jpg
│   │       Malik4.jpg
│   │
│   ├───Tampilan                      # Tampilan
│   │       Tampilan.png
│   │       Tampilan1.png
│   │       
└───test                              # Testing cases
            Copa1.jpg
            Copa2.jpg
            Copa3.jpg
            Copa4.jpg
            Copa5.jpg
            Jauza1.jpg
            Jauza2.jpg
            Jauza3.jpg
            Jauza4.jpg
            Jauza5.jpg
            Malik.jpg
            Malik1.jpg
            Malik2.jpg
            Malik3.jpg
            Malik4.jpg

<h2>Cara menjalankan program</h2>
<ol>
    <li>Install seluruh libary yang diperlukan</li>
    <li>Clone repositori ini</li>
    <li>Buka cmd pada Windows atau terminal pada Linux</li>
    <li>Ubah direktori ke lokasi repositori yang sudah di-clone</li>
    <li>Ketik 'python3 src/app.py'</li>
    <li>Salin port yang muncul di terminal lalu jalankan pada browser</li>
    <li>Masukkan gambar query dan zip dataset</li>
    <li>Tentukan pencarian berdasarkan tekstur atau warna</li>
    <li>Tekan 'Search'</li>
    <li>Tunggu dan hasil akan ditampilkan</ol>
</ol>