from flask import Flask

app = Flask(__name__)

# ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room1 = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800"

def layout(content, title="Daniel's Grand Hotel"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            :root {{ --bg: #f0f2f5; --text: #333; --card: white; --header: #004d40; }}
            .dark-mode {{ --bg: #1a1a1a; --text: #f0f0f0; --card: #2d2d2d; --header: #002d26; }}
            
            body {{ margin:0; font-family: 'Segoe UI', sans-serif; background: var(--bg); color: var(--text); text-align: center; transition: 0.5s; }}
            .header {{ background: var(--header); color: white; padding: 15px; position: sticky; top: 0; z-index: 1000; }}
            nav a {{ color:white; margin:0 7px; text-decoration:none; font-weight:bold; font-size: 12px; }}
            .card {{ background: var(--card); max-width:600px; margin: 20px auto; border-radius:15px; padding: 20px; box-shadow:0 4px 15px rgba(0,0,0,0.1); }}
            .btn {{ background:#ffcc00; color:black; padding:12px 25px; text-decoration:none; border-radius:25px; font-weight:bold; display: inline-block; cursor:pointer; border:none; }}
            .call-btn {{ background: #28a745; color: white; padding: 10px 20px; border-radius: 20px; text-decoration: none; font-weight: bold; position: fixed; bottom: 20px; left: 20px; z-index: 1001; }}
            .mode-toggle {{ background: #444; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer; font-size: 10px; }}
            footer {{ background: #263238; color: white; padding: 30px; margin-top: 40px; }}
            .marquee {{ background: #ffcc00; color: #000; font-weight: bold; padding: 5px; }}
        </style>
    </head>
    <body>
        <div class="marquee"><marquee>ማስታወቂያ፦ ለማንኛውም ዌብሳይት ስራ በ 0986980130 ይደውሉልን! (Daniel ICT)</marquee></div>
        <div class="header">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 10px;">
                <button class="mode-toggle" onclick="toggleMode()">🌓 Mode</button>
                <div id="clock" style="font-size: 12px; font-weight: bold;"></div>
            </div>
            <h2 style='margin:10px 0;'>🏨 {title}</h2>
            <nav>
                <a href='/'>HOME</a> | <a href='/rooms'>ROOMS</a> | <a href='/menu'>MENU</a> | <a href='/register' style='color:#ffcc00;'>REGISTER</a>
            </nav>
        </div>
        
        <a href="tel:0986980130" class="call-btn" onclick="playClick()">📞 ደውል</a>

        {content}
        
        <footer>
            <h3>የክፍያ አማራጮች</h3>
            <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:10px; text-align:left;">
                <p>📱 <b>Telebirr:</b> 0986980130</p>
                <p>🏦 <b>Abyssinia:</b> 153682704 (ዳንኤል ሙሉጌታ)</p>
            </div>
            <p style="margin-top:20px; font-size: 11px;">© 2026 Daniel Mulugeta ICT</p>
        </footer>

        <script>
            function toggleMode() {{ document.body.classList.toggle('dark-mode'); }}
            function updateClock() {{
                const now = new Date();
                document.getElementById('clock').innerText = now.toLocaleTimeString();
            }}
            setInterval(updateClock, 1000);
            function playClick() {{
                let audio = new Audio('https://www.soundjay.com/buttons/button-16.mp3');
                audio.play();
            }}
        </script>
    </body>
    </html>
    """

@app.route('/')
def home():
    content = f"""
    <div style='padding: 40px 20px;'>
        <img src='{my_photo}' style='width: 140px; height: 140px; border-radius: 50%; border: 4px solid white;'>
        <h1>Daniel's Grand Hotel</h1>
        <p>በኢትዮጵያ ቀዳሚው ዘመናዊ መስተንግዶ!</p>
        <div class="card">
            <h3>እንኳን ደህና መጡ</h3>
            <p>የእኛን ዌብሳይት ስለጎበኙ እናመሰግናለን::</p>
            <button class="btn" onclick="location.href='/register'; playClick()">ቦታ ይያዙ</button>
        </div>
    </div>
    """
    return layout(content)

@app.route('/menu')
def menu():
    content = """<div class='card'><h2>የምግብ ዝርዝር</h2><p>ክትፎ ..... 500 ብር</p><p>ጥብስ ..... 400 ብር</p></div>"""
    return layout(content, "Hotel Menu")

@app.route('/rooms')
def rooms():
    content = f"""<div class='card' style='padding:0;'><img src='{room1}' style='width:100%;'><h3>VIP Suite</h3><p>$200 / Night</p></div>"""
    return layout(content, "Rooms")

@app.route('/register')
def register():
    content = """<div class='card'><h2>ምዝገባ</h2><form><input type='text' placeholder='ስም' style='width:80%; padding:10px;'><br><br><button class='btn'>ላክ</button></form></div>"""
    return layout(content, "Register")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
