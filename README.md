# NoteApp_Python

# 📝 Notebook App

A simple note-taking desktop application built with Python and Tkinter. This app lets you create, rename, delete, and save multiple notes — all organized neatly in tabs.

---

## 💡 Features

- 🗂 **Tabbed Interface** — Work on multiple notes at once using tabbed navigation.
- ➕ **Create Notes** — Add new notes with a single click.
- ✏️ **Rename Tabs** — Easily rename notes via right-click or the "Rename" button.
- 🗑 **Delete Notes** — Remove unwanted notes (at least one tab must remain).
- 💾 **Save Notes** — Save all your notes to a local JSON file.
- 🔁 **Auto-Load on Startup** — Previously saved notes are automatically restored when you reopen the app.

---

## 📂 Note Storage

All notes are saved locally in a file called `notes_storage.json`, which is created in the same directory as the app.

> **Note:** The app depends on `notes_storage.json` to fully function. If it doesn’t exist, it will be created automatically when you save your first note.

---

## 🚀 Getting Started

### Requirements

- Python 3.6 or higher
- No external libraries required — everything uses built-in Python modules

### How to Run

```bash```
git clone https://github.com/yourusername/notebook-app.git
cd notebook-app
python notebook_app.py


## 🛠 Tech Stack
Python 3
Tkinter for GUI
JSON and os for file handling

## 📌 Notes
Make sure the script has permission to read/write in the directory, as it saves data to notes_storage.json.

Rename tabs by right-clicking on them or using the "Rename Note" button.

### 🖼 Optional Screenshot
You can add a screenshot here to show off the UI. Save it as screenshot.png and update the path in the README.md.

## ✅ To-Do / Ideas for Future
 Dark mode

 Autosave feature

 Font and theme customization

 Export notes to .txt or .pdf

Made in 02/07/2025
