import { useLocation } from 'react-router-dom';
import BackHome from '../Components/BackHome';
import { useState } from 'react';
import EditButton from '../Components/EditButton';
import DeleteUserButton from '../Components/DeleteUserButton';
import "../css/UserSettings.css"

const UserSettings = () => {
    const location = useLocation();
    const [newName, setNewName] = useState(location.state.username);
    const [newPassword, setNewPassword] = useState("");
    const [password, setPassword] = useState("");







    const beforeName = (content) => {
        content.newUsername = newName;
        content.password = password
    };

    const afterName = () => {
        location.state.username = newName;
        setPassword(() => "");
    };

    const beforePassword = (content) => {
        content.oldPassword = password;
        content.newPassword = newPassword;
    };

    const afterPassword = () => {
        setPassword(() => "");
        setNewPassword(() => "");
    };



    return (
        <div>
            <BackHome username={location.state.username} projects={location.state.projects} />

            <div className="user_settings">
                <h1>User Settings</h1>

                <label>New Username:</label>
                <input
                    type="text"
                    value={newName}
                    onChange={((event) => setNewName(() => event.target.value))}
                />
                <EditButton
                    toUrl="http://localhost:5000/api/change_username"
                    content={{
                        oldUsername: location.state.username,
                        newUsername: "",
                        password: ""
                    }}
                    doBefore={beforeName}
                    doAfter={afterName}
                />

                <label>New Password:</label>
                <input
                    type="text"
                    value={newPassword}
                    placeholder="new password"
                    onChange={((event) => setNewPassword(() => event.target.value))}
                />
                <EditButton
                    toUrl="http://localhost:5000/api/change_password"
                    content={{
                        username: location.state.username,
                        oldPassword: "",
                        newPassword: ""
                    }}
                    doBefore={beforePassword}
                    doAfter={afterPassword}
                />

                <DeleteUserButton
                    getUsername={() => location.state.username}
                    getPassword={() => password}
                />

            </div>

            <div className="confirm">
                <label>Confirm Your Action With Your Password:</label>
                <input
                    type="text"
                    value={password}
                    onChange={((event) => setPassword(() => event.target.value))}
                />
            </div>


        </div>
    );
}
 
export default UserSettings;