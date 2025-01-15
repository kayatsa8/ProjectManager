import { useState } from "react";
import { useHistory, useLocation, useParams } from "react-router-dom/cjs/react-router-dom.min";
import useFetch from "../useFetch";

const EditProject = () => {
    const {projectName} = useParams();
    const location = useLocation();
    const history = useHistory();
    const username = location.state.username;
    const projects = location.state.projects;
    const project = location.state.project;

    const [nameNew, setNameNew] = useState(project.name);
    const [newDesc, setNewDesc] = useState(project.description);
    const [newLangs, setNewLangs] = useState(() => {
        const temp = project.languages.reduce((str, curr) => str + ", " + curr, "");
        return temp.substring(2);
    });
    const [newTools, setNewTools] = useState(() => {
        const temp = project.tools.reduce((str, curr) => str + ", " + curr, "");
        return temp.substring(2);
    });

    const [url, setUrl] = useState(null);
    const [content, setContent] = useState(null);
    const {response, isPending, error} = useFetch(url, "PATCH", content);
    




    const handleBackButton = () => {
        history.push(`/project/${projectName}`, {username: username, projects: projects});
    };

    const handleSubmit = (event) => {
        event.preventDefault();

        if(nameNew !== project.name){
            setContent(() => {return {
                username: username,
                projectName: projectName,
                newProjectName: nameNew
            };});

            setUrl(() => "http://localhost:5000/api/change_project_name");
        }

        if(newDesc !== project.description){
            setContent(() => {return {
                username: username,
                projectName: nameNew,
                description: newDesc
            };});

            setUrl(() => "http://localhost:5000/api/change_project_description");
        }

        let langList = newLangs.split(", ");
        let toolList = newTools.split(", ");

        if(langList.length === 1 && langList[0] === ""){
            langList = [];
        }

        if(toolList.length === 1 && toolList[0] === ""){
            toolList = [];
        }

        if(langList !== project.languages){
            setContent(() => {return {
                username: username,
                projectName: nameNew,
                languages: langList
            };});

            setUrl(() => "http://localhost:5000/api/change_project_languages");
        }

        if(toolList !== project.tools){
            setContent(() => {return {
                username: username,
                projectName: nameNew,
                tools: toolList
            };});

            setUrl(() => "http://localhost:5000/api/change_project_tools")
        }
    };


    return (
        <div>
            <button onClick={() => handleBackButton()}>Back</button>

            <h1>Edit Project</h1>

            <form onSubmit={(event) => handleSubmit(event)}>
                <label>Title:</label>
                <input 
                    type="text"
                    value={nameNew}
                    onChange={(event) => {setNameNew(() => event.target.value)}}
                />

                <label>Description:</label>
                <textarea
                    value={newDesc}
                    onChange={(event) => {setNewDesc(() => event.target.value)}}
                />

                <label>Languages:</label>
                <textarea
                    value={newLangs}
                    onChange={(event) => {setNewLangs(() => event.target.value)}}
                />

                <label>Tools:</label>
                <textarea
                    value={newTools}
                    onChange={(event) => {setNewTools(() => event.target.value)}}
                />

                <button>Confirm Edit</button>
            </form>


        </div>
    );
}
 
export default EditProject;