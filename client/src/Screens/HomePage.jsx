import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import useFetch from "../useFetch";
import { useEffect, useState } from "react";
import { useLocation } from 'react-router-dom';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import ProjectList from "../Components/ProjectList";

const HomePage = () => {
    const [url, setUrl] = useState(null);
    const [content, setContent] = useState({username: ""});
    const {response, isPending, error} = useFetch(url, "PATCH", content);
    const history = useHistory();
    const location = useLocation();

    const handleLogout = () => {
        setContent({username: location.state.username});
        setUrl("http://localhost:5000/api/log_out");
    };

    const handleSettings = () => {
        console.log("handle settings");
    };

    const handleAddProject = () => {
        history.push("/add_project", {username: location.state.username, projects: location.state.projects})
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

        history.push("/");

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
        <div>
            <button onClick={() => handleLogout()}>Logout</button>
            <button onClick={() => handleSettings()}>Settings</button>
            <ProjectList projects={location.state.projects}/>
            <button onClick={() => handleAddProject()}>Add Project</button>
        </div>
    );
}
 
export default HomePage;