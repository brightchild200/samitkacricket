import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import PlayerStats from './components/PlayerStats';

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/players" component={PlayerStats} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;