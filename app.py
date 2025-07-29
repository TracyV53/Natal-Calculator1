from flask import Flask, render_template, request
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    location = request.form['location']
    
    dt = Datetime(date, time, '+00:00')  # You can improve timezone logic later
    pos = GeoPos('34.05', '-118.25')     # Example: Los Angeles (replace later with location logic)
    
    chart = Chart(dt, pos)
    sun = chart.get('SUN')
    moon = chart.get('MOON')
    
    return f"<h2>{name}'s Chart</h2><p>Sun: {sun.sign}</p><p>Moon: {moon.sign}</p>"
