# Job Application Tracker

A command-line job application tracking application built with Python and JSON.

This application allows users to store, manage, search, update, and track job applications using a persistent JSON file. It helps organize the job search process by keeping important application details such as company name, position, application status, date applied, job link, and notes in one place.

---

## Features

- Add new job applications
- View all saved applications
- Search applications by company name or position title
- Update application status
- Delete applications
- Filter applications by status
- Automatic date tracking when applications are added
- Predefined application statuses for consistency
- Persistent JSON data storage
- Case-insensitive searching
- Menu-driven command-line interface
- Error handling for missing or invalid JSON files

---

## Application Statuses

- Applied
- Interview Scheduled
- Interviewed
- Rejected
- Offer Received

---

## Technologies Used

- Python
- JSON
- File Handling
- Datetime Module
- Git & GitHub

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/jjuuls/Job-Application-Tracker.git
```

2. Navigate to the project folder:

```bash
cd Job-Application-Tracker
```

3. Run the application:

```bash
python main.py
```

---

## Example Menu

```text
Job Application Tracker

1. Add application
2. View all applications
3. Search applications
4. Update application status
5. Delete application
6. Filter by status
7. Exit
```

---

## Example Application Record

```json
{
    "company": "Google",
    "position": "Junior Python Developer",
    "location": "Remote",
    "date_applied": "2026-05-20",
    "status": "Applied",
    "link": "https://example-job-link.com",
    "notes": "Applied through company website"
}
```

---

## Project Structure

```text
Job-Application-Tracker/
│
├── main.py
├── applications.json
├── README.md
└── .gitignore
```

---

## Future Improvements

- Edit existing application details
- Sort applications by date
- Export applications to CSV
- Application statistics dashboard
- Interview scheduling reminders
- Company contact tracking
- Resume and cover letter tracking
- Graphical User Interface (GUI)

---

## Author

Julian Gonzalez
