# Must run .\.env\Scripts\activate inside of the codezen folder
"""Import Flask from Flask Lib"""
from flask import Flask, render_template

app = Flask(__name__)

# Landing Page
@app.route('/')
def landing_page():
    """Return Landing Page"""
    return render_template('index.html')

# Featues Page
@app.route('/features')
def features_page():
    """Return Features Page"""
    return render_template('features.html')

# FAQ Page
@app.route('/faq')
def faq_page():
    """Return FAQ Page"""
    return render_template('faq.html')

# About Page
@app.route('/about')
def about_page():
    """Return About Page"""
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
