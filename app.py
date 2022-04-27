from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message
from config import email,senha

app = Flask(__name__)
app.secret_key = 'vitorborqge'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

app.config.update(mail_settings)
mail =Mail(app)

class Contato:
    def __init__(self, name, email, subject, message):
        self.nome = name,
        self.email = email,
        self.subject = subject,
        self.mensagem = message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["name"],
            request.form["email"],
            request.form["subject"],
            request.form["mensagem"]
        )
        msg = Message(
             subject = f'{formContato.name} te enviou uma mensagem no portfolio',
             sender = app.config.get("MAIL_USERNAME"),
             recipients = ['vitorborgesvieira02@gmail.com', app.config.get("MAIL_USERNAME")],
             body = f'''
     
             {formContato.name} te enviou uma mensagem no portfolio, com o assunto {formContato.subject}, o email dele é {formContato.email} com a mensagem:
     
             {formContato.mensagem}

             '''
        )
        mail.send(msg)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
