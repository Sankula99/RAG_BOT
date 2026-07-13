// Chat interface component
import React, { useState } from 'react';
import SourceCitation from './SourceCitation';
const ChatInterface: React.FC = () => {
    const [messages, setMessages] = useState<{ text: string; sources?: { source: string; title: string; url: string }[] }[]>([]);
    const [input, setInput] = useState('');
    const handleSend = async () => {
        if (!input.trim()) return;
        const userMessage = { text: input };
        setMessages((prev) => [...prev, userMessage]);
        setInput('');
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',

                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: input }),
            });
            if (!response.ok) {
                throw new Error('Chat API error');
            }
            const data = await response.json();
            const botMessage = { text: data.reply, sources: data.sources };
            setMessages((prev) => [...prev, botMessage]);
        } catch (error) {
            console.error('Error sending message:', error);
        }
    };
    return (
        <div style={{ padding: '20px' }}>
            <h2>Chat Interface</h2>
            <div style={{ marginBottom: '20px' }}>
                {messages.map((msg, index) => (
                    <div key={index} style={{ marginBottom: '10px' }}>
                        <p>{msg.text}</p>
                        {msg.sources && msg.sources.length > 0 && (
                            <div style={{ marginLeft: '20px' }}>
                                <h4>Sources:</h4>
                                {msg.sources.map((source, idx) => (
                                    <SourceCitation key={idx} source={source.source} title={source.title} url={source.url} />
                                ))}
                            </div>
                        )}  
                    </div>
                ))}
            </div>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                placeholder="Type your message..."
                style={{ width: '80%', padding: '10px' }}
            />
            <button onClick={handleSend} style={{ padding: '10px', marginLeft: '10px' }}>
                Send
            </button>
</div>
     );
}

export default ChatInterface;