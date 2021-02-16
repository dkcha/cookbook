from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os, requests, json


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
API_KEY = 'df65b5e6b04543ed9b6dcb739521e1cc'

from models import Recipe


@app.route('/')
def init():
	return redirect('/index')

@app.route('/index')
def index():
	data = db.session.query(Recipe).all()
	print(type(data))
	print(data)
	for i in data:
		print(i.name)
	return render_template('index.html')
	#return render_template('list.html', title='RecipeList', first_name1=data[0].id, last_name1=data[0].name)
	#return "Hello World!"

@app.route('/recipe_post', methods=['GET'])
def recipe_post():
	print('what do u mean')
	return render_template('recipe_post.html')


#@app.route('/<name>')
#def hello_name(name):
#    return "Hello {}!".format(name)

@app.route('/api/random', methods=['GET'])
def get_random():
	params = request.args
	recipes = []
	#items = []
	response = requests.get('https://api.spoonacular.com/recipes/random?apiKey=' + API_KEY +'&number=2').json()

	#print(response)

	for i in response:
		#print(response[i])
		items = {}
		#print(i)
		for j in response[i]:
			#print(j)

			recipes.append(j)
			#print(j)
			#for k in j:
			#	print('k: ' + k)
			#	print('j[k]: ' + str(j[k]))
			#print(response[i][j])
		#print(i + ' and its value: ' + response[i])
	#print(response.json())
#print(type(response))
	#print(response['recipes'])
	#print(response['recipes'][0])#['title'])
	#for i in response['recipes']:
	#	print(i)
	#print(items)
	#for i in items:
	#	print(i + ': ' + str(items[i]))
	#print(type(items))

	#for i in items:
	#	print(items['spoonacularSourceUrl'])
	print(recipes)
	return render_template('list.html', title='RecipeList', recipes=recipes)

if __name__ == '__main__':
    app.run()