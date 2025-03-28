from flask import Flask, request, jsonify, send_from_directory, render_template
import sqlite3
import os

app = Flask(__name__)

# Инициализация базы данных
def init_db():
    if not os.path.exists('feedback.db'):
        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE feedback (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, message TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        name = request.form['name']
        message = request.form['message']

        if not name or not message:
            return jsonify({'message': 'Пожалуйста, заполните все поля.'}), 400

        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()
        c.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Отзыв успешно отправлен!'}), 200
    except Exception as e:
        return jsonify({'message': 'Ошибка: ' + str(e)}), 500

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/healthz')
def healthz():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True)