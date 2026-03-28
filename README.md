# 📇 Persistent Contact Book (Python CLI)

A command-line Contact Book application built using Python that stores contacts permanently using file handling.

Unlike basic programs where data disappears after closing, this version saves contacts to a file and loads them automatically when the program restarts.

---

## 🚀 Features

* ➕ Add new contacts
* 📋 View all contacts
* 🔍 Search contact by name
* ❌ Delete contact
* 💾 Automatic file saving
* 📂 Auto-load saved contacts on startup

---

## 🛠 Technologies Used

* Python 3
* Dictionary (HashMap concept)
* File Handling (`read` and `write` modes)
* `os` module
* CLI (Command Line Interface)

---

## 📂 Project Structure

```
contact_book_file.py
contacts.txt
README.md
```

---

## ▶️ How It Works

1. When the program starts:

   * It checks if `contacts.txt` exists.
   * If it exists, it loads saved contacts into memory.

2. When adding or deleting a contact:

   * The dictionary updates.
   * The file is rewritten automatically.

This ensures data persistence.

---

## ▶️ How to Run

1. Clone the repository:

```
git clone <your-repository-link>
```

2. Navigate into the folder:

```
cd persistent-contact-book-python
```

3. Run the program:

```
python contact_book_file.py
```

---

## 🧠 Concepts Practiced

* Dictionaries (Key-Value storage)
* File handling with `open()`
* Context manager using `with`
* String manipulation (`split()`, `strip()`)
* Data persistence logic
* Menu-driven program design

---

## 📈 Future Improvements

* Update existing contacts
* Add email field
* Prevent duplicate entries
* Convert into GUI version
* Store data using JSON format

---

## 🎓 Learning Outcome

This project strengthens understanding of:

* Permanent data storage
* File I/O operations
* Basic database-like logic
* Real-world application flow

---

## 👨‍💻 Author

Built as part of a structured Python + DSA roadmap from beginner to advanced level.

---

⭐ If you find this useful, consider giving it a star!

