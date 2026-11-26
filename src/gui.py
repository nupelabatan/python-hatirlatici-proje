import tkinter as tk
from tkinter import messagebox

class ArayuzYoneticisi:
    @staticmethod
    def onay_penceresi_goster(gorev_metni, tarih_saat):
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)

        mesaj = f"Yeni bir plan tespit edildi!\n\nGörev: {gorev_metni}\nZaman: {tarih_saat}\n\nHatırlatıcıya kaydedilsin mi?"
        cevap = messagebox.askyesno("Akıllı Hatırlatıcı - Onay", mesaj, parent=root)

        root.destroy()
        return cevap

    @staticmethod
    def hatirlatma_bildirimi_goster(gorev_metni, tarih_saat):
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)

        mesaj = f"⏰ ZAMANI GELDİ!\n\nPlanlanan Görev: {gorev_metni}\nSaat: {tarih_saat}"
        messagebox.showinfo("Akıllı Hatırlatıcı Bildirimi", mesaj, parent=root)

        root.destroy()
