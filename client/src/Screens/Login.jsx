import { useState } from "react";
import UsernamePassword from "./UsernamePassword";
import useFetch from "../useFetch";

const Login = () => {
    const [url, setUrl] = useState(null);
    const [content, setContent] = useState({username: "", password: ""});
    const {response, isPending, error} = useFetch(url, "PATCH", content);

    const onButtonPressed = (username, password) => {
        setContent(() => {return {username: username, password: password}});

        setUrl(() => null);
        setUrl(() => "http://localhost:5000/api/log_in")
        // TODO: go to home page
    };

    const handleRegisterButton = () => {
        // TODO: navigate to register page
    };


    return (
        <div>
            <UsernamePassword 
                headline="Login"
                buttonName="Login"
                onButtonPressed={(username, password) => onButtonPressed(username, password)}
            />
            <button onClick={handleRegisterButton}>Register</button>

            {response && response.error &&
                <div>
                    server error: {response.value.message}
                </div>
            }

            {error &&
                <div>
                    error: {error}
                </div>
            }

            {isPending && <div>pending...</div>}
        </div>
    );
}
 
export default Login;