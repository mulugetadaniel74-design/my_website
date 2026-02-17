from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ background: #121212; color: white; text-align: center; font-family: sans-serif; padding: 20px; }}
            .card {{ background: #1e1e1e; padding: 20px; border-radius: 20px; border: 2px solid #ffcc00; margin: 10px; }}
            .btn {{ background: #ffcc00; color: black; padding: 15px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block; }}
            .marquee {{ color: #ffcc00; font-weight: bold; border-bottom: 1px solid #333; padding: 10px; }}
        </style>
    </head>
    <body>
        <div class="marquee"><marquee>Daniel ICT: 0986980130 - ማንኛውንም ዌብሳይት እናሰራለን!</marquee></div>
        <h1>🏨 Daniel Luxury Hotel</h1>
        <p>🕒 የአሁኑ ሰዓት: {now}</p>
        
        <div class="card">
            <h3>እንኳን ደህና መጡ</h3>
            <p>በኢትዮጵያ ምርጡ እና ዘመናዊው ሆቴል!</p>
            <a href="tel:0986980130" class="btn">📞 አሁኑኑ ይደውሉ</a>
        </div>

        <div class="card" style="text-align: left;">
            <h4 style="color:#ffcc00;">💰 የክፍያ አማራጮች</h4>
            <p>ቴሌብር: 0986980130</p>
            <p>አቢሲኒያ: 153682704 (ዳንኤል ሙሉጌታ)</p>
        </div>

        <p style="font-size: 10px; color: #666;">© 2026 Designed by Daniel Mulugeta</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
