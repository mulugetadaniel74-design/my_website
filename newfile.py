from flask import Flask, request

app = Flask(__name__)

# ምስሎች (Images)
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room_vip = "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=800"
food_kitfo = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800"

def layout(content, title="Daniel's Hotel"):
    return f"""
    <!DOCTYPE html>
    <body style='margin:0; font-family: sans-serif; background: #f4f4f4; text-align: center;'>
        <div style='background: #004d40; color: white; padding: 15px; position: sticky; top: 0; z-index: 100;'>
            <h2 style='margin:0;'>🏨 {title}</h2>
            <nav style='margin-top:10px;'>
                <a href='/' style='color:white; margin:10px; text-decoration:none; font-weight:bold;'>Home</a> | 
                <a href='/rooms' style='color:white; margin:10px; text-decoration:none; font-weight:bold;'>Rooms</a> | 
                <a href='/menu' style='color:white; margin:10px; text-decoration:none; font-weight:bold;'>Menu</a> |
                <a href='/register' style='color:#ffcc00; margin:10px; text-decoration:none; font-weight:bold;'>Register Now</a>
            </nav>
        </div>
        {content}
        <footer style='background: #333; color: white; padding: 20px; margin-top: 50px;'>
            <p>📞 0986980130 | Telegram: @Godis1256</p>
        </footer>
    </body>
    """

@app.route('/')
def home():
    content = f"""
    <div style='padding: 50px;'>
        <img src='{my_photo}' style='width: 150px; height: 150px; border-radius: 50%; border: 4px solid #004d40; object-fit: cover;'>
        <h1>Welcome to Daniel's Grand Hotel</h1>
        <p>Expert ICT Services & Premium Hospitality in Ethiopia</p>
        <div style='margin-top: 30px;'>
            <a href='/register' style='background:#ffcc00; color:black; padding:15px 40px; text-decoration:none; border-radius:30px; font-weight:bold;'>GET STARTED</a>
        </div>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = f"""
    <div style='padding: 30px;'>
        <h2>Luxury Rooms</h2>
        <div style='background:white; max-width:500px; margin:auto; border-radius:15px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.1);'>
            <img src='{room_vip}' style='width:100%; height:300px; object-fit:cover;'>
            <div style='padding:20px;'><h3>VIP Suite</h3><p>Price: $200/night</p></div>
        </div>
    </div>
    """
    return layout(content, "Hotel Rooms")

@app.route('/menu')
def menu():
    content = f"""
    <div style='padding: 30px;'>
        <h2>Special Menu</h2>
        <div style='background:white; max-width:500px; margin:auto; border-radius:15px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.1);'>
            <img src='{food_kitfo}' style='width:100%; height:300px; object-fit:cover;'>
            <div style='padding:20px;'><h3>Traditional Ethiopian Kitfo</h3></div>
        </div>
    </div>
    """
    return layout(content, "Restaurant Menu")

@app.route('/register')
def register():
    # ማሳሰቢያ፡ በፎቶ 1000012768 ያገኘኸውን ያንተን ሊንክ እዚህ ጋር ተክቼዋለሁ
    content = """
    <div style='padding: 20px;'>
        <div style='background:white; max-width:400px; margin:auto; padding:30px; border-radius:20px; box-shadow:0 10px 20px rgba(0,0,0,0.1); text-align:left;'>
            <h2 style='text-align:center;'>Register Now</h2>
            <form action="https://formspree.io/f/mqkazpjd" method="POST">
                <label>Full Name:</label>
                <input type='text' name='name' style='width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;' required>
                <label>Phone Number:</label>
                <input type='tel' name='phone' style='width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;' required>
                <label>Service:</label>
                <select name='service' style='width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;'>
                    <option>Room Booking</option>
                    <option>Food Order</option>
                </select>
                <button type='submit' style='width:100%; background:#004d40; color:white; padding:15px; border:none; border-radius:8px; font-weight:bold; cursor:pointer; margin-top:10px;'>SEND TO DANIEL</button>
            </form>
        </div>
    </div>
    """
    return layout(content, "Guest Registration")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
