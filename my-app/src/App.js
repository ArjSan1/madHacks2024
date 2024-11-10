import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import './styles/App.css'

function App() {
  const { loginWithRedirect, logout, isAuthenticated } = useAuth0();

  return (
    <div className="App">
      <h1>It's Time to<br/>Cast Your Ballot<br/></h1>

      {isAuthenticated ? (
        <div>
          {/* change to go to voting page */}
          <button className="star-button" onClick={() => logout({ returnTo: window.location.origin })}>
            Get Started
          </button>
          <button id="logout-button" onClick={() => logout({ returnTo: window.location.origin })}>
            Log Out
          </button>
        </div>
      ) : (
        <button className="star-button" onClick={() => loginWithRedirect()}>Log In</button>
      )}
    </div>
  );
}

export default App;
