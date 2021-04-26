from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', upto = 300)


@app.route('/hello', methods=['GET'])
def hello():
    return '<h1>Hello</h1>'


@app.route('/calc', methods=['GET'])
def calc():
    x = int(request.args.get('upto'))
    # Размер последовательности
    razmer = x
    # Заполняем массив 
    mas = [[i,0] for i in range(razmer+1)]
    # Запуск алгоритма
    for i in range(2, int(razmer/2)):
        for j in range(2*i, razmer+1, i):
            mas[j][1] = 1
    # Результат
    res = []
    for i in mas:
        if i[1] == 0:  res.append(str(i[0]))
    return '; '.join(res)


@app.route('/encrypt', methods=['GET'])
def encrypt():
    thetext = request.args.get('theText')
    thekey = request.args.get('theKey')
    # Check input values
    if len(thetext) < 1:
        return 'Не задан исходный текст'
    if len(thekey) < 1:
        return 'Не задан ключ шифрования'
    thekey = int(thekey)
    if thekey < -32 or thekey > 32:
        return 'Неверное значение ключа'
    # Values OK
    alpb1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alpb2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ext = 0
    if thekey < 0: ext = 33
    res = ''
    for ltr in thetext:
        enc = ''
        i1 = alpb1.find(ltr)
        i2 = alpb2.find(ltr)
        if i1 >= 0:
            enc = alpb1[i1 + ext + thekey]
        elif i2 >= 0:
            enc = alpb2[i2 + ext + thekey]
        else:
            enc = ' '
        res += enc
    return '<p>Результат:</p><b>' + res + '</b>'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
