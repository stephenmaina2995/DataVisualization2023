from flask import Flask,render_template,jsonify,url_for,request,redirect
import json, random
# from werkzurg.utils import secure_filename
import io
import base64
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns

ALLOWED_EXTENSIONS = set(['csv'])

fig,ax=plt.subplots(figsize=(6,6))
ax=sns.set_style(style="darkgrid")

x=[i for i in range(100)]
y=[i for i in range(100)]

app = Flask(__name__)

data = pd.read_csv('CANISHackathon2023.csv', skiprows=1)

data.to_csv()

@app.route('/home')
def home():
    
    data = pd.read_csv('CANISHackathon2023.csv')
    
    return data.to_html()


if __name__ == '__main__':
    app.run(debug=True)