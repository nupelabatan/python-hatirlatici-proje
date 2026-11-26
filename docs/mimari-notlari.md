# Sistem Mimarisi ve Tasarım Dokümanı

## 1. Proje Amacı
Kullanıcıların günlük metinlerinden tarih, saat ve görev bilgilerini arka planda otomatik yakalayarak etkileşimli onay ile SQLite veritabanına kaydeden ve zamanı geldiğinde proaktif hatırlatma sunan Nesne Yönelimli (OOP) Python uygulamasıdır.

## 2. Modüler Yapı
* **`main.py`:** `pynput` ile klavye girişlerini dinler ve arka planda zamanlayıcı döngüsünü çalıştırır.
* **`parser.py`:** Ham metin içerisindeki zaman zarflarını ve saat kalıplarını Regex (Düzenli İfadeler) ile ayıklar.
* **`database.py`:** SQLite veritabanı bağlantısını ve görevlerin CRUD işlemlerini yönetir.

## 3. Veritabanı Şeması ('gorevler'Tablosu)
* 'id': Otomatik artan birincil anahtar (INTEGER PRIMARY KEY)
* 'gorev_metni': Kullanıcının yazdığı orijinal plan cümlesi (TEXT)
* 'tarih_saat': Ayrıştırılmış hedef zaman (YYYY-AA-GG SS:DD)
* 'durum': Görev durumu (Bekliyor / Hatirlatildi)
