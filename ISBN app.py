from flask import Flask, request, jsonify

app = Flask(__name__)

def is_valid_isbn10(isbn):
    # Remove hyphens and spaces
    isbn = isbn.replace("-", "").replace(" ", "")

    # Must be 10 characters
    if len(isbn) != 10:
        return False

    total = 0

    for i in range(10):
        char = isbn[i]

        if char == 'X':
            if i != 9:  # X only allowed as check digit
                return False
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False

        total += (i + 1) * value

    return total % 11 == 0


@app.route('/check_isbn10', methods=['GET'])
def check_isbn10():
    isbn = request.args.get('isbn', '')

    if not isbn:
        return jsonify({"error": "Please provide an ISBN"}), 400

    valid = is_valid_isbn10(isbn)

    return jsonify({
        "isbn": isbn,
        "valid": valid
    })


if __name__ == '__main__':
    app.run(debug=True)