from flask import Flask, render_template, request
from storage.blob_storage import BlobStorage
from etl.extract import read_csv_from_blob
from etl.transform import transform_sales
from etl.load import load_sales
import os
import time
from etl.job_logger import log_job
from etl.upload_logger import log_uploaded_file
from services.dashboard_service import DashboardService
from flask import redirect
from flask import url_for



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

    start = time.time()

    try:
        file = request.files["file"]

        if file.filename == "":
            return "No file selected"

        filename = blob.upload_file(file)

        log_uploaded_file(

            filename,

            f"salesfiles/{filename}",

            file.content_length,

            "Admin",

            "Uploaded"

        )

        df = read_csv_from_blob(filename)
        df = transform_sales(df)
        load_sales(df)

        duration = round(time.time() - start, 2)

        log_job(
            filename,
            len(df),
            "SUCCESS",
            duration,
        )
        return redirect(url_for("dashboard"))
        return f"""
        <h2>ETL Completed Successfully</h2>

        File : {filename}<br>

        Records Loaded : {len(df)}

        <br><br>

        <a href='/'>Home</a>

        <br>

        <a href='/dashboard'>Dashboard</a>
        """
    except Exception as ex:
        duration = round(time.time() - start, 2)
        log_job(
            locals().get("filename", ""),
            0,
            "FAILED",
            duration,
            str(ex),
        )
        return str(ex)

@app.route("/dashboard")
def dashboard():

    summary = DashboardService.get_summary()

    jobs = DashboardService.get_recent_jobs()

    sales = DashboardService.get_sales()

    return render_template(

        "dashboard.html",

        summary=summary,

        jobs=jobs,

        sales=sales

    )


if __name__ == "__main__":
    app.run(debug=True)

