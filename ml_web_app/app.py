# from flask import Flask, render_template, request
# import pickle
# import numpy as np

# app = Flask(__name__)

# # Memuat model KMeans dari file
# with open('model/kmeans_model.pkl', 'rb') as f:
#     kmeans_model = pickle.load(f)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Mengambil data dari form
#     kopi = float(request.form['kopi'])
#     kelapa_sawit = float(request.form['kelapa_sawit'])
#     sarang_burung_walet = float(request.form['sarang_burung_walet'])
#     susu_dan_olahannya = float(request.form['susu_dan_olahannya'])

#     # Membuat array fitur untuk prediksi
#     features = np.array([[kopi, kelapa_sawit, sarang_burung_walet, susu_dan_olahannya]])

#     # Melakukan prediksi
#     prediction = kmeans_model.predict(features)

#     # Menampilkan hasil prediksi
#     return render_template('index.html', prediction_text=f'Cluster: {prediction[0]}')

# if __name__ == "__main__":
#     app.run(debug=True)



# 2


from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Memuat model KMeans dari file
with open('model/kmeans_model.pkl', 'rb') as f:
    kmeans_model = pickle.load(f)

# Rekomendasi berdasarkan cluster
recommendations = {
    0: "Cluster 0: Disarankan untuk fokus pada peningkatan produksi kopi dan kelapa sawit. Pertimbangkan untuk mengekspor produk kopi premium ke pasar internasional.",
    1: "Cluster 1: Disarankan untuk meningkatkan produksi sarang burung walet. Produk ini memiliki permintaan tinggi di pasar Asia.",
    2: "Cluster 2: Disarankan untuk diversifikasi produk dengan mengekspor susu dan olahannya. Pasar luar negeri sangat membutuhkan produk susu berkualitas.",
    3: "Cluster 3: Disarankan untuk diversifikasi produk dan fokus pada pemasaran produk berkualitas. Pertimbangkan untuk mengekspor kopi dan produk olahan susu ke pasar internasional.",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Mengambil data dari form
    kopi = float(request.form['kopi'])
    kelapa_sawit = float(request.form['kelapa_sawit'])
    sarang_burung_walet = float(request.form['sarang_burung_walet'])
    susu_dan_olahannya = float(request.form['susu_dan_olahannya'])

    # Membuat array fitur untuk prediksi
    features = np.array([[kopi, kelapa_sawit, sarang_burung_walet, susu_dan_olahannya]])

    # Melakukan prediksi
    prediction = kmeans_model.predict(features)

    # Mendapatkan rekomendasi berdasarkan cluster yang diprediksi
    cluster_number = prediction[0]
    recommendation_text = recommendations.get(cluster_number, "Rekomendasi tidak tersedia untuk cluster ini.")

    # Menampilkan hasil prediksi dan rekomendasi
    return render_template('index.html', 
                           prediction_text=f'Cluster: {cluster_number}', 
                           recommendation_text=recommendation_text)

if __name__ == "__main__":
    app.run(debug=True)