import os
import numpy as np
from sklearn.metrics import accuracy_score, log_loss
from keras.preprocessing.image import load_img, img_to_array
from keras.utils import to_categorical
from tensorflow.keras.models import load_model


# Ana klasör yolu
ana_klasor = "/home/han/Downloads/test"


# Alt klasörlerin isimleri
alt_klasorler = ["/home/han/Downloads/test/bacterial_blight",
                 "/home/han/Downloads/test/brown_streak_disease",
                 "/home/han/Downloads/test/green_mottle",
                 "/home/han/Downloads/test/healthy",
                 "/home/han/Downloads/test/mosaic_disease"]


# Verileri ve etiketleri depolamak için boş listeler
X = []
y = []


# Alt klasörlerdeki verileri yükleme ve etiketleme
for i, alt_klasor in enumerate(alt_klasorler):
    alt_klasor_yolu = os.path.join(ana_klasor, alt_klasor)
    for dosya_adi in os.listdir(alt_klasor_yolu):
        dosya_yolu = os.path.join(alt_klasor_yolu, dosya_adi)
        img = load_img(dosya_yolu, target_size=(180, 180))
        img_array = img_to_array(img)
        X.append(img_array)
        y.append(i)  # Her alt klasör için farklı etiket


# Veriyi ve etiketleri Numpy dizilerine dönüştürme
X = np.array(X)
y = np.array(y)


# Verileri karıştırma
sirali_indeksler = np.arange(X.shape[0])
np.random.shuffle(sirali_indeksler)
X = X[sirali_indeksler]
y = y[sirali_indeksler]


# Modeli yükleyip verileri tahmin etme
model = load_model('/home/han/Documents/EE470_Model_BEST_5_.h5')  # Kaydedilmiş modeli yükleme
predictions = model.predict(X)  # Verileri tahmin etme


# Gerçek etiketlerin ve tahminlerin hazırlanması
true_labels = y
true_labels_cat = to_categorical(true_labels, num_classes=len(alt_klasorler))  # Gerçek etiketlerin kategorik hale getirilmesi
pred_prob_cat = predictions  # Tahmin olasılıklarının hesaplanması


# Doğruluk oranını ve kaybı hesaplama
accuracy = accuracy_score(true_labels, np.argmax(predictions, axis=1))
loss = log_loss(true_labels_cat, pred_prob_cat)


print(f"Doğruluk Oranı: {accuracy}")
print(f"Kayıp: {loss}")






