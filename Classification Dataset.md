#  Classification Dataset

Repository ini berisi kumpulan dataset Machine Learning yang dikelompokkan menjadi tiga jenis klasifikasi, yaitu **Binary Classification, Multiclass Classification, dan Multilabel Classification**.

Tujuan pengumpulan dataset ini adalah untuk memahami perbedaan karakteristik setiap jenis klasifikasi serta mengetahui alasan suatu dataset termasuk ke dalam klasifikasi, bukan regresi.

Seluruh dataset diperoleh dari [Kaggle](https://www.kaggle.com/).

---

##  1. Pengertian Classification

Classification merupakan salah satu metode Supervised Learning dalam Machine Learning yang digunakan untuk memprediksi kategori atau kelas dari suatu data berdasarkan pola yang dipelajari dari data training.

Classification berbeda dengan Regression. Perbedaannya terletak pada jenis output yang dihasilkan:

| Classification | Regression |
|---|---|
| Menghasilkan kategori atau kelas | Menghasilkan nilai numerik kontinu |
| Contoh: Spam atau Not Spam | Contoh: Prediksi harga rumah |
| Contoh: Diabetes atau Tidak | Contoh: Prediksi suhu |
| Evaluasi: Accuracy, Precision, Recall, F1-Score | Evaluasi: MAE, MSE, RMSE, R² |

### Mengapa 9 dataset ini termasuk Classification, bukan Regression?

Kesembilan dataset dipilih karena tujuan prediksinya adalah menentukan kategori atau label tertentu, bukan memperkirakan nilai numerik kontinu.

Meskipun beberapa dataset memiliki fitur berupa angka, seperti usia, kadar gula darah, ukuran bunga, dan kandungan kimia, hal tersebut tidak menjadikannya sebagai regresi.

Hal yang menentukan jenis tugas Machine Learning adalah **variabel target (label) yang ingin diprediksi**, bukan apakah fitur input berbentuk angka atau teks.

---

# 2. Binary Classification

## Pengertian

Binary Classification merupakan jenis klasifikasi yang hanya memiliki dua kemungkinan kelas atau kategori pada variabel target.

Contoh:
- Ya atau Tidak.
- Positif atau Negatif.
- Spam atau Bukan Spam.
- Churn atau Tidak Churn.

## Dataset

### 1. Spam Email Detection Dataset

 [Download Dataset - Kaggle](https://www.kaggle.com/datasets/ssssws/spam-email-detection-dataset-clean-and-ml-ready)

**Deskripsi:**

Dataset ini digunakan untuk mengidentifikasi apakah suatu email termasuk spam (pesan yang tidak diinginkan) atau ham (email normal).

**Alasan termasuk Binary Classification:**

Dataset ini memiliki dua kategori target, yaitu:
- Spam: Email yang terindikasi sebagai pesan tidak diinginkan.
- Ham: Email normal atau bukan spam.

Model Machine Learning mempelajari karakteristik isi email untuk menentukan salah satu dari dua kategori tersebut.

Dataset ini termasuk Classification karena hasil prediksinya berupa kategori email, bukan nilai numerik kontinu.

### 2. Diabetes Prediction Dataset

 [Download Dataset - Kaggle](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)

**Deskripsi:**

Dataset ini berisi informasi kesehatan dan karakteristik pasien yang digunakan untuk memprediksi kemungkinan seseorang menderita diabetes.

Beberapa fitur yang tersedia antara lain:
- Gender.
- Age.
- Hypertension.
- Heart Disease.
- Smoking History.
- BMI.
- HbA1c Level.
- Blood Glucose Level.

**Alasan termasuk Binary Classification:**

Variabel target pada dataset ini adalah `diabetes`, yang memiliki dua kemungkinan nilai:
- 0: Tidak menderita diabetes.
- 1: Menderita diabetes.

Model memprediksi status diabetes berdasarkan karakteristik dan kondisi kesehatan pasien.

Dataset ini termasuk Classification karena output yang dihasilkan adalah kategori status diabetes, bukan prediksi nilai kadar gula darah.

### 3. Telco Customer Churn Dataset

 [Download Dataset - Kaggle](https://www.kaggle.com/datasets/abbas829/telco-customer-churn-dataset)

**Deskripsi:**

Dataset ini berisi informasi pelanggan perusahaan telekomunikasi, seperti data demografi, layanan yang digunakan, informasi kontrak, dan biaya berlangganan.

**Alasan termasuk Binary Classification:**

Variabel target `Churn` memiliki dua kategori:
- Yes: Pelanggan berhenti menggunakan layanan.
- No: Pelanggan tetap menggunakan layanan.

Model bertujuan memprediksi apakah seorang pelanggan akan berhenti berlangganan atau tetap menjadi pelanggan.

Dataset ini termasuk Classification karena hasil prediksinya berupa dua kategori status pelanggan, bukan nilai numerik seperti total biaya berlangganan.

---

# 3. Multiclass Classification

## Pengertian

Multiclass Classification merupakan jenis klasifikasi yang memiliki lebih dari dua kelas atau kategori, tetapi setiap data hanya memiliki satu kelas target.

Contoh:
- Klasifikasi jenis bunga.
- Klasifikasi jenis kacang.
- Klasifikasi kualitas produk.

## Dataset

### 1. Iris Classification Challenge

 [Download Dataset - Kaggle](https://www.kaggle.com/competitions/iris-classification-challenge)

**Deskripsi:**

Dataset Iris digunakan untuk mengklasifikasikan jenis bunga Iris berdasarkan ukuran sepal dan petal.

Terdapat empat fitur utama:
- Sepal Length.
- Sepal Width.
- Petal Length.
- Petal Width.

**Alasan termasuk Multiclass Classification:**

Dataset ini memiliki tiga kategori target, yaitu:
- Iris Setosa.
- Iris Versicolor.
- Iris Virginica.

Setiap bunga hanya memiliki satu spesies sebagai label target.

Model bertugas menentukan satu dari tiga jenis bunga berdasarkan ukuran bagian-bagian bunga tersebut.

Dataset ini termasuk Classification karena hasil prediksinya berupa kategori spesies bunga, bukan nilai ukuran bunga.

### 2. Wine Quality Dataset

 [Download Dataset - Kaggle](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset)

**Deskripsi:**

Dataset ini berisi informasi karakteristik kimia wine yang digunakan untuk menentukan tingkat kualitasnya.

Beberapa fitur yang tersedia:
- Fixed Acidity.
- Volatile Acidity.
- Citric Acid.
- Residual Sugar.
- Chlorides.
- Density.
- pH.
- Sulphates.
- Alcohol.

**Alasan termasuk Multiclass Classification:**

Variabel target `quality` berisi skor kualitas wine yang dapat diperlakukan sebagai kategori kelas.

Contohnya:
- Quality 3.
- Quality 4.
- Quality 5.
- Quality 6.
- Quality 7.
- Quality 8.

Model memprediksi kategori kualitas wine berdasarkan karakteristik kimianya.

Dataset ini termasuk Multiclass Classification apabila setiap skor kualitas diperlakukan sebagai kelas yang berbeda.

**Catatan:** Dataset ini juga dapat digunakan untuk Regression apabila target `quality` diprediksi sebagai nilai numerik. Oleh karena itu, jenis tugas ditentukan berdasarkan pendekatan pemodelan yang digunakan.

### 3. Dry Beans Dataset

 [Download Dataset - Kaggle](https://www.kaggle.com/datasets/whenamancodes/dry-beans-dataset)

**Deskripsi:**

Dataset Dry Beans digunakan untuk mengklasifikasikan varietas kacang kering berdasarkan karakteristik bentuk dan ukuran fisiknya.

Beberapa fitur yang tersedia:
- Area.
- Perimeter.
- Major Axis Length.
- Minor Axis Length.
- Aspect Ratio.
- Eccentricity.
- Convex Area.
- Extent.

**Alasan termasuk Multiclass Classification:**

Dataset ini memiliki tujuh kategori varietas kacang, yaitu:
1. Seker.
2. Barbunya.
3. Bombay.
4. Cali.
5. Dermosan.
6. Horoz.
7. Sira.

Setiap sampel kacang hanya memiliki satu kategori varietas.

Model bertujuan menentukan jenis kacang berdasarkan karakteristik fisiknya.

Dataset ini termasuk Classification karena output yang diprediksi berupa salah satu dari tujuh varietas kacang, bukan nilai numerik ukuran kacang.

---

# 4. Multilabel Classification

## Pengertian

Multilabel Classification merupakan jenis klasifikasi yang memungkinkan satu data memiliki lebih dari satu label sekaligus.

Berbeda dengan Binary dan Multiclass Classification, Multilabel Classification tidak membatasi setiap sampel hanya memiliki satu kategori target.

Contoh:

Satu gambar mobil dapat memiliki dua label:
- Car.
- Red.

Artinya, satu sampel dapat memiliki beberapa karakteristik yang harus diprediksi secara bersamaan.

## Dataset

### 1. Multilabel Small Car and Color Dataset

 [Download Dataset - Kaggle](https://www.kaggle.com/datasets/julichitai/multilabel-small-car-and-color-dataset)

**Deskripsi:**

Dataset ini digunakan untuk mengenali kendaraan dan karakteristik warnanya berdasarkan gambar.

**Alasan termasuk Multilabel Classification:**

Dataset ini dikategorikan sebagai Multilabel Classification karena terdapat dua aspek label yang ingin dikenali, yaitu:
- Jenis atau kategori kendaraan.
- Warna kendaraan.

Sebagai contoh, satu gambar dapat memiliki label Car dan Red secara bersamaan.

Model tidak hanya menentukan satu kategori tunggal, tetapi juga dapat memprediksi beberapa label yang menggambarkan objek tersebut.

### 2. Multi-label Image Classification Dataset

 [Download Dataset - Kaggle](https://www.kaggle.com/datasets/meherunnesashraboni/multi-label-image-classification-dataset)

**Deskripsi:**

Dataset ini digunakan untuk melakukan klasifikasi gambar berdasarkan beberapa kategori atau karakteristik yang terdapat di dalam gambar.

**Alasan termasuk Multilabel Classification:**

Satu gambar memungkinkan memiliki lebih dari satu label sekaligus.

Sebagai contoh, apabila sebuah gambar mengandung beberapa objek, gambar tersebut dapat memiliki label:
- Person.
- Car.
- Tree.

Model bertugas mengidentifikasi seluruh label yang relevan dalam satu gambar, bukan hanya memilih satu kelas yang paling dominan.

Dengan demikian, dataset ini termasuk Multilabel Classification apabila anotasi targetnya memang mengizinkan beberapa label aktif pada satu gambar.

### 3. Road Issues Detection Dataset

 [Download Dataset - Kaggle](https://www.kaggle.com/datasets/programmerrdai/road-issues-detection-dataset/data)

**Deskripsi:**

Dataset ini berkaitan dengan identifikasi berbagai permasalahan yang ditemukan pada kondisi jalan melalui gambar.

Contoh permasalahan yang dapat menjadi kategori identifikasi:
- Jalan berlubang.
- Kerusakan permukaan jalan.
- Permasalahan fasilitas jalan.
- Kondisi lingkungan jalan.

**Alasan termasuk Multilabel Classification:**

Dataset ini dapat dikategorikan sebagai Multilabel Classification apabila satu gambar dapat memiliki beberapa label permasalahan jalan sekaligus.

Contohnya, satu gambar jalan dapat menunjukkan jalan berlubang dan kerusakan permukaan jalan secara bersamaan.

Model harus mampu mengidentifikasi lebih dari satu permasalahan dalam satu gambar.

**Catatan:** Pastikan format anotasi dataset yang diunduh menggunakan beberapa label pada tingkat gambar. Jika anotasinya berupa bounding box untuk mendeteksi objek, tugas tersebut lebih tepat disebut Object Detection, bukan Multilabel Classification biasa.

---

# 5. Perbandingan Ketiga Jenis Classification

| Aspek | Binary | Multiclass | Multilabel |
|---|---|---|---|
| Jumlah kategori | 2 | Lebih dari 2 | Beberapa label |
| Label per data | 1 | 1 | Bisa lebih dari 1 |
| Output | Dua kelas | Satu dari banyak kelas | Kombinasi beberapa label |
| Contoh | Spam / Ham | Setosa / Versicolor / Virginica | Car + Red |

### Ringkasan Dataset

| Jenis Classification | Jumlah Dataset | Dataset |
|---|---:|---|
| Binary Classification | 3 | Spam Email, Diabetes, Telco Churn |
| Multiclass Classification | 3 | Iris, Wine Quality, Dry Beans |
| Multilabel Classification | 3 | Small Car and Color, Multi-label Image, Road Issues |
| **Total** | **9** | **Dataset** |

---

# 6. Kesimpulan

Berdasarkan sembilan dataset yang telah dikumpulkan, Classification dapat dibagi menjadi tiga jenis berdasarkan karakteristik label targetnya.

1. **Binary Classification** digunakan ketika data hanya memiliki dua kemungkinan kelas.
2. **Multiclass Classification** digunakan ketika data memiliki lebih dari dua kelas, tetapi setiap sampel hanya mempunyai satu label.
3. **Multilabel Classification** digunakan ketika satu sampel dapat memiliki beberapa label secara bersamaan.

Kesembilan dataset tersebut termasuk dalam ruang lingkup Supervised Learning karena memiliki target atau label yang digunakan sebagai acuan dalam proses pelatihan model.

Perbedaan utama ketiganya bukan terletak pada jumlah fitur atau banyaknya data, melainkan pada struktur dan karakteristik label yang diprediksi.

---

##  Sumber Dataset

Seluruh dataset bersumber dari Kaggle:

- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Kaggle Competitions](https://www.kaggle.com/competitions)

