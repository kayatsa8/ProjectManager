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
    const {response, isPending, error} = useFetch("http://localhost:5000/api/get_project", "GET", content);


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
        }

    }, [response])




    return (
        <div>
            <BackHome username={location.state.username} projects={location.state.projects}/>

            <h1>{projectName}</h1>
        </div>
    );
}
 
export default ProjectView;