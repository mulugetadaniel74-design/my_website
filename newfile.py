from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Daniel's Website</h1><img src='https://github.com/mulugetadaniel74-design/my_website/blob/main/Screenshot_20260212_001355.png?raw=true' width='300'>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
