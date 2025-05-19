# Ürün İsmi + Açıklama Üretici

 DescroGen

## İçindekiler

- [Proje Açıklaması](#proje-açıklaması)
- [Özellikler](#özellikler)
- [Teknoloji Yığını](#teknoloji-yığını)
- [Ön Koşullar](#ön-koşullar)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Dosyalar ve Scriptler](#dosyalar-ve-scriptler)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Gelecek Geliştirmeler](#gelecek-geliştirmeler)
- [Lisans](#lisans)
- [İletişim](#iletişim)

## Proje Açıklaması

Ürün İsmi + Açıklama Üretici projesi, kullanıcıdan aldığı ürün başlığına dayanarak otomatik metin açıklamaları üreten bir web uygulamasıdır. Bu proje, hem şablon tabanlı (rule-based) hem de veri-temelli (Markov zinciri) üretken yapay zeka tekniklerini bir arada kullanarak üç farklı açıklama önerisi sunar.

- **Şablon Tabanlı Üretim:** Önceden tanımlı cümle şablonları ve özellik listelerinden rastgele seçim yapar.
- **Markov Zinciri Üretimi:** Eğitim verisindeki cümlelerden öğrenilen n-gram geçiş olasılıklarını kullanarak benzersiz metinler oluşturur.
- **Dinamik Özellikler:** Her açıklamaya rastgele fiyat ve puan (★★★★★) eklenerek daha gerçekçi ürün tanıtımları hazırlanır.

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
- HTML / CSS / Bootstrap (veya tercih edilen stil kütüphanesi)

## Ön Koşullar

- Python 3.7 veya üzeri
- Git

## Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/kullanici_adi/urun-aciklama-ureticisi.git
   cd urun-aciklama-ureticisi
   ```
2. Sanal ortam oluşturun ve etkinleştirin:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
4. Veri dosyalarını oluşturun (opsiyonel):
   ```bash
   python convert_all_csvs.py
   python populate_aciklamalar.py
   ```

## Kullanım

1. Uygulamayı çalıştırın:
   ```bash
   python app.py
   ```
2. Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.
3. Açılan sayfadan kategori seçip "Üret" butonuna tıklayın.
4. Üç farklı açıklamayı ve fiyat/puan bilgisini görüntüleyin.
5. İsterseniz Markov modu için `generator.urun_uret(kategori, mode="markov")` parametresini kullanın.

## Proje Yapısı

```
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
```

## Dosyalar ve Scriptler

- **app.py:** Flask sunucusu ve web arayüzü.
- **generator.py:** `urun_uret` fonksiyonu; template ve Markov modellerini içerir.
- **convert_all_csvs.py:** Amazon veri CSV’lerini `urun_verisi.csv` dosyasına dönüştürür.
- **populate_aciklamalar.py:** Her kategori `.txt` dosyasını minimum cümle sayısına tamamlar.
- **data/**: Ürün verisi ve açıklama örnekleri.
- **templates/index.html:** Kullanıcı arayüzü.

## Katkıda Bulunma

1. Depoyu fork’layın.
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-özellik`).
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik ekle'`).
4. Branch’inizi push’layın (`git push origin feature/yeni-özellik`).
5. Pull request oluşturun.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## İletişim

- **Adınız Soyadınız** 
- Ekin TARHAN
- ekintrhn@gmail.com
- GitHub: [EkinTARHAN](https://github.com/EkinTARHAN)

