from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/news/')
def news():

    context = [
        {'name': 'Интернет-магазин и одежда' },
        {'description':
             'Впервые с октября 2023 года в интернет-магазине "Corratec" появятся '
             'болоневые штаны и утепленные толстовки с меховым подкладом изнутри, благодаря чему '
             'в суровые морозы при длительном нахождении на улице будет тепло.'
         },
        {'date': '23-11-2023',
         }
    ]
    return render_template('news.html', news=context)



if __name__ == '__main__':
    app.run()
