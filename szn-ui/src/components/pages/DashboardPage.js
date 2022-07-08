import React from 'react';
import Dashboard from '../Dashboard';
import './DashboardPage.css';

function DashboardPage() {
  return (
    <Dashboard>
    <div className="dashboard-page">
        <div className="dashboard-container-nfts">
            <div className="nft-displays"></div>
            <div className="nft-displays"></div>
            <div className="nft-displays"></div>
        </div>
        <div className="dashboard-container-statsandscore">
            <div className="live-score"></div>
            <div className="stats"></div>
            <div className="stats"></div>
            <div className="stats"></div>
            <div className="stats"></div>
            <div className="stats"></div>
            <div className="stats"></div>
        </div>
        <div className="dashboard-container-social-media">
            <div className="social-media"></div>
            <div className="social-media"></div>
            <div className="social-media"></div>
            <div className="social-media"></div>
        </div>
        <div className="dashboard-container-nfts">
            <div className="upcoming-events"></div>
        </div>
    </div>
    </Dashboard>
  )
}

export default DashboardPage