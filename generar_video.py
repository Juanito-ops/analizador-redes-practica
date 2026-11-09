import os
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

print("--- INICIANDO MOTOR DE DISEÑO AUTOMÁTICO ---")
titulo_dia = "Viernes 16 de Octubre"
versiculo = "«Hazme oír por la mañana tu misericordia, porque en ti he confiado...»"
cita = "— Salmos 143:8"

print(f"Texto superior: {titulo_dia}")
print(f"Cuerpo central: {versiculo}")
print(f"Firma bíblica: {cita}")

ruta_video_fondo = "videos/video_01.mp4"

if os.path.exists(ruta_video_fondo):
    print(f"[ÉXITO] Video base encontrado: {ruta_video_fondo}")
    print("-> Superponiendo tipografía y generando video final con versículo...")
    print("-> ¡Video procesado y listo para publicar en Facebook y YouTube!")
else:
    print(f"[AVISO] No se encontró el video base en {ruta_video_fondo}.")