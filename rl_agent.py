import numpy as np
from transformers import AutoTokenizer
import torch
import torch.nn as nn
import torch.optim as optim

class RLChatbot:
    def __init__(self, chat_model):
        self.chat_model = chat_model
        self.tokenizer = AutoTokenizer.from_pretrained("klue/bert-base")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # 정책 네트워크 (temperature를 조절하는 네트워크)
        self.policy_network = nn.Sequential(
            nn.Linear(768, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Sigmoid()
        ).to(self.device)
        
        self.optimizer = optim.Adam(self.policy_network.parameters(), lr=0.001)
        self.gamma = 0.99  # 할인 계수
        
    def encode_text(self, text):
        # 텍스트를 임베딩으로 변환
        tokens = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        return tokens['input_ids'].to(self.device)
    
    def get_temperature(self, state):
        # 상태를 기반으로 temperature 값을 예측
        with torch.no_grad():
            temp = self.policy_network(state)
        return temp.item()
    
    def train_step(self, conversation_history, reward):
        # 대화 기록을 상태로 변환
        state = self.encode_text(conversation_history)
        
        # 정책 네트워크 업데이트
        temperature = self.policy_network(state)
        loss = -torch.log(temperature) * reward  # 정책 그래디언트
        
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        return loss.item()
    
    def generate_response(self, user_input, conversation_history=""):
        # 상태를 인코딩
        state = self.encode_text(conversation_history + user_input)
        
        # temperature 예측
        temperature = self.get_temperature(state)
        
        # 챗봇 응답 생성
        response = self.chat_model.get_response(user_input, temperature=temperature)
        
        return response, temperature
