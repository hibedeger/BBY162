s1="“Sinekli Bakkal” Romanının Yazarı Aşağıdakilerden Hangisidir? "
s2="Aşağıda Verilen İlk Çağ Uygarlıklarından Hangisi Yazıyı İcat Etmiştir? "
s3="Tsunami Felaketinde En Fazla Zarar Gören Güney Asya Ülkesi Aşağıdakilerden Hangisidir? "
s4="2003 Yılında Euro Vizyon Şarkı Yarışmasında Ülkemizi Temsil Eden Ve Yarışmada Birinci Gelen Sanatçımız Kimdir? "
s5="Mustafa Kemal Atatürk’ün Nüfusa Kayıtlı Olduğu İl Hangisidir? "
c1=[["a:  Reşat Nuri Güntekin"],["b: Halide Edip Adıvar"],["c: Ziya Gökalp"],["d: Ömer Seyfettin"]]
c2=[["a: Hititler"],["b: Elamlar"],["c: Sümerler"],["d: Urartular"]]
c3=[["a: Endonezya"],["b: Tayland"],["c: Komoa"],["d: Srilanka"]]
c4=[["a: Athena"],["b: Sertab Erener"],["c: Kenan Doğulu"],["d: Manga"]]
c5=[["a: İstanbul"],["b: Ankara"],["c: Samsun"],["d: Gaziantep"]]
puan=0
print("Bilgi yarışması programına hoş geldiniz.")
isim=input("İsmin nedir? : >>>")
print("")
print("Kurallar çok basit ",isim)
print("")
print("Çoktan seçmeli soruların cevaplarından doğru olduğunu düşündüğün şıkkı gir.")

print("PUANLAMA")
print("")
print("Her doğru cevap sana 30 puan kazandırır iken her yanlış cevap 10 puan kaybettirir. ")
print("")
print("Hazırsan başlayalım",isim)
print("")
print("SORU 1")
print(s1)
soru1=input(c1).lower()
if soru1=="b":
    puan+=30
    print("Doğru Cevap, Puanın", puan)
else:
    puan=puan-10
    print("Yanlış Cevap, Puanın",puan)
print("")
print("SORU 2")

print(s2)
soru2=input(c2).lower()
if soru2=="c":
    puan += 30
    print("Doğru Cevap, Puanın", puan)
else:
    puan -= 10
    print("Yanlış Cevap, Puanın", puan)
print("")
print("SORU 3")
print(s3)
soru3=input(c3).lower()
if soru3=="a":
    puan += 30
    print("Doğru Cevap, Puanın", puan)
else:
    puan -= 10
    print("Yanlış Cevap, Puanın", puan)
print("")
print("SORU 4")
print(s4)
soru4=input(c4).lower()
if soru4=="b":
    puan += 30
    print("Doğru Cevap, Puanın", puan)
else:
    puan += 10
    print("Yanlış Cevap, Puanın", puan)
print("")
print("SORU 5")
print(s5)
soru5=input(c5).lower()
if soru5=="d":
    puan +=  30
    print("Doğru Cevap, Puanın", puan)
else:
    puan -=10
print("")
print("OYUN BİTTİ. PUANIN:",puan)

