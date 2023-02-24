from flask import Flask, request, render_template
import get_page_SourceCode

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    print("start")
    if request.method == 'POST': 
        count = request.form.get('count')
        get_page_SourceCode.start(int(count))
        return render_template('done.html')
    return render_template('index.html')


    

if __name__ =='__main__':  
    app.run(debug = True) 
