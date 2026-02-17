@app.route('/')
def home():
    return """
    <html>
    <body style="text-align:center; font-family:sans-serif; background:#f4f4f4; padding:50px;">
        <h1 style="color:#1a237e;">Daniel Supreme Hotel</h1>
        <p>ዌብሳይቱ በተሳካ ሁኔታ ሰርቷል!</p>
        <div style="background:white; padding:20px; border-radius:15px; display:inline-block; box-shadow:0 5px 15px rgba(0,0,0,0.1);">
            <p>📱 Telebirr: 0986980130</p>
            <p>🏦 Abyssinia: 153682704</p>
            <button onclick="alert('እንኳን ደህና መጡ!')" style="background:#ffd700; border:none; padding:10px 20px; border-radius:20px; font-weight:bold; cursor:pointer;">BOOK NOW</button>
        </div>
        <p style="margin-top:20px;">ዲዛይነር፡ ዳንኤል ሙሉጌታ</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
