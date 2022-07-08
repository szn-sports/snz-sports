import React from 'react';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import DashboardPage from './components/pages/DashboardPage'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar/>
        <Routes>
          <Route path="/Dashboard" component={DashboardPage}/>
        </Routes>
      </Router>
      <Dashboard/>
    </div>
  );
}

export default App;
