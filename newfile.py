from flask import Flask

app = Flask(__name__)

# ምስሎች (Images)
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room1 = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800"
food1 = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800"

def layout(content, title="Daniel's Hotel"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ margin:0; font-family: 'Segoe UI', sans-serif; background: #f0f2f5; text-align: center; color: #333; }}
            .header {{ background: #004d40; color: white; padding: 15px; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.2); }}
            nav a {{ color:white; margin:0 7px; text-decoration:none; font-weight:bold; font-size: 12px; }}
            .card {{ background:white; max-width:600px; margin: 20px auto; border-radius:15px; padding: 20px; box-shadow:0 4px 15px rgba(0,0,0,0.1); }}
            .btn {{ background:#ffcc00; color:black; padding:12px 25px; text-decoration:none; border-radius:25px; font-weight:bold; display: inline-block; }}
            .social-btn {{ background: #25D366; color: white; padding: 10px 20px; border-radius: 20px; text-decoration: none; display: inline-block; margin: 5px; font-weight: bold; }}
            footer {{ background: #263238; color: white; padding: 30px; margin-top: 40px; }}
            .menu-item {{ display: flex; justify-content: space-between; border-bottom: 1px dashed #ccc; padding: 10px 0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2 style='margin:0;'>🏨 {title}</h2>
            <nav style='margin-top:10px;'>
                <a href='/'>HOME</a> | <a href='/rooms'>ROOMS</a> | <a href='/menu'>MENU</a> | <a href='/gallery'>GALLERY</a> | <a href='/register' style='color:#ffcc00;'>REGISTER</a>
            </nav>
        </div>
        {content}
        <footer>
            <h3>የስራ ሰዓት (Opening Hours)</h3>
            <p>ሰኞ - እሁድ: 24 ሰዓት ክፍት ነን</p>
            <hr style="border: 0.5px solid #444; width: 50%;">
            <h3>አድራሻ እና ማህበራዊ ሚዲያ</h3>
            <p>📍 አዲስ አበባ፣ ኢትዮጵያ | 📞 0986980130</p>
            <div style="margin-top:20px;">
                <a href="https://wa.me/251986980130" class="social-btn">WhatsApp</a>
                <a href="https://t.me/Godis1256" class="social-btn" style="background:#0088cc;">Telegram</a>
                <a href="https://www.tiktok.com/@musicstudio438" class="social-btn" style="background:#000;">TikTok</a>
            </div>
            <p style="margin-top:20px; font-size: 11px; color: #999;">© 2026 Daniel Mulugeta ICT</p>
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
        <p>በኢትዮጵያ ምርጥ መስተንግዶ እና ምቾት!</p>
        
        <div class="card">
            <h3>የደንበኞች ምስክርነት</h3>
            <p style="font-style: italic;">"ምርጥ አገልግሎት እና በጣም ጣፋጭ ምግብ ነው:: ለሁላችሁም እመክራለሁ!"</p>
            <p><strong>- አቶ በረከት</strong> ⭐⭐⭐⭐⭐</p>
        </div>
        
        <a href='/register' class="btn">አሁኑኑ ቦታ ይያዙ</a>
    </div>
    """
    return layout(content)

@app.route('/menu')
def menu():
    content = f"""
    <div style='padding: 20px;'>
        <h2>የምግብ እና የመጠጥ ዝርዝር</h2>
        <div class="card">
            <div class="menu-item"><span>ልዩ ክትፎ (Special Kitfo)</span> <span>500 ETB</span></div>
            <div class="menu-item"><span>የበግ ጥብስ (Lamb Tibs)</span> <span>450 ETB</span></div>
            <div class="menu-item"><span>ፆም በያይነቱ (Fasting Plate)</span> <span>300 ETB</span></div>
            <div class="menu-item"><span>ቡና እና ሻይ (Coffee & Tea)</span> <span>50 ETB</span></div>
            <div class="menu-item"><span>ለስላሳ መጠጦች (Soft Drinks)</span> <span>60 ETB</span></div>
        </div>
        <img src="{food1}" style="width:100%; max-width:400px; border-radius:15px;">
    </div>
    """
    return layout(content, "Hotel Menu")

@app.route('/rooms')
def rooms():
    content = f"""<div style='padding:20px;'><h2>አሪፍ ክፍሎቻችን</h2><div class="card" style="padding:0;"><img src='{room1}' style='width:100%;'><div style='padding:20px;'><h3>VIP Suite</h3><p>ምቹ አልጋ፣ ዋይፋይ እና ቴሌቪዥን ያለው</p><p><strong>$200 / Night</strong></p><a href='/register' class="btn">BOOK NOW</a></div></div></div>"""
    return layout(content, "Hotel Rooms")

@app.route('/gallery')
def gallery():
    content = """<div style='padding: 20px;'><h2>የፎቶ ማሳያ</h2><p>የሆቴሉን ውበት በቅርቡ በሰፊው እናሳያለን...</p></div>"""
    return layout(content, "Gallery")

@app.route('/register')
def register():
    content = """
    <div style='padding: 20px;'>
        <div class="card" style='text-align:left;'>
            <h2 style='text-align:center;'>ቦታ ለማስያዝ እዚህ ይሙሉ</h2>
            <form action="https://formspree.io/f/xlgwjnee" method="POST">
                <input type='text' name='name' placeholder="ሙሉ ስም" style='width:100%; padding:12px; margin:10px 0; border:1px solid #ddd; border-radius:8px;' required>
                <input type='tel' name='phone' placeholder="ስልክ ቁጥር" style='width:100%; padding:12px; margin:10px 0; border:1px solid #ddd; border-radius:8px;' required>
                <input type="hidden" name="_next" value="https://daniel-zt06.onrender.com/">
                <button type='submit' class="btn" style='width:100%; border:none; cursor:pointer;'>መረጃውን ላክ</button>
            </form>
        </div>
    </div>
    """
    return layout(content, "Register")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
