import pandas as pd
import os
import random

input_folder = "Amazon_Data"
output_file = "data/urun_verisi.csv"

# Kullanılabilecek açıklama şablonları
sablonlar = [
    "{isim}, kullanıcı deneyimini üst seviyeye taşıyor.",
    "Yeni {isim}, şıklık ve performansı bir araya getiriyor.",
    "{isim}, gelişmiş özellikleriyle hayatınızı kolaylaştırır.",
    "Evinizin vazgeçilmezi: {isim}.",
    "{isim}, kaliteyi uygun fiyatla sunar.",
    "{isim}, her alanda etkileyici bir performans sunar."
]

all_data = []

for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)
        try:
            df = pd.read_csv(file_path)
            df.columns = [col.lower().strip() for col in df.columns]

            if 'name' not in df.columns:
                print(f"⚠️ {filename} içinde 'name' sütunu yok. Atlanıyor.")
                continue

            df = df[['name']].dropna()
            df = df.sample(n=min(100, len(df)), random_state=42)

            kategori = filename.replace(".csv", "").strip().lower()

            def ayir(baslik):
                kelimeler = str(baslik).strip().split()
                if len(kelimeler) >= 2:
                    return kelimeler[0], kelimeler[1]
                elif len(kelimeler) == 1:
                    return kelimeler[0], "Ürün"
                else:
                    return "Genel", "Ürün"

            df[['isim_kelime1', 'isim_kelime2']] = df['name'].apply(lambda x: pd.Series(ayir(x)))

            def rastgele_sablon(k1, k2):
                isim = f"{k1} {k2}"
                sablon = random.choice(sablonlar)
                return sablon.replace("{isim}", isim)

            df['aciklama_sablon'] = df.apply(
                lambda row: rastgele_sablon(row['isim_kelime1'], row['isim_kelime2']), axis=1
            )

            df['kategori'] = kategori

            all_data.append(df[['kategori', 'isim_kelime1', 'isim_kelime2', 'aciklama_sablon']])

        except Exception as e:
            print(f"❌ Hata oluştu: {filename} → {e}")

# Sonuçları birleştir
if all_data:
    os.makedirs("data", exist_ok=True)
    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_csv(output_file, index=False)
    print(f"✅ {output_file} başarıyla oluşturuldu. Toplam {len(final_df)} satır.")
else:
    print("❌ Uygun veri bulunamadı.")
