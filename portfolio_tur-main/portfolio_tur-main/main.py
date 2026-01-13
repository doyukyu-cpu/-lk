# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


@app.route("https://discord.com/oauth2/authorize?client_id=1435295627696410724")
def function_name():
   

if __name__ == "__main__":
    app.run(debug=True)
