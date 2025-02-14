import { useState, useEffect } from "react";
import useFetch from "../useFetch";
import { toast } from 'react-toastify';

const EditButton = ({toUrl, content, doBefore, doAfter}) => {
    const [url ,setUrl] = useState(null);
    const {response, isPending, error} = useFetch(url, "PATCH", content);


    const handleClick = () => {
        doBefore(content);
        setUrl(() => toUrl);
    };


    useEffect(() => {
        if(!error){
            return;
        }

        toast.error(error, {
            position: "bottom-left",
            autoClose: 4000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
            theme: "colored",
        });

        setUrl(() => null);
    }, [error]);

    useEffect(() => {
        if(!response){
            return;
        }

        if(response.error){
            toast.error(response.message, {
                position: "bottom-left",
                autoClose: 4000,
                hideProgressBar: false,
                closeOnClick: true,
                pauseOnHover: true,
                draggable: true,
                progress: undefined,
                theme: "colored",
            });

            return;
        }

        toast.success(`Changes were applied successfully`, {
            position: "bottom-left",
            autoClose: 4000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
            theme: "colored",
        });               

        setUrl(() => null);
        doAfter();

    }, [response]);



    return (
        <button className="edit" onClick={() => handleClick()}>Confirm Edit</button>
    );
}
 
export default EditButton;