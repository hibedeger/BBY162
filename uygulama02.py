print("beni ne  kadar tanıyorsun")
sorular=['hangi yemeği en çok severim?','ne kitaplar okumayı en cok tercih ederim ?','ne yapmaktan zevk alırım?',\
        'en nefret ettiğim durum nedir?','dişarda neler yaparım?']
cevaplar=['yaprak sarma','romantik','gezmek','emrivâki','aklınıza gelebilecek herşey']
toplampuan= 0
for i in  range(len(sorular)):
    print ( " Soru "  +  str(i + 1 ) + " : " + sorular[i])
    cevap = input("cevabını yaz bakalım :)>>>> ")
    if cevaplar[i] == cevap.lower():
        print("Tebrikler doğru cevap")
        toplampuan += 1
    else:
        print("üzgünum hala tanıyamamışsın:(")
        print("tekrar dene")
        print("Puanınız: " + str(int((toplampuan / len(sorular)) * 100)))



