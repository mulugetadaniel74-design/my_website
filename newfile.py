from flask import Flask
import datetime

app = Flask(__name__)

# ምስሎች (Images)
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
hotel_view = "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200"
room_img = "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800"

def layout(content, title="Daniel's Luxury Hub"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            :root {{ --main: #004d40; --accent: #ffcc00; --bg: #f4f7f6; }}
            body {{ margin:0; font-family: 'Poppins', sans-serif; background: var(--bg); text-align: center; }}
            .header {{ background: var(--main); color: white; padding: 15px; position: sticky; top: 0; z-index: 1000; }}
            .marquee {{ background: var(--accent); color: black; font-weight: bold; padding: 5px; }}
            .hero-img {{ width: 100%; height: 250px; object-fit: cover; border-radius: 0 0 30px 30px; }}
            .card {{ background: white; max-width: 600px; margin: 20px auto; border-radius: 20px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
            .btn {{ background: var(--accent); color: black; padding: 15px 30px; border-radius: 30px; text-decoration: none; font-weight: bold; border: none; cursor: pointer; display: inline-block; }}
            .call-now {{ position: fixed; bottom: 20px; right: 20px; background: #28a745; color: white; padding: 12px 25px; border-radius: 30px; text-decoration: none; font-weight: bold; z-index: 1001; }}
            footer {{ background: #1a1a1a; color: white; padding: 40px 20px; margin-top: 50px; border-radius: 30px 30px 0 0; }}
        </style>
    </head>
    <body>
        <div style="background:#111; color:white; font-size:12px; padding:5px;">
            <span id="liveClock"></span> | ☀️ አዲስ አበባ: 22°C
        </div>
        <div class="marquee"><marquee>🔥 Daniel ICT: ማንኛውንም አይነት ዌብሳይት በታላቅ ቅናሽ እናሰራለን! በ 0986980130 ይደውሉ 🔥</marquee></div>
        
        <div class="header">
            <h3 style="margin:0;">🏨 DANIEL LUXURY HOTEL</h3>
        </div>

        <a href="tel:0986980130" class="call-now">📞 አሁኑኑ ይደውሉ</a>

        {content}

        <footer>
            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; text-align: left; margin-bottom: 20px;">
                <h4 style="margin:0; color:var(--accent);">💰 የክፍያ መረጃ</h4>
                <p>ቴሌብር: 0986980130</p>
                <p>አቢሲኒያ: 153682704 (ዳንኤል ሙሉጌታ)</p>
            </div>
            <p>👥 የጎብኝዎች ብዛት: 1,432</p>
            <p style="font-size: 11px; color:#888;">Designed by Daniel Mulugeta ICT © 2026</p>
        </footer>

        <script>
            function updateClock() {{ document.getElementById('liveClock').innerText = new Date().toLocaleTimeString(); }}
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
    <img src="{hotel_view}" class="hero-img">
    <div style="padding: 20px;">
        <img src="{my_photo}" style="width:120px; height:120px; border-radius:50%; border:5px solid var(--accent); margin-top:-80px; position:relative; box-shadow: 0 5px 15px rgba(0,0,0,0.3);">
        <h1>Daniel's Grand Hotel</h1>
        <div style="color:var(--accent); margin-bottom:10px;">★★★★★</div>
        <p>እንኳን ወደ ኢትዮጵያ ምርጡ እና ዘመናዊው ሆቴል በሰላም መጡ!</p>
        
        <div class="card">
            <img src="{room_img}" style="width:100%; border-radius:15px; margin-bottom:15px;">
            <h3>የቪአይፒ ክፍሎች</h3>
            <p>ምቾትና ውበት የተላበሱ ክፍሎቻችንን አሁኑኑ ይዘዙ::</p>
            <button class="btn" onclick="location.href='/register'">አሁኑኑ ቦታ ይያዙ</button>
        </div>
    </div>
    """
    return layout(content)

@app.route('/register')
def register():
    content = """
    <div class="card">
        <h2>የእንግዳ ምዝገባ</h2>
        <input type="text" placeholder="ሙሉ ስም" style="width:95%; padding:15px; margin:10px 0; border-radius:10px; border:1px solid #ccc;">
        <input type="tel" placeholder="ስልክ ቁጥር" style="width:95%; padding:15px; margin:10px 0; border-radius:10px; border:1px solid #ccc;">
        <button class="btn" style="width:100%;" onclick="fireConfetti()">መረጃውን ላክ</button>
        <p><a href="/" style="color:blue;">ወደ መነሻ ገጽ ተመለስ</a></p>
    </div>
    """
    return layout(content, "Register Now")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
