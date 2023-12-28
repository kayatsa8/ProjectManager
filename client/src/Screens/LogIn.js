import { useState, useEffect } from "react";
import {Link} from "react-router-dom";

const LogIn = () => {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    
    const [error, setError] = useState(null);
    const [isPending, setIsPending] = useState(false);

    const [response, setResponse] = useState({});


    const sendLogInRequest = () => {
           
        const body = {username, password};
        setIsPending(true);
    
        fetch("http://127.0.0.1:5000/api/log_in", {
            method: "PATCH",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(body)
        })
        .then((res) => {
            if(!res.ok){
                throw Error("Could not fetch!");
            }

            return res.json();
        })
        .then((serverResponse) => {
            setResponse(serverResponse);
            setIsPending(false);
            setError(serverResponse.message);
        })
        .catch((err) => {
            setError(err.message);
            setIsPending(false);
            setResponse({});
        });
    
    }

    useEffect(() => {
        if(!response.error){
            console.log(response);
        }
    }, [response]);

    const handleSubmit = (event) => {
        event.preventDefault();
        sendLogInRequest();
    }



    return ( 
        <div className="login">
            <h2>Log In to Your User</h2>

            <form onSubmit={(event) => {handleSubmit(event)}}>

                <label>Username:</label>
                <input
                    type="text"
                    required
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="username"
                />

                <label>Password:</label>
                <input
                    type="text"
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="password"
                />

                {!isPending && <button>Log In</button>}
                {isPending && <button disabled>Waiting...</button>}
                {error && <div className="error">{error}</div>}

                <div className="links">
                    <Link to="/register">not registered yet?</Link>
                </div>

            </form>
        </div>
     );
}
 
export default LogIn;

