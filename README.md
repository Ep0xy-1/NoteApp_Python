# NoteApp_Python

📝 Notebook App (Tkinter + Python)
A simple, clean, and lightweight note-taking app built using Python and Tkinter. It allows you to create, save, rename, and delete multiple notes in one interface using tabs.

🔧 Features
Tabbed Notes Interface
Write and switch between different notes using a familiar tab system.

Create New Notes
Easily add new notes with the “New Note” button.

Rename Notes
Right-click a tab or click the “Rename Note” button to change the title of any note.

Delete Notes
Remove unwanted notes. (You must keep at least one tab open.)

Save Notes
All your notes can be saved to a local file with one click using the “Save” button.

Automatic Note Loading
On startup, any saved notes are loaded back in, so you can continue right where you left off.

📂 Storage System
All notes are saved to a file called notes_storage.json. This file is created automatically in the same directory where the script is run.

Important:
For the app to fully work (especially saving/loading), make sure the script can access or create a file called:

pgsql
Copy
Edit
notes_storage.json
This is where all your notes will be stored in JSON format. If the file is missing, it will be created when you save notes for the first time.

🚀 How to Run
Make sure you have Python installed (Python 3.6+ recommended).

Save the script (e.g., notebook_app.py).

Open a terminal or command prompt.

Run the app using:

bash
Copy
Edit
python notebook_app.py
📌 Requirements
This app only uses standard Python libraries:

tkinter (comes with Python)

json

os

You don’t need to install any external packages.

🧠 Extra Info
Notes are saved only when you click the “Save” button.

Right-click on any tab title to quickly rename it.

If you try to delete the last remaining tab, the app will show an error message to prevent data loss.

Enjoy writing your thoughts and to-do lists in a simple, local notebook app that just works — no cloud, no login, no distractions.

Made in 02/07/2025
