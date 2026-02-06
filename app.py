from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/qrcode", methods=["GET"])
def get_qrcode():
    url = request.args.get("url", type=str)
    type_img = request.args.get("img", type=str)
    return jsonify("teste sempre")



if __name__ == "__main__":
    app.run(debug=True)

