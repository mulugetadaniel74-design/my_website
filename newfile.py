from flask import Flask, request

app = Flask(__name__)

# ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room_img = "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=600"
food_img = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600"

def layout(content, title="Daniel's Hotel"):
    return f"""
    <body style='margin:0; font-family: sans-serif; background: #f0f2f5; text-align: center;'>
        <div style='background: #004d40; color: white; padding: 15px; position: sticky; top: 0; z-index: 100;'>
            <h2 style='margin:0;'>🏨 {title}</h2>
            <nav style='margin-top:10px;'>
                <a href='/' style='color:white; margin:10px; text-decoration:none;'>Home</a> | 
                <a href='/rooms' style='color:white; margin:10px; text-decoration:none;'>Rooms</a> | 
                <a href='/menu' style='color:white; margin:10px; text-decoration:none;'>Menu</a> |
                <a href='/register' style='color:#ffcc00; margin:10px; text-decoration:none;'>Register Now</a>
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
        <img src='{my_photo}' style='width: 150px; height: 150px; border-radius: 50%; border: 4px solid #004d40; object-fit: cover;'>
        <h1>Welcome to Daniel's Grand Hotel</h1>
        <div style='margin-top: 30px;'>
            <a href='/register' style='background:#ffcc00; color:black; padding:15px 40px; text-decoration:none; border-radius:30px; font-weight:bold;'>GET STARTED</a>
        </div>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = f"<div style='padding:20px;'><h2>Our Rooms</h2><img src='{room_img}' style='width:90%; max-width:500px; border-radius:15px;'><p>VIP Suite - $200</p></div>"
    return layout(content)

@app.route('/menu')
def menu():
    content = f"<div style='padding:20px;'><h2>Our Menu</h2><img src='{food_img}' style='width:90%; max-width:500px; border-radius:15px;'><p>Traditional Kitfo</p></div>"
    return layout(content)

@app.route('/register')
def register():
    content = f"""
    <div style='padding: 20px;'>
        <div style='background:white; max-width:450px; margin:auto; padding:30px; border-radius:20px; box-shadow:0 10px 20px rgba(0,0,0,0.1);'>
            <h2>Choose Your Service</h2>
            
            <div style='display:flex; align-items:center; gap:10px; background:#f9f9f9; padding:10px; border-radius:10px; margin-bottom:15px;'>
                <img src='{room_img}' style='width:80px; height:60px; border-radius:5px; object-fit:cover;'>
                <p style='margin:0; font-weight:bold;'>Luxury Room Selection</p>
            </div>

            <form action='/confirm' method='POST' style='text-align:left;'>
                <label>Full Name</label>
                <input type='text' name='name' style='width:100%; padding:10px; margin:10px 0;' required>
                
                <label>Select Your Room</label>
                <select name='service' style='width:100%; padding:10px; margin:10px 0;'>
                    <option>VIP Suite ($200)</option>
                    <option>Family Room ($150)</option>
                    <option>Traditional Kitfo Order</option>
                </select>
                
                <button type='submit' style='width:100%; background:#004d40; color:white; padding:15px; border:none; border-radius:8px; font-weight:bold;'>CONFIRM NOW</button>
            </form>
        </div>
    </div>
    """
    return layout(content, "Registration")

@app.route('/confirm', methods=['POST'])
def confirm():
    name = request.form.get('name')
    service = request.form.get('service')
    return layout(f"<div style='padding:50px;'><h1>✅ Done!</h1><p>{name}, you chose {service}.</p></div>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
