import qrcode
from qrcode.image.svg import SvgImage # Gerador em SVG
from io import BytesIO # Simulador de arquivo em memória

def qrcode_generator(url: str, img_type: str = "png") -> BytesIO:
    
    if not url: 
        raise ValueError("URL inválida")

    qr = qrcode.make(url) # Criação do qrcode
    buffer = BytesIO() # Criando a memória

    img_type = img_type.lower()

    if img_type == "png": # Salvando em PNG
        qr.save(buffer, format="PNG")
    
    elif img_type == "jpeg": # Salvando em JPEG
        qr.save(buffer, format="JPEG")
    
    elif img_type == "svg": # Salvando em svg
        factory = SvgImage
        img = qrcode.make(url, image_factory=factory)
        img.save(buffer)
        
    else:
        raise ValueError("Tipo de imagem não suportado")

    buffer.seek(0) # Coloca a memória apontando para o começo
    
    return buffer
