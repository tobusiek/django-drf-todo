export enum CategoryName {
  NONE = "",
  JOB = "Job",
  HOME = "Home",
  SHOPPING = "Shopping",
}

export type Category = {
  id: number;
  name: CategoryName;
};

export enum PriorityLevel {
  NONE = "",
  LOW = "Low",
  MID = "Medium",
  HIGH = "High",
}

export type Priority = {
  id: number;
  level: PriorityLevel;
};

export enum ProgressStatus {
  UNDONE = "Undone",
  IN_PROGRESS = "In progress",
  DONE = "Done",
  WONT_DO = "Won't do",
}

export type Progress = {
  id: number;
  status: ProgressStatus;
};

export type Task = {
  id: number;
  title: string;
  description: string;
  slug: string;
  created_at: string;
  last_modified: string;
  due_to: string | undefined;
  category: Category;
  priority: Priority;
  progress: Progress;
};
