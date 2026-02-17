from flask import Flask

app = Flask(__name__)

# ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room1 = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800"

def layout(content, title="Daniel's Hotel"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ margin:0; font-family: 'Segoe UI', sans-serif; background: #f0f2f5; text-align: center; color: #333; }}
            .header {{ background: #004d40; color: white; padding: 15px; position: sticky; top: 0; z-index: 1000; }}
            nav a {{ color:white; margin:0 7px; text-decoration:none; font-weight:bold; font-size: 12px; }}
            .card {{ background:white; max-width:600px; margin: 20px auto; border-radius:15px; padding: 20px; box-shadow:0 4px 15px rgba(0,0,0,0.1); }}
            .btn {{ background:#ffcc00; color:black; padding:12px 25px; text-decoration:none; border-radius:25px; font-weight:bold; display: inline-block; }}
            .call-btn {{ background: #28a745; color: white; padding: 10px 20px; border-radius: 20px; text-decoration: none; font-weight: bold; position: fixed; bottom: 20px; right: 20px; z-index: 1001; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }}
            footer {{ background: #263238; color: white; padding: 30px; margin-top: 40px; }}
            .marquee {{ background: #ffcc00; color: #000; font-weight: bold; padding: 5px; font-size: 14px; }}
            .payment-box {{ background: #ffffff; padding: 15px; border-radius: 10px; margin-top: 20px; text-align: left; color: #333; }}
            .telebirr {{ border-left: 5px solid #00adef; margin-bottom: 10px; padding-left: 10px; }}
            .abyssinia {{ border-left: 5px solid #1976d2; padding-left: 10px; }}
        </style>
    </head>
    <body>
        <div class="marquee"><marquee>ማስታወቂያ፦ ማንኛውንም አይነት ዌብሳይት በተመጣጣኝ ዋጋ ለማሰራት በ 0986980130 ይደውሉልን! (Daniel ICT)</marquee></div>
        <div class="header">
            <h2 style='margin:0;'>🏨 {title}</h2>
            <nav style='margin-top:10px;'>
                <a href='/'>HOME</a> | <a href='/rooms'>ROOMS</a> | <a href='/gallery'>GALLERY</a> | <a href='/register' style='color:#ffcc00;'>REGISTER</a>
            </nav>
        </div>
        
        <a href="tel:0986980130" class="call-btn">📞 ደውል (Call)</a>

        {content}
        
        <footer>
            <h3>የክፍያ አማራጮች (Payment Methods)</h3>
            <div class="payment-box">
                <div class="telebirr">
                    <p><strong>📱 Telebirr (ቴሌብር)</strong></p>
                    <p>ቁጥር: 0986980130</p>
                </div>
                <div class="abyssinia">
                    <p><strong>🏦 የአቢሲኒያ ባንክ (Bank of Abyssinia)</strong></p>
                    <p>ቁጥር: 153682704</p>
                    <p>ስም: ዳንኤል ሙሉጌታ</p>
                </div>
            </div>
            
            <div style="margin-top:30px;">
                <a href="https://wa.me/251986980130" style="color:#25D366; text-decoration:none; margin:10px; font-weight:bold;">WhatsApp</a>
                <a href="https://t.me/Godis1256" style="color:#0088cc; text-decoration:none; margin:10px; font-weight:bold;">Telegram</a>
                <a href="https://www.tiktok.com/@musicstudio438" style="color:#ff0050; text-decoration:none; margin:10px; font-weight:bold;">TikTok</a>
            </div>
            <p style="margin-top:20px; font-size: 11px; color: #999;">© 2026 Daniel Mulugeta ICT - Professional Developer</p>
        </footer>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = f"""
    <div style='padding: 40px 20px;'>
        <img src='{my_photo}' style='width: 140px; height: 140px; border-radius: 50%; border: 4px solid white; box-shadow: 0 5px 15px rgba(0,0,0,0.2);'>
        <h1>Daniel's Grand Hotel</h1>
        <p>እንኳን ወደ ሆቴላችን በሰላም መጡ!</p>
        <div class="card">
            <h3>ልዩ መረጃ</h3>
            <p>አሁን ዌብሳይታችን ላይ በቀጥታ የክፍያ መረጃዎችን ማግኘት ይችላሉ::</p>
            <a href='/register' class="btn">አሁኑኑ ቦታ ይያዙ</a>
        </div>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = f"""<div style='padding:20px;'><h2>አሪፍ ክፍሎቻችን</h2><div class="card" style="padding:0;"><img src='{room1}' style='width:100%;'><div style='padding:20px;'><h3>VIP Suite</h3><p>$200 / Night</p><a href='/register' class="btn">BOOK NOW</a></div></div></div>"""
    return layout(content, "Hotel Rooms")

@app.route('/gallery')
def gallery():
    return layout("<h2>Gallery Page - በቅርቡ ይጠብቁ!</h2>")

@app.route('/register')
def register():
    content = """
    <div style='padding: 20px;'>
        <div class="card">
            <h2>የእንግዳ ምዝገባ</h2>
            <form action="https://formspree.io/f/xlgwjnee" method="POST">
                <input type='text' name='name' placeholder="ሙሉ ስም" style='width:90%; padding:12px; margin:10px 0; border:1px solid #ddd; border-radius:8px;' required>
                <input type='tel' name='phone' placeholder="ስልክ ቁጥር" style='width:90%; padding:12px; margin:10px 0; border:1px solid #ddd; border-radius:8px;' required>
                <button type='submit' class="btn" style='width:90%; border:none; cursor:pointer;'>መረጃውን ላክ</button>
            </form>
        </div>
    </div>
    """
    return layout(content, "Register")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
