import React from 'react';
import {Routes, Route} from 'react-router-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import QuizSelect from './components/QuizSelect';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<QuizSelect/>}/>
      </Routes>
    </Router>
  );
}

export default App;
