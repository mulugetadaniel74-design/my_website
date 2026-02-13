from flask import Flask

app = Flask(__name__)

# ምስሎች (Images)
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room1 = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800"
room2 = "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800"
food1 = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800"
hotel_view = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=800"

def layout(content, title="Daniel's Hotel"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ margin:0; font-family: 'Segoe UI', sans-serif; background: #f0f2f5; text-align: center; color: #333; }}
            .header {{ background: #004d40; color: white; padding: 20px; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.2); }}
            nav a {{ color:white; margin:0 10px; text-decoration:none; font-weight:bold; font-size: 13px; }}
            .card {{ background:white; max-width:600px; margin: 20px auto; border-radius:15px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.1); }}
            .btn {{ background:#ffcc00; color:black; padding:12px 25px; text-decoration:none; border-radius:25px; font-weight:bold; display: inline-block; transition: 0.3s; }}
            .social-btn {{ background: #0088cc; color: white; padding: 10px 20px; border-radius: 20px; text-decoration: none; display: inline-block; margin: 5px; font-size: 14px; font-weight: bold; }}
            .tiktok-btn {{ background: #000000; color: white; }}
            .gallery-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 15px; }}
            .gallery-grid img {{ width: 100%; border-radius: 10px; height: 150px; object-fit: cover; }}
            footer {{ background: #263238; color: white; padding: 30px; margin-top: 40px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2 style='margin:0;'>🏨 {title}</h2>
            <nav style='margin-top:10px;'>
                <a href='/'>HOME</a> | <a href='/rooms'>ROOMS</a> | <a href='/gallery'>GALLERY</a> | <a href='/register' style='color:#ffcc00;'>REGISTER</a>
            </nav>
        </div>
        {content}
        <footer>
            <h3>አድራሻ እና ማህበራዊ ሚዲያ</h3>
            <p>📍 አዲስ አበባ፣ ኢትዮጵያ (Addis Ababa, Ethiopia)</p>
            <p>📞 0986980130</p>
            <div style="margin-top:20px;">
                <a href="https://t.me/Godis1256" class="social-btn">Telegram</a>
                <a href="https://www.tiktok.com/@musicstudio438" class="social-btn tiktok-btn">TikTok</a>
            </div>
            <p style="margin-top:20px; font-size: 12px; color: #999;">© 2026 Daniel Mulugeta ICT</p>
        </footer>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = f"""
    <div style='padding: 50px 20px;'>
        <img src='{my_photo}' style='width: 150px; height: 150px; border-radius: 50%; border: 5px solid white; box-shadow: 0 5px 15px rgba(0,0,0,0.2);'>
        <h1 style='margin-top:20px;'>Daniel's Grand Hotel</h1>
        <p>እንኳን ወደ ሆቴላችን በሰላም መጡ! ምርጥ መስተንግዶ ይጠብቅዎታል::</p>
        <div style="margin-top:30px;">
            <a href='/register' class="btn">አሁኑኑ ቦታ ይያዙ</a>
        </div>
    </div>
    """
    return layout(content)

@app.route('/gallery')
def gallery():
    content = f"""<div style='padding: 20px;'><h2>የፎቶ ማሳያ (Gallery)</h2><div class="gallery-grid"><img src="{hotel_view}"><img src="{room1}"><img src="{room2}"><img src="{food1}"></div></div>"""
    return layout(content, "Hotel Gallery")

@app.route('/rooms')
def rooms():
    content = f"""<div style='padding:20px;'><h2>አሪፍ ክፍሎቻችን</h2><div class="card"><img src='{room1}' style='width:100%;'><div style='padding:20px;'><h3>VIP Suite</h3><p>Price: $200 / Night</p><a href='/register' class="btn">BOOK NOW</a></div></div></div>"""
    return layout(content, "Hotel Rooms")

@app.route('/register')
def register():
    content = """
    <div style='padding: 20px;'>
        <div class="card" style='padding:30px; text-align:left;'>
            <h2 style='text-align:center;'>የእንግዳ ምዝገባ</h2>
            <form action="https://formspree.io/f/xlgwjnee" method="POST">
                <input type='text' name='name' placeholder="ሙሉ ስም" style='width:100%; padding:12px; margin:10px 0; border:1px solid #ddd; border-radius:8px;' required>
                <input type='tel' name='phone' placeholder="ስልክ ቁጥር" style='width:100%; padding:12px; margin:10px 0; border:1px solid #ddd; border-radius:8px;' required>
                <input type="hidden" name="_next" value="https://daniel-zt06.onrender.com/">
                <button type='submit' class="btn" style='width:100%; border:none; cursor:pointer;'>መረጃውን ላክ</button>
            </form>
        </div>
    </div>
    """
    return layout(content, "Guest Registration")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
