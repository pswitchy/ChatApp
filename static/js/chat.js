// static/js/chat.js
class ChatManager {
    constructor() {
        this.messageContainer = document.getElementById('messages-container');
        this.messageForm = document.getElementById('message-form');
        this.messageInput = document.getElementById('message-input');
        this.websocket = null;
        this.typing = false;
        this.typingTimeout = null;
        
        this.init();
    }

    init() {
        this.connectWebSocket();
        this.setupEventListeners();
        this.scrollToBottom();
    }

    connectWebSocket() {
        const roomName = document.getElementById('room-name').value;
        const wsScheme = window.location.protocol === "https:" ? "wss" : "ws";
        this.websocket = new WebSocket(
            `${wsScheme}://${window.location.host}/ws/chat/${roomName}/`
        );

        this.websocket.onmessage = (e) => this.handleMessage(e);
        this.websocket.onclose = () => this.handleWebSocketClose();
    }

    setupEventListeners() {
        this.messageForm.addEventListener('submit', (e) => this.handleSubmit(e));
        this.messageInput.addEventListener('input', () => this.handleTyping());
        
        // File upload
        document.getElementById('file-upload').addEventListener('change', (e) => 
            this.handleFileUpload(e)
        );
    }

    handleMessage(event) {
        const data = JSON.parse(event.data);
        this.appendMessage(data);
        this.scrollToBottom();
        
        if (!document.hasFocus()) {
            this.sendNotification(data.message, data.sender);
        }
    }

    appendMessage(data) {
        const messageHTML = this.createMessageElement(data);
        this.messageContainer.insertAdjacentHTML('beforeend', messageHTML);
    }

    scrollToBottom() {
        this.messageContainer.scrollTop = this.messageContainer.scrollHeight;
    }

    handleSubmit(event) {
        event.preventDefault();
        const message = this.messageInput.value.trim();
        if (message) {
            this.sendMessage(message);
            this.messageInput.value = '';
        }
    }

    sendMessage(message) {
        this.websocket.send(JSON.stringify({
            'message': message,
            'type': 'message'
        }));
    }

    handleTyping() {
        if (!this.typing) {
            this.typing = true;
            this.websocket.send(JSON.stringify({
                'type': 'typing',
                'typing': true
            }));
        }

        clearTimeout(this.typingTimeout);
        this.typingTimeout = setTimeout(() => {
            this.typing = false;
            this.websocket.send(JSON.stringify({
                'type': 'typing',
                'typing': false
            }));
        }, 1000);
    }

    handleWebSocketClose() {
        console.log('WebSocket connection closed');
        setTimeout(() => this.connectWebSocket(), 1000);
    }
}

// Initialize chat when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('messages-container')) {
        new ChatManager();
    }
});

// static/js/notifications.js
class NotificationManager {
    constructor() {
        this.permission = null;
        this.init();
    }

    init() {
        if ('Notification' in window) {
            this.requestPermission();
        }
    }

    async requestPermission() {
        try {
            this.permission = await Notification.requestPermission();
        } catch (error) {
            console.error('Error requesting notification permission:', error);
        }
    }

    sendNotification(title, options = {}) {
        if (this.permission === 'granted' && document.hidden) {
            const defaultOptions = {
                icon: '/static/images/favicon.ico',
                badge: '/static/images/favicon.ico',
                vibrate: [200, 100, 200],
                ...options
            };

            new Notification(title, defaultOptions);
        }
    }
}

// Initialize notifications
const notificationManager = new NotificationManager();