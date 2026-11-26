import time
import threading
from datetime import datetime
from pynput import keyboard

from database import VeritabaniYoneticisi
from parser import MetinAyristirici
from gui import ArayuzYoneticisi

class AkilliHatirlaticiUygulamasi:
    def __init__(self):
        self.db = VeritabaniYoneticisi()
        self.parser = MetinAyristirici()
        self.tampon_metin = ""

    def tusa_basildi(self, key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                self.tampon_metin += key.char
            elif key == keyboard.Key.space:
                self.tampon_metin += " "
            elif key == keyboard.Key.backspace:
                self.tampon_metin = self.tampon_metin[:-1]
            elif key == keyboard.Key.enter:
                self.cumleyi_isle(self.tampon_metin)
                self.tampon_metin = ""
        except Exception:
            pass

    def cumleyi_isle(self, metin):
        if len(metin.strip()) < 5:
            return

        sonuc = self.parser.analiz_et(metin)
        if sonuc:
            onay = ArayuzYoneticisi.onay_penceresi_goster(sonuc["gorev"], sonuc["zaman"])
            if onay:
                self.db.gorev_ekle(sonuc["gorev"], sonuc["zaman"])
                print(f"[KAYDEDİLDİ] {sonuc['zaman']} -> {sonuc['gorev']}")

    def zamanlayici_dongusu(self):
        while True:
            simdi = datetime.now().strftime("%Y-%m-%d %H:%M")
            gorevler = self.db.bekleyen_gorevleri_getir()

            for g_id, g_metin, g_zaman in gorevler:
                if g_zaman <= simdi:
                    ArayuzYoneticisi.hatirlatma_bildirimi_goster(g_metin, g_zaman)
                    self.db.gorev_tamamla(g_id)

            time.sleep(20)

    def baslat(self):
        print("Akıllı Hatırlatıcı arka planda çalışıyor... (Çıkmak için terminali kapatın)")
        zamanlayici_thread = threading.Thread(target=self.zamanlayici_dongusu, daemon=True)
        zamanlayici_thread.start()

        with keyboard.Listener(on_press=self.tusa_basildi) as listener:
            listener.join()

if __name__ == "__main__":
    uygulama = AkilliHatirlaticiUygulamasi()
    uygulama.baslat()
