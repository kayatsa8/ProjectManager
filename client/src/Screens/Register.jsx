import { useState } from "react";
import UsernamePassword from "./UsernamePassword";
import useFetch from "../useFetch";

const Register = () => {
    const [url, setUrl] = useState(null);
    const [content, setContent] = useState({username:"", password: ""});
    const {response, isPending, error} = useFetch(url, "POST", content);


    const onButtonPressed = (username, password) => {
        setContent({username: username, password: password});

        setUrl(null);
        setUrl(() => "http://localhost:5000/api/register_user");
        // TODO: use history to go to login page
    };


    return ( 
        <div>
            <UsernamePassword
                headline="Register"
                buttonName="Register"
                onButtonPressed={onButtonPressed}
            />
        </div>
     );
}
 
export default Register;