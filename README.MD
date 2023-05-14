## GPT-3 Chatbot  <br/>
This is a simple Flask app that uses OpenAI's GPT-3 API to create a chatbot that can generate responses to user input. The chatbot uses the Davinci engine and a temperature of 0.5 to generate responses.

## Setup
1. Clone this repository to your local machine.
2. Install the required dependencies by running pip install -r requirements.txt.
3. Set your OpenAI API key as an environment variable named OPENAI_API_KEY.
4. Start the Flask server by running python app.py.
## Usage
1. Visit http://localhost:5000 in your web browser.
2. Enter some text in the input box and click the "Send" button.
3. The chatbot will generate a response based on the input and display it on the page.
## Configuration
You can configure the chatbot by editing the generate_response() function in app.py. For example, you can change the engine, temperature, or maximum number of tokens used by the API. See the [OpenAI API documentation](https://platform.openai.com/docs/introduction) for more information.
