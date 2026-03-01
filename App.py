from flask import Flask, request, jsonify

app = Flask(__name__)

def ai_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! I'm your AI."
    elif "how are you" in user_input.lower():
        return "I'm functioning perfectly!"
    else:
        return "I am still learning."

@app.route("/")
def home():
    return "Your AI is running globally!"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = ai_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
