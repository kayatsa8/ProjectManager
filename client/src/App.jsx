import { useState } from "react";
import useFetch from "./useFetch"
import UsernamePassword from "./Screens/UsernamePassword";
import Register from "./Screens/Register";


function App() {
  return (
    <Register />
  );



  // const [url, setUrl] = useState(null);
  // const {response, isPending, error} = useFetch(url, "PATCH", {username: "admin", password: "admin"});

  // const handleClick = () => {
  //   setUrl(u => u = "http://localhost:5000//api/log_in");
  //   console.log(response);
  // };


  // return (
  //   <>
  //     <div>
  //       <button onClick={() => handleClick()}>click</button>

  //       {response &&
  //         <div>
  //           name: {response.value.username}

  //           {response.value.projects.map(project => (
  //             <div key={project}>
  //               <p>project: {project}</p>
  //             </div>
  //           ))}
  //         </div>
  //       }
  //     </div>
  //   </>
  // );
}

export default App
