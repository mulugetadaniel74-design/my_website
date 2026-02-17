
import random
from flask import Flask

app = Flask(__name__)

@app.route('/spin')
def spin_game():
    items = ["🔔", "🍒", "💎", "7️⃣", "🍀"]
    # 3 ምስሎችን በድንገት ይመርጣል
    slot1 = random.choice(items)
    slot2 = random.choice(items)
    slot3 = random.choice(items)
    
    result = "እንደገና ይሞክሩ!"
    color = "red"
    
    if slot1 == slot2 == slot3:
        result = "እንኳን ደስ አለዎት! አሸንፈዋል!"
        color = "gold"
        
    return f"""
    <div style="text-align:center; padding:50px; font-family:sans-serif; background:#111; color:white; height:100vh;">
        <h1>🎰 Daniel's Lucky Spin 🎰</h1>
        <div style="font-size:80px; margin:30px; background:#222; padding:20px; border-radius:20px; border:4px solid gold;">
            {slot1} | {slot2} | {slot3}
        </div>
        <h2 style="color:{color};">{result}</h2>
        <br>
        <a href="/spin" style="background:gold; color:black; padding:20px 40px; border-radius:50px; text-decoration:none; font-weight:bold; font-size:24px;">SPIN AGAIN</a>
        <br><br>
        <a href="/" style="color:white;">ወደ መነሻ ገጽ ተመለስ</a>
    </div>
    """
