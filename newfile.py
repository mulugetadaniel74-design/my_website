from flask import Flask
import datetime

app = Flask(__name__)

# ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
hotel_view = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200"

def layout(content, title="Daniel Supreme"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            :root {{ --gold: #d4af37; --deep: #002d26; --glass: rgba(255, 255, 255, 0.1); }}
            body {{ margin:0; font-family: 'Segoe UI', sans-serif; background: #f0f2f5; scroll-behavior: smooth; }}
            
            /* 1. Header & Nav */
            .header {{ background: var(--deep); color: white; padding: 10px; position: sticky; top:0; z-index:2000; }}
            nav {{ display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-top: 10px; }}
            nav a {{ color: white; text-decoration: none; font-size: 12px; border: 1px solid var(--gold); padding: 5px 12px; border-radius: 20px; }}
            
            /* 2. Hero & Profile */
            .hero {{ width: 100%; height: 350px; object-fit: cover; clip-path: ellipse(100% 70% at 50% 30%); }}
            .p-img {{ width: 130px; height: 130px; border-radius: 50%; border: 5px solid white; position: absolute; top: 250px; left: 50%; transform: translateX(-50%); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }}

            /* 3. Modern Cards */
            .card {{ background: white; max-width: 600px; margin: 100px auto 20px; border-radius: 30px; padding: 30px; box-shadow: 0 20px 40px rgba(0,0,0,0.05); text-align: center; }}
            .btn-lux {{ background: linear-gradient(90deg, #d4af37, #f4c430); color: black; padding: 15px 40px; border-radius: 50px; font-weight: bold; text-decoration: none; display: inline-block; box-shadow: 0 10px 20px rgba(212,175,55,0.3); }}

            /* 4. Comparison Table */
            .price-table {{ width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 14px; }}
            .price-table th, .price-table td {{ border: 1px solid #eee; padding: 12px; }}
            .price-table th {{ background: #f9f9f9; }}

            /* 5. Floating Socials */
            .social-bar {{ position: fixed; left: 10px; top: 50%; transform: translateY(-50%); display: flex; flex-direction: column; gap: 10px; z-index: 3000; }}
            .social-bar a {{ background: var(--deep); color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; text-decoration: none; }}

            /* 6. TikTok Box */
            .tiktok-box {{ background: #000; color: white; padding: 20px; border-radius: 20px; margin: 20px auto; max-width: 500px; }}
        </style>
    </head>
    <body>
        <div class="social-bar">
            <a href="https://t.me/Godis1256"><i class="fab fa-telegram"></i></a>
            <a href="https://www.tiktok.com/@musicstudio438"><i class="fab fa-tiktok"></i></a>
            <a href="tel:0986980130"><i class="fas fa-phone"></i></a>
        </div>

        <div class="header">
            <h3>🏨 DANIEL SUPREME HOTEL</h3>
            <nav>
                <a href="/">HOME</a>
                <a href="/rooms">ROOMS</a>
                <a href="/menu">MENU</a>
                <a href="/gallery">GALLERY</a>
                <a href="/register">BOOK</a>
            </nav>
        </div>

        {content}

        <footer>
            <div class="card" style="background:#111; color:white; margin: 50px auto 0;">
                <h4 style="color:var(--gold);">💰 Payment Info</h4>
                <p>Telebirr: 0986980130 | Bank: 153682704</p>
                <p style="font-size: 10px;">Designed & Developed by Daniel Mulugeta (ICT Specialist)</p>
            </div>
        </footer>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = f"""
    <div style="position:relative;">
        <img src="{hotel_view}" class="hero">
        <img src="{my_photo}" class="p-img">
    </div>
    <div class="card">
        <h1>Welcome to Daniel's Hub</h1>
        <p>የኢትዮጵያ ቀዳሚው ዘመናዊ ሆቴል::</p>
        <div style="display:flex; justify-content:center; gap:20px; font-size:25px; color:var(--deep); margin:20px;">
            <i class="fas fa-wifi"></i> <i class="fas fa-swimmer"></i> <i class="fas fa-utensils"></i> <i class="fas fa-spa"></i>
        </div>
        
        <h3>🏨 የክፍሎች ዋጋ ዝርዝር</h3>
        <table class="price-table">
            <tr><th>Room Type</th><th>Price</th><th>Extra</th></tr>
            <tr><td>Standard</td><td>2,500 ETB</td><td>Free WiFi</td></tr>
            <tr><td>VIP Suite</td><td>5,000 ETB</td><td>Breakfast</td></tr>
            <tr><td>Presidential</td><td>10,000 ETB</td><td>Pool Access</td></tr>
        </table>
        <br>
        <a href="/register" class="btn-lux">Book Your Room Now</a>
    </div>

    <div class="tiktok-box">
        <h4>📱 Latest TikTok Updates</h4>
        <p>Follow @musicstudio438 for more!</p>
        <a href="https://www.tiktok.com/@musicstudio438" style="color:var(--gold);">Watch Videos</a>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    return layout("<div class='card'><h2>Rooms - Coming Soon with 360 View!</h2></div>")

@app.route('/menu')
def menu():
    return layout("<div class='card'><h2>Menu - Order Fresh Foods Online!</h2></div>")

@app.route('/gallery')
def gallery():
    return layout("<div class='card'><h2>Gallery - Beautiful Hotel Views</h2></div>")

@app.route('/register')
def register():
    content = """
    <div class="card">
        <h2>Quick Reservation</h2>
        <input type="text" placeholder="Full Name" style="width:90%; padding:15px; margin:10px; border-radius:15px; border:1px solid #ddd;">
        <input type="number" id="n" placeholder="Nights" oninput="calc()" style="width:90%; padding:15px; margin:10px; border-radius:15px; border:1px solid #ddd;">
        <p>Total: <b id="total">0</b> ETB</p>
        <button class="btn-lux" style="width:95%;">Confirm My Stay</button>
        <script>
            function calc() {
                document.getElementById('total').innerText = document.getElementById('n').value * 2500;
            }
        </script>
    </div>
    """
    return layout(content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
