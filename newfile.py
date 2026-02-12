from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <body style='background-color: #121212; color: white; text-align: center; font-family: Arial, sans-serif; padding: 20px;'>
        <div style='border: 2px solid #00ffcc; padding: 20px; border-radius: 15px; display: inline-block; max-width: 500px;'>
            <h1 style='color: #00ffcc;'>JOB OPPORTUNITY!</h1>
            <h2 style='color: #ffcc00;'>Position: Graphic Designer</h2>
            <p style='font-size: 18px;'>We are looking for a creative designer to join Daniel's team.</p>
            
            <div style='text-align: left; display: inline-block; margin-top: 10px;'>
                <p>✅ <b>Requirements:</b> Proficiency in Photoshop & Illustrator</p>
                <p>✅ <b>Experience:</b> 1+ Year</p>
                <p>✅ <b>Salary:</b> Negotiable</p>
            </div>
            
            <hr style='border: 0.5px solid #444; margin: 20px 0;'>
            <p>Interested? Send your CV to:</p>
            <a href='mailto:mulugetadaniel74@gmail.com' style='background-color: #00ffcc; color: black; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;'>APPLY NOW</a>
            <p style='margin-top: 20px; font-size: 12px; color: #888;'>Posted on Daniel Mulugeta's Official Website</p>
        </div>
    </body>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
