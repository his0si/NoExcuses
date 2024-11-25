class ConversationAnalyzer:
    def analyze_conversation(self, conversation_history):
        reward = 0
        
        # 1. 대화 흐름 분석
        if self.is_coherent_conversation(conversation_history):
            reward += 0.4
            
        # 2. 사용자 참여도 분석
        engagement = self.calculate_user_engagement(conversation_history)
        reward += engagement * 0.3
        
        # 3. 목표 달성 여부 분석
        if self.check_goal_completion(conversation_history):
            reward += 0.3
            
        return reward