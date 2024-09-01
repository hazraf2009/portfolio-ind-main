#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<feedback {self.id}>'
    
#Halaman Konten Berjalan
@app.route('/')
def index():
    return render_template('index.html')


#Keterampilan Dinamis
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_db=button_db, button_html=button_html)

@app.route('/feedback', methods=['POST'])
def Feedback():
    email= request.form['email']
    text = request.form['text']

    #Tugas #3. Buat agar data pengguna direkam ke dalam database
    feed = feedback(email=email, text=text)
    db.session.add(feed)
    db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
