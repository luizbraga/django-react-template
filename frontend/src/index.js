import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import App from './components/app';


const initialState = {};
const target = document.getElementById('root');

const node (
  <Provider store={createStoreWithMiddleware(reducers)}>
    <App />
  </Provider>
)

ReactDOM.render(node, target);
