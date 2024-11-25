from flask import Flask, request, jsonify
from flask_cors import CORS
from chat_model import ChatModel

app = Flask(__name__)
CORS(app)

# ChatModel 인스턴스 생성
try:
    chat_model = ChatModel()
    print("ChatModel 초기화 성공!")
except Exception as e:
    print(f"ChatModel 초기화 실패: {str(e)}")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        print(f"받은 메시지: {message}")  # 디버깅용
        
        # ChatModel을 사용하여 응답 생성
        response = chat_model.get_response(message)
        print(f"생성된 응답: {response}")  # 디버깅용
        
        return jsonify({"response": response})
    except Exception as e:
        print(f"오류 발생: {str(e)}")  # 디버깅용
        return jsonify({"response": f"오류가 발생했습니다: {str(e)}"})

@app.route('/')
def home():
    return jsonify({"message": "서버가 정상적으로 실행 중입니다."})

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify
from chat_model import ChatModel
from rl_agent import RLChatbot

app = Flask(__name__)
chat_model = ChatModel()
rl_agent = RLChatbot(chat_model)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['message']
    conversation_history = data.get('history', '')
    
    # RL 에이전트를 통해 응답 생성
    response, temperature = rl_agent.generate_response(user_input, conversation_history)
    
    # 사용자 피드백이 있는 경우 학습
    if 'feedback' in data:
        reward = float(data['feedback'])
        rl_agent.train_step(conversation_history + user_input + response, reward)
    
    return jsonify({
        'response': response,
        'temperature': temperature
    })

if __name__ == '__main__':
    app.run(debug=True)