from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
    
    return f"""
    <body style='background-color: #f9f9f9; color: #333; text-align: center; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0;'>
        
        <div style='background-color: #004d40; color: white; padding: 40px 20px;'>
            <h1 style='margin: 0; font-size: 36px;'>🏨 Daniel's Grand Hotel</h1>
            <p style='font-size: 18px;'>Experience Luxury, Comfort & Delicious Cuisine</p>
        </div>

        <div style='padding: 40px; background: white;'>
            <img src='{my_photo}' style='width: 150px; height: 150px; border-radius: 50%; border: 5px solid #004d40; object-fit: cover;'>
            <h2>Daniel Mulugeta</h2>
            <p style='font-style: italic; color: #666;'> "Welcome to my hotel, where we treat you like royalty." </p>
        </div>

        <div style='background: #e0f2f1; padding: 40px 20px;'>
            <h2 style='color: #004d40;'>🛏️ Our Luxury Rooms (አልጋዎች)</h2>
            <div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;'>
                <div style='background: white; padding: 20px; border-radius: 10px; width: 250px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                    <h3>VIP Suite</h3>
                    <p>King-size bed, City view, Free WiFi & Jacuzzi.</p>
                    <p style='font-weight: bold; color: #004d40;'>Price: $200/night</p>
                </div>
                <div style='background: white; padding: 20px; border-radius: 10px; width: 250px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                    <h3>Family Room</h3>
                    <p>Two double beds, perfect for 4 people.</p>
                    <p style='font-weight: bold; color: #004d40;'>Price: $150/night</p>
                </div>
            </div>
        </div>

        <div style='padding: 40px 20px;'>
            <h2 style='color: #d32f2f;'>🍕 Our Special Menu (ምግቦች)</h2>
            <div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;'>
                <div style='background: white; border-left: 5px solid #d32f2f; padding: 15px; width: 200px; text-align: left;'>
                    <h4>Traditional Kitfo</h4>
                    <p>Served with Kocho & Cheese.</p>
                </div>
                <div style='background: white; border-left: 5px solid #d32f2f; padding: 15px; width: 200px; text-align: left;'>
                    <h4>Special Pizza</h4>
                    <p>Cheesy Pepperoni & Veggies.</p>
                </div>
                <div style='background: white; border-left: 5px solid #d32f2f; padding: 15px; width: 200px; text-align: left;'>
                    <h4>Fresh Juice</h4>
                    <p>Avocado, Mango & Papaya.</p>
                </div>
            </div>
        </div>

        <footer style='background: #333; color: white; padding: 30px;'>
            <p>📍 Located at: Addis Ababa, Ethiopia</p>
            <p>📞 Call us: +251 9XX XXX XXX</p>
            <button style='background: #ffcc00; border: none; padding: 10px 20px; font-weight: bold; border-radius: 5px; cursor: pointer;'>Book Now</button>
        </footer>
    </body>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
