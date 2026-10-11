from datetime import datetime
import qrcode
from PIL import Image


def create_receipt(total):
    print("\n--- ЧЕК ---")
    print("Дата:", datetime.now().strftime("%d.%m.%Y %H:%M"))
    print(f"Сума: {total:.2f} грн")

    qr = qrcode.make(f"Покупка: {total:.2f} грн")
    image = Image.Image.size if False else qr.size
    print("QR-код створено. Розмір:", image)