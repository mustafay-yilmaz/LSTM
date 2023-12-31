Genel Proje Açıklaması
Projemiz Doğal Dil İşleme algoritması olan LSTM algoritmasını kullanarak, makine öğrenmesi sayesinde rastgele Türkçe kelime ve cümle üretebilmektedir.
Projemizde LSTM algoritması modelinin iç yapısı detaylı şekilde açıklanıp kullanılmaktadır ve hazır model ile manuel hazırlanmış model çalıştırılıp doğruluk, kayıp ve karmaşıklık gibi değerleri karşılaştırılmaktadır. 
2 adet veri seti kullanılmıştır. İlk veri seti Oğuz Atay’ın Tutunamayanlar kitabından alınmış olup toplam 963 cümle bulunmaktadır. İkinci veri setinde 5749 cümle bulunmaktadır.

Projemizde tek problem için 2 farklı çözüm bulunmaktadır. İlk çözüm LSTM algoritmasının iç yapısının manuel olarak yazılıp herhangi bir makine öğrenmesi kütüphanesi import edilmeden hazırlanmıştır.
Diğer çözümde ise tensorflow, keras gibi derin öğrenme kütüphaneleri kullanılarak çözüme ulaşılmıştır.

İlk çözümün açıklanması (LSTM_Manuel):
Bu çözümde 3 farklı Python dosyası bulunmaktadır.
lstm.py dosyasında lstm algoritmasının iç yapısı bulunmaktadır, train.py dosyasında lstm.py dosyasındaki modüller import edilip manuel olarak oluşturduğumuz model eğitilip kaydedilmektedir,
predict.py doyasında ise eğitilmiş modelin pratiğe geçmektedir. Not: lstm.py dosyası tek başına çalışınca sonuç vermemektedir.

İkinci Çözümün Açıklanması (LSTM):
Bu çözümde, train.csv veri setinden çekilen cümlelerle model eğitilmektedir ve eğitilmiş modele kelimeler vererek cümle üretilmesi sağlanmaktadır.
