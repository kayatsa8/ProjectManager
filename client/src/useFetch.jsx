import { useState, useEffect } from 'react';
















const getPostBoby = (data) => {
  return {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  };
};
