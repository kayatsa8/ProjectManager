import { useEffect, useState } from "react";
import useFetch from "../useFetch";
import { toast } from 'react-toastify';
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";

const DeleteUserButton = ({getUsername, getPassword}) => {
    const [url, setUrl] = useState(null);
    const [content, setContent] = useState(null);
    const {response, isPending, error} = useFetch(url, "DELETE", content);
    const history = useHistory();
    const [sure, setSure] = useState(false);

    
    const handleDelete = () => {
        const username = getUsername();
        const password = getPassword();

        setContent(() => ({username: username, password: password}));
    };

    useEffect(() => {
        if(!content){
            return;
        }

        setUrl(() => "http://localhost:5000/api/delete_user");
    }, [content]);

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
            setContent(null);

            return;
        }


        toast.success("The user was deleted successfully!", {
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
    }, [response]);


    return (
        <div>
            {!sure && <button className="delete" onClick={() => setSure(() => true)}>Delete User</button>}
            {sure && <p>Are you sure?</p>}
            {sure && <button onClick={handleDelete}>Yes</button>}
            {sure && <button onClick={() => setSure(() => false)}>No</button>}
        </div>
    );
}
 
export default DeleteUserButton;