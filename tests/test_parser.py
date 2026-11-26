from parser import MetinAyristirici

def test_saat_ve_gun_ayristirma():
    ayristirici = MetinAyristirici()
    sonuc = ayristirici.analiz_et("Salı 14:00'te ders çalışacağım")
    assert sonuc is not None
    assert "14:00" in sonuc["zaman"]

def test_gecersiz_metin():
    ayristirici = MetinAyristirici()
    sonuc = ayristirici.analiz_et("Sadece normal bir cümle yazıyorum")
    assert sonuc is None
