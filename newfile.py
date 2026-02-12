from flask import Flask

app = Flask(__name__)

# ያንተ ፎቶና የሆቴል ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room_img = "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=800"
food_img = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800"

def layout(content, title="Daniel's Hotel"):
    return f"""
    <body style='margin:0; font-family: "Segoe UI", sans-serif; background: #f0f2f5;'>
        <div style='background: #004d40; color: white; padding: 15px; text-align: center; position: sticky; top: 0; z-index: 100;'>
            <h2 style='margin:0;'>🏨 {title}</h2>
        </div>
        {content}
        <footer style='background: #222; color: white; padding: 30px; text-align: center;'>
            <p>📞 0986980130 | <a href='https://t.me/Godis1256' style='color: #0088cc; text-decoration: none;'>Telegram</a></p>
            <p style='font-size: 12px; color: #888;'>ICT Expert & Luxury Hospitality</p>
        </footer>
    </body>
    """

@app.route('/')
def home():
    content = f"""
    <div style='background: url("{room_img}") center/cover; height: 300px; display: flex; align-items: center; justify-content: center; color: white; text-shadow: 2px 2px 10px rgba(0,0,0,0.8);'>
        <div style='text-align: center;'>
            <h1 style='font-size: 40px;'>Daniel's Grand Hotel</h1>
            <p style='font-size: 20px;'>Where Comfort Meets Quality</p>
        </div>
    </div>
    <div style='padding: 30px; text-align: center;'>
        <img src='{my_photo}' style='width: 120px; height: 120px; border-radius: 50%; border: 4px solid #004d40; object-fit: cover; margin-top: -80px; background: white;'>
        <h3>Welcome to Our ICT Powered Hotel</h3>
        <p style='color: #666; max-width: 600px; margin: auto;'>We provide top-notch hospitality and modern technology services under one roof.</p>
        <div style='display: flex; justify-content: center; gap: 15px; margin-top: 30px;'>
            <a href='/rooms' style='background: #004d40; color: white; padding: 15px 25px; text-decoration: none; border-radius: 8px; font-weight: bold;'>Browse Rooms</a>
            <a href='/menu' style='background: #d32f2f; color: white; padding: 15px 25px; text-decoration: none; border-radius: 8px; font-weight: bold;'>Our Kitchen</a>
        </div>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = f"""
    <div style='padding: 20px;'>
        <h2 style='text-align: center; color: #004d40;'>Luxury Living Space</h2>
        <div style='background: white; border-radius: 15px; overflow: hidden; max-width: 500px; margin: 20px auto; box-shadow: 0 5px 15px rgba(0,0,0,0.1);'>
            <img src='{room_img}' style='width: 100%; height: 250px; object-fit: cover;'>
            <div style='padding: 20px;'>
                <h3>VIP Suite (ቪአይፒ አልጋ)</h3>
                <p style='color: #666;'>Ultra-fast WiFi, 4K Smart TV, and a stunning city view. Designed by our ICT team.</p>
                <p style='font-size: 24px; color: #004d40; font-weight: bold;'>$200/night</p>
                <a href='tel:0986980130' style='display: block; text-align: center; background: #ffcc00; color: black; padding: 12px; text-decoration: none; border-radius: 5px; font-weight: bold;'>BOOK ROOM</a>
            </div>
        </div>
        <p style='text-align: center;'><a href='/' style='color: #004d40;'>← Back to Home</a></p>
    </div>
    """
    return layout(content, "Hotel Rooms")

@app.route('/menu')
def menu():
    content = f"""
    <div style='padding: 20px;'>
        <h2 style='text-align: center; color: #d32f2f;'>Delicious Experience</h2>
        <div style='background: white; border-radius: 15px; overflow: hidden; max-width: 500px; margin: 20px auto; box-shadow: 0 5px 15px rgba(0,0,0,0.1);'>
            <img src='{food_img}' style='width: 100%; height: 250px; object-fit: cover;'>
            <div style='padding: 20px;'>
                <h3>Our Signature Menu</h3>
                <ul style='list-style: none; padding: 0; line-height: 2;'>
                    <li>✅ <b>Traditional Kitfo</b> - Served with Kocho</li>
                    <li>✅ <b>ICT Special Pizza</b> - Perfect Tech Fuel</li>
                    <li>✅ <b>Fresh Fruit Juice</b> - 100% Organic</li>
                </ul>
                <a href='https://t.me/Godis1256' style='display: block; text-align: center; background: #d32f2f; color: white; padding: 12px; text-decoration: none; border-radius: 5px; font-weight: bold;'>ORDER NOW ON TELEGRAM</a>
            </div>
        </div>
        <p style='text-align: center;'><a href='/' style='color: #d32f2f;'>← Back to Home</a></p>
    </div>
    """
    return layout(content, "Food & Drinks")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
