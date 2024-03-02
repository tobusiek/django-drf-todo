import React from "react";
import { Task } from "./Task";

type TaskViewProps = {
  task: Task;
};

export const TaskView: React.FunctionComponent<TaskViewProps> = ({ task }) => {
  return (
    <div>
      <p>
        <span>{task.title}</span>
        <span>{task.progress.status}</span>
        <span>{task.category.name}</span>
        <span>{task.due_to && new Date(task.due_to).toString()}</span>
      </p>
    </div>
  );
};
