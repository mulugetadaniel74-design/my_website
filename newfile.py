import smtplib
from email.message import EmailMessage
from flask import Flask, request

# ... (ሌላው የቆየው ኮድህ እንዳለ ይሁንና /confirm የሚለውን ብቻ በዚህ ተካው)

@app.route('/confirm', methods=['POST'])
def confirm():
    name = request.form.get('name')
    phone = request.form.get('phone')
    service = request.form.get('service')

    # ኢሜይል ለመላክ የሚያገለግል መረጃ
    msg = EmailMessage()
    msg.set_content(f"አዲስ ደንበኛ ተመዝግቧል!\n\nስም: {name}\nስልክ: {phone}\nአገልግሎት: {service}")
    msg['Subject'] = 'አዲስ የሆቴል ምዝገባ ከዌብሳይትህ'
    msg['From'] = 'mulugetadaniel74@gmail.com'
    msg['To'] = 'mulugetadaniel74@gmail.com'

    # ማሳሰቢያ፡ ይህ ክፍል እንዲሰራ የ Gmail 'App Password' ያስፈልግሃል
    try:
        # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.login('mulugetadaniel74@gmail.com', 'የአንተ_ፓስወርድ')
        # server.send_message(msg)
        # server.quit()
        status = "Success! መረጃው ተልኳል።"
    except:
        status = "መረጃው ተመዝግቧል (ኢሜይል ለመላክ ተጨማሪ ሴቲንግ ያስፈልጋል)።"

    content = f"""
    <div style='padding: 50px;'>
        <h2 style='color: green;'>✅ ምዝገባው ተጠናቋል!</h2>
        <p>እናመሰግናለን <b>{name}</b>! መረጃህ ደርሶናል።</p>
        <p style='color: #666;'>{status}</p>
        <a href='/' style='color: #004d40; font-weight:bold;'>ወደ ዋናው ገጽ ተመለስ</a>
    </div>
    """
    return layout(content, "Confirmation")
    
