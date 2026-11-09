import json
import os
from datetime import datetime

# 1. Cargar el calendario de textos desde la carpeta config
ruta_calendario = "config/calendario.json"

if not os.path.exists(ruta_calendario):
    print("Error: No se encontró el archivo calendario.json")
    exit()

with open(ruta_calendario, "r", encoding="utf-8") as f:
    calendario = json.load(f)

# 2. Simular el día actual (por ejemplo, hoy elegiremos el Día 1)
# Más adelante esto cambiará para que avance solo cada 24 horas
dia_actual = "1"

if dia_actual in calendario:
    contenido = calendario[dia_actual]
    video_esperado = contenido["archivo_video"]
    
    # 3. Verificar si el video físico existe en la carpeta videos/
    ruta_video = os.path.join("videos", video_esperado)
    
    print(f"--- SIMULANDO PUBLICACIÓN DEL DÍA {dia_actual} ---")
    print(f"Título: {contenido['titulo']}")
    print(f"Descripción: {contenido['descripcion']}")
    
    if os.path.exists(ruta_video):
        print(f"[ÉXITO] Video encontrado en la carpeta: {ruta_video}")
        print("-> Simulando subida a Facebook y YouTube... ¡Publicado con éxito!")
    else:
        print(f"[AVISO] El texto está listo, pero falta colocar el archivo '{video_esperado}' dentro de la carpeta 'videos/'.")
else:
    print(f"No hay contenido programado para el día {dia_actual}.")