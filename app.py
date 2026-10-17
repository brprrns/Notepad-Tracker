from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save_file():
    data = request.get_json()

    file_path = data.get("file_path")
    content = data.get("content", "")

    if not file_path:
        return jsonify({"error": "File path is required"}), 400

    try:
        path = Path(file_path)

        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(content, encoding="utf-8")

        return jsonify({
            "message": "File saved successfully"
        })

    except OSError as error:
        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    app.run(debug=True)