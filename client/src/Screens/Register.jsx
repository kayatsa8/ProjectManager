import { useState, useEffect } from "react";
import UsernamePassword from "../Components/UsernamePassword";
import useFetch from "../useFetch";
import { useHistory } from "react-router-dom";
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Register = () => {
    const [url, setUrl] = useState(null);
    const [content, setContent] = useState({username:"", password: ""});
    const {response, isPending, error} = useFetch(url, "POST", content);
    const history = useHistory();


    const onButtonPressed = (username, password) => {
        setContent(() => {return {username: username, password: password}});

        setUrl(() => "http://localhost:5000/api/register_user");
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

        toast.success('New user was created!', {
            position: "bottom-left",
            autoClose: 4000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
            theme: "colored",
        });
        history.push("/");

    }, [response])

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
                headline="Register"
                buttonName="Register"
                onButtonPressed={onButtonPressed}
            />
        </div>
     );
}
 
export default Register;