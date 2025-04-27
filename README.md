# Assignment_on_Python - Hero Vired

This assignment involved solving three major questions related to DevOps practices using **Python**, **GitHub**, and **Visual Studio Code**.

Repository Name: **Assignment_on_Python**

---

## Overall Setup
- **Created a new GitHub repository** named `Assignment_on_Python`.
- **Cloned** the repository locally using Visual Studio Code.
- **Created separate Python files** for each question.
- Followed **branching, pushing, committing** via Git and coding via Visual Studio Code.

---

## Q1: Password Strength Checker

### Visual Studio Code Work
- Created a Python file: `check_password_strength.py`.
- Implemented a function `check_password_strength(password)` to validate:
  - Minimum 8 characters
  - Contains uppercase and lowercase letters
  - Contains at least one digit
  - Contains at least one special character
- Wrote another function to **prompt the user for input** and provide feedback on the password strength.

### GitHub Work
- Added the file in a branch.
- Committed the code with a clear commit message.
- Pushed changes to GitHub.

### How to Run
```bash
python check_password_strength.py
```

---

## Q2: CPU Health Monitor

### Visual Studio Code Work
- Created a Python file: `monitor_cpu_health.py`.
- Used the `psutil` library to monitor CPU usage.
- Program keeps running and alerts if CPU usage crosses 80%.
- Handled interruptions and errors properly.

### GitHub Work
- Added the `monitor_cpu_health.py` to a new branch.
- Committed and pushed the file.

### How to Run
```bash
python monitor_cpu_health.py
```

---

## Q3: Backup Important Files

### Visual Studio Code Work
- Created a Python script: `backup.py`.
- Wrote logic to:
  - Take source and destination directory paths as command-line arguments.
  - Copy files from source to destination.
  - If a file with the same name already exists, append a timestamp.
  - Handled all possible errors like folder not found, etc.

### GitHub Work
- Created a branch for this task.
- Committed and pushed the file to the remote repository.

### How to Run
```bash
python backup.py source_folder destination_folder
```
Example:
```bash
python backup.py "/home/user/Documents" "/home/user/Backup"
```

---

## Final GitHub Workflow
- Created separate branches for each task.
- Pushed all changes to GitHub.
- Created Pull Requests (PRs) and merged into `main` branch after verifying.

---

# Key Points
- Visual Studio Code was used mainly for **coding and testing locally**.
- GitHub was used for **branching, committing, pushing, and merging pull requests**.

# Thank you!

---

### Files Summary
- `check_password_strength.py` ➔ Password validation program.
- `monitor_cpu_health.py` ➔ CPU usage monitoring.
- `backup.py` ➔ Backup script with timestamp handling.

