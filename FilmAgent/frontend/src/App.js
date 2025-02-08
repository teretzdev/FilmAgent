import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import PromptList from './components/PromptList';
import PromptForm from './components/PromptForm';
import PromptPreview from './components/PromptPreview';

const App = () => {
  return (
    <Router>
      <div>
        <header style={styles.header}>
          <nav style={styles.nav}>
            <ul style={styles.navList}>
              <li style={styles.navItem}>
                <Link to="/" style={styles.navLink}>Prompt List</Link>
              </li>
              <li style={styles.navItem}>
                <Link to="/form" style={styles.navLink}>Prompt Form</Link>
              </li>
              <li style={styles.navItem}>
                <Link to="/preview" style={styles.navLink}>Prompt Preview</Link>
              </li>
            </ul>
          </nav>
        </header>
        <main style={styles.main}>
          <Routes>
            <Route path="/" element={<PromptList />} />
            <Route path="/form" element={<PromptForm />} />
            <Route path="/preview" element={<PromptPreview />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

const styles = {
  header: {
    backgroundColor: '#282c34',
    padding: '10px 20px',
    color: 'white',
    textAlign: 'center',
  },
  nav: {
    display: 'flex',
    justifyContent: 'center',
  },
  navList: {
    listStyleType: 'none',
    display: 'flex',
    padding: 0,
    margin: 0,
  },
  navItem: {
    margin: '0 15px',
  },
  navLink: {
    color: 'white',
    textDecoration: 'none',
    fontSize: '18px',
  },
  main: {
    padding: '20px',
  },
};

export default App;
