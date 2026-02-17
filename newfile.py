
from flask import Flask

app = Flask(__name__)

# ምስሎች (ከፎቶህ የተወሰዱ)
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
hotel_view = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200"

def layout(content, title="Daniel Luxury Hotel"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{title}</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            body {{ margin:0; font-family: 'Segoe UI', sans-serif; background: #f0f2f5; text-align: center; }}
            .header {{ background: #004d40; color: white; padding: 15px; position: sticky; top: 0; z-index: 1000; }}
            nav {{ display: flex; justify-content: center; gap: 10px; margin-top: 10px; flex-wrap: wrap; }}
            nav a {{ color: white; text-decoration: none; font-weight: bold; font-size: 14px; background: rgba(255,255,255,0.1); padding: 8px 15px; border-radius: 5px; }}
            .card {{ background: white; max-width: 500px; margin: 20px auto; border-radius: 20px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
            .hero-img {{ width: 100%; height: 250px; object-fit: cover; }}
            .profile-img {{ width: 140px; height: 140px; border-radius: 50%; border: 5px solid white; margin-top: -70px; position: relative; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }}
            .btn {{ background: #ffcc00; color: black; padding: 15px 35px; border-radius: 35px; text-decoration: none; font-weight: bold; display: inline-block; border: none; font-size: 18px; cursor: pointer; }}
            input, select {{ width: 90%; padding: 12px; margin: 10px 0; border-radius: 10px; border: 1px solid #ddd; background: #f9f9f9; }}
            footer {{ background: #111; color: white; padding: 25px; margin-top: 50px; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h3 style="margin:0;">🏨 {title}</h3>
            <nav>
                <a href="/">HOME</a>
                <a href="/rooms">ROOMS</a>
                <a href="/menu">MENU</a>
                <a href="/register">REGISTER</a>
            </nav>
        </div>
        {content}
        <footer>
            <p>📱 ቴሌብር: 0986980130 | 🏦 አቢሲኒያ: 153682704</p>
            <p>© 2026 Designed by Daniel Mulugeta</p>
        </footer>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = f"""
    <img src="{hotel_view}" class="hero-img">
    <img src="{my_photo}" class="profile-img">
    <h1 style="margin-top:10px;">Daniel's Grand Hotel</h1>
    <p style="color:#666; padding: 0 20px;">የተሟላ ምቾት እና ዘመናዊ አገልግሎት በአንድ ላይ</p>
    <div style="margin: 20px;">
        <a href="/register" class="btn">አሁኑኑ ይመዝገቡ</a>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = """
    <div class="card">
        <h2>የመኝታ ክፍሎች</h2>
        <div style="text-align: left; line-height: 1.8;">
            <p>✅ VIP Suite - 5,000 ETB</p>
            <p>✅ Standard Room - 2,500 ETB</p>
            <p>✅ Luxury Studio - 3,500 ETB</p>
        </div>
        <a href="/register" class="btn">ቦታ ያዙ</a>
    </div>
    """
    return layout(content, "Hotel Rooms")

@app.route('/menu')
def menu():
    content = """
    <div class="card">
        <h2>የምግብ ዝርዝር</h2>
        <div style="text-align: left;">
            <p>🥘 ልዩ ክትፎ ....... 600 ብር</p>
            <p>🥩 በግ ጥብስ ....... 500 ብር</p>
            <p>🍕 ፒዛ ........... 450 ብር</p>
        </div>
    </div>
    """
    return layout(content, "Food Menu")

@app.route('/register')
def register():
    # Formspree ID ተስተካክሏል
    content = """
    <div class="card">
        <h2 style="color: #333;">የእንግዳ ምዝገባ</h2>
        <form action="https://formspree.io/f/mnnjlrvv" method="POST">
            <label>ሙሉ ስም</label><br>
            <input type="text" name="name" placeholder="ለምሳሌ፡ Daniel Mulugeta" required>
            <br>
            <label>ስልክ ቁጥር</label><br>
            <input type="tel" name="phone" placeholder="09..." required>
            <br>
            <label>የሚፈልጉት አገልግሎት</label><br>
            <select name="service">
                <option>ክፍል ማስያዝ (Room Booking)</option>
                <option>ምግብ ማዘዝ (Order Food)</option>
                <option>ሌላ (Other)</option>
            </select>
            <br><br>
            <button type="submit" class="btn" style="width: 100%;">መረጃውን ላክ</button>
        </form>
    </div>
    """
    return layout(content, "Register Now")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
