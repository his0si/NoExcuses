class ResponseQualityChecker:
    def evaluate_response(self, response, context):
        score = 0
        
        # 1. 문법적 완성도 체크
        if self.check_grammar(response):
            score += 0.3
            
        # 2. 컨텍스트 관련성 체크
        relevance = self.calculate_relevance(response, context)
        score += relevance * 0.4
        
        # 3. 응답의 구체성 체크
        specificity = self.check_specificity(response)
        score += specificity * 0.3
        
        return score