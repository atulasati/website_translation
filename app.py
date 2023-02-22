from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('translated_index.html')

@app.route('/translated_0/')
def translated_0():
    return render_template('translated_0.html')

@app.route('/translated_1/')
def translated_1():
    return render_template('translated_1.html')

@app.route('/translated_2/')
def translated_2():
    return render_template('translated_2.html')

@app.route('/translated_3/')
def translated_3():
    return render_template('translated_3.html')

@app.route('/translated_4/')
def translated_4():
    return render_template('translated_4.html')

    

if __name__ =='__main__':  
    app.run(debug = True) 
