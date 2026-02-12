from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
    
    return f"""
    <body style='background-color: #f9f9f9; color: #333; text-align: center; font-family: sans-serif; margin: 0; padding: 0;'>
        
        <div style='background-color: #004d40; color: white; padding: 40px 20px;'>
            <h1 style='margin: 0;'>🏨 Daniel's Grand Hotel</h1>
            <p>Experience Luxury, Comfort & Delicious Cuisine</p>
        </div>

        <div style='padding: 30px; background: white;'>
            <img src='{my_photo}' style='width: 140px; height: 140px; border-radius: 50%; border: 4px solid #004d40; object-fit: cover;'>
            <h2>Daniel Mulugeta</h2>
            <p style='color: #666;'>Founder & CEO</p>
            
            <div style='margin-top: 15px;'>
                <a href='https://t.me/Godis1256' style='background: #0088cc; color: white; padding: 10px 20px; text-decoration: none; border-radius: 25px; font-weight: bold; display: inline-block;'>Contact on Telegram</a>
            </div>
        </div>

        <div style='background: #e0f2f1; padding: 30px;'>
            <h2 style='color: #004d40;'>🛏️ Our Rooms & 🍕 Special Menu</h2>
            <p>VIP Suites, Family Rooms, Traditional Kitfo & more!</p>
        </div>

        <footer style='background: #333; color: white; padding: 40px 20px;'>
            <h3>Contact Us</h3>
            <p>📍 Location: Addis Ababa, Ethiopia</p>
            <p>📞 Phone: <a href='tel:+251986980130' style='color: #ffcc00; text-decoration: none; font-weight: bold;'>0986980130</a></p>
            <p>✉️ Email: mulugetadaniel74@gmail.com</p>
            <br>
            <a href='tel:+251986980130' style='background: #ffcc00; color: black; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold;'>CALL NOW</a>
        </footer>
    </body>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
