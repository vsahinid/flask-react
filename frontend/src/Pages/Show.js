import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Delete from "../Components/Delete/Delete";
import { Link } from "react-router-dom";

const Show = () => {
  const { id } = useParams();
  const [todo, setTodo] = useState([]);

  useEffect(() => {
    fetch(`/api/${id}`)
      .then((response) => response.json())
      .then((data) => setTodo(data));
  }, [id]);
  return (
    <div>
      {todo.length > 0 &&
        todo.map((data) => <div key={id}>{data.content}</div>)}
      <Delete id={id} />
      <hr />
      <Link to="/">Back to Home</Link>
    </div>
  );
};

export default Show;
