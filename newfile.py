from flask import Flask, request

app = Flask(__name__)

my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"

def layout(content, title="Daniel's Grand Hotel"):
    return f"""
    <body style='margin:0; font-family: sans-serif; background: #f4f4f4; text-align: center;'>
        <div style='background: #004d40; color: white; padding: 15px;'>
            <h2 style='margin:0;'>🏨 {title}</h2>
            <nav style='margin-top:10px;'>
                <a href='/' style='color:white; margin:10px; text-decoration:none;'>Home</a> | 
                <a href='/rooms' style='color:white; margin:10px; text-decoration:none;'>Rooms</a> | 
                <a href='/book' style='color:white; margin:10px; text-decoration:none;'>Book Now</a>
            </nav>
        </div>
        {content}
        <footer style='background: #333; color: white; padding: 20px; margin-top: 40px;'>
            <p>📞 Contact: 0986980130 | Telegram: @Godis1256</p>
        </footer>
    </body>
    """

@app.route('/')
def home():
    content = f"""
    <div style='padding: 40px;'>
        <img src='{my_photo}' style='width: 130px; border-radius: 50%; border: 4px solid #004d40;'>
        <h1>Welcome to Daniel's Grand Hotel</h1>
        <p>Expert ICT Services & Premium Hospitality</p>
        <div style='margin-top:20px;'>
            <a href='/rooms' style='background: #004d40; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px;'>View Rooms</a>
            <a href='/book' style='background: #ffcc00; color: black; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight:bold;'>Book Online</a>
        </div>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = """
    <div style='padding: 20px;'>
        <h2>Our Rooms</h2>
        <div style='background:white; margin:10px auto; padding:20px; max-width:400px; border-radius:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);'>
            <h3>VIP Suite - $200/night</h3>
            <p>Full ICT services included.</p>
            <a href='/book' style='color:#004d40; font-weight:bold;'>Select This Room</a>
        </div>
    </div>
    """
    return layout(content, "Hotel Rooms")

@app.route('/book')
def book():
    content = """
    <div style='padding: 30px; background: white; max-width: 400px; margin: 20px auto; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);'>
        <h2 style='color: #004d40;'>Booking Form</h2>
        <form action='/confirm' method='POST' style='text-align: left;'>
            <label>Full Name:</label><br>
            <input type='text' name='name' style='width:100%; padding:10px; margin:10px 0;' required><br>
            <label>Phone Number:</label><br>
            <input type='tel' name='phone' style='width:100%; padding:10px; margin:10px 0;' required><br>
            <label>Room Type:</label><br>
            <select name='room' style='width:100%; padding:10px; margin:10px 0;'>
                <option>VIP Suite</option>
                <option>Family Room</option>
                <option>Standard Room</option>
            </select><br><br>
            <button type='submit' style='width:100%; background:#004d40; color:white; padding:15px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;'>CONFIRM BOOKING</button>
        </form>
    </div>
    """
    return layout(content, "Book a Room")

@app.route('/confirm', methods=['POST'])
def confirm():
    name = request.form.get('name')
    room = request.form.get('room')
    content = f"""
    <div style='padding: 50px;'>
        <h2 style='color: green;'>✅ Booking Successful!</h2>
        <p>Thank you, <b>{name}</b>. We have reserved the <b>{room}</b> for you.</p>
        <p>Our team will call you shortly to confirm.</p>
        <a href='/' style='color: #004d40;'>Return Home</a>
    </div>
    """
    return layout(content, "Confirmation")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
