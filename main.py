import mediapipe as mp
import cv2
import os


videos = [
    
]


def procesaVideo(nombre_video):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    # Ruta donde se guardará el video procesado
    output_path = f"videoprocesado/{nombre_video}_procesado.mp4" #"videoprocesado/vid1_processed.mp4"

    # Parámetros para el video de salida
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 20.0  # Ajusta esto según el fps del video original
    output_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Ajusta esto según el ancho deseado del video de salida
    output_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Ajusta esto según la altura deseada del video de salida

    # Inicializar el objeto VideoWriter
    out = cv2.VideoWriter(output_path, fourcc, fps, (output_width, output_height))


    cap = cv2.VideoCapture(f"videos/{nombre_video}.mp4")


    ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) // 4
    alto = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 4
    # Redimensionar la ventana para ajustarse a las dimensiones del video
    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Frame", ancho, alto)

    with mp_pose.Pose(
        static_image_mode = False
        ) as pose:
        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            height, width, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)
            
            if results.pose_landmarks is not None:
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(128,0,250), thickness=2, circle_radius=3),
                    mp_drawing.DrawingSpec(color=(255,255,255), thickness=2, circle_radius=3),
                )
            
            # Escribir el fotograma procesado en el video de salida
            out.write(frame)

            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break


    cap.release()
    out.release()
    cv2.destroyAllWindows()

for vid in videos:
    procesaVideo(vid)