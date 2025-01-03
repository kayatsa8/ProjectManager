import { Link } from "react-router-dom";
import Card from "./Card";

const ProjectList = ({projects, username}) => {
    return (
        <div>
            {
                projects.map((project) => (
                    <div key={project}>
                        <Link to={{pathname: `/project/${project}`, state: {username: username}}}>
                            <Card projectName={project}/>
                        </Link>
                    </div>
                ))
            }
        </div>
    );
}
 
export default ProjectList;


// https://medium.com/@hammadrao891/passing-data-via-links-in-react-a-guide-to-effective-data-transfer-1e0b030e2a12
