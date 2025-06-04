import React, { useState, useEffect } from 'react';

function App() {
  const [username, setUsername] = useState('');
  const [userId, setUserId] = useState(null);
  const [answer, setAnswer] = useState('');
  const [messages, setMessages] = useState([]);
  const [chatInput, setChatInput] = useState('');

  const conversationId = userId; // simple placeholder

  useEffect(() => {
    if (conversationId) {
      fetch(`/conversations/${conversationId}`)
        .then(res => res.json())
        .then(data => setMessages(data));
    }
  }, [conversationId]);

  const register = async e => {
    e.preventDefault();
    const res = await fetch('/users/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username })
    });
    const data = await res.json();
    setUserId(data.id);
  };

  const submitQuestionnaire = async e => {
    e.preventDefault();
    await fetch('/questionnaires/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId, answer })
    });
    setAnswer('');
  };

  const sendMessage = async e => {
    e.preventDefault();
    await fetch('/messages/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: userId,
        conversation_id: conversationId,
        message: chatInput
      })
    });
    setChatInput('');
    // refresh messages
    const res = await fetch(`/conversations/${conversationId}`);
    const data = await res.json();
    setMessages(data);
  };

  if (!userId) {
    return (
      <div>
        <h1>Register</h1>
        <form onSubmit={register}>
          <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }

  return (
    <div>
      <h1>Welcome, {username}</h1>
      <form onSubmit={submitQuestionnaire}>
        <label>What do you often do in your leisure time?</label>
        <br />
        <textarea value={answer} onChange={e => setAnswer(e.target.value)} />
        <br />
        <button type="submit">Save Answer</button>
      </form>
      <h2>Chat</h2>
      <div style={{ border: '1px solid #ccc', padding: '10px', height: '200px', overflowY: 'scroll' }}>
        {messages.map(m => (
          <div key={m.id}>{m.message}</div>
        ))}
      </div>
      <form onSubmit={sendMessage}>
        <input value={chatInput} onChange={e => setChatInput(e.target.value)} />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
