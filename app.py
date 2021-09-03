from flask import Flask, jsonify
from flask import Flask, render_template

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello ศราวุฒิ อิ่มอุไร เลขที่7 ม.4/7"

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

@app.route(',/,')
def hi():
    return "สวัสดีค้าบบบ"    
        
if __name__ == "__main__":
    app.run(debug=False)
