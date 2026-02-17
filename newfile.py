from flask import Flask

app = Flask(__name__)

# ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
hotel_view = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200"
room_img = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800"
food_img = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800"

def layout(content, title="Daniel Luxury Hotel"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            body {{ margin:0; font-family: 'Poppins', sans-serif; background: #f0f2f5; text-align: center; }}
            .header {{ background: #004d40; color: white; padding: 15px; position: sticky; top: 0; z-index: 1000; }}
            nav {{ display: flex; justify-content: center; gap: 15px; margin-top: 10px; flex-wrap: wrap; }}
            nav a {{ color: white; text-decoration: none; font-weight: bold; font-size: 14px; background: rgba(255,255,255,0.1); padding: 5px 10px; border-radius: 5px; }}
            nav a:hover {{ background: #ffcc00; color: black; }}
            .card {{ background: white; max-width: 600px; margin: 20px auto; border-radius: 20px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
            .btn {{ background: #ffcc00; color: black; padding: 12px 25px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block; }}
            footer {{ background: #1a1a1a; color: white; padding: 30px; margin-top: 50px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h3 style="margin:0;">🏨 {title}</h3>
            <nav>
                <a href="/">HOME</a>
                <a href="/rooms">ROOMS</a>
                <a href="/menu">MENU</a>
                <a href="/gallery">GALLERY</a>
                <a href="/register">BOOK NOW</a>
            </nav>
        </div>
        {content}
        <footer>
            <p>📱 Telebirr: 0986980130 | 🏦 Abyssinia: 153682704</p>
            <p>© 2026 Developed by Daniel Mulugeta ICT</p>
        </footer>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = f"""
    <img src="{hotel_view}" style="width:100%; height:250px; object-fit:cover;">
    <img src="{my_photo}" style="width:130px; height:130px; border-radius:50%; border:5px solid #ffcc00; margin-top:-70px; position:relative; background:white;">
    <h1>Daniel's Grand Hotel</h1>
    <div style="color:#ffcc00;">★★★★★</div>
    <div class="card">
        <h3>ልዩ መስተንግዶ</h3>
        <p>እንኳን ወደ ኢትዮጵያ ምርጡ ሆቴል በሰላም መጡ! ለላቀ ምቾት እኛን ይምረጡ::</p>
        <a href="/register" class="btn">አሁኑኑ ቦታ ይያዙ</a>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = f"""
    <div class="card">
        <h2>የመኝታ ክፍሎች</h2>
        <img src="{room_img}" style="width:100%; border-radius:15px;">
        <h3>VIP Suite</h3>
        <p>ዋጋ፡ 5,000 ብር በሌሊት</p>
        <a href="/register" class="btn">አሁኑኑ እዘዝ</a>
    </div>
    """
    return layout(content, "Rooms")

@app.route('/menu')
def menu():
    content = f"""
    <div class="card">
        <h2>የምግብ ዝርዝር (Menu)</h2>
        <img src="{food_img}" style="width:100%; border-radius:15px;">
        <div style="text-align:left; padding:10px;">
            <p>🥘 ልዩ ክትፎ ....... 600 ብር</p>
            <p>🍖 በግ ጥብስ ....... 500 ብር</p>
            <p>🍕 ፒዛ ........... 450 ብር</p>
        </div>
    </div>
    """
    return layout(content, "Food Menu")

@app.route('/gallery')
def gallery():
    content = f"""
    <div class="card">
        <h2>ጋላሪ (Gallery)</h2>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
            <img src="{hotel_view}" style="width:100%; border-radius:10px;">
            <img src="{room_img}" style="width:100%; border-radius:10px;">
            <img src="{food_img}" style="width:100%; border-radius:10px;">
            <img src="{my_photo}" style="width:100%; border-radius:10px;">
        </div>
    </div>
    """
    return layout(content, "Photo Gallery")

@app.route('/register')
def register():
    content = """
    <div class="card">
        <h2>የእንግዳ ምዝገባ</h2>
        <p>መረጃዎን ይሙሉና አስደሳች ጊዜ ያሳልፉ!</p>
        <input type="text" placeholder="ሙሉ ስም" style="width:90%; padding:12px; margin:10px; border-radius:10px; border:1px solid #ccc;">
        <input type="tel" placeholder="ስልክ ቁጥር" style="width:90%; padding:12px; margin:10px; border-radius:10px; border:1px solid #ccc;">
        <button class="btn" style="width:95%;" onclick="alert('ተሳክቷል! እናመሰግናለን::')">መረጃ ላክ</button>
    </div>
    """
    return layout(content, "Book Now")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
