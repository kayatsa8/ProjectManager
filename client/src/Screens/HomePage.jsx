import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import useFetch from "../useFetch";
import { useState } from "react";

const HomePage = ({username}) => {
    const [url, setUrl] = useState(null);
    const [content, setContent] = useState({username: ""});
    const {response, isPending, error} = useFetch(url, "PATCH", content);
    const history = useHistory();

    const handleLogout = () => {
        setContent({username: username});
    };

    return (
        <div>
            <button onClick={() => handleLogout()}>Logout</button>
        </div>
    );
}
 
export default HomePage;