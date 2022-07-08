import React, {useState} from 'react'
import { Link } from 'react-router-dom';
import './Navbar.css';
import {FaList} from 'react-icons/fa';
import {FiMonitor} from 'react-icons/fi';
import {BsPerson} from 'react-icons/bs';
import {AiOutlineCalendar} from 'react-icons/ai';
import {BsGear} from 'react-icons/bs';


function Navbar() {
  return (
    <>
    <nav className="navbar">
        <div className="navbar-container">
            <Link to="/" className="navbar-link"><img src={process.env.PUBLIC_URL + '/logomaybe.jpg'} className="navbar-logo" /></Link>
            <ul className="navbar-list">
            <li class="navbar-item">
                <FaList size = "1.2vw"/>
                <Link to="/Dashboard" className="navbar-links">
                Dashboard
                </Link>
            </li>
            <li class="navbar-item">
                <FiMonitor size = "1.2vw"/>
                <a href="/" class="navbar-links">
                Live game
                </a>
            </li>
            <li class="navbar-item">
                <BsPerson size = "1.2vw"/>
                <a href="/" class="navbar-links">
                Your SZN-NFTS
                </a>
            </li>
            <li class="navbar-item">
                <AiOutlineCalendar size = "1.2vw"/>
                <a href="/" class="navbar-links">
                Game Schedules
                </a>
            </li>
            <li class="navbar-item">
                <BsGear size = "1.2vw"/>
                <a href="/" class="navbar-links">Settings</a>
            </li>
            </ul>
            <div class="navbar-wallet-connect">
                <a>User Info Here</a>
            </div>
        </div>
    </nav>
    </>
  )
}

export default Navbar