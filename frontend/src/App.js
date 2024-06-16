import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [token, setToken] = useState('');
  const [userInfo, setUserInfo] = useState(null);
  const [newPassword, setNewPassword] = useState('');

  const handleRegister = async () => {
    try {
      const response = await axios.post('/auth/register', {
        username,
        password
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage(error.response.data.message);
    }
  };

  const handleLogin = async () => {
    try {
      const response = await axios.post('/auth/login', {
        username,
        password
      });
      setMessage('Logged in!');
      setToken(response.data.token);
    } catch (error) {
      setMessage(error.response.data.message);
    }
  };

  const fetchUserInfo = async () => {
    try {
      const response = await axios.get('/user', {
        headers: {
          'x-access-token': token
        }
      });
      setUserInfo(response.data);
    } catch (error) {
      setMessage('Failed to fetch user info');
    }
  };

  const handleUpdatePassword = async () => {
    try {
      const response = await axios.put('/user', {
        password: newPassword
      }, {
        headers: {
          'x-access-token': token
        }
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Failed to update password');
    }
  };

  const handleRecoverPassword = async () => {
    try {
      const response = await axios.post('/user/recover', {
        username,
        new_password: newPassword
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Failed to recover password');
    }
  };

  useEffect(() => {
    if (token) {
      fetchUserInfo();
    }
  }, [token]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Auth Service</h1>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button onClick={handleRegister}>Register</button>
        <button onClick={handleLogin}>Login</button>
        <p>{message}</p>
        {userInfo && (
          <div>
            <h2>User Info</h2>
            <p>Username: {userInfo.username}</p>
            <input
              type="password"
              placeholder="New Password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
            />
            <button onClick={handleUpdatePassword}>Update Password</button>
          </div>
        )}
        <div>
          <h2>Recover Password</h2>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="New Password"
            value={newPassword}
            onChange={(e) => setNewPassword(e.target.value)}
          />
          <button onClick={handleRecoverPassword}>Recover Password</button>
        </div>
      </header>
    </div>
  );
}

export default App;
