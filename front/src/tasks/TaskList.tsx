import { useEffect, useState } from "react";
import axios from "axios";
import { Task } from "./Task";
import { TaskEdit } from "./TaskEdit";
import { TaskView } from "./TaskView";

export const TaskList: React.FunctionComponent = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [selectedTask, setSelectedTask] = useState<Task | null>(null);

  useEffect(() => {
    axios
      .get("http://localhost:8000/tasks/")
      .then((res) => {
        setTasks(res.data?.results);
      })
      .catch((err) => console.log(err));
  }, []);

  function handleTaskClick(task: Task) {
    setSelectedTask(task);
  }

  return (
    <div>
      <h2>Tasks:</h2>
      <ul>
        {tasks.map((task) => {
          return (
            <li key={task.slug} onClick={() => handleTaskClick(task)}>
              <TaskView task={task} />
            </li>
          );
        })}
      </ul>
      {selectedTask && <TaskEdit task={selectedTask} />}
    </div>
  );
};
