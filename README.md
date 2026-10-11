# Prediksi Risiko Stroke dengan Machine Learning

## Deskripsi Proyek
Proyek ini merupakan praktikum machine learning untuk menganalisis dataset risiko stroke dan membangun model klasifikasi yang memprediksi kategori `Stroke_Risk`.

Tahapan yang dilakukan dalam notebook:
- Memuat dan memahami dataset.
- Melakukan Exploratory Data Analysis (EDA), termasuk pemeriksaan missing values, duplikasi, distribusi data, dan korelasi.
- Memisahkan fitur (`X`) dan target (`y`), kemudian membagi data menjadi data training dan testing.
- Melakukan preprocessing melalui `Pipeline` dan `ColumnTransformer`, meliputi imputasi missing values, standardisasi fitur numerik, serta encoding fitur kategorikal.
- Melatih dan membandingkan tiga algoritma klasifikasi: Logistic Regression, Random Forest, dan Hist Gradient Boosting.
- Mengevaluasi model menggunakan Accuracy, Precision, Recall, F1-Score, Classification Report, dan Confusion Matrix.
- Menyimpan model Hist Gradient Boosting ke file `stroke_model.pkl` menggunakan Joblib.

## Struktur Folder

Pastikan susunan file di repository seperti berikut agar lokasi dataset sesuai dengan kode di notebook:

```text
stroke-risk-prediction/
├── README.md
├── requirements.txt
├── stroke_risk_analysis.ipynb
├── stroke_model.pkl
└── Dataset/
    └── stroke_risk_prediction_dataset.csv
```

> Nama notebook boleh berbeda. Jika menggunakan nama lain, sesuaikan dengan file notebook yang kamu unggah. Nama dan lokasi file dataset harus cocok dengan kode `pd.read_csv("Dataset/stroke_risk_prediction_dataset.csv")`.

## Dataset
Dataset yang digunakan adalah `stroke_risk_prediction_dataset.csv`. Target prediksi pada proyek ini adalah kolom `Stroke_Risk`.

Jika dataset berasal dari Kaggle atau sumber lain, cantumkan tautan sumber dan ikuti lisensi atau ketentuan penggunaan dataset tersebut.

## Persiapan dan Menjalankan Notebook

1. Instal Python (disarankan Python 3.10 atau versi yang kompatibel dengan versi library yang digunakan).
2. Unduh atau clone repository ini ke komputer.
3. Buka terminal pada folder proyek.
4. Instal library yang dibutuhkan:

   ```bash
   pip install -r requirements.txt
   ```

5. Buka notebook `stroke_risk_analysis.ipynb` menggunakan Jupyter Notebook, JupyterLab, atau VS Code.
6. Pastikan file dataset berada di folder `Dataset/`.
7. Jalankan sel notebook dari atas ke bawah.

## Memuat Model yang Sudah Disimpan

File `stroke_model.pkl` berisi pipeline model yang telah disimpan dengan Joblib. Untuk memuatnya kembali:

```python
import joblib

model = joblib.load("stroke_model.pkl")
```

Pipeline mencakup preprocessing dan model klasifikasi, sehingga data baru harus memiliki kolom fitur yang sesuai dengan data yang digunakan saat pelatihan.

## Catatan Penting
- Hasil evaluasi hanya menggambarkan performa model pada eksperimen dan pembagian data yang digunakan; hasil tersebut bukan pengganti diagnosis atau saran tenaga medis.
- File model `.pkl` sebaiknya hanya dimuat jika berasal dari sumber yang tepercaya.
- Untuk reproduksibilitas yang lebih baik, gunakan versi Python dan library yang konsisten dengan lingkungan saat model dilatih.

## Teknologi
- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- Joblib
- Jupyter Notebook
