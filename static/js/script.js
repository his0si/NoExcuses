function displayMessage(message, sender) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value.trim();
    
    if (message === '') return;

    // 사용자 메시지 표시
    displayMessage(message, 'user');

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // 봇 응답 표시
        displayMessage(data.response, 'bot');
    })
    .catch(error => {
        console.error('Error:', error);
        displayMessage('오류가 발생했습니다.', 'bot');
    });

    messageInput.value = '';
}

// Enter 키로도 메시지 전송
document.getElementById('messageInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});