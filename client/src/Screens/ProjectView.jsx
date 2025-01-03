import { useLocation } from 'react-router-dom';
import { useParams } from "react-router-dom";
import BackHome from '../Components/BackHome';




const ProjectView = () => {
    const location = useLocation();
    const {projectName} = useParams();

    return (
        <div>
            <BackHome username={location.state.username} projects={location.state.projects}/>

            <h1>{projectName}</h1>
        </div>
    );
}
 
export default ProjectView;