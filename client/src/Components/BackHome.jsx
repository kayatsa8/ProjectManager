import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import "../css/BackHome.css"

const BackHome = ({username, projects}) => {
    const history = useHistory();

    
    const handleClick = () => {
        history.push("/home", {username: username, projects: projects});
    };

    
    return (
        <button className="back_home" onClick={() => handleClick()}>Back</button>
    );
}
 
export default BackHome;