import React, { useState, useRef, useEffect } from 'react';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const chatMessagesRef = useRef(null);

  useEffect(() => {
    // 새 메시지가 추가될 때마다 스크롤을 아래로 이동
    if (chatMessagesRef.current) {
      chatMessagesRef.current.scrollTop = chatMessagesRef.current.scrollHeight;
    }
  }, [messages]);

  const displayMessage = (message, sender) => {
    setMessages(prev => [...prev, { text: message, sender }]);
  };

  const handleSendMessage = async () => {
    const message = inputMessage.trim();
    if (message === '') return;

    // 사용자 메시지 표시
    displayMessage(message, 'user');
    setInputMessage('');

    try {
      const response = await fetch('/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      // 봇 응답 표시
      displayMessage(data.response, 'bot');
    } catch (error) {
      console.error('Error:', error);
      displayMessage('오류가 발생했습니다.', 'bot');
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>Chat bot</h2>
      </div>
      <div className="chat-messages" ref={chatMessagesRef}>
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}-message`}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="chat-input">
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type Message"
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chat;