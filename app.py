from flask import Flask, request, jsonify, send_file
from services import qrcode_services as qr_def
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# Rota principal
@app.route("/api/qrcode", methods=["GET"])
@limiter.limit("30 per minute")
def get_qrcode():
    
    # Leitura de parâmetros
    url = request.args.get("url") # URL do site
    img_type = request.args.get("img", "png") # Tipo de imagem, png como padrão

    # Caso sem url passada
    if not url:
        return jsonify({"erro": "Parâmetro 'url' é obrigatório"}), 400

    try: # Gerador de qrcode
        qr_img = qr_def.qrcode_generator(url, img_type)
        
        # Resposta
        return send_file(
            qr_img,
            mimetype=f"image/{img_type}",
            download_name=f"qrcode.{img_type}"
        )

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    


if __name__ == "__main__":
    app.run()

