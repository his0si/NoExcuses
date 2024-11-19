from flask import Flask, request, jsonify, render_template
from chat_model import ChatModel
import logging

app = Flask(__name__)
# 로깅 설정 추가
logging.basicConfig(level=logging.DEBUG)

try:
    chat_model = ChatModel()
    logging.info("ChatModel successfully initialized")
except Exception as e:
    logging.error(f"Failed to initialize ChatModel: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message')
        logging.info(f"Received message: {message}")
        
        response = chat_model.get_response(message)
        logging.info(f"Bot response: {response}")
        
        return jsonify({'response': response})
    except Exception as e:
        logging.error(f"Error in chat route: {str(e)}")
        return jsonify({'response': '오류가 발생했습니다.'}), 500

if __name__ == '__main__':
    app.run(debug=True)