import logging
from pathlib import Path

from flask import Flask, jsonify, render_template, request

from git_manager import commit_file
from logger_config import setup_logger

setup_logger()

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save_file():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    file_path = data.get("file_path")
    content = data.get("content", "")

    if not file_path:
        return jsonify({"error": "File path is required"}), 400

    try:
        path = Path(file_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            content,
            encoding="utf-8",
        )

        logger.info("File saved: %s", path)

        commit_file(path)

        logger.info("Git commit created: %s", path)

        return jsonify(
            {
                "message": (
                    "File saved and committed successfully."
                )
            }
        )

    except OSError as error:
        logger.exception("File operation failed")
        return jsonify({"error": str(error)}), 500

    except RuntimeError as error:
        logger.exception("Git operation failed")
        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    app.run(debug=True)