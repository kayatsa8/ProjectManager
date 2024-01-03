import { useState, useEffect } from "react";
import {useHistory} from "react-router-dom";


const Register = () => {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    
    const [error, setError] = useState(null);
    const [isPending, setIsPending] = useState(false);
    const [done, setDone] = useState(false);

    const [response, setResponse] = useState({});

    const history = useHistory();


    const sendRegisterRequest = () => {
           
        const body = {username, password};
        setIsPending(true);
    
        fetch("http://127.0.0.1:5000/api/register_user", {
            method: "POST",
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
            setDone(true);
        })
        .catch((err) => {
            setError(err.message);
            setIsPending(false);
            setResponse({});
        });
    
    }

    useEffect(() => {
        if(done && !response.error){
            history.push("/");
        }
    }, [response]);

    const handleSubmit = (event) => {
        event.preventDefault();
        sendRegisterRequest();
    }

    const handleBackClick = () => {
        history.push("/");
    }



    return ( 
        <div className="register">
            <h2>Register</h2>

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

                {!isPending && <button>Register</button>}
                {isPending && <button disabled>Waiting...</button>}
                {error && <div className="error">{error}</div>}

            </form>

            <div className="backButton">
                <button onClick={handleBackClick}>back</button>
            </div>
            
        </div>
     );
}
 
export default Register;

