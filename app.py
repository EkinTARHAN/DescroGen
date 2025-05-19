from flask import Flask, render_template, request
import pandas as pd
from generator import urun_uret
import webbrowser
import threading

app = Flask(__name__)

# Tüm CSV kategorilerini dropdown’a alıyoruz
df = pd.read_csv("data/urun_verisi.csv")
kategoriler = sorted(df["kategori"].str.lower().unique())

@app.route("/", methods=["GET", "POST"])
def index():
    urunler = []
    hata = ""
    secili_kategori = ""

    if request.method == "POST":
        secili_kategori = request.form.get("kategori")
        basarili, sonuc = urun_uret(secili_kategori)
        if basarili:
            urunler = sonuc
        else:
            hata = sonuc[0]

    return render_template(
        "index.html",
        kategoriler=kategoriler,
        secili_kategori=secili_kategori,
        urunler=urunler,
        hata=hata
    )

if __name__ == "__main__":
    # 1.5 saniye sonra varsayılan tarayıcıda aç
    threading.Timer(1.5, lambda: webbrowser.open("http://127.0.0.1:5000/")).start()
    app.run(debug=True)
