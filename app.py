from flask import Flask, render_template, request
from weather import get_lat_long, get_current_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city_name')
        state = request.form.get('state_name')
        country = request.form.get('country_name')
        lat, lon = get_lat_long(city, state, country)
        if lat and lon:
            weather_data = get_current_weather(lat, lon)
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
