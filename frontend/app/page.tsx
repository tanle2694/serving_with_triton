'use client';

import React, { useState } from 'react';
import Head from 'next/head';
import styles from './page.module.css';
import MLModelManager from './components/MLModelManager';

export default function HomePage() {
  const [activeTab, setActiveTab] = useState('mlmodel');

  return (
    <div className={styles.container}>
      <Head>
        <title>ML Model Serving System</title>
        <meta name="description" content="Manage and serve machine learning models" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <nav className={styles.navbar}>
        <div className={styles.navItem}>
          <span className={styles.homeIcon}>⌂</span> Home
        </div>
        <div 
          className={`${styles.navItem} ${activeTab === 'mlmodel' ? styles.active : ''}`}
          onClick={() => setActiveTab('mlmodel')}
        >
          <span className={styles.icon}>📊</span> ML Model
        </div>
      </nav>

      <main className={styles.main}>
        {activeTab === 'mlmodel' && <MLModelManager />}
      </main>
    </div>
  );
}