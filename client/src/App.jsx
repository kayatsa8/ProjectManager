import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './Screens/Login';
import Register from './Screens/Register';
import NotFound from './Screens/NotImplemented';
import HomePage from './Screens/HomePage';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import AddProject from './Screens/AddProject';
import ProjectView from './Screens/ProjectView';
import EditProject from './Screens/EditProject';


function App() {
  return (
    <Router>
      <div className="App">
        <div className="content">
          <Switch>

            <Route exact path="/">
              <Login />
            </Route>

            <Route exact path="/register">
              <Register />
            </Route>

            <Route exact path="/home">
              <HomePage />
            </Route>

            <Route exact path="/add_project">
              <AddProject />
            </Route>

            <Route exact path="/project/:projectName">
              <ProjectView />
            </Route>

            <Route exact path="/edit/:projectName">
              <EditProject />
            </Route>

            <Route path="*">
              <NotFound />
            </Route>
            
          </Switch>
        </div>

        <ToastContainer />

      </div>
    </Router>
  );
}

export default App
