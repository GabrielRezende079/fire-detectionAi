import cv2
from ultralytics import YOLO

# Carregar o modelo treinado
model = YOLO("runs/detect/train3/weights/best.pt")

# Capturar vídeo da webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Fazer a detecção na imagem capturada
    results = model(frame)

    # Desenhar os resultados na tela
    for r in results:
        boxes = r.boxes.xyxy  # Coordenadas dos bounding boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Exibir o vídeo com a detecção
    cv2.imshow("Fire Detection", frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
