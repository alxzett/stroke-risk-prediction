# Panduan Pemilihan Algoritma Klasifikasi (Machine Learning)

Repositori ini merangkum kondisi ideal penggunaan berbagai algoritma klasifikasi berdasarkan publikasi paper ilmiah, jurnal akademik (termasuk terindeks SINTA dan Scopus), serta dokumentasi web resmi yang terpercaya.

##  Ringkasan

| Algoritma | Kondisi Ideal / Kapan Digunakan | Kelebihan Utama | Keterbatasan | 
| ----- | ----- | ----- | ----- | 
| **Logistic Regression** | Baseline model, klasifikasi biner, butuh probabilitas kelas, hubungan fitur dan target cenderung linear. | Cepat, mudah diinterpretasi, hemat komputasi. | Buruk pada pola non-linear kompleks & fitur yang saling berkorelasi tinggi (multikolinearitas). | 
| **Naive Bayes** | Klasifikasi teks (spam, analisis sentimen), data dimensi tinggi, butuh prediksi super cepat (real-time). | Sangat cepat, bekerja baik meski dengan data latih yang relatif sedikit. | Asumsi fitur saling independen jarang terjadi di dunia nyata. | 
| **K-Nearest Neighbors (KNN)** | Dataset kecil-menengah, jumlah fitur sedikit, pola batas keputusan sangat tidak beraturan (non-linear). | Tanpa fase *training* (lazy learner), intuitif, mudah diimplementasikan. | Lambat saat prediksi jika data besar, sensitif terhadap *outlier* dan skala data. | 
| **Decision Tree (CART/C4.5)** | Butuh transparansi aturan (*explainable AI*), campuran data numerik & kategorikal, tanpa perlu normalisasi. | Sangat mudah divisualisasikan & dijelaskan ke non-teknis. | Sangat rentan *overfitting* dan tidak stabil terhadap perubahan kecil pada data. | 
| **Support Vector Machine (SVM)** | Dimensi tinggi (fitur > sampel), pemisahan margin yang jelas (teks, citra medis, bioinformatika). | Efektif di ruang dimensi tinggi, fleksibel dengan *kernel trick*. | Komputasi berat pada dataset besar (>100.000 baris), sulit diinterpretasi. | 
| **Random Forest** | Data tabular umum, banyak *noise* atau *missing values*, ingin akurasi tinggi tanpa banyak *tuning*. | Tahan *overfitting*, stabil, bisa mengukur tingkat kepentingan fitur (*feature importance*). | Ukuran model besar, prediksi lebih lambat dibanding model linear. | 
| **Gradient Boosting (XGBoost/LightGBM)** | Kompetisi data, data tabular kompleks, distribusi kelas timpang (*imbalanced data*), prioritas akurasi maksimal. | Performa & akurasi tertinggi untuk data tabular. | Rentan *overfitting* jika parameter tidak di-*tuning* dengan tepat, sensitif terhadap *outlier*. | 

##   Berdasarkan Kondisi Dataset

1. **Jika Dataset Kecil (< 1.000 baris):**
   * Gunakan **Naive Bayes**, **Logistic Regression**, atau **SVM** (linear). Hindari model yang terlalu kompleks agar tidak *overfitting*.

2. **Jika Dataset Sangat Besar (> 100.000 baris):**
   * Gunakan **LightGBM**, **XGBoost**, atau **Logistic Regression (dengan SGD)**. Hindari KNN dan SVM dengan kernel non-linear karena waktu komputasi kuadratik/kubik.

3. **Jika Jumlah Fitur Sangat Banyak (Teks / Genomik):**
   * Gunakan **Naive Bayes** (Multinomial/Bernoulli) atau **Linear SVM**.

4. **Jika Butuh Interpretasi Bisnis / Medis (White-Box):**
   * Gunakan **Decision Tree** atau **Logistic Regression** (melihat nilai *odds ratio*).

5. **Jika Data Kotor (Banyak Outlier & Missing Values):**
   * Gunakan algoritma berbasis pohon seperti **Random Forest** atau **XGBoost** (sudah memiliki penanganan *missing value* bawaan dan tidak sensitif terhadap skala/outlier).

##  Referensi

* **Paper & Jurnal Internasional:**
  * Fernández-Delgado, M., Cernadas, E., Barro, S., & Amorim, D. (2014). *Do we need hundreds of classifiers to solve real world classification problems?*. The Journal of Machine Learning Research (JMLR), 15(1), 3133-3181. *(Studi komparasi 179 algoritma pada 121 dataset yang menyimpulkan Random Forest dan SVM sebagai algoritma terbaik untuk penggunaan umum).*
  * Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). *Why do tree-based models still outperform deep learning on typical tabular data?*. Advances in Neural Information Processing Systems (NeurIPS), 35, 507-520. *(Paper rujukan utama yang membuktikan keunggulan Random Forest, XGBoost, dan LightGBM pada data tabular).*
  * Chen, T., & Guestrin, C. (2016). *XGBoost: A scalable tree boosting system*. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785-794. *(Paper dasar algoritma Gradient Boosting modern).*
  * Kotsiantis, S. B. (2007). *Supervised machine learning: A review of classification techniques*. Informatica, 31(3), 249-268. *(Jurnal rujukan klasik untuk perbandingan karakteristik Decision Tree, Naive Bayes, KNN, dan SVM).*

* **Website & Dokumentasi Resmi Terpercaya:**
  * **Scikit-Learn Official Documentation:** [Choosing the right estimator (Flowchart & Guidelines)](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) - Dokumentasi standar industri untuk pemilihan algoritma berbasis ukuran dan sifat sampel.
  * **Google Machine Learning Education:** [Machine Learning Guides & Crash Course](https://developers.google.com/machine-learning) - Panduan resmi dari tim riset dan *engineering* Google terkait pemilihan model klasifikasi dan penanganan data.
  * **Microsoft Azure Machine Learning Documentation:** [Machine Learning Algorithm Cheat Sheet](https://learn.microsoft.com/en-us/azure/machine-learning/algorithm-cheat-sheet) - Panduan teknis pemilihan algoritma berdasarkan kebutuhan bisnis dan sifat data dari Microsoft.