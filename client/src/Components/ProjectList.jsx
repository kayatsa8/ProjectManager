import { Link } from "react-router-dom";
import Card from "./Card";

const ProjectList = ({projects, username}) => {
    return (
        <div className="list">
            {
                projects.map((project) => (
                    <div className="card" key={project}>
                        <Link to={{pathname: `/project/${project}`, state: {username: username, projects: projects}}}>
                            <Card projectName={project}/>
                        </Link>
                    </div>
                ))
            }
        </div>
    );
}
 
export default ProjectList;

