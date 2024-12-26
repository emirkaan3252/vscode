
tel_rehberi = {}

def tel_no_ekle(x):
    print("Ekleme ekranına hoşgeldiniz")
    yeni_kisi = input("Eklemek istediğiniz kişinin adını yazınız: ")
    yeni_numara = input("Eklemek istediğiniz kişinin telefon numarasını yazınız: ")
    x[yeni_kisi] = yeni_numara
    print(f"{yeni_kisi} rehbere eklendi.")

def tel_rehber_göster(x):
    print("Rehbere hoşgeldiniz")
    if not x:
        print("Rehberde kişi bulunmuyor.")
    else:
        for i, j in x.items():
            print(i, ":", j)

def no_sil(x):
    print("Silme ekranına hoşgeldiniz")
    silinecek_kisi = input("Silmek istediğiniz kişinin adını yazınız: ")
    if silinecek_kisi in x:
        x.pop(silinecek_kisi)
        print(f"{silinecek_kisi} rehberden silindi.")
    else:
        print(f"{silinecek_kisi} rehberde bulunamadı.")

while True:
    print("****HOŞGELDİNİZ*****")
    print("****SEÇİM YAPINIZ***")
    seçim_yap = int(input("1-Ekle\n2-Sil\n3-Rehberi gör\n4-Çıkış\n"))

    if seçim_yap == 1:
        tel_no_ekle(tel_rehberi)
    elif seçim_yap == 2:
        no_sil(tel_rehberi)
    elif seçim_yap == 3:
        tel_rehber_göster(tel_rehberi)
    elif seçim_yap == 4:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Uygun tuşlara basınız.")
