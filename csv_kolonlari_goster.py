import pandas as pd

# Örnek bir CSV dosyasının yolu (Amazon_Data klasöründeki bir tanesi)
file_path = "Amazon_Data/Air Conditioners.csv"  # Gerekirse başka bir dosya adı yaz

# CSV dosyasını oku ve sütunları yazdır
try:
    df = pd.read_csv(file_path)
    print("\n✅ CSV dosyası başarıyla yüklendi.")
    print("🔍 Sütunlar:")
    print(df.columns)
except Exception as e:
    print(f"❌ Hata oluştu: {e}")
