import React, { useState, useEffect } from "react";
import Card from "../Components/Card/Card";
import Form from "../Components/Form/Form";

const TodoPage = () => {
  const [todo, setTodo] = useState([]);

  useEffect(() => {
    fetch("/api")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((data) => setTodo(data));
  }, []);
  return (
    <>
      <Form />
      <Card listOfTodos={todo} />
    </>
  );
};

export default TodoPage;
