import sqlite3
from datetime import datetime

class VeritabaniYoneticisi:
    def __init__(self, db_adi="hatirlatici.db"):
        self.db_adi = db_adi
        self.tablo_olustur()

    def baglan(self):
        return sqlite3.connect(self.db_adi)

    def tablo_olustur(self):
        with self.baglan() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS gorevler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    gorev_metni TEXT NOT NULL,
                    tarih_saat TEXT NOT NULL,
                    durum TEXT DEFAULT 'Bekliyor',
                    olusturulma_zamani TEXT
                )
            """)
            conn.commit()

    def gorev_ekle(self, gorev_metni, tarih_saat):
        with self.baglan() as conn:
            cursor = conn.cursor()
            simdi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO gorevler (gorev_metni, tarih_saat, olusturulma_zamani)
                VALUES (?, ?, ?)
            """, (gorev_metni, tarih_saat, simdi))
            conn.commit()

    def bekleyen_gorevleri_getir(self):
        with self.baglan() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, gorev_metni, tarih_saat FROM gorevler WHERE durum = 'Bekliyor'")
            return cursor.fetchall()

    def gorev_tamamla(self, gorev_id):
        with self.baglan() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE gorevler SET durum = 'Hatirlatildi' WHERE id = ?", (gorev_id,))
            conn.commit()
