from flask import Flask, render_template, request,send_from_directory,redirect,url_for
import smtplib



OWN_EMAIL = "ahmed.fawzy.a2020a@gmail.com"
TO = "ahmed.fawzy.akf@gmail.com"
OWN_PASSWORD = "zlabwxvpegwimzuy"


app = Flask(__name__)


def send_email(name, email,  message,subject):
    email_message = f"Subject:{name} Sent New Message From Your Websie - {subject}\n\nName: {name}\nEmail:  {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL,TO, email_message)


@app.route("/", methods=["GET", "POST"])



def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"],  data["message"],data["subject"])
        return redirect(url_for("contact"))

    return render_template("index.html")


    










@app.route('/download')
def download():
    return send_from_directory('static', path="files/Ahmed Fawzy - Resume.pdf")





if __name__ == "__main__":
    app.run(debug=True)



