import { Link } from "react-router-dom";
import Card from "./Card";

const ProjectList = ({projects}) => {
    return (
        <div>
            {
                projects.map((project) => (
                    <div key={project}>
                        <Link to={`/project/${project}`}>
                            <Card projectName={project} />
                        </Link>
                    </div>
                ))
            }
        </div>
    );
}
 
export default ProjectList;