import tkinter as tk
from tkinter import messagebox
from storage import load_tasks, save_tasks

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Todo List")
        self.geometry("320x400")
        self.tasks = load_tasks()

        # ===== widget =====
        self.entry = tk.Entry(self, width=20, font=("Arial", 14))
        self.entry.pack(pady=10)

        add_btn = tk.Button(self, text="Add", command=self.add_task)
        add_btn.pack()

        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE, font=("Arial", 14))
        self.listbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        del_btn = tk.Button(self, text="Delete", command=self.delete_task)
        del_btn.pack(pady=5)

        self.render()

    # ===== logic =====
    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showinfo("Entry is invalid", "Please type your task.")
            return
        self.tasks.append({"text": text, "done": False})
        save_tasks(self.tasks)
        self.entry.delete(0, tk.END)
        self.render()

    def delete_task(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        self.tasks.pop(idx)
        save_tasks(self.tasks)
        self.render()

    def toggle_done(self, event):
        idx = self.listbox.curselection()[0]
        self.tasks[idx]["done"] = not self.tasks[idx]["done"]
        save_tasks(self.tasks)
        self.render()

    def render(self):
        self.listbox.delete(0, tk.END)
        for t in self.tasks:
            mark = "✅" if t["done"] else "❌"
            self.listbox.insert(tk.END, f"{mark} {t['text']}")
        # complete task by double-clicking
        self.listbox.bind("<Double-Button-1>", self.toggle_done)

if __name__ == "__main__":
    TodoApp().mainloop()
