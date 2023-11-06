
# Streamlit Multi-Page App with Google Authentication

This application integrates two separate Streamlit apps into a single multi-page application with Google authentication.

## Structure

The project is structured as follows:

- `pages/`: Directory containing individual Streamlit apps as modules.
- `streamlit_app.py`: The main entry point for the multi-page Streamlit app.
- `requirements.txt`: The Python requirements file for the application.
- `Dockerfile`: Instructions for building the Docker container for this app.
- `.dockerignore`: Specifies patterns that should be ignored by Docker.
- `.env`: An environment variables file template for configuration (rename to .env and fill in the values).

## Setup

### Local Development

1. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit app locally:
   ```
   streamlit run streamlit_app.py
   ```

### Docker Deployment

1. Build the Docker image:
   ```
   docker build -t streamlit-multi-app .
   ```

2. Run the Docker container:
   ```
   docker run -p 8501:8501 streamlit-multi-app
   ```

## Configuration

Before running the app, ensure you have a `.env` file with the necessary environment variables set, including:

- Google OAuth client ID and secret
- Any database configuration if used by the apps
- Any other service credentials (e.g., OpenAI API key)

## Usage

Once the application is running, navigate to the provided URL (usually `http://localhost:8501`) and use the sidebar to switch between different Streamlit applications.

For detailed instructions on setting up Google authentication and configuring the `.env` file, refer to the official Streamlit and Google OAuth documentation.

## Production Deployment

For production deployment, use the `docker-compose.yml` (to be created) with the Docker and `.env` configurations. Ensure that the Docker Compose file is set up with the correct domain and SSL configurations if needed.
