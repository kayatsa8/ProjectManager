import { useEffect, useState } from "react";
import useFetch from "../useFetch";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { toast } from 'react-toastify';



const DeleteProjectButton = ({username, projectName, projects}) => {
    const [url, setUrl] = useState(null);
    const content = {username: username, projectName: projectName};
    const {response, isPending, error} = useFetch(url, "DELETE", content);
    const history = useHistory();

    const handleClick = () => {
        setUrl(() => "http://localhost:5000/api/delete_project");
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

        const ps = projects.filter((p) => p !== projectName);

        history.push("/home", {username: username, projects: ps});

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
        <button className="delete" onClick={() => handleClick()}>Delete</button>
    );
}
 
export default DeleteProjectButton;