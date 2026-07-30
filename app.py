from flask import Flask, render_template, request
from storage.blob_storage import BlobStorage
from etl.extract import read_csv_from_blob
from etl.transform import transform_sales
from etl.load import load_sales
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

    df = read_csv_from_blob(filename)

    df = transform_sales(df)

    load_sales(df)

    return f"""
    <h2>ETL Completed Successfully</h2>

    File : {filename}<br>

    Records Loaded : {len(df)}

    <br><br>

    <a href='/'>Home</a>

    <br>

    <a href='/dashboard'>Dashboard</a>
    """

@app.route("/dashboard")
def dashboard():

    return "<h2>Dashboard Coming Soon</h2>"


if __name__ == "__main__":
    app.run(debug=True)

