print("""
***********************************
Faktöriyel Bulma

Programdan çıkmak için q tuşuna basıp Enter'a basınız
***********************************
""")

while True:
    number = input("Lütfen Faktöriyel Hesaplamasını istediniz Sayıyı Giriniz: ")

    if (number == 'q' or number == 'Q'):
        print("Programdan çıkılıyor...")
        break
    else:
        fak = 1
        number = int(number)
        for i in range(1, number + 1):
            fak = i * fak
        print(fak)

#4! = 4*3*2*1

