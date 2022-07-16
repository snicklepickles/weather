from flask import Flask

app = Flask('weather-app')

@app.route('/')
def index():
   return 'Hello World!'

app.run()
