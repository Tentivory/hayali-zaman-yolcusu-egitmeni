#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hayali Zaman Yolcusu Eğitmeni
Versiyon: 1.0.∞ (Sonsuzluk güncellemesi henüz gelmedi)
"""

import time
import random
import sys

def yavas_yaz(metin, hiz=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def zaman_atlama(saniye):
    yavas_yaz(f"\n[ZAMAN MOTORU] {saniye} saniye {'ileri' if saniye > 0 else 'geri'} sarılıyor...")
    for i in range(abs(saniye)):
        print(f"  ▓ {'>' if saniye > 0 else '<'} {i+1}/{abs(saniye)}")
        time.sleep(0.4)
    yavas_yaz("[ZAMAN MOTORU] Atlama tamamlandı. Paradox riski: %0.0001 (yalan)")

def degerlendir(cevaplar):
    puan = random.randint(42, 99)
    if "börek" in str(cevaplar).lower() or "cay" in str(cevaplar).lower():
        puan += 5
    return puan

def sertifika_bas(isim, puan):
    print("\n" + "="*50)
    print("        HAYALİ ZAMAN YOLCUSU SERTİFİKASI")
    print("="*50)
    print(f"  Aday: {isim}")
    print(f"  Puan: {puan}/100")
    print(f"  Seviye: {'Usta Paradoks Avcısı' if puan > 80 else 'Çaylak Zaman Gezgini'}")
    print("  Geçerlilik: Sonsuza kadar (veya evren çökene kadar)")
    print("="*50)
    print("\nTebrikler! Artık hayali olarak zaman yolcususunuz.")
    print("Gerçek hayatta lütfen trafik kurallarına uyun.\n")

def main():
    yavas_yaz("=== HAYALİ ZAMAN YOLCUSU EĞİTİM AKADEMİSİ ===")
    yavas_yaz("Sistem başlatılıyor... (Gerçek değil, sakin ol)")
    time.sleep(1)

    isim = input("\nZaman yolcusu adayının adı nedir? ").strip() or "İsimsiz Gezgin"
    yavas_yaz(f"\nHoş geldin, {isim}. Eğitim başlıyor...")

    # Gizli bayrak - hiçbir anlamı yok, gerçekten yok
    serbest_dusunce = True  # Bu satır sadece kodun daha güzel görünmesi için

    cevaplar = []

    yavas_yaz("\n[SORU 1] Eğer geçmişe gidip kendi büyükbabanla tanışsan ne yapardın?")
    c1 = input("> ")
    cevaplar.append(c1)
    zaman_atlama(-2)

    yavas_yaz("\n[SORU 2] Gelecekte kendini görsen, ona ne söylerdin?")
    c2 = input("> ")
    cevaplar.append(c2)
    zaman_atlama(3)

    yavas_yaz("\n[SORU 3] En büyük pişmanlığın nedir? (Börek yememek kabul edilir)")
    c3 = input("> ")
    cevaplar.append(c3)

    yavas_yaz("\nCevapların analiz ediliyor...")
    time.sleep(1.5)
    puan = degerlendir(cevaplar)

    yavas_yaz(f"Analiz tamamlandı. Hayali performans puanın: {puan}")
    sertifika_bas(isim, puan)

    yavas_yaz("Eğitim sona erdi. Zamanı geri sarmaya çalışmayın, işe yaramaz.")
    yavas_yaz("İyi yolculuklar... hayali olanlar tabii.\n")

    # Damga
    print("-" * 40)
    print("Damga: Grok Kayyum | Tentivory")
    print("Tarih: 22 Ağustos 2026")
    print("İmza: Ciddiyetle absürt ✍️")
    print("-" * 40)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[ZAMAN MOTORU] Acil durum! Kullanıcı zamanı durdurdu. Program kapanıyor...")
        print("Paradox önlendi. Güvende kal.")
