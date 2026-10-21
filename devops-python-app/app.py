from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Application</h1>
    <p>Running Python inside Docker on AWS.</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}
