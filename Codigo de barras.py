from barcode import EAN13
from barcode.writer import ImageWriter

# Gera o código de barras, e fica salvo no lugar desejado #
with open(r'D:\Desktop\bar-code-generator\barcode.png', 'wb') as f:
    EAN13('495043089', writer=ImageWriter()).write(f)