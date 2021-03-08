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
	params = request.args
	recipes = []
	response = requests.get('https://api.spoonacular.com/recipes/random?apiKey=' + API_KEY +'&number=1').json()

	for i in response:
		items = {}
		for j in response[i]:
			recipes.append(j)

	#print(recipes[0]['analyzedInstructions'])
	print(recipes[0]['spoonacularSourceUrl'])
	#<h4>{{ recipe['analyzedInstructions'][0]['steps'][recipe]['number'] }}:</h4> 
	return render_template('recipe_post.html',  
		recipe_title=recipes[0]['title'], 		
		recipes=recipes, 						
		steps=recipes[0]['analyzedInstructions'][0]['steps'],
		ingredients=recipes[0]['extendedIngredients'],
		recipe_image=recipes[0]['image'],
		recipe_base=recipes[0]
	)


@app.route('/contact', methods=['GET'])
def contact():
	return render_template('contact.html')

#@app.route('/<name>')
#def hello_name(name):
#    return "Hello {}!".format(name)

@app.route('/api/random', methods=['GET'])
def get_random():
	params = request.args
	recipes = []
	#items = []
	response = requests.get('https://api.spoonacular.com/recipes/random?apiKey=' + API_KEY +'&number=1').json()

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
	return render_template('list.html', ecipe_title=recipes[0]['title'], 		
		recipes=recipes, 						
		steps=recipes[0]['analyzedInstructions'][0]['steps'],
		ingredients=recipes[0]['extendedIngredients'])

if __name__ == '__main__':
    app.run()