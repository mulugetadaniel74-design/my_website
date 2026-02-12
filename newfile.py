
from flask import Flask, request

app = Flask(__name__)

# ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room_img = "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=800"
food_img = "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800"

def layout(content, title="Daniel's Hotel"):
    return f"""
    <body style='margin:0; font-family: sans-serif; background: #f4f4f4; text-align: center;'>
        <div style='background: #004d40; color: white; padding: 15px; position: sticky; top: 0;'>
            <h2 style='margin:0;'>🏨 {title}</h2>
            <nav style='margin-top:10px;'>
                <a href='/' style='color:white; margin:10px; text-decoration:none;'>Home</a> | 
                <a href='/rooms' style='color:white; margin:10px; text-decoration:none;'>Rooms</a> | 
                <a href='/menu' style='color:white; margin:10px; text-decoration:none;'>Menu</a>
            </nav>
        </div>
        {content}
    </body>
    """

@app.route('/')
def home():
    content = f"""
    <div style='padding: 50px;'>
        <img src='{my_photo}' style='width: 150px; border-radius: 50%; border: 4px solid #004d40;'>
        <h1>Welcome to Daniel's Grand Hotel</h1>
        <div style='margin-top:20px;'>
            <a href='/register' style='background:#ffcc00; color:black; padding:15px 40px; text-decoration:none; border-radius:30px; font-weight:bold;'>GET STARTED</a>
        </div>
    </div>
    """
    return layout(content)

@app.route('/rooms')
def rooms():
    content = f"<div style='padding:30px;'><h2>Our Rooms</h2><img src='{room_img}' style='width:95%; max-width:500px; border-radius:15px;'><p>VIP Suite - $200</p></div>"
    return layout(content)

@app.route('/menu')
def menu():
    content = f"<div style='padding:30px;'><h2>Our Menu</h2><img src='{food_img}' style='width:95%; max-width:500px; border-radius:15px;'><p>Traditional Kitfo</p></div>"
    return layout(content)

@app.route('/register')
def register():
    # ማሳሰቢያ፡ 'YOUR_ID' በሚለው ቦታ Formspree ላይ የምታገኘውን ኮድ ታስገባለህ
    content = """
    <div style='padding: 20px;'>
        <div style='background:white; max-width:400px; margin:auto; padding:30px; border-radius:20px; box-shadow:0 10px 20px rgba(0,0,0,0.1);'>
            <h2>Guest Registration</h2>
            <p style='font-size:12px; color:red;'>መረጃው በቀጥታ ወደ ዳንኤል ኢሜይል ይላካል</p>
            <form action="https://formspree.io/f/mulugetadaniel74@gmail.com" method="POST">
                <label>Full Name:</label>
                <input type="text" name="name" style='width:100%; padding:10px; margin:10px 0;' required>
                <label>Email Address:</label>
                <input type="email" name="email" style='width:100%; padding:10px; margin:10px 0;' required>
                <label>Message:</label>
                <textarea name="message" style='width:100%; padding:10px; margin:10px 0;' placeholder="የፈለጉትን ክፍል ይጥቀሱ"></textarea>
                <button type="submit" style='width:100%; background:#004d40; color:white; padding:15px; border:none; border-radius:8px; font-weight:bold;'>SEND TO EMAIL</button>
            </form>
        </div>
    </div>
    """
    return layout(content, "Register Now")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
