import os


import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, HorizontalBarsDrawer, VerticalBarsDrawer, CircleModuleDrawer, GappedSquareModuleDrawer


def qr_unstyled():
    text = _text_input()
    name_file = _name_image()
    if not os.path.exists('./output/'):
        os.makedirs('./output/')
    name_file = os.path.join('./output/', name_file + ".png")
    # Generate QR object
    qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=9,
                    border=3)
    qr.add_data(text)
    qr.make(fit=True)
    # Edit style QR
    img = qr.make_image(back_color=(255, 255, 255), fill_color=(0, 0, 0))  # Color RGB
    # Save image QR
    img.save(name_file)
    print(f'[OK] QR code created successfully: {name_file}')


def qr_styled(style):
    text = _text_input()
    name_file = _name_image()
    if not os.path.exists('./output/'):
        os.makedirs('./output/')
    name_file = os.path.join('./output/', name_file + ".png")
    # Generate QR object
    qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=9,
                    border=3)
    qr.add_data(text)
    qr.make(fit=True)
    # Edit style QR
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=style)
    # Save image QR
    img.save(name_file)
    print(f'[OK] QR code created successfully: {name_file}')


def _text_input():
    while True:    
        try:
            text = input("Write your text. \n>>> ")
            if(not(text and text.strip())):
                raise ValueError("Error -- Cannot enter an empty string")
            return text
        except ValueError as error:
            print("Error -- Cannot enter an empty string")
            continue


def _name_image():
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:   
        try:
            text = input("Enter image name. \n>>> ")
            if(not(text and text.strip())):
                raise ValueError("\n[Error] Cannot enter an empty string")
            return text
        except ValueError:
            attempts += 1
            print("\n[Error] Cannot enter an empty string")
            continue
    print("Exceeded maximum attempts.")
    text = 'qr_code'
    print("Default name was set >>> " + text)
    return text
