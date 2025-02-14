import { useEffect, useState } from "react";
import useFetch from "../useFetch";
import { toast } from 'react-toastify';
import "../css/ProjectView.css";



const ChangeStatusButton = ({projectName, username, setIsCompleted}) => {
    const [url, setUrl] = useState(null);
    const {response, isPending, error} = useFetch(url, "PATCH", {username: username, projectName: projectName});


    const handleClick = () => {
        setUrl(() => "http://localhost:5000/api/mark_project");
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
        }
        else{
            setIsCompleted((c) => !c);
        }

        setUrl(() => null);

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
        <button onClick={() => handleClick()}>Change Status</button>
    );
}
 
export default ChangeStatusButton;