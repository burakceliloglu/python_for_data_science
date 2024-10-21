# 1
x = 8
у = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = 11, 2, 3, 41
d = {"Name": "Jake",
"Age": 27,
"Adress": "Downtown" }
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

# Solution(1)
type(s)

# 2
text = "The goal is to turn data into information, and information into insight."

# Solution(2)
text.upper().replace(",", "").replace(".", "").split()

# 3
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

"""Adim 1: Verilen listenin eleman sayisina bakiniz.
Adim 2: Sifirinci ve onuncu indeksteki elemanlar agiriniz.
Adim 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi olusturunuz.
Adim 4: Sekizinci indeksteki elemani siliniz.
Adim 5: Yeni bir eleman ekleyiniz.
Adim 6: Sekizinci indekse "N" elemanini tekrar ekleyiniz."""

# Solution(3)
len(lst)
lst[0]
lst[10]
lst[0:4]
lst.pop(8)
lst
lst.append("Æ")
lst.insert(8, "N")

#4
"""Verilen sözlük yapisina asagidaki adimlar uygulayiniz."""
dict = {'Christian': ["America", 18],
'Daisy': ["England", 12],
'Antonioé' : ["Spain",22],
'Dante': ["Italy", 25]}
"""Adim 1: Key degerlerine erisiniz.
Adim 2: Value'lara erisiniz.
Adim 3: Daisy key'ine ait 12 degerini 13 olarak güncelleyiniz.
Adim 4: Key degeri Ahmet value degeri [Turkey,24] olan yeni bir deger ekleyiniz.
Adim 5: Antonio' yu dictionary'den siliniz."""

# Solution(4)
dict.keys()
dict.values()
dict.update({'Daisy':["England", 13]})
dict
dict.update({'Ahmet':["Turkey", 24]})
dict.pop("Antonioé")

# 5
"""Argüman olarak bir liste alan, listenin içerisindeki tek ve gift 
sayilar ayri listelere atayan ve bu listeleri return eden fonksiyon yaziniz."""
l=12,13,18,93,221


# Solution(5)
def func(l):
    E = []
    O = []
    for i in l:
        if i % 2 == 0:
            E.append(i)
        else:
            O.append(i)
    return E, O

even_list, odd_list = func(l)
even_list
odd_list

# 6
"""Aşağida verilen listede mühendislik ve tip fakülterinde dereceye giren ögrencilerin 
isimleri bulunmaktadir. Sirasiyla ilk üg ögrenci mühendislik fakültesinin bagar sirasin 
temsil ederken son üg ögrenci de tip fakültesi ögrenci sirasina aittir. Enumarate
kullanarak ögrenci derecelerini fakülte özelinde yazdiriniz. """
ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece" ]
"""
Beklenen gikti:
Mühendislik Fakültesi 1 . ögrenci: Ali
Mühendislik Fakültesi 2 . ögrenci: Veli
Mühendislik Fakültesi 3 . ögrenci: Ayse
Tup Fakültesi 1 . ögrenci: Talat
Tup Fakültesi 2 . ögrenci: Zeynep
Tip Fakültesi 3 . ögrenci: Ece """

# Solution(6)
for index, value in enumerate(ogrenciler, 1):
    if index < 4:
        print("Mühendislik Fakültesi ",index, ". " ,value)
    else:
        index -= 3
        print("Tıp Fakültesi ", index, ". ", value)

# 7
"""Agagida 3 adet liste verilmistir. Listelerde sirasi ile bir dersin kodu, kredisi 
ve kontenjan bilgileri yer almaktadir. Zip kullanarak ders bilgilerini bastiriniz."""
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204" ]
kredi = [3,4,2,41]
kontenjan = [30,75, 150, 25]
"""
Beklenen ikti:
Kredisi 3 olan CMP1005 kodlu dersin kontenjant 30 kisidir.
Kredisi 4 olan PSY1001 kodlu dersin kontenjant 75 kisidir.
Kredisi 2 olan HUK1005 kodlu dersin kontenjant 150 kigidir.
Kredisi 4 olan SEN2204 kodlu dersin kontenjant 25 kisidir."""

# Solution(7)
list(zip(ders_kodu, kredi, kontenjan))
for lesson in list(zip(ders_kodu, kredi, kontenjan)):
    print("Kredisi ", lesson[1], " olan ", lesson[1], " kodlu dersin kontenjant ", lesson[2], " kişidir.")
    print(f"Kredisi {lesson[1]} olan {lesson[1]} kodlu dersin kontenjant {lesson[2]} kişidir.")

# 8 
"""Asagida 2 adet set verilmistir. Sizden istenilen eger 1. küme 2. kümeyi kapsiyor 
ise ortak elemanlarini eger kapsamiyor ise 2. kümenin 1. kümeden farkini 
yazdiracak fonksiyonu tanimlamaniz beklenmektedir."""
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])
"""Beklenen ikti:
{'function', 'acut', 'miuul', 'lambda'}
Kapsayip kapsamadigini kontrol etmek için issuperset() metodunu,
farkli ve ortak elemanlar için ise intersection ve difference metodlarini kullaniniz."""

if kume1.issuperset(kume2):
    print(kume2)
else:
    print(kume2 - kume1)