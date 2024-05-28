# Valorant Stats App

The Valorant Stats App is a web application that allows users to view their Valorant game statistics by integrating with the Riot API. The app uses OAuth2 for secure authentication and authorization, enabling users to log in with their Riot Games account. After logging in, users can see their game stats displayed on a dashboard.

## Features

- User authentication via Riot API using OAuth2
- Fetch and display Valorant game stats
- User-friendly interface built with Bootstrap

## Project Structure

my_valorant_app/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes.py
│   ├── oauth.py
│   └── utils.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── dashboard.html
│
├── .env
├── main.py
├── pyproject.toml
└── poetry.lock

## Requirements

- Python 3.8+
- Poetry (for dependency management)
- Riot API credentials (Client ID, Client Secret, Deployment API Key)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/valorant-stats-app.git
   cd valorant-stats-app

2. **Set up environment variables:**
   Create a `.env` file in the root directory with the following content:
   ```dotenv
   RSO_BASE_URL=https://auth.riotgames.com
   RSO_CLIENT_ID=your_client_id
   RSO_CLIENT_SECRET=your_client_secret
   DEPLOYMENT_API_KEY=your_deployment_api_key
   APP_BASE_URL=http://localhost.riotgames.com:3000
   APP_CALLBACK_PATH=/oauth-callback
   RESPONSE_TYPE=code
   SCOPE=openid

3. **Add to your hosts file:**
   - **MacOS/Linux:** Append `127.0.0.1 local.exampleapp.com` to `/etc/hosts`
   - **Windows:** Append `127.0.0.1 local.exampleapp.com` to `C:\\Windows\\System32\\Drivers\\etc\\hosts`

4. **Install dependencies:**
   Use Poetry to install the necessary dependencies:
   ```sh
   pip install poetry
   poetry install

5. **Run the app:**
   Start the Flask app:
   ```sh
   poetry run python main.py

6. **Access the app:**
   Open your browser and navigate to `http://local.exampleapp.com:3000`

## Usage

1. Visit the home page and click on the "Login" button.
2. Authenticate with your Riot Games account.
3. View your Valorant stats on the dashboard.
    