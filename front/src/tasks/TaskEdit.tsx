import React, { useState, useEffect } from "react";
import DateTimePicker from "react-datetime-picker";
import "react-datetime-picker/dist/DateTimePicker.css";
import "react-calendar/dist/Calendar.css";
import "react-clock/dist/Clock.css";
import { CategoryName, PriorityLevel, ProgressStatus, Task } from "./Task";

type TaskEditProps = {
  task: Task;
};

type ValuePiece = Date | null;

type Value = ValuePiece | [ValuePiece, ValuePiece];

export const TaskEdit: React.FunctionComponent<TaskEditProps> = ({ task }) => {
  const [editedTask, setEditedTask] = useState<Task>(task);
  const [dueTo, setDueTo] = useState<Value>(
    task.due_to
      ? new Date(new Date(task.due_to).toISOString().substring(0, 23))
      : new Date(Date.now()),
  );

  useEffect(() => {
    setEditedTask(task);
  }, [task]);

  useEffect(() => {
    console.log("Updated task:", editedTask);
  }, [editedTask]);

  function handleInputChange(
    event: React.ChangeEvent<
      HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
    >,
  ) {
    const { name, value } = event.target;
    setEditedTask((prevTask) => ({ ...prevTask, [name]: value }));
  }

  function handleSubmit(event: React.FormEvent) {
    event.preventDefault();

    const dueToString =
      dueTo instanceof Date ? dueTo.toISOString().substring(0, 23) : null;

    setEditedTask((prevTask) => ({
      ...prevTask,
      due_to: dueToString! + "Z",
    }));
  }

  function generateOptions<T extends { [name: string]: string }>(
    optionsProvider: T,
  ): JSX.Element[] {
    return Object.entries(optionsProvider).map((entry) => {
      const [key, value] = entry;
      return (
        <option key={key} value={value}>
          {value}
        </option>
      );
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Edit task</h2>
      <label htmlFor="title">Title:</label>
      <input
        type="text"
        name="title"
        id="title"
        value={editedTask.title}
        onChange={handleInputChange}
      />

      <label htmlFor="description">Description:</label>
      <textarea
        name="description"
        id="description"
        value={editedTask.description}
        onChange={handleInputChange}
      />

      <label htmlFor="last_modified">Last modified:</label>
      <input
        type="datetime-local"
        name="last_modified"
        id="last_modified"
        defaultValue={
          editedTask.last_modified &&
          new Date(editedTask.last_modified).toISOString().substring(0, 23)
        }
        onChange={handleInputChange}
        readOnly
      />

      <label htmlFor="due_to">Due to:</label>
      <DateTimePicker
        name="due_to"
        id="due_to"
        value={dueTo}
        onChange={setDueTo}
      />

      <label htmlFor="category">Category:</label>
      <select
        name="category"
        id="category"
        onChange={handleInputChange}
        value={editedTask.category.name}
      >
        {generateOptions(CategoryName)}
      </select>

      <label htmlFor="priority">Priority:</label>
      <select
        name="priority"
        id="priority"
        onChange={handleInputChange}
        value={editedTask.priority.level}
      >
        {generateOptions(PriorityLevel)}
      </select>

      <label htmlFor="progress">Progress:</label>
      <select
        name="progress"
        id="progress"
        onChange={handleInputChange}
        value={editedTask.progress.status}
      >
        {generateOptions(ProgressStatus)}
      </select>

      <button type="submit">Submit</button>
    </form>
  );
};
