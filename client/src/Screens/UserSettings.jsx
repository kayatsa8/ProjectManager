import { useLocation } from 'react-router-dom';
import BackHome from '../Components/BackHome';

const UserSettings = () => {
    const location = useLocation();



    return (
        <div>
            <BackHome username={location.state.username} projects={location.state.projects} />
        </div>
    );
}
 
export default UserSettings;