===============================
PIN KONTROL UYGULAMASI
===============================

Bu uygulama, kullanıcıdan 4 haneli bir PIN kodu girmesini ister ve girilen kodu "1234" ile karşılaştırarak doğru olup olmadığını kontrol eder.

Uygulama, arka planda bir Turing makinesi mantığı kullanarak doğrulama işlemi yapar.

-------------------------------
NASIL KULLANILIR?
-------------------------------

1. Uygulamayı açın (atm_pin.exe).
2. Karşınıza 4 kutucuk çıkacaktır. PIN kodunuzu buraya yazın.
3. PIN kodu girildikçe kutular arasında geçiş otomatik olur.
4. 4. haneyi de girdikten sonra:
   - İsterseniz "Kontrol Et" butonuna basarak
   - Ya da klavyeden ENTER tuşuna basarak
     doğrulama yapabilirsiniz.

-------------------------------
ÖZELLİKLER
-------------------------------

- PIN girişleri sansürlenmiştir (****).
- Sağdaki 👁‍🗨 butonuna tıklayarak PIN'i geçici olarak görünür hale getirebilirsiniz.
- Hatalı girişte hata mesajı gösterilir ve giriş alanları temizlenir.
- Doğru girişte başarı mesajı verilir.
- Giriş süreci konsolda bir bant üzerinde görsel olarak takip edilebilir (debug amaçlıdır).

-------------------------------
GEREKSİNİMLER (sadece .py dosyasıyla çalışacaklar için)
-------------------------------

- Python 3.11+
- Tkinter kütüphanesi (Python ile birlikte gelir)

Uygulama çalıştırma:
python atm_pin.py

-------------------------------
NOTLAR
-------------------------------

- Varsayılan doğru PIN: 1234
- Bu proje eğitim amaçlıdır.

-------------------------------
GELİŞTİRİCİ
-------------------------------

Bu uygulama Nazım Gür tarafından geliştirilmiştir.
