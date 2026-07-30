from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Azure ETL Demo</h2>
    <p>Application is running successfully.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)