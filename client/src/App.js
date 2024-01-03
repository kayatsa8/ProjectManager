import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import LogIn from "./Screens/LogIn";
import Register from "./Screens/Register";
import Home from "./Screens/Home";


function App() {
  return (
    <div className="App">
      <Router>
        <div className="switch">
          <Switch>
            <Route exact path="/">
              <LogIn />
            </Route>
            <Route exact path="/register">
              <Register />
            </Route>
            <Route exact path="/home">
              <Home />
            </Route>
            <Route path="*">
              default
            </Route>
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default App;
