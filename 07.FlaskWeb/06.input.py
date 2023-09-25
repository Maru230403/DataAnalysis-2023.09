from flask import Flask, render_template, request

app = Flask(__name__)          

@app.route('/')                 # localhost:5000/   을 서비스하기 위한 코드                 
def index():                    
    return '''<h1>입력값 받기</h1>
            <button onclick="location.href='/calc'">셀렉트(calc 사례)</button>
            <button onclick="location.href='/lang'">라디오 및 체크박스(lang, food 사례)</button>
    '''

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'GET':
        op_list = ['+', '-', '*', '/', '//', '%', '**']
        return render_template('06.calc_form.html', op_list=op_list)
    else:
        num1 = int(request.form['num1'])
        op = request.form['op']
        num2 = int(request.form['num2'])
        result = eval(f'{num1}{op}{num2}')        # eval() : ()안의 식의 답을 리턴해줌
        return f'''
            <h2>{num1} {op} {num2} = {result}</h2>
            <button onclick="location.href='/calc'">재실행</button>
        '''

@app.route('/lang', methods=['GET', 'POST'])
def lang():
    lang_dict = {'en':'영어','fr':'프랑스어','es':'스페인어', 'jp':'일본어','cn':'중국어'}
    food_list = ['삼겹살', '갈비탕', '불고기', '피자', '햄버거']
    if request.method == 'GET':
        return render_template('06.lang_food.html', lang_dict=lang_dict, food_list=food_list)
    else:
        language = request.form['language']
        foods = request.form.getlist('food')    
        # getlist('food')를 쓰면 값이 불러와짐, 위의 방식으로 쓰면 체크하지않거나 
        # 여러값이 올 때 값을 불러오지 못함?
        selected_foods = []
        for food_index in foods:
            selected_foods.append(food_list[(int(food_index))])

        return f'''
                <h2>선택한 언어: {lang_dict[language]}</h2>
                <h2>선택한 음식: {selected_foods}</h2>
                <button onclick="location.href='/lang'">재실행</button>
                '''


if __name__ == '__main__':
    app.run(debug=True)