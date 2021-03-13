import React from "react";

const Form = ({ userInput, onFormChange, onFormSubmit }) => {
  const handleChange = (event) => {
    onFormChange(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onFormSubmit();
  };
  return (
    <form onSubmit={handleSubmit} class="mb-6">
      <label
        class="mb-2 uppercase font-bold text-lg text-grey-darkest"
        for="content"
      >
        Todo
      </label>
      <input
        class="border py-2 px-3 text-grey-darkest"
        required
        onChange={handleChange}
        type="text"
        value={userInput}
      />
      <button
        type="submit"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Create Todo
      </button>
    </form>
  );
};

export default Form;
