import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    if not ret:
        print("Kamera açılamadı")
        break
    
    frame = cv2.flip(frame, 1)  # 1 değeri ile yatayda ters çevir
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
   
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'surat', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    
    cv2.imshow('Yüz Tespiti', frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
