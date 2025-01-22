import { useHistory } from "react-router-dom/cjs/react-router-dom.min";

const BackHome = ({username, projects}) => {
    const history = useHistory();

    
    const handleClick = () => {
        history.push("/home", {username: username, projects: projects});
    };

    
    return (
        <button onClick={() => handleClick()}>Back</button>
    );
}
 
export default BackHome;