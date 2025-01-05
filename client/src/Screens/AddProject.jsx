import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { useLocation } from 'react-router-dom';
import { useState, useEffect } from "react";
import useFetch from "../useFetch";
import { toast } from 'react-toastify';
import BackHome from "../Components/BackHome";



const AddProject = () => {
    const history = useHistory();
    const location = useLocation();
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [languages, setLanguages] = useState("");
    const [tools, setTools] = useState("");

    const [url, setUrl] = useState(null);
    const [content, setContent] = useState({});
    const {response, isPending, error} = useFetch(url, "POST", content);

    const handleSubmit = (event) => {
        event.preventDefault();

        let langList = languages.split(", ");
        let toolList = tools.split(", ");

        if(langList.length === 1 && langList[0] === ""){
            langList = [];
        }

        if(toolList.length === 1 && toolList[0] === ""){
            toolList = [];
        }

        setContent(() => {return {
            username: location.state.username,
            projectName: title,
            description: description,
            languages: langList,
            tools: toolList
        }});
        
        setUrl(() => "http://localhost:5000/api/add_project");
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

        toast.success(`Project ${title} was created successfully!`, {
            position: "bottom-left",
            autoClose: 4000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
            theme: "colored",
        });                

        history.push("/home", {username: location.state.username, projects: [...location.state.projects, title]});

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
            <BackHome username={location.state.username} projects={location.state.projects}/>
            
            <form onSubmit={(event) => handleSubmit(event)}>

                <h1>Add Project</h1>

                <label>Title: </label>
                <input 
                    type="text"
                    required
                    value={title}
                    placeholder="the project's title"
                    onChange={(event) => {setTitle(() => event.target.value)}}
                />

                <label>Description: </label>
                <textarea
                    value={description}
                    placeholder="write a description for your project"
                    onChange={(event) => {setDescription(() => event.target.value)}}
                />

                <label>Languages: </label>
                <textarea
                    value={languages}
                    placeholder="enter the languages comma seperated. for example: Java, Python, ..."
                    onChange={(event) => setLanguages(() => event.target.value)}
                />

                <label>Tools: </label>
                <textarea
                    value={tools}
                    placeholder="enter the tools comma seperated. for example: Spring Boot, React, ..."
                    onChange={(event) => setTools(() => event.target.value)}
                />

                {!isPending && <button>Add</button>}
                {isPending && <p>Sending...</p>}

            </form>
                
        </div>
    );
}
 
export default AddProject;