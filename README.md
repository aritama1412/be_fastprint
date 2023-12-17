# be_fastprint

how to install:

1. buat virtual machine dengan menjalankan perintah:
    python -m venv env
2. aktifkan dengan perintah:
    env\Scripts\activate
    pip install django
4. git clone https://github.com/aritama1412/be_fastprint.git
5. buat database mysql dengan nama "test_be_fastprint_python" atau nama apapun. Pastikan pada settings.py nama database sama dengan yang baru anda buat
6. pindah kedalam folder project dan jalankan perintah:
  pip3 install requests
  python manage.py migrate
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver

###########
untuk akses API
pertama buka aplikasi POSTMAN dan 
buat request baru dengan method POST dan url: https://recruitment.fastprint.co.id/tes/api_tes_programmer
lalu bukan bagian body dan kirim data.
setelah kirim data, maka akan muncul pesan "{"error":1,"ket":"username dan password tidak boleh kosong"}"
buka bagian "Headers" dan pada bagian "X-Credentials-Username" copy username yang ada (contoh: tesprogrammer171223C19)
untuk password, cek pada bagian "X-Credentials-Password" maka akan terdapat hint, password merupakan hash md5 dari "bisacoding-17-12-23" (sesuaikan pada tanggal hari ini)
untuk mendapatkan hash md5, buka https://www.md5hashgenerator.com/ dan pastekan passwordnya, maka akan muncul seperti ini: "70d631bc99f745d0935f5ee8a75a2a1e"

buka views.py isi username dan password dari data yang baru saja di dapat
