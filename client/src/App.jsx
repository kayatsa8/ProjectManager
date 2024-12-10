import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './Screens/Login';
import Register from './Screens/Register';
import NotFound from './Screens/NotImplemented';


function App() {
  return (
    <Router>
      <div className="App">
        {/* TODO: navigation of some sort */}

        <div className="content">
          <Switch>

            <Route exact path="/">
              <Login />
            </Route>

            <Route exact path="/register">
              <Register />
            </Route>

            <Route path="*">
              <NotFound />
            </Route>
            
          </Switch>
        </div>

      </div>
    </Router>
  );
}

export default App
