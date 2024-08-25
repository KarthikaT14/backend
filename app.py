from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    
    # Extract numbers and alphabets
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]

    # Find the highest lowercase alphabet
    lowercase_alphabets = [x for x in alphabets if x.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

    # Example static user information
    user_info = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
    }
    
    return jsonify(user_info)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
