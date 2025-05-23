from flask import Flask, request, jsonify
import subprocess
import uuid
import os

app = Flask(__name__)
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route("/download", methods=["GET"])
def download():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "Missing query"}), 400

    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    command = ["spotdl", "--output", filepath, query]

    try:
        subprocess.run(command, check=True)
        return jsonify({"url": f"https://your-railway-domain/{filepath}"})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
