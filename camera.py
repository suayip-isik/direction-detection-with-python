import cv2
import numpy as np

# Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

# Renk filtresi için HSV değerleri
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

while True:
    # Kameradan görüntü al
    ret, frame = cap.read()
    
    # Görüntüyü HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Renk filtresi uygula
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Kenarları belirle
    edges = cv2.Canny(mask, 75, 150)
    
    # Konturları bul
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Tüm konturları dolaş
    for cnt in contours:
        # Kontur alanını hesapla
        area = cv2.contourArea(cnt)
        if area > 500:
            # Konturu çevreleyen dikdörtgeni bul
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Okun yönünü tespit et
            if w > h:
                if x > frame.shape[1] / 2:
                    print("Sağa doğru ok işareti")
                else:
                    print("Sola doğru ok işareti")
            else:
                if y > frame.shape[0] / 2:
                    print("Aşağı doğru ok işareti")
                else:
                    print("Yukarı doğru ok işareti")
    
    # Görüntüyü göster
    cv2.imshow("Frame", frame)
    
    # Çıkış yapmak için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
cap.release()

# Tüm pencereleri kapat
cv2.destroyAllWindows()
