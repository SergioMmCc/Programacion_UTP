from PIL import Image
import numpy as np
import os

# Ruta de la imagen original
imagen_path = os.path.expanduser("~/Documents/vga_controller/barca.jpg")

# Ruta de salida del archivo .mif
mif_path = os.path.expanduser("~/Documents/vga_controller/imagen.mif")

# Cargar la imagen y redimensionarla a 640x480
img = Image.open(imagen_path).convert("RGB").resize((640, 480))

# Convertir a numpy array y extraer los valores de color
img_array = np.array(img, dtype=np.uint8)

# Convertir cada píxel en un formato de 8 bits (RGB332: RRR GGG BB)
def rgb_to_8bit(r, g, b):
    r_3bit = (r >> 5) & 0b111  # 3 bits para rojo
    g_3bit = (g >> 5) & 0b111  # 3 bits para verde
    b_2bit = (b >> 6) & 0b11   # 2 bits para azul
    return (r_3bit << 5) | (g_3bit << 2) | b_2bit

# Convertir la imagen completa a 8 bits por píxel
img_8bit = np.array([[rgb_to_8bit(r, g, b) for r, g, b in row] for row in img_array], dtype=np.uint8)

# Generar archivo .mif con valores en hexadecimal
with open(mif_path, 'w') as f:
    f.write("DEPTH = 307200;\nWIDTH = 8;\nADDRESS_RADIX = HEX;\nDATA_RADIX = HEX;\nCONTENT BEGIN\n")
    for i, value in enumerate(img_8bit.flatten()):
        f.write(f"{i:X} : {value:02X};\n")  # Convertir a hexadecimal y escribir en formato MIF
    f.write("END;\n")

print(f"Archivo {mif_path} generado correctamente en formato MIF con valores hexadecimales.")