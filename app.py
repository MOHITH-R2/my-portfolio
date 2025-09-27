from flask import Flask, request, render_template, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    file_exists = os.path.isfile('messages.csv')
    with open('messages.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name','Email','Message'])
        writer.writerow([name, email, message])

    flash('Message sent successfully!')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
