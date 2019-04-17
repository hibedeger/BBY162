import random
sorular=["tsoru","bsoru","rsoru","bilsoru","telsoru"]
kelimelistesi=["televizyon","buzdolabı","radyo","bilgisayar","telefon"]
kelime=random.choice(kelimelistesi)
olanharf=[]
olmayanharf=[]
hak=10
i =0
while hak>0:
    i=i+1
    print(sorular[i])
    a=input("harf girin:").lower()
    if a==kelime:
        print("doğru cevap")
        break
    elif a in kelime[0:22]:
        print("harf var")
        olanharf.append(a)
        print("Olan Harfler: ", olanharf)
        print("Olmayan Harfler:", olmayanharf)
        continue
    elif a not in kelime [0:6]:
        print("harf yok:")
        olmayanharf.append(a)
        hak-=1
        print("Kalan Hakkınız: ", hak)
        print("Olan Harfler: ", olanharf)
        print("Olmayan Harfler:", olmayanharf)
        continue
    elif a in olanharf and a in olmayanharf:
        print("daha önce girildi:")
        continue
    else:
        print("hatalı girdi!!!")
        continue
