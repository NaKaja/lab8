import os
import random
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

dog_folder = 'static/dogs'
cat_folder = 'static/cats'
bunny_folder = 'static/bunnies'

def get_random_image(folder):
    images = [f for f in os.listdir(folder) if f.endswith(('.gif', '.webp'))]
    return random.choice(images)

@app.route('/')
def index():
    return redirect(url_for(random.choice(['dog', 'cat', 'bunny'])))

@app.route('/dog')
def dog():
    random_dog_path = 'dogs/' + get_random_image(dog_folder)
    return render_template('index.html', path=random_dog_path)

@app.route('/cat')
def cat():
    random_cat_path = 'cats/' + get_random_image(cat_folder)
    return render_template('index.html', path=random_cat_path)
    
@app.route('/bunny')
def bunny():
    random_bunny_path = 'bunnies/' + get_random_image(bunny_folder)
    return render_template('index.html', path=random_bunny_path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')