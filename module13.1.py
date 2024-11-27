from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/Mod_13_1/<int:number>', methods=['GET'])
def check_prime(number):
    result = is_prime(number)
    return jsonify({"Number": number, "isPrime": result})

if __name__ == '__main__':
    app.run(debug=True)