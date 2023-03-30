#kodlama.io ödev2
öğrenciler=[]
def giriş():
    Key="açık"
    while Key=="açık":
        print("1:Öğrenci kaydı\n2:Öğrenci kayıt silme\n3:Öğrenci listesi\n4:Öğrenci sorgulama\n5:Çıkış")
        Olay=int(input("yapmak istediğiniz işlemi seçin:"))
        match Olay:
            case 1:
                adet=int(input("Kaydı yapılacak öğrenci sayısını giriniz:"))
                for i in range(adet):
                    isim=input("öğrencinin ismi:")
                    soyisim=input("Öğrencinin soyismi:")
                    öğrenciler.append(isim+" "+soyisim)
            case 2:
                adet=int(input("Kaydı silinecek öğrenci sayısını giriniz:"))
                for i in range(adet):
                    isim=input("öğrencinin ismi:")
                    soyisim=input("Öğrencinin soyismi:")
                    öğrenciler.remove(isim+" "+soyisim)
            case 3:
                for i in öğrenciler:
                    print(i)
            case 4:
                print("1:numara sorgulama\n2:isim sorgulama")
                işlem=int(input("Lütfen işlem seçin:"))
                if işlem==1:
                    isim=input("Öğrencinin adı:")
                    soyisim=input("Öğrencinin soy ismi:")
                    öğrenci=isim+" "+soyisim
                    j=0
                    while j<len(öğrenciler):
                        if öğrenciler[j]==öğrenci:
                            print(isim+" "+soyisim+" numarası:",j)
                        j+=1
                else:
                    j=int(input("öğrencinin numarası:"))
                    print(j,"numaralı öğrencinin adı:"+öğrenciler[j])                    
            case 5:
                print("sistem kapatılıyor")
                Key="baybay"
giriş()
