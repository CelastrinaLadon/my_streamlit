Profile Page with Configurable Settings

This project is a customizable profile page built using Streamlit. The application allows users to configure LinkedIn and CV details, along with other content, through a config.json file for easy management.

Features

Streamlit-based UI: A simple, interactive, and user-friendly interface.

Configurable Details: Manage profile information such as LinkedIn URL and CV links directly from the config.json file.

Reusable and Maintainable: Designed to simplify customization and configuration without modifying the core code.

Setup and Installation

Clone the repository:

git clone <repository_url>
cd <repository_name>

Install the required dependencies:

pip install -r requirements.txt

Prepare the config.json file:

Add or edit the LinkedIn and CV details in the config.json file as per the example below.

Run the application:

streamlit run app.py

Configuration

Edit the config.json file to update profile details. Example:

{
  "linkedin": "https://www.linkedin.com/in/your-profile",
  "cv": "https://example.com/your-cv.pdf",
  "details": {
    "name": "Your Name",
    "title": "Your Title",
    "description": "A brief description about yourself."
  }
}

How It Works

The application reads the config.json file at runtime.

Dynamic fields like LinkedIn and CV links are rendered in the profile page based on the JSON configuration.

Contributions

Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

