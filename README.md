
**Genel Proje Açıklaması**

Projemiz Doğal Dil İşleme algoritması olan LSTM algoritmasını kullanarak, makine öğrenmesi sayesinde rastgele Türkçe kelime ve cümle üretebilmektedir.
Projemizde LSTM algoritması modelinin iç yapısı detaylı şekilde açıklanıp kullanılmaktadır ve hazır model ile manuel hazırlanmış model çalıştırılıp doğruluk, kayıp ve karmaşıklık gibi değerleri karşılaştırılmaktadır. 
2 adet veri seti kullanılmıştır. İlk veri seti Oğuz Atay’ın Tutunamayanlar kitabından alınmış olup toplam 963 cümle bulunmaktadır. İkinci veri setinde 5749 cümle bulunmaktadır.

Projemizde tek problem için 2 farklı çözüm bulunmaktadır. İlk çözüm LSTM algoritmasının iç yapısının manuel olarak yazılıp herhangi bir makine öğrenmesi kütüphanesi import edilmeden hazırlanmıştır.
Diğer çözümde ise tensorflow, keras gibi derin öğrenme kütüphaneleri kullanılarak çözüme ulaşılmıştır.

**İlk çözümün açıklanması (LSTM_Manuel):**

Bu çözümde 3 farklı Python dosyası bulunmaktadır.
lstm.py dosyasında lstm algoritmasının iç yapısı bulunmaktadır, train.py dosyasında lstm.py dosyasındaki modüller import edilip manuel olarak oluşturduğumuz model eğitilip kaydedilmektedir,
predict.py doyasında ise eğitilmiş modelin pratiğe geçmektedir. Not: lstm.py dosyası tek başına çalışınca sonuç vermemektedir.

**İkinci Çözümün Açıklanması (LSTM):**

Bu çözümde, train.csv veri setinden çekilen cümlelerle model eğitilmektedir ve eğitilmiş modele kelimeler vererek cümle üretilmesi sağlanmaktadır.

**Kurulum ve Çalıştırma:**

1- import edilmesi gereken kütüphaneler

Eğer bilgisayarınızda pip yüklüyse terminale bu komutları yazarak kütüphaneleri yükleyebilirsiniz

* Numpy 

      pip install numpy
* Pandas 

      pip install pandas
      
* joblib

      pip install joblib
* Tensorflow

      pip install tensorflow

* Keras

      pip install Keras
* tkinter

      pip install tkinter
* matplotlib

      pip install matplotlib

2 - Çalıştırma

- "UI_designed_project" adlı klasöre girip sağ tıklayıp VS Code ile çalıştır seçeneğine tıklayın
- Ardından main.py dosyasını çalıştırıp uygulamayı kullanabilirsiniz

**Uygulama İçi Görüntüler:**

![enter image description here](https://github.com/wassapman/LSTM/blob/main/UI_designed_project/img/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-02%20172410.png?raw=true)
![enter image description here](https://github.com/wassapman/LSTM/blob/main/UI_designed_project/img/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-02%20173232.png?raw=true)
![enter image description here](https://github.com/wassapman/LSTM/blob/main/UI_designed_project/img/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-03%20124812.png?raw=true)
