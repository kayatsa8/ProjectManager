import { useLocation } from 'react-router-dom';
import { useParams } from "react-router-dom";




const ProjectView = () => {
    const location = useLocation();
    const {projectName} = useParams();

    return (
        <div>
            <p>{location.state.username}</p>
            <p>{projectName}</p>
        </div>
    );
}
 
export default ProjectView;