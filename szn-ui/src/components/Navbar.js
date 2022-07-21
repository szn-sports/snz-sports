import React, {useState} from 'react'
import { Link } from 'react-router-dom';
import './Navbar.css';
import {FaList} from 'react-icons/fa';
import {FiMonitor} from 'react-icons/fi';
import {BsPerson} from 'react-icons/bs';
import {AiOutlineCalendar} from 'react-icons/ai';
import {BsGear} from 'react-icons/bs';
import {RiDashboardLine} from 'react-icons/ri';


function Navbar() {
  return (
    <>
    <nav className="navbar">
        <div className="navbar-container">
            <img src={process.env.PUBLIC_URL + '/logomaybe.jpg'} className="navbar-logo" />
            <ul className="navbar-list">
            <li class="navbar-item">
                
                <a href="/" className="navbar-links">
                <RiDashboardLine size = "1.5vw" className="navbar-icons"/>
                Dashboard
                </a>
            </li>
            <li class="navbar-item">
                
                <a href="/" class="navbar-links">
                <FiMonitor size = "1.5vw" className="navbar-icons"/>
                Live game
                </a>
            </li>
            <li class="navbar-item">
                
                <a href="/" class="navbar-links">
                <BsPerson size = "1.5vw" className="navbar-icons"/>
                Your SZN-NFTS
                </a>
            </li>
            <li class="navbar-item">
                <a href="/" class="navbar-links">
                <AiOutlineCalendar size = "1.5vw" className="navbar-icons"/>
                Game Schedules
                </a>
            </li>
            <li class="navbar-item">
                
                <a href="/" class="navbar-links">
                <BsGear size = "1.5vw" className="navbar-icons"/>Settings
                </a>
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