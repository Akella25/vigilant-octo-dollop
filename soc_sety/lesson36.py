# З використанням фрейморку Flask розробити проект соціальної мережі з наступним функціоналом:
# 1. На стартовій сторінці є форма реєстрації, яка містить три поля: email, password та nickname.
# При заповненні форми, після кліку на кнопку Submit створюється новий користувач.
# Дані про всіх коритувачів доадтково зберігаються у файлі data/users.json.
# При створенні нового користувача інформація про нього додається до цього файлу.
# Поле nickname може містити тільки букви і цифри, у іншому разі реєстарція не виконується і сервер повертає помилку з кодом 400.
# 2. Також на стартовій сторінці є посилання на сторінку /login, де існуючий користувач може увійти у свій акаунт,
# використовуючи email та password, які він вказав при реєстрації.
# Якщо користувача з таким мейлом не існує - сервер має перенаправляти користувача на стартову сторінку (сторінку реєстрації).
# Якщо користувач з таким мейлом є, але не підходить пароль - сервер має повертати відповідь зі статус кодом помилки 401.
# 3. Якщо користувач ввів правильні мейл та пароль - сервер перенаправляє його за адресою /{nickname}.
# Там користувач може переглянути інформацію про свій обліковий запис: email та nickname,
# а також додати зображення-аватар, вказавши URL на зовнішньому ресурсі. Також на цій сторінці має бути посилання на сторінку /{nickname}/posts.
# 4. На сторінці /{nickname}/posts є форма додавання новго посту з полями title та content.
# При кліку на кнопку Create новий пост має бути створено. Також на цій сторінці показуються всі існуючі пости користувача,
# відсортовані від найновіших до найстаріших. Усі пости користувача зберігаються у файлі data/<nickname>_posts.json.
# При створенні нового поста він також додається до цього файлу.
# 5. Має бути присутня сторінка /news, де будуть відображатися всі пости всіх користувачів, відсортовані від найновіших до найстаріших

from flask import Flask, request, render_template, redirect, abort, url_for
from PIL import Image
import requests
import os

from .users import User
from .utils import search_user

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nickname = request.form['nickname']
        password = int(request.form['password'])
        email = request.form['email']
        if nickname.isalpha():
            new_user = User(nickname=nickname, password=password, email=email)
        else:
            abort(404)
        new_user.dump_json()
    return render_template('index.html')





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = int(request.form['password'])
        for user in User.list_user:
            if email == user.email and password == user.password:
                return redirect(f'/{user.nickname}')
            elif email == user.email and password != user.password:
                return abort(401)
            elif email != user.email:
                return redirect(url_for('index'))
    return render_template('login.html', users=User.list_user)


@app.route('/<nickname>', methods=['GET', 'POST'])
def nickname(nickname):
    page_user = None
    for user in User.list_user:
        if nickname == user.nickname:
            page_user = user
        if request.method == 'POST':
            url = request.form['img']
            path = os.path.join(os.getcwd(), 'static', f'{nickname}.jpg')
            page_user.img = f'{nickname}.jpg'
            with Image.open(requests.get(url, stream=True).raw) as image:
                image.save(path)
        return render_template('user.html', user_email=user.email, user_nickname=user.nickname)
    # return render_template('user.html', user_img=page_user.img)


@app.route('/<nickname>/posts', methods=['GET', 'POST'])
def posts(nickname):
    user = search_user(User.list_user, nickname)
    # return render_template('posts.html', test=User.list_user)
    if request.method == 'POST':
        tetle = request.form['title']
        content = request.form['content']
        user.add_posts(tetle, content)
        user.posts[-1].add_json(nickname)
        user_post_sort = sorted(user.posts, reverse=True)
        # return render_template('posts.html', test=user.posts)
        if len(user_post_sort) > 0:
            return render_template('posts.html', test=user_post_sort)
            return render_template('posts.html', posts=user_post_sort)
        else:
            return render_template('posts.html')
    return render_template('posts.html')


@app.route('/news')
def news():
    list_news = []
    for user in User.list_user:
        for post in user.posts:
            list_news.append(post)
    list_news.sort(reverse=True)
    return render_template('news.html', news=list_news)


