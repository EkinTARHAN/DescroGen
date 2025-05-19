import os
import random

# Kaç cümleye tamamlamak istiyorsunuz?
HEDEF_SATIR_SAYISI = 15

# Generic şablonlar ve özellik havuzları
templates = [
    "Bu {kategori}, {özellik} sunar.",
    "{kategori} ile {özellik} artık çok kolay.",
    "Şıklık ve {özellik} bir arada: {kategori}.",
    "{kategori}, {özellik} konusunda öncü.",
    "{kategori} sayesinde {özellik} parmaklarınızın ucunda."
]

ozellikler = [
    "hızlı kullanım",
    "enerji tasarrufu",
    "uzun ömürlü performans",
    "kolay kurulum",
    "şık tasarım",
    "sessiz çalışma",
    "yüksek verimlilik",
    "hafif yapı",
    "konforlu deneyim",
    "güçlü dayanıklılık",
    "pratik taşıma",
    "suya dayanıklılık",
    "gelişmiş güvenlik",
    "uyarlanabilir ayar",
    "uzun pil ömrü"
]

def doldur_dosya(path, kategori):
    # Mevcut cümleleri oku
    with open(path, encoding="utf-8") as f:
        satirlar = [l.strip() for l in f if l.strip()]

    # Eksikse otomatik doldur
    while len(satirlar) < HEDEF_SATIR_SAYISI:
        tpl = random.choice(templates)
        oz = random.choice(ozellikler)
        cümle = tpl.format(kategori=kategori.title(), özellik=oz)
        if cümle not in satirlar:
            satirlar.append(cümle)

    # Dosyayı tekrar yaz
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(satirlar))

def main():
    base = os.path.join("data", "aciklamalar")
    for fn in os.listdir(base):
        if fn.lower().endswith(".txt"):
            kategori = fn[:-4]  # "headphones.txt" → "headphones"
            path = os.path.join(base, fn)
            print(f"Dolduruyor: {fn}")
            doldur_dosya(path, kategori)
    print("Tamamlandı! Her dosyada en az", HEDEF_SATIR_SAYISI, "cümle var artık.")

if __name__ == "__main__":
    main()
