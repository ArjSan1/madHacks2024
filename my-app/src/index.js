import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import { Auth0Provider } from '@auth0/auth0-react';
import App from './App';
import './styles/index.css';

ReactDOM.render(
  <BrowserRouter>
    <Auth0Provider
      domain="dev-ika1qx37xfnpi6xb.us.auth0.com"
      clientId="tFK8XsKE5WBUHJpk9JSFFTtbRT524gzJ"
      authorizationParams={{
        redirect_uri: window.location.origin,
      }}
    >
      <App />
    </Auth0Provider>
  </BrowserRouter>,
  document.getElementById('root')
);
