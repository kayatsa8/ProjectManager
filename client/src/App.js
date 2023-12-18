import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import LogIn from "./Screens/LogIn";


function App() {
  return (
    <div className="App">
      <Router>
        <div className="switch">
          <Switch>
            <Route exact path="/">
              <LogIn />
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