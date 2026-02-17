import random
from flask import Flask

app = Flask(__name__)

# ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
hotel_view = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200"

def layout(content, title="Daniel's App"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: sans-serif; margin: 0; text-align: center; background: #f0f2f5; }}
            .nav {{ background: #004d40; padding: 15px; color: white; position: sticky; top: 0; }}
            .nav a {{ color: white; text-decoration: none; margin: 0 10px; font-weight: bold; }}
            .card {{ background: white; margin: 20px auto; padding: 20px; max-width: 500px; border-radius: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
            .btn {{ background: gold; color: black; padding: 15px 30px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block; border: none; cursor: pointer; }}
        </style>
    </head>
    <body>
        <div class="nav">
            <a href="/">HOME</a> | <a href="/spin">SPIN GAME</a>
        </div>
        {content}
    </body>
    </html>
    """

@app.route('/')
def home():
    content = f"""
    <img src="{hotel_view}" style="width:100%; height:200px; object-fit:cover;">
    <div class="card">
        <img src="{my_photo}" style="width:100px; border-radius:50%; margin-top:-50px; border: 5px solid white;">
        <h1>Daniel's Grand Hotel</h1>
        <p>እንኳን በሰላም መጡ! አሁን ጌም መጫወትም ይችላሉ::</p>
        <a href="/spin" class="btn">ወደ ጌም ሂድ (Play Game)</a>
    </div>
    """
    return layout(content)

@app.route('/spin')
def spin():
    items = ["🔔", "🍒", "💎", "7️⃣", "🍀"]
    s1, s2, s3 = random.choice(items), random.choice(items), random.choice(items)
    
    msg = "እንደገና ይሞክሩ!"
    if s1 == s2 == s3: msg = "💰 አሸንፈዋል! 💰"

    content = f"""
    <div class="card" style="background: #111; color: white;">
        <h2>🎰 Daniel's Spin 🎰</h2>
        <div style="font-size: 60px; background: #222; padding: 20px; border-radius: 15px; margin: 20px 0;">
            {s1} | {s2} | {s3}
        </div>
        <h3>{msg}</h3>
        <a href="/spin" class="btn">SPIN (አሽከርክር)</a>
        <br><br>
        <a href="/" style="color: grey;">ወደ ሆቴሉ ተመለስ</a>
    </div>
    """
    return layout(content, "Lucky Spin")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
