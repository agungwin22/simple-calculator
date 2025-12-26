# Simple Calculator

Kalkulator sederhana berbasis Python yang memiliki antarmuka interaktif di terminal, mendukung berbagai operasi matematika dasar dan lanjutan.

## 🚀 Fitur Utama

### Operasi Matematika yang Didukung:
- **Penjumlahan (+)** - Menambahkan dua bilangan
- **Pengurangan (-)** - Mengurangi bilangan pertama dengan kedua
- **Perkalian (* atau x)** - Mengalikan dua bilangan
- **Pembagian (/)** - Membagi bilangan pertama dengan kedua (dengan pengecekan pembagi nol)
- **Modulus (%)** - Menghitung sisa hasil bagi
- **Pangkat (^ atau **)** - Menghitung bilangan pertama pangkat kedua

### Fitur Tambahan:
- **Reset Kalkulator** - Mengembalikan hasil ke nilai 0
- **Penanganan Error** - Validasi input dan penanganan pembagian dengan nol
- **Antarmuka Interaktif** - Tampilan yang user-friendly dengan pembatas visual
- **Multi-platform** - Mendukung Windows, Linux, dan macOS

## 🏗️ Struktur Kode

### File Proyek:
- **App.py** - File utama berisi implementasi kelas Calculator dan CalculatorMenu
- **Display.py** - File yang mengimpor dan menjalankan kalkulator

### Kelas dan Metode:

#### 1. **Kelas `Calculator`**
Kelas inti yang menangani logika perhitungan matematika.

**Atribut:**
- `result` - Menyimpan hasil perhitungan terakhir

**Metode:**
- `tambah(num1, num2)` - Melakukan penjumlahan
- `kurang(num1, num2)` - Melakukan pengurangan
- `kali(num1, num2)` - Melakukan perkalian
- `bagi(num1, num2)` - Melakukan pembagian dengan validasi pembagi nol
- `modulus(num1, num2)` - Menghitung modulus dengan validasi pembagi nol
- `pangkat(num1, num2)` - Menghitung pangkat
- `reset()` - Mengatur ulang hasil ke 0
- `get_result()` - Mengembalikan hasil terakhir

#### 2. **Kelas `CalculatorMenu`**
Kelas yang menangani antarmuka pengguna dan alur program.

**Atribut:**
- `calc` - Objek dari kelas Calculator

**Metode:**
- `menu()` - Menampilkan header dan informasi program
- `screen()` - Loop utama untuk menampilkan antarmuka dan memproses input

## 🖥️ Cara Menjalankan

### Opsi 1: Menjalankan langsung App.py
```bash
python App.py
```

### Opsi 2: Menjalankan melalui Display.py
```bash
python Display.py
```

## 📋 Persyaratan Sistem
- Python 3.x
- Sistem operasi: Windows, Linux, atau macOS

## 🎯 Cara Penggunaan
1. Program akan menampilkan header "SIMPLE CALCULATOR"
2. Masukkan angka pertama
3. Pilih operator (+, -, *, /, %, ^)
4. Masukkan angka kedua
5. Program akan menampilkan hasil perhitungan
6. Pilih 'y' untuk melanjutkan atau 'n' untuk keluar

## ⚠️ Catatan Penting
- Untuk pembagian dengan nol, program akan menampilkan pesan error
- Input harus berupa angka valid (float/integer)
- Operator pangkat dapat menggunakan simbol '^' atau '**'
- Operator perkalian dapat menggunakan '*' atau 'x'
- Program membersihkan layar setiap iterasi untuk pengalaman pengguna yang lebih baik

## 🔧 Teknis Implementasi
- Menggunakan konsep OOP (Object-Oriented Programming)
- Error handling dengan try-except blocks
- Validasi input untuk mencegah crash program
- Kompatibilitas multi-platform dengan penanganan perintah clear screen

## 👨‍💻 Developer
Dikembangkan oleh **agungwin22** - Kalkulator sederhana dengan fungsionalitas lengkap dan antarmuka yang intuitif.

---

**Enjoy calculating!** 🧮
