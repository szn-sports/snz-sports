import React from 'react';
import './MainPage.css';
import { useLocation } from 'react-router-dom';    

function PageBackground() {
      return (
      <div className="dashboard">
         <div className="dashboard-container inner-shadow">
            <div className="dashboard-page">
                  <div className="dashboard-container-nfts">
                        <div className="nft-displays outer-shadow"></div>
                        <div className="nft-displays outer-shadow"></div>
                        <div className="nft-displays outer-shadow"></div>
                  </div>
                  <div className="dashboard-container-statsandscore">
                        <div className="live-score outer-shadow"></div>
                        <div className="stats-container">
                        <div className="stats stat--1 outer-shadow"></div>
                        <div className="stats stat--2 outer-shadow"></div>
                        <div className="stats stat--3 outer-shadow"></div>
                        <div className="stats stat--4 outer-shadow"></div>
                        <div className="stats stat--5 outer-shadow"></div>
                        <div className="stats stat--6 outer-shadow"></div>
                        </div>
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
         </div>
      </div>
      )
   
}

export default PageBackground