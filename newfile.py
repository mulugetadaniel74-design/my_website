
from flask import Flask

app = Flask(__name__)

# ምስሎች (Image Links)
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room1 = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800"
hotel_view = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=800"

def layout(content, title="Daniel's Grand Hotel"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <style>
            :root {{ --bg: #f0f2f5; --text: #333; --card: white; --header: #004d40; }}
            .dark-mode {{ --bg: #1a1a1a; --text: #f0f0f0; --card: #2d2d2d; --header: #002d26; }}
            
            body {{ margin:0; font-family: 'Segoe UI', sans-serif; background: var(--bg); color: var(--text); text-align: center; transition: 0.5s; }}
            .header {{ background: var(--header); color: white; padding: 15px; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.3); }}
            nav a {{ color:white; margin:0 7px; text-decoration:none; font-weight:bold; font-size: 13px; }}
            .card {{ background: var(--card); max-width:600px; margin: 20px auto; border-radius:20px; padding: 25px; box-shadow:0 10px 30px rgba(0,0,0,0.1); }}
            .btn {{ background: linear-gradient(45deg, #ffcc00, #ff9900); color:black; padding:15px 30px; text-decoration:none; border-radius:30px; font-weight:bold; display: inline-block; cursor:pointer; border:none; transition: 0.3s; }}
            .btn:hover {{ transform: scale(1.05); }}
            .floating-tg {{ position: fixed; bottom: 80px; right: 20px; background: #0088cc; color: white; padding: 15px; border-radius: 50%; text-decoration: none; box-shadow: 0 4px 15px rgba(0,0,0,0.3); z-index: 1001; }}
            .call-btn {{ background: #28a745; color: white; padding: 12px 20px; border-radius: 30px; text-decoration: none; font-weight: bold; position: fixed; bottom: 20px; right: 20px; z-index: 1001; }}
            footer {{ background: #1a1a1a; color: white; padding: 40px; margin-top: 50px; border-radius: 30px 30px 0 0; }}
            .stars {{ color: #ffcc00; font-size: 24px; margin: 10px 0; }}
        </style>
    </head>
    <body class="">
        <div style="background: #ffcc00; color: #000; font-weight: bold; padding: 8px;">
            <marquee>🔥 Daniel ICT: ማንኛውንም አይነት ዌብሳይት በታላቅ ቅናሽ እናሰራለን! በ 0986980130 ይደውሉ 🔥</marquee>
        </div>

        <div class="header">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 10px;">
                <button onclick="toggleMode()" style="background:none; border:1px solid white; color:white; border-radius:15px; cursor:pointer;">🌓 Mode</button>
                <div id="clock" style="font-size: 14px; letter-spacing: 1px;"></div>
            </div>
            <h2 style='margin:10px 0;'>🏨 {title}</h2>
            <nav>
                <a href='/'>HOME</a> | <a href='/rooms'>ROOMS</a> | <a href='/gallery'>GALLERY</a> | <a href='/register' style='color:#ffcc00;'>REGISTER</a>
            </nav>
        </div>
        
        <a href="https://t.me/Godis1256" class="floating-tg">💬</a>
        <a href="tel:0986980130" class="call-btn">📞 Call Now</a>

        {content}
        
        <footer>
            <h3>የክፍያ መረጃ (Secure Payment)</h3>
            <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:15px; text-align:left; display:inline-block;">
                <p>📱 <b>Telebirr:</b> 0986980130</p>
                <p>🏦 <b>Bank of Abyssinia:</b> 153682704</p>
                <p>👤 <b>Account:</b> Daniel Mulugeta</p>
            </div>
            <div style="margin-top:30px;">
                <p>Follow Us:</p>
                <a href="https://www.tiktok.com/@musicstudio438" style="color:white; margin:10px;">TikTok</a> | 
                <a href="https://t.me/Godis1256" style="color:white; margin:10px;">Telegram</a>
            </div>
            <p style="margin-top:20px; color: #666; font-size: 12px;">Developed by Daniel Mulugeta ICT © 2026</p>
        </footer>

        <script>
            function toggleMode() {{ document.body.classList.toggle('dark-mode'); }}
            function updateClock() {{
                const now = new Date();
                document.getElementById('clock').innerText = now.toLocaleTimeString();
            }}
            setInterval(updateClock, 1000);
            function fireConfetti() {{
                confetti({{ particleCount: 150, spread: 70, origin: {{ y: 0.6 }} }});
                alert("ተመዝግበዋል! በቅርቡ እናገኝዎታለን::");
            }}
        </script>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = f"""
    <div style='padding: 40px 20px;'>
        <img src='{my_photo}' style='width: 150px; height: 150px; border-radius: 50%; border: 5px solid #ffcc00; box-shadow: 0 0 20px rgba(255,204,0,0.4);'>
        <h1>Daniel's Grand Hotel</h1>
        <div class="stars">★★★★★</div>
        <p>እንኳን ወደ ኢትዮጵያ ምርጡ ሆቴል በሰላም መጡ::</p>
        
        <div class="card">
            <img src="{hotel_view}" style="width:100%; border-radius:15px; margin-bottom:15px;">
            <h3>የተሟላ አገልግሎት</h3>
            <p>ምቹ ክፍሎች፣ ጣፋጭ ምግቦች እና ፈጣን ኢንተርኔት በሆቴላችን ያገኛሉ::</p>
            <button class="btn" onclick="location.href='/register'">አሁኑኑ ቦታ ይያዙ</button>
        </div>
    </div>
    """
    return layout(content)

@app.route('/register')
def register():
    content = """
    <div class='card'>
        <h2>የእንግዳ ምዝገባ ቅጽ</h2>
        <p>መረጃዎን ሲልኩ አስደሳች ስጦታ ይጠብቅዎታል!</p>
        <div style="text-align:left; padding:10px;">
            <label>ሙሉ ስም</label>
            <input type='text' style='width:100%; padding:12px; margin:10px 0; border-radius:10px; border:1px solid #ccc;'>
            <label>ስልክ ቁጥር</label>
            <input type='tel' style='width:100%; padding:12px; margin:10px 0; border-radius:10px; border:1px solid #ccc;'>
        </div>
        <button class='btn' onclick='fireConfetti()'>መረጃውን ላክ (Submit)</button>
    </div>
    """
    return layout(content, "Register")

@app.route('/rooms')
def rooms():
    content = f"""
    <div class='card' style='padding:0; overflow:hidden;'>
        <img src='{room1}' style='width:100%;'>
        <div style='padding:20px;'>
            <h3>የቪአይፒ ክፍል (VIP Room)</h3>
            <p>ዋጋ በሌሊት: 5,000 ብር</p>
            <button class='btn' onclick="location.href='/register'">አሁን እዘዝ</button>
        </div>
    </div>
    """
    return layout(content, "Rooms")

@app.route('/gallery')
def gallery():
    return layout("<h2>Gallery - በቅርቡ አዳዲስ ፎቶዎች ይገባሉ!</h2>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
