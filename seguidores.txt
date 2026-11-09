from datetime import datetime

# Simulación de datos para práctica segura
fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
seguidores_instagram = 1250
seguidores_facebook = 3400

reporte = f"[{fecha_actual}] - Instagram: {seguidores_instagram} seguidores | Facebook: {seguidores_facebook} seguidores\n"

# Guardar en un archivo de historial dentro del repositorio
with open("historial_metricas.txt", "a") as archivo:
    archivo.write(reporte)

print("¡Reporte generado con éxito y guardado en historial_metricas.txt!")