from flask import Flask, request
from main import parse_request


app = Flask(__name__)
app.json.ensure_ascii = False


@app.get("/health")
def health():
    return {"status": "ok"}


@app.route("/parse", methods=["GET", "POST"])
def parse_report():
    if request.method == "POST":
        text = request.get_data(as_text=True)
    else:
        text = request.args.get("text", "")

    if not text.strip():
        return {"error": "Параметр text обязателен"}, 400

    return parse_request(text)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)