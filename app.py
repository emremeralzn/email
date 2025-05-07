from flask import Flask, request, jsonify
from flask_cors import CORS
from email_dto import EmailDto
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)  # Tüm domainlere CORS izni verir

@app.route("/api/email", methods=["POST"])
def send_email():
    try:
        data = request.get_json()
        email_data = EmailDto(**data)

        # Mail ayarları
        msg = EmailMessage()
        msg["From"] = "pelinsy66@gmail.com"
        msg["To"] = "pelinsy66@gmail.com"
        msg["Subject"] = f"Blog Contact: {email_data.subject}"
        msg.set_content(f"Gönderen: {email_data.to}\n\nMesaj:\n{email_data.body}")

        # Gmail SMTP ile gönderim
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login("pelinsy66@gmail.com", "toaewuhwtouhhwbz")  # Gmail uygulama şifresi
            smtp.send_message(msg)

        return jsonify({"message": "Mail başarıyla gönderildi."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
