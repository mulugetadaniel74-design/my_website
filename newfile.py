
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # ያንተ የፎቶ ሊንክ ከ GitHub
    my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
    
    return f"""
    <body style='background-color: #f4f4f4; color: #333; text-align: center; font-family: Arial, sans-serif; margin: 0; padding: 0;'>
        <div style='background-color: #004d40; color: white; padding: 20px;'>
            <h1 style='margin: 0;'>🏨 Daniel's Luxury Hotel & Hospital</h1>
            <p>Quality Care & Comfort in One Place</p>
        </div>

        <div style='display: flex; justify-content: center; gap: 20px; padding: 30px; flex-wrap: wrap;'>
            
            <div style='background: white; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); width: 300px; padding: 20px;'>
                <img src='{my_photo}' style='width: 100%; border-radius: 10px; border: 3px solid #004d40;'>
                <h3 style='margin-top: 15px;'>Daniel Mulugeta</h3>
                <p style='color: #004d40; font-weight: bold;'>Founder & CEO</p>
                <p>Welcome to our world-class luxury hotel and medical center.</p>
                <button style='background: #004d40; color: white; border: none; padding: 10px; width: 100%; border-radius: 5px; cursor: pointer;'>Learn More</button>
            </div>

            <div style='background: white; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); width: 300px; padding: 20px;'>
                <img src='https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=400' style='width: 100%; border-radius: 5px;'>
                <h3>Modern Hospital</h3>
                <p>24/7 Professional medical care for your family.</p>
                <button style='background: #d32f2f; color: white; border: none; padding: 10px; width: 100%; border-radius: 5px; cursor: pointer;'>Contact Doctor</button>
            </div>

        </div>

        <footer style='background: #333; color: white; padding: 20px; margin-top: 20px;'>
            <p>Contact: +251 9XX XXX XXX | Email: mulugetadaniel74@gmail.com</p>
            <p style='font-size: 12px; color: #aaa;'>© 2026 Daniel Mulugeta. All Rights Reserved.</p>
        </footer>
    </body>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
