import React from 'react';
import Navbar from './components/Navbar';
import Dashboard from './components/MainPage';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar/>
        <Routes>
        </Routes>
      </Router>
      <Dashboard/>
    </div>
  );
}

export default App;
