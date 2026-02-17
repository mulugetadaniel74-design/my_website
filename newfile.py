
from flask import Flask

app = Flask(__name__)

# ምርጥ ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
hotel_view = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200"
room_img = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800"
food_img = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800"

def layout(content, title="Daniel Luxury Hotel"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{title}</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
        <style>
            :root {{ --gold: #ffcc00; --dark-green: #004d40; --light-bg: #f8f9fa; }}
            body {{ margin:0; font-family: 'Poppins', sans-serif; background: var(--light-bg); color: #333; overflow-x: hidden; }}
            
            /* Navbar Style */
            .header {{ background: var(--dark-green); padding: 10px 0; position: sticky; top: 0; z-index: 1000; box-shadow: 0 4px 12px rgba(0,0,0,0.15); }}
            nav {{ display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; padding: 5px; }}
            nav a {{ color: white; text-decoration: none; font-size: 13px; font-weight: 600; padding: 8px 15px; border-radius: 50px; transition: 0.3s; border: 1px solid rgba(255,255,255,0.2); }}
            nav a:hover {{ background: var(--gold); color: black; border-color: var(--gold); }}
            .active {{ background: var(--gold); color: black; border-color: var(--gold); }}

            /* Hero Section */
            .hero-container {{ position: relative; width: 100%; height: 300px; }}
            .hero-img {{ width: 100%; height: 100%; object-fit: cover; filter: brightness(0.8); }}
            .profile-wrapper {{ position: absolute; bottom: -60px; left: 50%; transform: translateX(-50%); }}
            .profile-img {{ width: 120px; height: 120px; border-radius: 50%; border: 5px solid white; box-shadow: 0 8px 20px rgba(0,0,0,0.2); }}

            /* Cards */
            .card {{ background: white; max-width: 550px; margin: 80px auto 20px; border-radius: 25px; padding: 30px; box-shadow: 0 15px 35px rgba(0,0,0,0.05); text-align: center; border: 1px solid #eee; }}
            .btn-gold {{ background: linear-gradient(135deg, #ffcc00, #ff9900); color: black; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: bold; display: inline-block; box-shadow: 0 5px 15px rgba(255,204,0,0.3); transition: 0.3s; border: none; }}
            .btn-gold:hover {{ transform: translateY(-3px); box-shadow: 0 8px 20px rgba(255,204,0,0.4); }}

            /* Footer */
            footer {{ background: #111; color: #999; padding: 40px 20px; text-align: center; margin-top: 60px; }}
            .footer-card {{ background: rgba(255,255,255,0.05); padding: 20px; border-radius: 20px; display: inline-block; text-align: left; color: white; }}
        </style>
    </head>
    <body class="animate__animated animate__fadeIn">
        <div class="header">
            <h2 style="color:white; margin:0 0 10px 0; text-align:center;">🏨 DANIEL LUXURY</h2>
            <nav>
                <a href="/" id="h-link">HOME</a>
                <a href="/rooms" id="r-link">ROOMS</a>
                <a href="/menu" id="m-link">MENU</a>
                <a href="/gallery" id="g-link">GALLERY</a>
                <a href="/register" style="background:white; color:black;">BOOK NOW</a>
            </nav>
        </div>

        {content}

        <footer>
            <div class="footer-card">
                <h4 style="margin:0 0 10px 0; color:var(--gold);">💰 Payment Methods</h4>
                <p style="margin:5px 0;">Telebirr: 0986980130</p>
                <p style="margin:5px 0;">Abyssinia: 153682704</p>
            </div>
            <p style="margin-top:20px; font-size:12px;">© 2026 Daniel Mulugeta ICT Specialist</p>
        </footer>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = f"""
    <div class="hero-container">
        <img src="{hotel_view}" class="hero-img">
        <div class="profile-wrapper">
            <img src="{my_photo}" class="profile-img">
        </div>
    </div>
    <div class="card animate__animated animate__fadeInUp">
        <h1 style="margin-bottom:5px;">Daniel's Grand Hotel</h1>
        <p style="color:var(--gold); font-size:20px;">★★★★★</p>
        <p style="color:#666; line-height:1.6;">Welcome to the pinnacle of Ethiopian hospitality. Experience luxury, comfort, and world-class service in the heart of the city.</p>
        <a href="/register" class="btn-gold">Explore & Book</a>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = f"""
    <div class="card animate__animated animate__zoomIn">
        <h2 style="color:var(--dark-green);">Luxury Suites</h2>
        <img src="{room_img}" style="width:100%; border-radius:20px; margin:15px 0;">
        <h3>VIP Presidential Suite</h3>
        <p style="color:#777;">High-speed WiFi, Mini Bar, and City View.</p>
        <p style="font-weight:bold; font-size:22px;">5,000 ETB / Night</p>
        <a href="/register" class="btn-gold">Reserve Now</a>
    </div>
    """
    return layout(content, "Luxury Rooms")

@app.route('/menu')
def menu():
    content = f"""
    <div class="card animate__animated animate__fadeInRight">
        <h2 style="color:var(--dark-green);">Exquisite Dining</h2>
        <img src="{food_img}" style="width:100%; border-radius:20px; margin:15px 0;">
        <div style="text-align:left; background:#f9f9f9; padding:20px; border-radius:15px;">
            <p>🥘 Special Kitfo ............ 600 ETB</p>
            <p>🥩 Lamb Tibs ............. 500 ETB</p>
            <p>🍕 Gourmet Pizza .......... 450 ETB</p>
        </div>
        <a href="tel:0986980130" class="btn-gold" style="margin-top:20px;">Order Delivery</a>
    </div>
    """
    return layout(content, "Food & Drinks")

@app.route('/gallery')
def gallery():
    content = f"""
    <div class="card animate__animated animate__fadeInUp" style="max-width:800px;">
        <h2 style="color:var(--dark-green);">Hotel Gallery</h2>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap:15px; padding:10px;">
            <img src="{hotel_view}" style="width:100%; border-radius:15px; box-shadow:0 5px 10px rgba(0,0,0,0.1);">
            <img src="{room_img}" style="width:100%; border-radius:15px; box-shadow:0 5px 10px rgba(0,0,0,0.1);">
            <img src="{food_img}" style="width:100%; border-radius:15px; box-shadow:0 5px 10px rgba(0,0,0,0.1);">
            <img src="{my_photo}" style="width:100%; border-radius:15px; box-shadow:0 5px 10px rgba(0,0,0,0.1);">
        </div>
    </div>
    """
    return layout(content, "Gallery")

@app.route('/register')
def register():
    content = """
    <div class="card animate__animated animate__pulse">
        <h2 style="color:var(--dark-green);">Guest Registration</h2>
        <p>Complete the form below to book your stay.</p>
        <div style="text-align:left;">
            <label style="font-weight:bold; font-size:14px;">Full Name</label>
            <input type="text" placeholder="Enter your name" style="width:100%; padding:12px; margin:8px 0 20px; border-radius:10px; border:1px solid #ddd;">
            <label style="font-weight:bold; font-size:14px;">Phone Number</label>
            <input type="tel" placeholder="09..." style="width:100%; padding:12px; margin:8px 0 20px; border-radius:10px; border:1px solid #ddd;">
        </div>
        <button class="btn-gold" style="width:100%;" onclick="alert('Booking Request Sent!')">Confirm Booking</button>
    </div>
    """
    return layout(content, "Book Your Stay")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
