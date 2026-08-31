<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&section=header&text=Education%20Center%20Management%20System%20(CLI)&fontSize=30&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/CLI-Terminal-111827?style=flat-square&logo=gnubash&logoColor=white"/>
<img src="https://img.shields.io/badge/OOP-Clean%20Architecture-16A34A?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/JSON-Database-F59E0B?style=flat-square&logo=json&logoColor=white"/>

</p>

---

<p align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=24&pause=1000&center=true&vCenter=true&width=900&lines=Education+Center+Management+System;Python+CLI+Application;Object-Oriented+Programming;JSON+Database;Clean+Architecture;Backend+Project" />

</p>


# 📖 About

Education Center Management System is a **Command Line Interface (CLI)** application developed in **Python** to simulate the management of a real education center.

The project follows **Object-Oriented Programming (OOP)** principles and uses **JSON files as a lightweight local database**. It is designed as a portfolio project to practice clean architecture, modular programming, CRUD operations, inheritance, validation, and file management.

> **Goal:** Build a maintainable, extensible and professional CLI application that can later be migrated to **SQLite**, **PostgreSQL**, or **Django** without major architectural changes.

---

# 🛠️ Built With

| Technology | Description |
|------------|-------------|
| 🐍 **Python 3.13** | Main programming language |
| 🏗️ **Object-Oriented Programming (OOP)** | Project architecture and code organization |
| 💾 **JSON** | Local data storage |
| 📅 **datetime** | Date and time management |
| 📆 **calendar** | Date validation |
| 🆔 **uuid** | Unique ID generation |
| 🖥️ **CLI** | Command Line Interface |
| 🧩 **Clean Architecture** | Modular project structure |
| 🔄 **CRUD** | Data management operations |
| 🌿 **Git** | Version control |
| 🐙 **GitHub** | Source code hosting |

---

# 📂 Project Structure

```text
education-center-management-cli/
│
├── data/
│   ├── attendances.json
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
│   ├── reports_service.py
│   ├── payment_service.py
|   ├── teacher_service.py
│   ├── student_service.py
│   └── user_service.py
│
├── utils/
│   ├── generator.py
│   └── validator.py
│
├── main.py
└── README.md
```

---

# 🖥️ Application Menus

## 🚀 Start Menu

```text
┌─────────────────────────────────────┐
│     EDUCATION CENTER MANAGEMENT     │
├─────────────────────────────────────┤
│ 1. Login                            │
│ 0. Exit                             │
└─────────────────────────────────────┘
```

---

## 👑 Admin Panel

```text
┌─────────────────────────────────────┐
│             ADMIN PANEL             │
├─────────────────────────────────────┤
│ 1. Profile                          │
│ 2. Students                         │
│ 3. Teachers                         │
│ 4. Courses                          │
│ 5. Groups                           │
│ 6. Payments                         │
│ 7. Attendance                       │
│ 8. Reports                          │
│ 0. Exit                             │
└─────────────────────────────────────┘
```

---

## 👨‍🎓 Student Management

```text
┌─────────────────────────────────────┐
│          STUDENT MANAGEMENT         │
├─────────────────────────────────────┤
│ 1. Add Student                      │
│ 2. Show Students                    │
│ 3. Search Student                   │
│ 4. Update Student                   │
│ 5. Delete Student                   │
│ 6. Student Block / Activate         │
│ 0. Back                             │
└─────────────────────────────────────┘
```

---

## 👨‍🏫 Teacher Management

```text
┌─────────────────────────────────────┐
│          TEACHER MANAGEMENT         │
├─────────────────────────────────────┤
│ 1. Add Teacher                      │
│ 2. Show Teachers                    │
│ 3. Search Teacher                   │
│ 4. Update Teacher                   │
│ 5. Delete Teacher                   │
│ 6. Block / Activate                 │
│ 0. Back                             │
└─────────────────────────────────────┘
```

---

## 📚 Course Management

```text
┌─────────────────────────────────────┐
│          COURSE MANAGEMENT          │
├─────────────────────────────────────┤
│ 1. Add Course                       │
│ 2. Show Courses                     │
│ 3. Update Course                    │
│ 4. Delete Course                    │
│ 5. Pause Course                     │
│ 0. Back                             │
└─────────────────────────────────────┘
```

---

## 👥 Group Management

```text
┌─────────────────────────────────────┐
│          GROUP MANAGEMENT           │
├─────────────────────────────────────┤
│ 1. Create Group                     │
│ 2. Show Groups                      │
│ 3. Add Student                      │
│ 4. Remove Student                   │
│ 5. Update Group                     │
│ 6. Delete Group                     │
│ 7. Pause Group                      │
│ 0. Back                             │
└─────────────────────────────────────┘
```

---

## 💳 Payment Management

```text
┌─────────────────────────────────────┐
│         PAYMENT MANAGEMENT          │
├─────────────────────────────────────┤
│ 1. Add Payment                      │
│ 2. Payment History                  │
│ 3. Unpaid Students                  │
│ 4. Delete Payment                   │
│ 5. Search Payment                   │
│ 0. Back                             │
└─────────────────────────────────────┘
```

---

## 📅 Attendance Management

```text
┌─────────────────────────────────────┐
│       ATTENDANCE MANAGEMENT         │
├─────────────────────────────────────┤
│ 1. Take Attendance                  │
│ 2. Show Attendance                  │
│ 3. Student Attendance               │
│ 0. Back                             │
└─────────────────────────────────────┘
```

---

## 📊 Reports

```text
┌─────────────────────────────────────┐
│               REPORTS               │
├─────────────────────────────────────┤
│ 1. Total Users                      │
│ 2. Total Students                   │
│ 3. Total Teachers                   │
│ 4. Total Groups                     │
│ 5. Total Courses                    │
│ 6. Total Attendances                │
│ 7. Total Payments                   │
│ 8. Total IDs                        │
│ 0. Back                             │
└─────────────────────────────────────┘
```

---

## 👨‍🏫 Teacher Panel

```text
┌─────────────────────────────────────┐
│            TEACHER PANEL            │
├─────────────────────────────────────┤
│ 1. My Profile                       │
│ 2. My Groups                        │
│ 3. Attendance                       │
│ 4. Payments                         │
│ 0. Exit                             │
└─────────────────────────────────────┘
```

---

## 👨‍🎓 Student Panel

```text
┌─────────────────────────────────────┐
│            STUDENT PANEL            │
├─────────────────────────────────────┤
│ 1. My Profile                       │
│ 2. My Group                         │
│ 3. Students                         │
│ 4. Attendance                       │
│ 0. Exit                             │
└─────────────────────────────────────┘
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

<div align="center">

# 👨‍💻 Author

<table align="center">
<tr>
<td align="center" width="220">

<img src="https://github.com/javlonbeksaidov-developer.png" width="150" height="150" style="border-radius:50%;" />

</td>

<td align="center">

<h3>SOFTWARE ENGINEER</h3>

<h3>Connect with me</h3>

<p align="center"><a href="https://t.me/saidov_1701"><img src="https://img.icons8.com/fluency/64/telegram-app.png" width="45" alt="Telegram"/></a>&nbsp;&nbsp;&nbsp;<a href="https://instagram.com/#"><img src="https://img.icons8.com/fluency/64/instagram-new.png" width="45" alt="Instagram"/></a>&nbsp;&nbsp;&nbsp;<a href="https://facebook.com/javlonbeksaidov.developer"><img src="https://img.icons8.com/fluency/64/facebook-new.png" width="45" alt="Facebook"/></a>&nbsp;&nbsp;&nbsp;<a href="https://youtube.com/@JavlonbekSaidov-Developer"><img src="https://img.icons8.com/fluency/64/youtube-play.png" width="45" alt="YouTube"/></a>&nbsp;&nbsp;&nbsp;<a href="javlonbeksaidov09@gmail.com"><img src="https://img.icons8.com/fluency/64/gmail-new.png" width="45" alt="Gmail"/></a></p>

</td>
</tr>
</table>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=2500&pause=1000&center=true&vCenter=true&width=650&lines=Javlonbek+Saidov+Alijon+o%27g%27li;Python+Backend+Developer" alt="Typing SVG" />

<br><br>

<strong>⭐ If you like this project, don't forget to give it a star!</strong>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer&animation=fadeIn" width="100%"/>
