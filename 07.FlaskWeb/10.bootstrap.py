from flask import Flask, render_template
import util.crawl_util as cu


app = Flask(__name__)

@app.route('/')     # localhost:5000/ 을 서비스하기 위한 코드
def index():
    return '<h1>부트스트랩</h1>'

@app.route('/list')
def list():
    return render_template('10.list.html')

@app.route('/form')
def form():
    return render_template('10.form.html')

@app.route('/modal')
def modal():
    return render_template('10.modal.html')

@app.route('/interpark')
def interpark():
    book_list = cu.get_bestseller()
    return render_template('interpark.html', book_list=book_list)

@app.route('/cctv')
def cctv():
    return render_template('10.cctv.html')

if __name__ == '__main__':
    app.run(debug=True)

