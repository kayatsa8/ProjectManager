import { useState } from "react";

const UsernamePassword = ({headline, buttonName, onButtonPressed}) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");


    const handleSubmit = (event) => {
        event.preventDefault();
        onButtonPressed(username, password);
    };



    return (
        <div>
            <h1>{headline}</h1>
            <form onSubmit={handleSubmit}>
                <label>Username:</label>
                <input 
                    type="text"
                    required
                    value={username}
                    placeholder="your user name"
                    onChange={(event) => {setUsername(() => event.target.value)}}
                />

                <label>password:</label>
                <input 
                    type="text"
                    required
                    value={password}
                    placeholder="your password"
                    onChange={(event) => {setPassword(() => event.target.value)}}
                />

                <button>{buttonName}</button>
            </form>
        </div>
    );
}
 
export default UsernamePassword;