from flask import Flask

app = Flask(__name__)

# ፎቶህ
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"

# የጋራ Header እና Footer
def layout(content):
    return f"""
    <body style='background-color: #f9f9f9; color: #333; text-align: center; font-family: sans-serif; margin: 0; padding: 0;'>
        <div style='background-color: #004d40; color: white; padding: 20px;'>
            <h1 style='margin: 0;'><a href='/' style='color: white; text-decoration: none;'>🏨 Daniel's Grand Hotel</a></h1>
        </div>
        {content}
        <footer style='background: #333; color: white; padding: 20px; margin-top: 50px;'>
            <p>📞 0986980130 | <a href='https://t.me/Godis1256' style='color: #0088cc;'>Telegram</a></p>
            <p><a href='/' style='color: #ffcc00;'>Back to Home</a></p>
        </footer>
    </body>
    """

@app.route('/')
def home():
    content = f"""
    <div style='padding: 40px;'>
        <img src='{my_photo}' style='width: 150px; border-radius: 50%; border: 4px solid #004d40;'>
        <h2>Welcome to Daniel's Grand Hotel</h2>
        <p>Expert ICT Services & Luxury Hospitality</p>
        <hr style='width: 50%; margin: 20px auto;'>
        <div style='margin-top: 20px;'>
            <a href='/rooms' style='display: inline-block; background: #004d40; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin: 10px; font-weight: bold;'>View Our Rooms (አልጋዎች)</a>
            <br>
            <a href='/menu' style='display: inline-block; background: #d32f2f; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin: 10px; font-weight: bold;'>View Our Menu (ምግቦች)</a>
        </div>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = """
    <div style='padding: 30px;'>
        <h2 style='color: #004d40;'>🛏️ Our Luxury Rooms</h2>
        <div style='background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 400px; margin: 20px auto;'>
            <h3>VIP Suite</h3>
            <p>King-size bed, Jacuzzi, and City View.</p>
            <p style='font-weight: bold; color: #004d40;'>Price: $200/night</p>
        </div>
        <div style='background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 400px; margin: 20px auto;'>
            <h3>Family Room</h3>
            <p>Two double beds for 4 people.</p>
            <p style='font-weight: bold; color: #004d40;'>Price: $150/night</p>
        </div>
    </div>
    """
    return layout(content)

@app.route('/menu')
def menu():
    content = """
    <div style='padding: 30px;'>
        <h2 style='color: #d32f2f;'>🍕 Our Special Menu</h2>
        <ul style='list-style: none; padding: 0; font-size: 20px;'>
            <li style='padding: 10px;'>🔥 Traditional Kitfo</li>
            <li style='padding: 10px;'>🍕 Special Pizza</li>
            <li style='padding: 10px;'>🍹 Fresh Juice</li>
        </ul>
    </div>
    """
    return layout(content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
