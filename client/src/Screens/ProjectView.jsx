import { useLocation } from 'react-router-dom';
import { useParams } from "react-router-dom";
import BackHome from '../Components/BackHome';
import useFetch from '../useFetch';
import { useEffect, useState } from 'react';
import { toast } from 'react-toastify';




const ProjectView = () => {
    const location = useLocation();
    const {projectName} = useParams();
    const content = {username: location.state.username, projectName: projectName};
    const {response, isPending, error} = useFetch("http://localhost:5000/api/get_project", "POST", content);
    const [languages, setLanguages] = useState("");
    const [tools, setTools] = useState("");


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

            return;
        }

        setLanguages(() => {
            let ls = response.value.languages.reduce((langStr, curr) => {return langStr + ", " + curr;}, "");
            ls = ls.slice(2);
            return ls;
        });

        setTools(() => {
            let ls = response.value.tools.reduce((toolStr, curr) => toolStr + ", " + curr, "");
            ls = ls.slice(2);
            return ls;
        });

    }, [response])




    return (
        <div>
            <BackHome username={location.state.username} projects={location.state.projects}/>

            {response && 
                <div>
                    <h1>{projectName}</h1>

                    <p>Status: {response.value.completed ? "Completed" : "Incomplete"}</p>

                    <p>{response.value.description !== "" ? response.value.description : "No Description"}</p>

                    <p>Languages: {languages}</p>

                    <p>Tools: {tools}</p>
                </div>
            }
        </div>
    );
}
 
export default ProjectView;