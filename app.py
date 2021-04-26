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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
