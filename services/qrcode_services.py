import qrcode
from qrcode.image.svg import SvgImage # Gerador em SVG
from io import BytesIO # Simulador de arquivo em memória
from qrcode.constants import ERROR_CORRECT_H # Correção de erro


def qrcode_generator(url: str, img_type: str = "PNG") -> BytesIO:
    
    if not url: 
        raise ValueError("URL inválida")
    
    img_type = img_type.upper()
    

    qr = qrcode.QRCode(
            version=None,                 
            error_correction=ERROR_CORRECT_H, # Melhor legibilidade no qrcode
            box_size=10,                   # Tamanho dos quadrados
            border=4                       # Margem
        )

    qr.add_data(url)
    qr.make(fit=True)
    
    buffer = BytesIO() # Criando a memória

    if img_type in ("PNG", "JPEG"): # Salvando em PNG ou JPEG
        img = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        img.save(buffer, format=img_type)    
        
    elif img_type == "SVG": # Salvando em svg
    
        img = qr.make_image(image_factory=SvgImage)
        img.save(buffer)
        
    else:
        raise ValueError("Tipo de imagem não suportado")

    buffer.seek(0) # Coloca a memória apontando para o começo
    
    return buffer
