from flask import Flask, request, jsonify
from flask_cors import CORS
from email_dto import EmailDto
import resend

app = Flask(__name__)
CORS(app)  # Tüm domainlere CORS izni verir

# Resend API key
RESEND_API_KEY = "YOUR RESEND API KEY"
resend.api_key = RESEND_API_KEY

@app.route("/api/email", methods=["POST"])
def send_email():
    try:
        data = request.get_json()
        email_data = EmailDto(**data)

        # Resend ile mail gönderimi
        params = {
            "from": "Acme <onboarding@resend.dev>",
            "to": "YOUR EMAIL ADDRESS",
            "subject": f"Blog Contact: {email_data.subject}",
            "text": f"Gönderen: {email_data.to}\n\nMesaj:\n{email_data.body}"
        }

        email = resend.Emails.send(params)

        return jsonify({"message": "Mail başarıyla gönderildi.", "id": email.get("id")}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
