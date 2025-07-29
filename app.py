from flask import Flask, render_template, request
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_data = None
    if request.method == 'POST':
        date = request.form.get('date')       # YYYY-MM-DD
        time = request.form.get('time')       # HH:MM
        timezone = request.form.get('timezone', '+00:00')  # e.g. +10:00
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')

        try:
            dt = Datetime(date, time, timezone)
            pos = GeoPos(latitude, longitude)
            chart = Chart(dt, pos)
            chart_data = {
                'Sun': chart.get('Sun').sign,
                'Moon': chart.get('Moon').sign,
                'Mercury': chart.get('Mercury').sign,
                'Venus': chart.get('Venus').sign,
                'Mars': chart.get('Mars').sign,
                'Jupiter': chart.get('Jupiter').sign,
                'Saturn': chart.get('Saturn').sign,
                'Uranus': chart.get('Uranus').sign,
                'Neptune': chart.get('Neptune').sign,
                'Pluto': chart.get('Pluto').sign,
            }
        except Exception as e:
            chart_data = {'error': str(e)}

    return render_template('index.html', chart=chart_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
