import speech_recognition as sr
import os
print(os.listdir())  # Verifica si 'ingles1.wav' aparece en la lista

recognizer = sr.Recognizer()


audio_file = r"C:\tu\ruta\ingles1.wav"
 

with sr.AudioFile(audio_file) as source:
    print("Escuchando el archivo de audio...")
    audio_data = recognizer.record(source) 
    try:
        print("Transcribiendo...")
        
        text = recognizer.recognize_google(audio_data, language="es-ES")  
        print("Transcripción completa: ")
        print(text)  
        with open("transcripcion.txt", "w", encoding="utf-8") as file:
            file.write(text)
        print("La transcripción se guardó en 'transcripcion.txt'.")
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"Error en el servicio de Google Speech Recognition; {e}")

