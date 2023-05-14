from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

openai.api_key = "Insert-your-openAI-API"

def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
  
    )

    return response.choices[0].text.strip()

@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    input_text = request.json["input_text"]
    response = generate_response(input_text)

    return jsonify({"response": response})


@app.route("/")
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run()
