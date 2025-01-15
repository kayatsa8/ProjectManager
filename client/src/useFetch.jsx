import { useState, useEffect } from 'react';


/**
 * 
 * @param {String} url 
 * @param {String} method 
 * @param {any} dataToSend
 */
const useFetch = (url, method, dataToSend = {}) => {
  const [response, setResponse] = useState(null);
  const [isPending, setIsPending] = useState(false);
  const [error, setError] = useState(null);
  const body = getRequestBoby(method, dataToSend);

  useEffect(() => {
    if(!url){
      return;
    }

    setIsPending(true);
    setError(null);

    fetch(url, body)
    .then(res => {
      if(!res.ok){
        return res.text().then(text => { throw new Error(text) });
      }

      return res.json();
    })
    .then(data => {
      setIsPending(false);
      setResponse(r => r = data);
      setError(null);
    })
    .catch(err => {
      setIsPending(false);
      setError(err.message);
    })
  }, [url]);

  return {response, isPending, error};
};

/**
 * 
 * @param {String} method 
 * @param {any} data 
 * @returns 
 */
const getRequestBoby = (method, data) => {
  return {
    method: method,
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  };
};






export default useFetch;
