import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import json
import os
 

class NotebookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notebook App")
        self.root.geometry("800x600")

        # Storage setup
        self.notes = {}
        self.current_file = None
        self.storage_file = "notes_storage.json"

        # Load existing notes
        self.load_notes()

        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        # Main Frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Right-click menu for renaming tabs
        self.tab_menu = tk.Menu(self.root, tearoff=0)
        self.tab_menu.add_command(label="Rename Note", command=self.rename_current_tab)

        # Bind right-click to menu
        self.notebook.bind("<Button-3>", self.show_tab_menu)

        # Control Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)

        ttk.Button(button_frame, text="New Note", command=self.add_note_tab).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save", command=self.save_notes).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Delete Note", command=self.delete_current_tab).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Rename Note", command=self.rename_current_tab).pack(side=tk.LEFT, padx=5)

        # Add default tab
        self.add_note_tab()

    def show_tab_menu(self, event):
        tab_index = self.notebook.index("@%d,%d" % (event.x, event.y))
        if tab_index >= 0:
            self.notebook.select(tab_index)
            self.tab_menu.post(event.x_root, event.y_root)

    def rename_current_tab(self):
        current_tab = self.notebook.select()
        if not current_tab:
            return

        tab_index = self.notebook.index(current_tab)
        current_title = self.notebook.tab(current_tab, "text")

        # Ask user for new name
        new_title = simpledialog.askstring(
            "Rename Note",
            "Enter new note name:",
            initialvalue=current_title,
            parent=self.root
        )

        if new_title and new_title != current_title:
            self.notebook.tab(current_tab, text=new_title)

    def add_note_tab(self, title="New Note", content=""):
        tab_frame = ttk.Frame(self.notebook)
        text_widget = tk.Text(tab_frame, wrap=tk.WORD)
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, content)

        self.notebook.add(tab_frame, text=title)
        self.notebook.select(tab_frame)

    def delete_current_tab(self):
        if len(self.notebook.tabs()) <= 1:
            messagebox.showerror("Error", "Cannot delete the last tab.")
            return

        current_tab = self.notebook.select()
        tab_index = self.notebook.index(current_tab)
        self.notebook.forget(current_tab)

    def save_notes(self):
        self.notes.clear()

        for tab_id in self.notebook.tabs():
            tab_frame = self.notebook.nametowidget(tab_id)
            text_widget = tab_frame.winfo_children()[0]
            title = self.notebook.tab(tab_id, "text")
            content = text_widget.get("1.0", tk.END).strip()

            if title and content:
                self.notes[title] = content

        # Save to file
        try:
            with open(self.storage_file, "w") as f:
                json.dump(self.notes, f, indent=4)
            messagebox.showinfo("Success", "Notes saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save notes:\n{str(e)}")

    def load_notes(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    self.notes = json.load(f)
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load notes:\n{str(e)}")
        return False

    def initialize_ui_from_storage(self):
        for title, content in self.notes.items():
            self.add_note_tab(title, content)


if __name__ == "__main__":
    root = tk.Tk()
    app = NotebookApp(root)

    if app.notes:
        # If notes were loaded, populate tabs
        app.initialize_ui_from_storage()

    root.mainloop()
