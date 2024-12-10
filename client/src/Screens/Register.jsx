import { useState } from "react";
import UsernamePassword from "./UsernamePassword";
import useFetch from "../useFetch";
import { useHistory } from "react-router-dom";

const Register = () => {
    const [url, setUrl] = useState(null);
    const [content, setContent] = useState({username:"", password: ""});
    const {response, isPending, error} = useFetch(url, "POST", content);
    const history = useHistory();


    const onButtonPressed = (username, password) => {
        setContent({username: username, password: password});

        setUrl(null);
        setUrl(() => "http://localhost:5000/api/register_user");
        history.push("/");
    };


    return ( 
        <div>
            <UsernamePassword
                headline="Register"
                buttonName="Register"
                onButtonPressed={onButtonPressed}
            />

            {response && response.error &&
                <div>
                    server error: {response.message}
                </div>
            }

            {error &&
                <div>
                    error: {error}
                </div>
            }

        </div>
     );
}
 
export default Register;