# መስመር 14 ላይ ያለውን በዚህ ተካው፡

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Daniel's Website</h1><p>Welcome to my first website!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
  
