# Hypervision Problem Selection Project

This is a simple web application built with Python and Flask. It allows users to browse and select from **20 different problem statements**. The user's name and email are then stored in a local SQLite database.

The core logic ensures that any single problem statement can only be selected a maximum of **3 times**.

## 🛠️ Technology Stack

* **Backend:** Python, Flask
* **Database:** SQLite
* **Frontend:** HTML, CSS, JavaScript
* [cite_start]**Production Server (optional):** Gunicorn [cite: 122, 123]

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    git clone [https://github.com/Rhythamverma/Hypervision_Problem_selection_project.git](https://github.com/Rhythamverma/Hypervision_Problem_selection_project.git)
    cd Hypervision_Problem_selection_project
    ```

2.  **(Recommended) Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  [cite_start]**Install the required dependencies from `requirements.txt`:** [cite: 122]
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Run the Flask application:**
    The `database.db` file and the necessary `selections` table will be created automatically on the first run.
    ```bash
    python app.py
    ```

2.  **Access the application:**
    Open your web browser and go to:
    `http://127.0.0.1:5000`

## ⚠️ Disclaimer

This is a basic project developed for a specific use case. It is **not** intended for production environments and has not been vetted for security vulnerabilities. Use at your own risk.
