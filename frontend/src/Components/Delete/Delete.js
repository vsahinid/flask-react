import React from "react";
import { useHistory, Link } from "react-router-dom";

const Delete = ({ id }) => {
  let history = useHistory();

  const deleteTodo = () => {
    fetch(`/api/${id}`, {
      method: "POST",
      body: JSON.stringify({
        id: id,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        history.push("/");
      });
  };
  return (
    <>
      <Link to="/">
        <button
          onClick={deleteTodo}
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
        >
          Delete
        </button>
      </Link>
    </>
  );
};

export default Delete;
