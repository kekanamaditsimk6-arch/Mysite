from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html>
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>My Site</title>
      </head>
      <body style="font-family:sans-serif;max-width:600px;margin:40px auto;padding:0 16px">
        <h1>Hello from Python</h1>
        <p>This site is running on Flask.</p>
      </body>
    </html>
    """

@app.route("/api/hello")
def hello():
    return jsonify(message="Hello from the API")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
