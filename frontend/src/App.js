import React from 'react';
import {Routes, Route} from 'react-router-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import QuizSelect from './components/QuizSelect';
import RandomQuiz from './components/RandomQuiz'

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<QuizSelect/>}/>
        <Route exact path="/random/:topic" element={<RandomQuiz/>}/>
      </Routes>
    </Router>
  );
}

export default App;
