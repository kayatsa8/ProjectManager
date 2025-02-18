import { useState, useEffect } from "react";
import UsernamePassword from "../Components/UsernamePassword";
import useFetch from "../useFetch";
import { useHistory } from "react-router-dom";
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Login = () => {
    const [url, setUrl] = useState(null);
    const [content, setContent] = useState({username: "", password: ""});
    const {response, isPending, error} = useFetch(url, "PATCH", content);
    const history = useHistory();

    const onButtonPressed = (username, password) => {
        setContent(() => {return {username: username, password: password}});

        setUrl(() => "http://localhost:5000/api/log_in")
    };

    const handleRegisterButton = () => {
        history.push("/register");
    };

    useEffect(() => {
        if(!response){
            return;
        }

        if(response.error){
            toast.error(response.message, {
                position: "bottom-left",
                autoClose: 4000,
                hideProgressBar: false,
                closeOnClick: true,
                pauseOnHover: true,
                draggable: true,
                progress: undefined,
                theme: "colored",
            });

            setUrl(() => null);

            return;
        }

        history.push("/home", {username: response.value.username, projects: response.value.projects});

    }, [response]);

    useEffect(() => {
        if(!error){
            return;
        }

        toast.error(error, {
            position: "bottom-left",
            autoClose: 4000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
            theme: "colored",
        });

        setUrl(() => null);
    }, [error]);


    return (
        <div className="login_register">
            <UsernamePassword 
                headline="Login"
                buttonName="Login"
                onButtonPressed={(username, password) => onButtonPressed(username, password)}
            />
            <button className="toRegister" onClick={handleRegisterButton}>Register</button>

            {isPending && <div className="login_pending">pending...</div>}
        </div>
    );
}
 
export default Login;