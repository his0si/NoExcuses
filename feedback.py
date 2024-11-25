class FeedbackSystem:
    def __init__(self):
        self.feedback_metrics = {
            'relevance': (0, 5),  # 응답의 관련성
            'helpfulness': (0, 5), # 응답의 유용성
            'clarity': (0, 5),     # 응답의 명확성
        }
    
    def calculate_reward(self, feedback_data):
        # 각 메트릭의 가중치 계산
        weights = {
            'relevance': 0.4,
            'helpfulness': 0.4,
            'clarity': 0.2
        }
        
        total_reward = 0
        for metric, weight in weights.items():
            if metric in feedback_data:
                score = feedback_data[metric]
                normalized_score = (score - self.feedback_metrics[metric][0]) / \
                                 (self.feedback_metrics[metric][1] - self.feedback_metrics[metric][0])
                total_reward += normalized_score * weight
        
        return total_reward

class ImplicitFeedbackSystem:
    def __init__(self):
        self.metrics = {}
    
    def calculate_implicit_reward(self, conversation_data):
        reward = 0
        
        # 1. 대화 지속성 체크
        if conversation_data.get('continued_conversation'):
            reward += 0.5
            
        # 2. 응답 시간 체크
        response_time = conversation_data.get('response_time', 0)
        if response_time < 5:  # 5초 이내 응답
            reward += 0.3
            
        # 3. 대화 길이 체크
        msg_length = len(conversation_data.get('message', ''))
        if 10 <= msg_length <= 200:  # 적절한 길이의 메시지
            reward += 0.2
            
        return reward