<h1 align="center">
🎓 Education Center Management System (CLI)
</h1>

<p align="center">

A modern, scalable and object-oriented Education Center Management System built with Python.

</p>

---

<p align="center">

<img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/CLI-Terminal-111827?style=for-the-badge&logo=gnubash&logoColor=white"/>
<img src="https://img.shields.io/badge/OOP-Clean%20Architecture-16A34A?style=for-the-badge"/>
<img src="https://img.shields.io/badge/JSON-Database-F59E0B?style=for-the-badge"/>

<br>

<img src="https://img.shields.io/github/stars/javlonbeksaidov-developer/education-center-managent-cli?style=for-the-badge&logo=github"/>
<img src="https://img.shields.io/github/forks/javlonbeksaidov-developer/education-center-managent-cli?style=for-the-badge&logo=github"/>
<img src="https://img.shields.io/github/issues/javlonbeksaidov-developer/education-center-managent-cli?style=for-the-badge"/>
<img src="https://img.shields.io/github/license/javlonbeksaidov-developer/education-center-managent-cli?style=for-the-badge"/>

</p>

---

<p align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=24&pause=1000&center=true&vCenter=true&width=900&lines=Education+Center+Management+System;Python+CLI+Application;Object-Oriented+Programming;JSON+Database;Clean+Architecture;Backend+Project" />

</p>

---

# 📖 About

Education Center Management System is a **Command Line Interface (CLI)** application developed in **Python** to simulate the management of a real education center.

The project follows **Object-Oriented Programming (OOP)** principles and uses **JSON files as a lightweight local database**. It is designed as a portfolio project to practice clean architecture, modular programming, CRUD operations, inheritance, validation, and file management.

> **Goal:** Build a maintainable, extensible and professional CLI application that can later be migrated to **SQLite**, **PostgreSQL**, or **Django** without major architectural changes.

---

# ✨ Features

| Module | Description | Status |
|----------|------------|:------:|
| 🔐 Authentication | Login & Logout | ✅ |
| 👤 User Management | Base User Model | ✅ |
| 👨‍🎓 Student Management | Full CRUD | ✅ |
| 👨‍🏫 Teacher Management | Full CRUD | ✅ |
| 📚 Course Management | Full CRUD | ✅ |
| 👥 Group Management | CRUD & Student Assignment | 🚧 |
| 💳 Payment Management | Payment Tracking | 🚧 |
| 📅 Attendance Management | Attendance Records | 🚧 |
| 🔍 Search System | Search by ID & Username | ✅ |
| 📝 Validation | Input Validation | ✅ |
| 💾 JSON Database | Persistent Storage | ✅ |

---

# 🛠 Built With

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| JSON | Local Database |
| datetime | Date & Time |
| calendar | Date Validation |
| UUID / Custom ID | Unique Identifiers |
| OOP | Project Architecture |

---

# 📂 Project Structure

```text
education-center-management-cli/
│
├── data/
│   ├── attendance.json
│   ├── courses.json
│   ├── groups.json
│   ├── ids.json
│   ├── payments.json
│   ├── students.json
│   ├── teachers.json
│   └── users.json
│
├── database/
│   └── json_service.py
│
├── menu/
│   ├── menu_admin.py
│   ├── menu_student.py
│   ├── menu_teacher.py
│   └── menu.py
|
├── models/
│   ├── admin.py
│   ├── attendance.py
│   ├── course.py
│   ├── group.py
│   ├── payment.py
│   ├── student.py
│   ├── teacher.py
│   └── user.py
│
├── panel/
│   ├── panel_admin.py
│   ├── panel_student.py
│   └── panel_teacher.py
|
├── services/
│   ├── attendance_service.py
│   ├── auth_service.py
│   ├── course_service.py
│   ├── group_service.py
│   ├── payment_service.py
|   ├── teacher_service.py
│   ├── student_service.py
│   └── user_service.py
│
├── utils/
│   ├── generator.py
│   └── validator.py
│
├── config.py
├── main.py
└── README.md
```

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/javlonbeksaidov-developer/education-center-managent-cli.git

# Navigate to the project
cd education-center-managent-cli

# Run the application
python main.py
```

---

# 🔄 Application Flow

```mermaid
flowchart TD

START(Start)

LOGIN(Login)

ROLE{Role}

ADMIN(Admin Panel)

TEACHER(Teacher Panel)

STUDENT(Student Panel)

SERVICES(Services)

DATABASE(JSON Database)

END(Exit)

START --> LOGIN

LOGIN --> ROLE

ROLE --> ADMIN

ROLE --> TEACHER

ROLE --> STUDENT

ADMIN --> SERVICES

TEACHER --> SERVICES

STUDENT --> SERVICES

SERVICES --> DATABASE

DATABASE --> END
```

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

<p align="center">

<a href="https://github.com/javlonbeksaidov-developer/education-center-managent-cli">
<img src="https://img.shields.io/badge/⭐_Star_This_Repository-GitHub-gold?style=for-the-badge">
</a>

</p>

---

# ❤️ Thanks for Visiting

<p align="center">

**Happy Coding! 🚀**

</p>

<!-- ========================================================== -->
<!--                        FOOTER                              -->
<!-- ========================================================== -->

<p align="center">

Made with ❤️ using Python by **Javlonbek Saidov**

</p>