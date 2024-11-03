import React, { useState, useEffect, useRef } from 'react';
import './ChatRoom.css';

const ChatRoom = () => {
    const [messages, setMessages] = useState([]);
    const [inputMessage, setInputMessage] = useState('');
    const [websocket, setWebsocket] = useState(null);
    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }

    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8080/chat');
        
        ws.onopen = () => {
            console.log('Connected to WebSocket');
        };

        ws.onmessage = (event) => {
            // Only handle received messages (not our own)
            setMessages(prev => [...prev, {
                text: event.data,
                type: 'received'
            }]);
        };

        ws.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        ws.onclose = () => {
            console.log('Disconnected from WebSocket');
        };

        setWebsocket(ws);

        return () => {
            ws.close();
        };
    }, []);

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const sendMessage = (e) => {
        e.preventDefault();
        if (inputMessage.trim() && websocket) {
            // First add the message to our local state
            setMessages(prev => [...prev, {
                text: inputMessage,
                type: 'sent'
            }]);
            
            // Then send it through WebSocket
            websocket.send(inputMessage);
            
            setInputMessage('');
        }
    };

    return (
        <div className="chat-container">
            <div className="chat-header">
                <h2>Chat Room</h2>
            </div>
            
            <div className="chat-messages">
                {messages.map((message, index) => (
                    <div 
                        key={index} 
                        className={`message ${message.type}`}
                    >
                        {message.text}
                    </div>
                ))}
                <div ref={messagesEndRef} />
            </div>
            
            <form onSubmit={sendMessage} className="chat-input-container">
                <input
                    type="text"
                    value={inputMessage}
                    onChange={(e) => setInputMessage(e.target.value)}
                    placeholder="Type a message..."
                    className="chat-input"
                />
                <button type="submit" className="send-button">
                    Send
                </button>
            </form>
        </div>
    );
};

export default ChatRoom;