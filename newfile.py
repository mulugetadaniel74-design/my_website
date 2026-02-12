from flask import Flask, request

app = Flask(__name__)

# ምስሎች (Images)
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room_vip = "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=800"
food_kitfo = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800"

def layout(content, title="Daniel's Hotel"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ margin:0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f2f5; text-align: center; color: #333; }}
            .header {{ background: #004d40; color: white; padding: 20px; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.2); }}
            nav a {{ color:white; margin:0 15px; text-decoration:none; font-weight:bold; font-size: 14px; transition: 0.3s; }}
            nav a:hover {{ color: #ffcc00; }}
            .card {{ background:white; max-width:500px; margin: 20px auto; border-radius:15px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.1); }}
            .btn {{ background:#ffcc00; color:black; padding:12px 30px; text-decoration:none; border-radius:25px; font-weight:bold; display: inline-block; transition: 0.3s; }}
            .btn:hover {{ background: #e6b800; transform: scale(1.05); }}
            input, select {{ width:100%; padding:12px; margin:10px 0; border:1px solid #ddd; border-radius:8px; box-sizing: border-box; }}
            footer {{ background: #263238; color: white; padding: 30px; margin-top: 40px; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h2 style='margin:0;'>🏨 {title}</h2>
            <nav style='margin-top:12px;'>
                <a href='/'>HOME</a>
                <a href='/rooms'>ROOMS</a>
                <a href='/menu'>MENU</a>
                <a href='/register' style='color:#ffcc00;'>REGISTER</a>
            </nav>
        </div>
        {content}
        <footer>
            <p>📍 Addis Ababa, Ethiopia</p>
            <p>📞 0986980130 | Telegram: @Godis1256</p>
            <p>© 2026 Daniel Mulugeta ICT Services</p>
        </footer>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = f"""
    <div style='padding: 60px 20px;'>
        <img src='{my_photo}' style='width: 160px; height: 160px; border-radius: 50%; border: 5px solid white; box-shadow: 0 5px 15px rgba(0,0,0,0.2); object-fit: cover;'>
        <h1 style='font-size: 2.5em; margin-top: 20px;'>Daniel's Grand Hotel</h1>
        <p style='font-size: 1.1em; color: #666;'>የተሟላ ምቾት እና ዘመናዊ አገልግሎት በአንድ ላይ</p>
        <div style='margin-top: 30px;'>
            <a href='/register' class="btn">አሁኑኑ ይመዝገቡ</a>
        </div>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = f"""<div style='padding:20px;'><h2>አሪፍ ክፍሎቻችን</h2><div class="card"><img src='{room_vip}' style='width:100%;'><div style='padding:20px;'><h3>VIP Suite</h3><p>Price: $200 / Night</p><a href='/register' class="btn">BOOK NOW</a></div></div></div>"""
    return layout(content, "Hotel Rooms")

@app.route('/menu')
def menu():
    content = f"""<div style='padding:20px;'><h2>ምርጥ ምግቦቻችን</h2><div class="card"><img src='{food_kitfo}' style='width:100%;'><div style='padding:20px;'><h3>Traditional Kitfo</h3><p>ትኩስ እና ጣፋጭ ክትፎ</p></div></div></div>"""
    return layout(content, "Restaurant Menu")

@app.route('/register')
def register():
    content = f"""
    <div style='padding: 30px 20px;'>
        <div class="card" style='padding:30px; text-align:left;'>
            <h2 style='text-align:center; margin-top:0;'>የእንግዳ ምዝገባ</h2>
            <form action="https://formspree.io/f/xlgwjnee" method="POST">
                <label>ሙሉ ስም</label>
                <input type='text' name='name' placeholder="ለምሳሌ፡ ዳንኤል ሙሉጌታ" required>
                <label>ስልክ ቁጥር</label>
                <input type='tel' name='phone' placeholder="09..." required>
                <label>የሚፈልጉት አገልግሎት</label>
                <select name='service'>
                    <option>ክፍል ማስያዝ (Room Booking)</option>
                    <option>ምግብ ማዘዝ (Food Order)</option>
                    <option>ሌላ (Other)</option>
                </select>
                <input type="hidden" name="_next" value="https://daniel-zt06.onrender.com/">
                <button type='submit' class="btn" style='width:100%; border:none; cursor:pointer; margin-top:10px;'>መረጃውን ላክ</button>
            </form>
        </div>
    </div>
    """
    return layout(content, "Register Now")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
