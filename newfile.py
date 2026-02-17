from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

# ምስሎች
my_photo = "https://github.com/mulugetadaniel74-design/my_website/blob/main/IMG_20250316_160655_800.jpg?raw=true"
room_vip = "https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=800"

def layout(content, title="Daniel's Ultimate"):
    return f"""
    <!DOCTYPE html>
    <html lang="am">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            :root {{ --primary: #1a237e; --gold: #ffd700; --white: #ffffff; --dark: #121212; }}
            body {{ margin:0; font-family: 'Segoe UI', sans-serif; transition: 0.5s; background: #f4f4f4; }}
            
            /* 1. Preloader */
            #loader {{ position: fixed; width: 100%; height: 100vh; background: white; z-index: 9999; display: flex; align-items: center; justify-content: center; }}
            .spinner {{ width: 50px; height: 50px; border: 5px solid #ddd; border-top: 5px solid var(--primary); border-radius: 50%; animation: spin 1s linear infinite; }}
            @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}

            .header {{ background: var(--primary); color: white; padding: 15px; text-align: center; position: sticky; top: 0; z-index: 100; }}
            .card {{ background: white; margin: 20px auto; max-width: 600px; padding: 25px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
            
            /* 3. Image Zoom */
            .zoom-img {{ transition: transform .3s; width: 100%; border-radius: 10px; cursor: pointer; }}
            .zoom-img:hover {{ transform: scale(1.05); }}

            .btn {{ background: var(--gold); border: none; padding: 12px 25px; border-radius: 25px; font-weight: bold; cursor: pointer; transition: 0.3s; }}
            .btn:hover {{ background: #e6c200; box-shadow: 0 5px 10px rgba(0,0,0,0.2); }}

            .footer {{ background: #212121; color: #aaa; padding: 40px 20px; text-align: center; border-radius: 40px 40px 0 0; }}
            
            /* Calculator Style */
            .calc-box {{ background: #e8eaf6; padding: 15px; border-radius: 10px; margin: 15px 0; }}
        </style>
    </head>
    <body onload="hideLoader()">
        <div id="loader"><div class="spinner"></div></div>

        <div class="header animate__animated animate__fadeInDown">
            <h2>🏨 DANIEL SUPREME</h2>
            <div style="font-size: 12px;">
                <span id="date"></span> | <span id="clock"></span>
            </div>
        </div>

        <div style="text-align: center; padding: 20px;">
            <div class="card animate__animated animate__zoomIn">
                <img src="{my_photo}" class="zoom-img" style="width:100px; height:100px; border-radius:50%; border:3px solid var(--gold);">
                <h3>እንኳን ደህና መጡ!</h3>
                <p>የቋንቋ ምርጫ (Language): <button onclick="alert('English is coming soon!')" class="btn" style="padding: 5px 10px; font-size: 10px;">EN</button></p>
            </div>

            <div class="card">
                <h3>💰 የዋጋ ማስያ (Estimator)</h3>
                <div class="calc-box">
                    <label>ስንት ሌሊት ይቆያሉ?</label><br>
                    <input type="number" id="nights" value="1" oninput="calcPrice()" style="width: 50px; padding: 5px;">
                    <p>ጠቅላላ ዋጋ: <b><span id="totalPrice">2500</span> ብር</b></p>
                </div>
            </div>

            <div class="card animate__animated animate__fadeInUp">
                <img src="{room_vip}" class="zoom-img">
                <h3>VIP Presidential Room</h3>
                <p>ባለ አምስት ኮከብ ምቾት</p>
                <button class="btn" onclick="shareSite()">🔗 ለጓደኛ ያጋሩ (Share)</button>
            </div>
        </div>

        <div class="footer">
            <div style="margin-bottom: 20px;">
                <a href="https://t.me/Godis1256" style="color:white; margin:15px; font-size:20px;"><i class="fab fa-telegram"></i></a>
                <a href="https://www.tiktok.com/@musicstudio438" style="color:white; margin:15px; font-size:20px;"><i class="fab fa-tiktok"></i></a>
                <a href="https://goo.gl/maps/example" style="color:white; margin:15px; font-size:20px;"><i class="fas fa-map-marker-alt"></i></a>
            </div>
            <p>💵 Telebirr: 0986980130 | 🏛️ Abyssinia: 153682704</p>
            <p style="font-size: 10px;">የዌብሳይቱ ዲዛይነር፡ ዳንኤል ሙሉጌታ (ICT)</p>
        </div>

        <script>
            function hideLoader() {{ document.getElementById('loader').style.display = 'none'; }}
            
            function updateClock() {{
                const now = new Date();
                document.getElementById('clock').innerText = now.toLocaleTimeString();
                document.getElementById('date').innerText = now.toDateString();
                
                // 6. Auto Night Mode (ከምሽቱ 12 ሰዓት በኋላ)
                if(now.getHours() >= 18 || now.getHours() <= 6) {{
                    document.body.style.background = "#121212";
                    document.body.style.color = "white";
                }}
            }}
            setInterval(updateClock, 1000);

            function calcPrice() {{
                let nights = document.getElementById('nights').value;
                document.getElementById('totalPrice').innerText = nights * 2500;
            }}

            function shareSite() {{
                if (navigator.share) {{
                    navigator.share({{ title: "Daniel Hotel", url: window.location.href }});
                }} else {{ alert("ሊንኩን ኮፒ አድርገው ይላኩ!"); }}
            }}
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
