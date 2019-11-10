from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/restaurants', methods=['POST'])
def restaurants():
    URL = 'https://api.yelp.com/v3/businesses/search'
    api_key = 'hzaOAgO2PdMwrhhHpDkAV5OaI-OcSfxci56eLfJ_8NB9u-fVqu8TSRgod-J51yqIdXrfEIbqQGzBouc_y_z_71BHnLweMBEDGIiAUZ7UrXa4sZsk145FB0U0t-oAWXYx'
    private_key = 'Bearer %s' % api_key
    HEADERS = {'Authorization': private_key}
    LOCATION = request.form['zip']
    RADIUS = 1000
    PARAMS = {'location': LOCATION, 'radius': RADIUS}
    r = requests.get(url = URL, headers = HEADERS, params = PARAMS)
    data = r.json()
    businesses = data['businesses']
    return render_template('restaurants.html', temp= businesses)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
