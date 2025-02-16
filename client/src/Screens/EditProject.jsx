import { useState } from "react";
import { useHistory, useLocation, useParams } from "react-router-dom/cjs/react-router-dom.min";
import EditButton from "../Components/EditButton";
import "../css/EditProject.css"

const EditProject = () => {
    const {projectName} = useParams();
    const location = useLocation();
    const history = useHistory();
    const username = location.state.username;
    let projects = location.state.projects;
    const project = location.state.project;

    const [newName, setNameNew] = useState(project.name);
    const [newDesc, setNewDesc] = useState(project.description);
    const [newLangs, setNewLangs] = useState(() => {
        const temp = project.languages.reduce((str, curr) => str + ", " + curr, "");
        return temp.substring(2);
    });
    const [newTools, setNewTools] = useState(() => {
        const temp = project.tools.reduce((str, curr) => str + ", " + curr, "");
        return temp.substring(2);
    });





    const handleBackButton = () => {
        history.push(`/project/${projectName}`, {username: username, projects: projects});
    };




    const beforeName = (content) => {
        content.projectName = projectName;
        content.newProjectName = newName;
    };

    const afterName = () => {
        project.name = newName;

        projects = projects.filter((pName) => pName != projectName);
        projects.push(newName);

        console.log(projects);

        history.push(`/edit/${project.name}`, {
            username: username,
            projects: projects,
            project: project
        });
    };

    const beforeDesciption = (content) => {
        content.description = newDesc;
    };

    const afterDescription = () => {
        project.description = newDesc;
    };

    const beforeLanguages = (content) => {
        let langList = newLangs.split(", ");

        if(langList.length === 1 && langList[0] === ""){
            langList = [];
        }

        content.languages = langList;
    };

    const afterLanguages = () => {
        let langList = newLangs.split(", ");

        if(langList.length === 1 && langList[0] === ""){
            langList = [];
        }

        project.languages = langList;
    };

    const beforeTools = (content) => {
        let toolList = newTools.split(", ");

        if(toolList.length === 1 && toolList[0] === ""){
            toolList = [];
        }

        content.tools = toolList;
    };

    const afterTools = () => {
        let toolList = newTools.split(", ");

        if(toolList.length === 1 && toolList[0] === ""){
            toolList = [];
        }

        project.tools = toolList;
    };






    return (
        <div>
            <button className="back_edit_project" onClick={() => handleBackButton()}>Back</button>

            <div className="edit_form">
                <h1>Edit Project</h1>

                <label>Title:</label>
                <input 
                    type="text"
                    value={newName}
                    onChange={(event) => {setNameNew(() => event.target.value)}}
                />
                <EditButton 
                    toUrl="http://localhost:5000/api/change_project_name"
                    content={{
                        username: username,
                        projectName: "",
                        newProjectName: ""
                    }}
                    doBefore={beforeName}
                    doAfter={afterName}
                />

                <label>Description:</label>
                <textarea
                    value={newDesc}
                    onChange={(event) => {setNewDesc(() => event.target.value)}}
                />
                <EditButton 
                    toUrl="http://localhost:5000/api/change_project_description"
                    content={{
                        username: username,
                        projectName: projectName,
                        description: ""
                    }}
                    doBefore={beforeDesciption}
                    doAfter={afterDescription}
                />

                <label>Languages:</label>
                <textarea
                    value={newLangs}
                    onChange={(event) => {setNewLangs(() => event.target.value)}}
                />
                <EditButton
                    toUrl="http://localhost:5000/api/change_project_languages"
                    content={{
                        username: username,
                        projectName: projectName,
                        languages: []
                    }}
                    doBefore={beforeLanguages}
                    doAfter={afterLanguages}
                />

                <label>Tools:</label>
                <textarea
                    value={newTools}
                    onChange={(event) => {setNewTools(() => event.target.value)}}
                />
                <EditButton
                    toUrl="http://localhost:5000/api/change_project_tools"
                    content={{
                        username: username,
                        projectName: projectName,
                        tools: []
                    }}
                    doBefore={beforeTools}
                    doAfter={afterTools}
                />
            </div>

        </div>
    );
}
 
export default EditProject;