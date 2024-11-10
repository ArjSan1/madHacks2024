import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import { Routes, Route, useNavigate } from 'react-router-dom';
import './styles/App.css';
import Vote from './Vote';

function App() {
  const { loginWithRedirect, logout, isAuthenticated } = useAuth0();
  const navigate = useNavigate();
  const goToVote = () => navigate('/Vote');

  return (
    <div className="App">
      <h1>It's Time to<br/>Cast Your Ballot<br/></h1>

      {isAuthenticated ? (
        <div>
          <button className="star-button" onClick={goToVote}>
            Get Started
          </button>
          <button id="logout-button" onClick={() => logout({ returnTo: window.location.origin })}>
            Log Out
          </button>
        </div>
      ) : (
        <button className="star-button" onClick={() => loginWithRedirect()}>Log In</button>
      )}
      <Routes>
        <Route path="/Vote" element={<Vote />} />
      </Routes>
    </div>
  );
}

export default App;
