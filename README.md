Tkinter GUI Oluşturma: Tkinter kullanarak bir pencere oluşturduk ve kullanıcıdan şifre uzunluğu, karakter kümesi ve gerçek şifre girmesini istedik.
Taramayı Başlatma: Kullanıcı "Kırmayı Başlat" butonuna tıkladığında start_brute_force fonksiyonu çalışır, kullanıcı girdilerini alır ve geçerliliklerini kontrol eder.
Brute Force: brute_force fonksiyonu, brute force yöntemiyle verilen karakter kümesi ve uzunluğa göre olası şifreleri dener. Doğru şifre bulunduğunda liste kutusuna eklenir ve süre hesaplanır.
İş Parçacıkları: Şifre kırma işlemi ayrı bir iş parçacığında çalıştırılır, böylece GUI donmaz ve kullanıcı deneyimi olumsuz etkilenmez.
