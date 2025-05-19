# import pandas as pd
# import random
# import markovify

# # CSV'den veri çek
# data = pd.read_csv("data/urun_verisi.csv")

# # Kategoriye göre açıklama örnekleri
# ornek_aciklamalar = {
#     "mens fashion": [
#         "Tarzınızı yansıtmak için ideal bir tercih.",
#         "Hem konforlu hem şık bir ürün.",
#         "Yeni sezonun favori parçası olmaya aday.",
#         "Günlük kullanımda rahatlığı ile öne çıkar.",
#         "Zarif ve modern tasarımıyla dikkat çeker.",
#         "Renk uyumu ile kombinlerinize şıklık katar.",
#         "Kaliteli kumaşı sayesinde uzun ömürlüdür.",
#         "Gardırobunuzun vazgeçilmezi olmaya aday.",
#         "Şehirli erkek stiline uygun bir detay.",
#         "Klasik ve spor giyime uyum sağlar.",
#         "Her mevsim şıklığınızı korur.",
#         "Rahat kesimiyle günlük kullanım için ideal.",
#         "Fark yaratmak isteyenlere özel bir parça.",
#         "Sade tasarımıyla her ortama uyum sağlar.",
#         "Estetik ve işlevselliği birleştirir."
#     ],
#     "headphones": [
#         "Müziğin tadını sonuna kadar çıkarın.",
#         "Yüksek ses kalitesi ve uzun pil ömrü.",
#         "Kablosuz bağlantı ile hareket özgürlüğü.",
#         "Her notayı en ince detayına kadar hissedin.",
#         "Gürültü engelleme teknolojisi ile kesintisiz keyif.",
#         "Stüdyo kalitesinde ses deneyimi sunar.",
#         "Günlük kullanıma uygun şık tasarım.",
#         "Katlanabilir yapısıyla kolayca taşınır.",
#         "Bluetooth 5.0 ile kesintisiz bağlantı.",
#         "Derin bass performansı ile fark yaratır.",
#         "Konforlu kulak yastıklarıyla uzun süre kullanım.",
#         "Net çağrı kalitesi sunar.",
#         "Hem spor hem seyahat için idealdir.",
#         "Şarj etmeden saatlerce müzik dinleyin.",
#         "Mobil cihazlarla tam uyum sağlar."
#     ],
#     "air conditioners": [
#         "Yaz sıcaklarında ideal serinlik sağlar.",
#         "Sessiz ve etkili soğutma performansı sunar.",
#         "Enerji tasarruflu yapısıyla öne çıkar.",
#         "Kolay kurulum ve kullanım imkanı.",
#         "Ferahlatıcı bir ortam için birebir.",
#         "Otomatik sıcaklık ayarlama sistemi mevcuttur.",
#         "Gece modu ile sessiz çalışma sunar.",
#         "Uzaktan kumandayla kolay kontrol imkanı.",
#         "Modern yaşam alanlarına uyumlu tasarım.",
#         "Yüksek BTU kapasitesiyle hızlı soğutma sağlar.",
#         "Filtre sistemi ile daha temiz hava sağlar.",
#         "Programlanabilir zamanlayıcı ile enerji verimliliği.",
#         "Çoklu fan hızları ile kişiselleştirme imkanı.",
#         "Estetik dış tasarımı ile şık görünüm.",
#         "Tüm mevsimlerde dengeli iklimlendirme sağlar."
#     ],
#     "watches": [
#         "Zamansız tasarımıyla stilinize şıklık katar.",
#         "Her kombine uyum sağlayan zarif detaylar.",
#         "Hassas zaman ölçümü ve dayanıklı yapı.",
#         "Modern ve klasik çizgileri bir araya getirir.",
#         "Günlük kullanım için ideal saat deneyimi.",
#         "Spor ve klasik giyime uyum sağlar.",
#         "Takvim ve kronometre fonksiyonları içerir.",
#         "Analog ve dijital seçenekleri mevcuttur.",
#         "Silikon kayışı ile konforlu bilek hissi.",
#         "Paslanmaz çelik gövde ile uzun ömürlü kullanım.",
#         "Suya dayanıklı yapısıyla her koşula uygun.",
#         "Stil sahibi kullanıcılar için özel tasarlandı.",
#         "Göz alıcı detaylarla tasarlanmış eşsiz bir saat.",
#         "Kadran aydınlatma özelliği ile gece kullanımına uygun.",
#         "Her ortamda şıklığınızı tamamlar."
#     ]
# }

# # Markov modelleri (state_size=1: çeşitlilik için)
# markov_modelleri = {
#     kategori: markovify.Text(" ".join(cumleler), state_size=1)
#     for kategori, cumleler in ornek_aciklamalar.items()
# }

# # Yedek açıklamalar
# fallbacklar = [
#     "Bu ürün fonksiyonelliğiyle öne çıkar.",
#     "Kullanıcı dostu tasarımıyla dikkat çeker.",
#     "Fark yaratan özellikleriyle ideal bir tercih.",
#     "Şıklık ve performans bir arada sunulur.",
#     "Günlük kullanımda pratik çözümler sağlar.",
#     "Konfor ve kaliteyi bir arada sunar.",
#     "Estetik görünümüyle öne çıkan bir üründür."
# ]

# # Ana üretim fonksiyonu
# def urun_uret(kategori, adet=3):
#     kategori = kategori.strip().lower()
#     secenekler = data[data['kategori'].str.lower() == kategori]

#     if len(secenekler) < adet:
#         mevcutlar = sorted(data['kategori'].str.lower().unique())
#         return None, [f"Bu kategoriye ait yeterli ürün yok. Mevcut kategoriler: {', '.join(mevcutlar)}"]

#     örnekler = secenekler.sample(adet)
#     sonuc = []
#     önceden_üretiler = set()  # Bu turdaki tüm açıklamaları takip eder

#     for _, row in örnekler.iterrows():
#         isim = f"{row['isim_kelime1']} {row['isim_kelime2']}"
#         model = markov_modelleri.get(kategori)
#         aciklama = None
#         denenenler = set()

#         for _ in range(20):  # Daha fazla deneme hakkı
#             olasi = model.make_sentence(tries=100) if model else None
#             if olasi and olasi not in denenenler and olasi not in önceden_üretiler:
#                 aciklama = olasi
#                 önceden_üretiler.add(olasi)
#                 break
#             if olasi:
#                 denenenler.add(olasi)

#         if not aciklama:
#             aciklama = random.choice(fallbacklar)

#         fiyat = random.randint(299, 2999)
#         puan = round(random.uniform(3.5, 5.0), 1)
#         yildiz = "★" * int(puan) + "☆" * (5 - int(puan))

#         sonuc.append((isim, aciklama, f"{fiyat} TL", f"{yildiz} {puan}/5"))

#     return True, sonuc

import os
import pandas as pd
import random
import markovify

# ——— Proje kök dizini ———
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ——— Ürün verisini yükle ———
data = pd.read_csv(os.path.join(BASE_DIR, "data", "urun_verisi.csv"))

# ——— Markov için .txt klasörünü tara ———
aciklama_klasoru = os.path.join(BASE_DIR, "data", "aciklamalar")
markov_modelleri = {}
if os.path.isdir(aciklama_klasoru):
    for dosya in os.listdir(aciklama_klasoru):
        if dosya.lower().endswith(".txt"):
            kategori = dosya[:-4].strip().lower()
            path = os.path.join(aciklama_klasoru, dosya)
            with open(path, "r", encoding="utf-8-sig", errors="ignore") as f:
                lines = [l.strip() for l in f.read().splitlines() if l.strip()]
            if len(lines) >= 5:
                text = " ".join(lines)
                # iki farklı model varyasyonu
                markov_modelleri[kategori] = (
                    markovify.Text(text, state_size=1),
                    markovify.Text(text, state_size=2)
                )

# ——— Generic şablon ve özellik havuzu ———
generic_templates = [
    "Bu {category}, {feature} sunar.",
    "{category} ile {feature} artık çok kolay.",
    "Şıklık ve {feature} bir arada: {category}.",
    "{category}, {feature} konusunda öncü.",
    "{category} sayesinde {feature} parmaklarınızın ucunda."
]
generic_features = [
    "yüksek performans", "uzun pil ömrü", "enerji tasarrufu",
    "kolay kullanım", "şık tasarım", "sessiz çalışma",
    "güvenli saklama", "hızlı erişim", "gelişmiş fonksiyonellik",
    "uygulama desteği", "modüler yapı", "dayanıklı malzeme"
]

# ——— Fallback cümleleri (nadiren kullanılır) ———
fallbacklar = [
    "Bu ürün fonksiyonelliğiyle öne çıkar.",
    "Günlük kullanıma pratik çözümler sunar.",
    "Kalite ve konforu bir arada yaşatır.",
    "Estetik ve dayanıklılığı bir arada sunar.",
    "Tasarımı kadar performansıyla da fark yaratır."
]

def urun_uret(kategori, adet=3):
    kat = kategori.strip().lower()
    # kategori yoksa bile, tüm CSV kategorileri için devam edeceğiz
    secenekler = data[data['kategori'].str.lower() == kat]
    if len(secenekler) < adet:
        mevcut = sorted(data['kategori'].str.lower().unique())
        return None, [f"Bu kategoriye ait yeterli ürün yok. Mevcut kategoriler: {', '.join(mevcut)}"]

    örnekler = secenekler.sample(adet)
    sonuc = []
    üretilen = set()

    for _, row in örnekler.iterrows():
        isim = f"{row['isim_kelime1']} {row['isim_kelime2']}"
        aciklama = None

        # 1) Eğer Markov modeli varsa, ondan üret
        if kat in markov_modelleri:
            models = markov_modelleri[kat]
            denenen = set()
            for _ in range(20):
                parcalar = []
                for m in models:
                    s = m.make_sentence(tries=100)
                    if s and s not in denenen:
                        parcalar.append(s)
                        denenen.add(s)
                if parcalar:
                    tmp = ". ".join(parcalar).rstrip(".") + "."
                    if tmp not in üretilen:
                        aciklama = tmp
                        üretilen.add(tmp)
                        break

        # 2) Model yoksa veya Markov’dan üretilemediyse generic şablonla üret
        if not aciklama:
            tpl = random.choice(generic_templates)
            feat = random.choice(generic_features)
            tmp = tpl.format(category=kat.title(), feature=feat)
            aciklama = tmp
            üretilen.add(tmp)

        # 3) Yine de açıklama yoksa statik fallback
        if not aciklama:
            aciklama = random.choice(fallbacklar)
            üretilen.add(aciklama)

        fiyat = random.randint(299, 2999)
        puan = round(random.uniform(3.5, 5.0), 1)
        yildiz = "★" * int(puan) + "☆" * (5 - int(puan))
        sonuc.append((isim, aciklama, f"{fiyat} TL", f"{yildiz} {puan}/5"))

    return True, sonuc

