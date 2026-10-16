
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Memuat model klasifikasi risiko stroke
model = joblib.load("stroke_model.pkl")

# Fitur yang digunakan saat pelatihan model
features = [
    "Age",
    "Gender",
    "Country",
    "Height_cm",
    "Weight_kg",
    "BMI",
    "Blood_Pressure_Systolic",
    "Blood_Pressure_Diastolic",
    "Heart_Rate",
    "Blood_Glucose",
    "HbA1c",
    "Total_Cholesterol",
    "HDL",
    "LDL",
    "Triglycerides",
    "Smoking_Status",
    "Alcohol_Consumption",
    "Physical_Activity_Level",
    "Sleep_Hours",
    "Stress_Level",
    "Diet_Quality",
    "Family_History_Stroke",
    "Family_History_Heart_Disease",
    "Diabetes",
    "Hypertension",
    "Heart_Disease",
    "Previous_TIA",
    "Atrial_Fibrillation",
    "Chronic_Kidney_Disease",
    "Medication_Adherence",
    "Exercise_Hours_Per_Week",
    "Daily_Walking_Minutes",
    "Work_Type",
    "Residence_Type",
    "Air_Pollution_Exposure"
]


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Mengambil data JSON
        content = request.get_json(silent=True)

        if not content or "data" not in content:
            return jsonify({
                "error": "JSON harus memiliki properti 'data'."
            }), 400

        data = content["data"]

        if not isinstance(data, list) or len(data) == 0:
            return jsonify({
                "error": "'data' harus berupa list berisi data pasien."
            }), 400

        # Mengubah data menjadi DataFrame
        df = pd.DataFrame(data)

        # Memastikan semua fitur tersedia
        missing = [f for f in features if f not in df.columns]

        if missing:
            return jsonify({
                "error": "Fitur berikut belum tersedia.",
                "missing_features": missing
            }), 400

        # Menyusun fitur sesuai urutan saat pelatihan
        df = df[features]

        # Melakukan prediksi untuk semua pasien
        predictions = model.predict(df)

        # Mengambil probabilitas jika model mendukungnya
        results = []

        for i, prediction in enumerate(predictions):
            result = {
                "pasien_ke": i + 1,
                "prediksi_risiko_stroke": str(prediction)
            }

            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba(df.iloc[[i]])[0]

                result["probabilitas"] = {
                    str(label): round(float(prob), 4)
                    for label, prob in zip(
                        model.classes_, probabilities
                    )
                }

            results.append(result)

        return jsonify({
            "jumlah_pasien": len(results),
            "hasil_prediksi": results
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
