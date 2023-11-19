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
.<br>
│   README.md<br>
│<br>
├───doc                             # Laporan<br>
│   ├───Algeo02-22028.pdf<br>
├───src                             # Source code<br>
│   │ app.py<br>
│   │ tekstur.py<br>
│   │ warna.py<br>
│   ├───templates<br>               # HTML
│   │       about.html<br>
│   │       concept.html<br>
│   │       home.html<br>
│   │       howtouse.html<br>
│   ├───static<br>                  # CSS and other picture
│   │       style.css<br>
│   ├────────upload<br>
│   │<br>
│   ├───img                         # image and screenshot<br>
│   │       31539.jpg<br>
│   │       UjiCoba1-HasilTekstur(1).png<br>
│   │       UjiCoba1-HasilTekstur(2).png<br>
│   │       UjiCoba1-HasilTekstur(3).png<br>
│   │       UjiCoba1-HasilWarna.png<br>
│   │       UjiCoba1-Query.png<br>
│   │       UjiCoba2-HasilTekstur.png<br>
│   │       UjiCoba2-HasilWarna.png<br>
│   │       UjiCoba1-Query.png<br>
│   │       UjiCoba3-HasilTekstur(1).png<br>
│   │       UjiCoba3-HasilTekstur(2).png<br>
│   │       UjiCoba3-HasilTekstur(3).png<br>
│   │       UjiCoba3-HasilTekstur(4).png<br>
│   │       UjiCoba3-HasilTekstur(5).png<br>
│   │       UjiCoba3-HasilTekstur(6).png<br>
│   │       UjiCoba3-HasilWarna(1).png<br>
│   │       UjiCoba3-HasilWarna(2).png<br>
│   │       UjiCoba3-HasilWarna(3).png<br>
│   │       UjiCoba3-HasilWarna(4).png<br>
│   │       UjiCoba3-Query.png<br>
│   │       UjiCobaContoh-Hasil.png<br>
│   │       UjiCobaContoh-Query.png<br>
│   │<br>
└───test                              # Testing cases<br>
        50gambaragakrandom<br>
        seratusGambar<br>
        31536.jpg<br>
        blue.jpg<br>
        warnaterang.jpg<br>
        
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