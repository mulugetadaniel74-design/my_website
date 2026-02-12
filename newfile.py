from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <body style='background-color: #1a1a1a; color: white; text-align: center; font-family: sans-serif; padding-top: 50px;'>
        <h1 style='color: #00ffcc;'>Welcome to Daniel Mulugeta's Website</h1>
        <p style='font-size: 20px;'>I am a Passionate Web Developer.</p>
        <hr style='width: 50%; border: 1px solid #00ffcc;'>
        <p>Contact me at: mulugetadaniel74@gmail.com</p>
    </body>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
