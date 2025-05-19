# DescroGen  
**Ürün İsmi + Açıklama Üretici**

![Project Logo](./assets/logo.png)

**Proje Linki:**  
[https://github.com/EkinTARHAN/descrogen](https://github.com/EkinTARHAN/descrogen)

**Canlı Demo (Opsiyonel):**  
`http://127.0.0.1:5000` — lokal olarak çalıştırdığınızda erişilebilir.

## İçindekiler

- [Proje Açıklaması](#proje-açıklaması)  
- [Veri Seti](#veri-seti)  
- [Özellikler](#özellikler)  
- [Teknoloji Yığını](#teknoloji-yığını)  
- [Ön Koşullar](#ön-koşullar)  
- [Kurulum](#kurulum)  
- [Kullanım](#kullanım)  
- [Proje Yapısı](#proje-yapısı)  
- [Dosyalar ve Scriptler](#dosyalar-ve-scriptler)  
- [Katkıda Bulunma](#katkıda-bulunma)  
- [Lisans](#lisans)  
- [İletişim](#iletişim)  

## Proje Açıklaması

DescroGen, kullanıcıdan aldığı ürün başlığına dayanarak otomatik metin açıklamaları üreten bir web uygulamasıdır.  
Bu proje, hem şablon tabanlı (rule-based) hem de veri-temelli (Markov zinciri) üretken yapay zeka tekniklerini bir arada kullanarak üç farklı açıklama önerisi sunar:

- **Şablon Tabanlı Üretim:** Önceden tanımlı cümle şablonları ve özellik listelerinden rastgele seçim yapar.  
- **Markov Zinciri Üretimi:** Eğitim verisindeki cümlelerden öğrenilen n-gram geçiş olasılıklarını kullanarak benzersiz metinler oluşturur.  
- **Dinamik Özellikler:** Her açıklamaya rastgele fiyat ve puan (★★★★★) eklenerek daha gerçekçi ürün tanıtımları hazırlanır.  

## Veri Seti

- **Ad:** Amazon Ürün Veri Seti  
- **Dosya:** `data/urun_verisi.csv`  
- **Link:** [Raw CSV](https://raw.githubusercontent.com/EkinTARHAN/descrogen/main/data/urun_verisi.csv)  

## Özellikler

- Kullanıcı dostu web arayüzü (Flask tabanlı).  
- Kategori seçimine göre dinamik açıklama üretimi.  
- Hem rule-based hem de Markov tabanlı metin oluşturma modları.  
- Aynı başlık için üç farklı açıklama alternatifi.  
- Fiyat ve puan (5 üzerinden yıldız) bilgisi otomatik ekleme.  
- `.csv` dosyası ve `.txt` dosyalarıyla kolay veri yönetimi.  

## Teknoloji Yığını

- Python 3.12.10  
- Flask  
- Pandas  
- markovify  
- Jinja2  
- HTML / CSS / Bootstrap (veya tercihinize göre başka bir stil kütüphanesi)  

## Ön Koşullar

- Python 3.7 veya üzeri  
- Git  

## Kurulum

1. Depoyu klonlayın:  
   ```bash
   git clone https://github.com/EkinTARHAN/descrogen.git
   cd descrogen
Sanal ortam oluşturun ve etkinleştirin:

bash
Kopyala
Düzenle
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Gerekli paketleri yükleyin:

bash
Kopyala
Düzenle
pip install -r requirements.txt
(Opsiyonel) Veri dosyalarını oluşturun:

bash
Kopyala
Düzenle
python convert_all_csvs.py
python populate_aciklamalar.py
Kullanım
Uygulamayı çalıştırın:

bash
Kopyala
Düzenle
python app.py
Tarayıcınızda http://127.0.0.1:5000 adresine gidin.

Açılan sayfadan kategori seçip Üret butonuna tıklayın.

Üç farklı açıklamayı, fiyat ve puan bilgisini görüntüleyin.

İsterseniz Markov modu için:

python
Kopyala
Düzenle
generator.urun_uret(kategori, mode="markov")
Proje Yapısı
cpp
Kopyala
Düzenle
├── app.py
├── generator.py
├── convert_all_csvs.py
├── populate_aciklamalar.py
├── data
│   ├── urun_verisi.csv
│   └── aciklamalar
│       ├── kategori1.txt
│       ├── kategori2.txt
│       └── ...
├── templates
│   └── index.html
├── static
│   └── assets
│       └── logo.png
└── requirements.txt
Dosyalar ve Scriptler
app.py: Flask sunucusu ve web arayüzü.

generator.py: urun_uret fonksiyonunu barındırır (template + Markov modeller).

convert_all_csvs.py: Amazon ürün CSV’lerini birleştirip data/urun_verisi.csv oluşturur.

populate_aciklamalar.py: Her kategori .txt dosyasını asgari satır sayısına tamamlar.

data/: Ürün verisi (.csv) ve açıklama örnekleri (.txt).

templates/index.html: Kullanıcı arayüzü HTML şablonu.

Katkıda Bulunma
Depoyu fork’layın.

Yeni bir branch oluşturun (git checkout -b feature/yeni-özellik).

Değişikliklerinizi commit edin (git commit -m "Yeni özellik ekle").

Branch’inizi push’layın (git push origin feature/yeni-özellik).

Pull request oluşturun.

Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.

İletişim
Ekin TARHAN

Email: ekintrhn@gmail.com

GitHub: EkinTARHAN
