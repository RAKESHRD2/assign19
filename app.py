from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/tweets', methods=['POST'])
def create_tweet():
    data = request.get_json()

    if 'text' not in data:
        return jsonify({'error': 'Missing text field'}), 400

    tweet_text = data['text']


    return jsonify({'message': 'Tweet created successfully', 'text': tweet_text}), 201

if __name__ == '__main__':
    app.run(debug=True)

