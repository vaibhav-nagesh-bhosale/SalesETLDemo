from flask import Flask, render_template, request
from storage.blob_storage import BlobStorage
import os

app = Flask(__name__)
blob = BlobStorage()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/uploadlocal", methods=["POST"])
def uploadlocal():

    file = request.files["file"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(filepath)

    return f"{file.filename} uploaded successfully!"


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    filename = blob.upload_file(file)

    return f"{filename} uploaded successfully to Azure Blob Storage!"


@app.route("/dashboard")
def dashboard():

    return "<h2>Dashboard Coming Soon</h2>"


if __name__ == "__main__":
    app.run(debug=True)

