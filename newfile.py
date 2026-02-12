from flask import Flask, request

app = Flask(__name__)

# ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room_img = "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=600"
food_img = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600"

# የጋራ መዋቅር (Header & Navigation)
def layout(content, title="Daniel's Hotel"):
    return f"""
    <body style='margin:0; font-family: "Segoe UI", Tahoma, sans-serif; background: #f0f2f5; text-align: center;'>
        <div style='background: #004d40; color: white; padding: 15px; position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
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
            <p>📞 Contact: 0986980130 | Telegram: @Godis1256</p>
        </footer>
    </body>
    """

@app.route('/')
def home():
    content = f"""
    <div style='padding: 60px 20px;'>
        <img src='{my_photo}' style='width: 160px; height: 160px; border-radius: 50%; border: 5px solid #004d40; object-fit: cover; box-shadow: 0 4px 10px rgba(0,0,0,0.2);'>
        <h1>Welcome to Daniel's Grand Hotel</h1>
        <p style='font-size: 18px; color: #555; max-width: 700px; margin: 20px auto;'>The best ICT powered hospitality in Ethiopia. We offer luxury rooms and delicious meals.</p>
        <div style='margin-top: 30px;'>
            <a href='/register' style='background:#ffcc00; color:black; padding:15px 35px; text-decoration:none; border-radius:30px; font-weight:bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>GET STARTED</a>
        </div>
    </div>
    """
    return layout(content, "Home Page")

@app.route('/rooms')
def rooms():
    content = f"""
    <div style='padding: 30px;'>
        <h2 style='color: #004d40;'>🛏️ Our Luxury Rooms</h2>
        <div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 20px;'>
            <div style='background:white; width: 300px; border-radius:15px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.1);'>
                <img src='{room_img}' style='width:100%; height:200px; object-fit:cover;'>
                <div style='padding:15px;'><h3>VIP Suite</h3><p>$200/night</p><a href='/register' style='color:#004d40; font-weight:bold;'>Book Now</a></div>
            </div>
        </div>
    </div>
    """
    return layout(content, "Hotel Rooms")

@app.route('/menu')
def menu():
    content = f"""
    <div style='padding: 30px;'>
        <h2 style='color: #d32f2f;'>🍕 Our Special Menu</h2>
        <div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 20px;'>
            <div style='background:white; width: 300px; border-radius:15px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.1);'>
                <img src='{food_img}' style='width:100%; height:200px; object-fit:cover;'>
                <div style='padding:15px;'><h3>Traditional Kitfo</h3><p>Special Ethiopian Taste</p></div>
            </div>
        </div>
    </div>
    """
    return layout(content, "Restaurant Menu")

@app.route('/register')
def register():
    content = """
    <div style='padding: 40px;'>
        <div style='background:white; max-width:450px; margin:auto; padding:35px; border-radius:20px; box-shadow:0 15px 30px rgba(0,0,0,0.15);'>
            <h2 style='color:#004d40; margin-bottom: 25px;'>Guest Registration Form</h2>
            <form action='/confirm' method='POST' style='text-align:left;'>
                <label style='font-weight:bold;'>Full Name</label>
                <input type='text' name='name' placeholder='Enter your name' style='width:100%; padding:12px; margin:10px 0 20px 0; border:1px solid #ddd; border-radius:8px;' required>
                
                <label style='font-weight:bold;'>Phone Number</label>
                <input type='tel' name='phone' placeholder='09...' style='width:100%; padding:12px; margin:10px 0 20px 0; border:1px solid #ddd; border-radius:8px;' required>
                
                <label style='font-weight:bold;'>Service Type</label>
                <select name='service' style='width:100%; padding:12px; margin:10px 0 25px 0; border:1px solid #ddd; border-radius:8px;'>
                    <option>Room Booking (አልጋ ለመያዝ)</option>
                    <option>Food Order (ምግብ ለማዘዝ)</option>
                    <option>ICT Consultation</option>
                </select>
                
                <button type='submit' style='width:100%; background:#004d40; color:white; border:none; padding:15px; font-weight:bold; border-radius:8px; cursor:pointer; font-size:16px;'>SUBMIT REGISTRATION</button>
            </form>
        </div>
    </div>
    """
    return layout(content, "Registration")

@app.route('/confirm', methods=['POST'])
def confirm():
    name = request.form.get('name')
    service = request.form.get('service')
    content = f"""
    <div style='padding: 80px 20px;'>
        <div style='background:white; max-width:500px; margin:auto; padding:40px; border-radius:15px; border-top: 8px solid #004d40;'>
            <h1 style='color: #004d40;'>Success! ✅</h1>
            <p style='font-size: 18px;'>Thank you, <b>{name}</b>!</p>
            <p>Your request for <b>{service}</b> has been received.</p>
            <p>We will contact you shortly on your phone.</p>
            <br>
            <a href='/' style='color: #004d40; font-weight:bold; text-decoration:none;'>← Back to Home Page</a>
        </div>
    </div>
    """
    return layout(content, "Confirmation")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
