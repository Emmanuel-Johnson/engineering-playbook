import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";

function Todo() {
  const [text, setText] = useState("");

  const todos = useSelector((state) => state.todos);

  const dispatch = useDispatch();

  function handleAdd() {
    dispatch({
      type: "ADD_TODO",
      payload: text,
    });

    setText("");
  }

  return (
    <div>
      <h1>Todo App</h1>

      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter todo"
      />

      <button onClick={handleAdd}>
        Add Todo
      </button>

      <ul>
        {todos.map((todo, index) => (
          <li key={index}>{todo}</li>
        ))}
      </ul>
    </div>
  );
}

export default Todo;