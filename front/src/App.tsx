import React from "react";
import { TaskList } from "./tasks/TaskList";

export const App: React.FunctionComponent = () => {
  return (
    <div className="App">
      <TaskList />
    </div>
  );
};
