from flask import Flask, request

app = Flask(__name__)

# ምስሎች (Images)
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room_vip = "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=600"
room_family = "https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=600"
food_kitfo = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600"
food_pizza = "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600"

def layout(content, title="Daniel's Hotel"):
    return f"""
    <body style='margin:0; font-family: sans-serif; background: #f4f4f4; text-align: center;'>
        <div style='background: #004d40; color: white; padding: 15px; position: sticky; top: 0; z-index: 100;'>
            <h2 style='margin:0;'>🏨 {title}</h2>
            <nav style='margin-top:10px;'>
                <a href='/' style='color:white; margin:10px; text-decoration:none; font-weight:bold;'>Home</a> | 
                <a href='/rooms' style='color:white; margin:10px; text-decoration:none; font-weight:bold;'>Rooms</a> | 
                <a href='/menu' style='color:white; margin:10px; text-decoration:none; font-weight:bold;'>Menu</a> |
                <a href='/register' style='color:#ffcc00; margin:10px; text-decoration:none; font-weight:bold;'>Register</a>
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
    <div style='padding: 60px 20px;'>
        <img src='{my_photo}' style='width: 150px; height: 150px; border-radius: 50%; border: 5px solid #004d40; object-fit: cover;'>
        <h1>Welcome to Daniel's Grand Hotel</h1>
        <p>Expert ICT Services & Premium Hospitality</p>
        <div style='margin-top: 30px;'>
            <a href='/register' style='background:#ffcc00; color:black; padding:15px 40px; text-decoration:none; border-radius:30px; font-weight:bold;'>GET STARTED</a>
        </div>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = f"""
    <div style='padding: 20px;'>
        <h2>Luxury Rooms Gallery</h2>
        <div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;'>
            <div style='background:white; width:280px; border-radius:15px; overflow:hidden; box-shadow:0 4px 8px rgba(0,0,0,0.1);'>
                <img src='{room_vip}' style='width:100%; height:200px; object-fit:cover;'>
                <div style='padding:15px;'><h3>VIP Suite</h3><p>$200/night</p></div>
            </div>
            <div style='background:white; width:280px; border-radius:15px; overflow:hidden; box-shadow:0 4px 8px rgba(0,0,0,0.1);'>
                <img src='{room_family}' style='width:100%; height:200px; object-fit:cover;'>
                <div style='padding:15px;'><h3>Family Room</h3><p>$150/night</p></div>
            </div>
        </div>
    </div>
    """
    return layout(content, "Our Rooms")

@app.route('/menu')
def menu():
    content = f"""
    <div style='padding: 20px;'>
        <h2>Our Delicious Menu</h2>
        <div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;'>
            <div style='background:white; width:280px; border-radius:15px; overflow:hidden; box-shadow:0 4px 8px rgba(0,0,0,0.1);'>
                <img src='{food_kitfo}' style='width:100%; height:200px; object-fit:cover;'>
                <div style='padding:15px;'><h3>Traditional Kitfo</h3></div>
            </div>
            <div style='background:white; width:280px; border-radius:15px; overflow:hidden; box-shadow:0 4px 8px rgba(0,0,0,0.1);'>
                <img src='{food_pizza}' style='width:100%; height:200px; object-fit:cover;'>
                <div style='padding:15px;'><h3>Special Pizza</h3></div>
            </div>
        </div>
    </div>
    """
    return layout(content, "Our Menu")

@app.route('/register')
def register():
    content = """
    <div style='padding: 20px;'>
        <div style='background:white; max-width:400px; margin:auto; padding:30px; border-radius:20px; box-shadow:0 10px 20px rgba(0,0,0,0.1);'>
            <h2>Guest Registration</h2>
            <form action='/confirm' method='POST' style='text-align:left;'>
                <label>Name:</label><input type='text' name='name' style='width:100%; padding:10px; margin:10px 0;' required>
                <label>Phone:</label><input type='tel' name='phone' style='width:100%; padding:10px; margin:10px 0;' required>
                <label>Service:</label>
                <select name='service' style='width:100%; padding:10px; margin:10px 0;'>
                    <option>VIP Suite Booking</option>
                    <option>Food Delivery</option>
                </select>
                <button type='submit' style='width:100%; background:#004d40; color:white; padding:15px; border:none; border-radius:8px; font-weight:bold;'>SUBMIT</button>
            </form>
        </div>
    </div>
    """
    return layout(content, "Register Now")

@app.route('/confirm', methods=['POST'])
def confirm():
    name = request.form.get('name')
    return layout(f"<div style='padding:50px;'><h1>✅ Done!</h1><p>Thank you {name}, we received your request.</p></div>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
