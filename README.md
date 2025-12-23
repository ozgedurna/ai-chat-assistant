# AI Chat Assistant

Production-ready AI assistant powered by Google Gemini AI. Full-stack application using FastAPI backend, Streamlit frontend, and Docker containerization.

## Requirements

- Docker Desktop (running)
- VS Code
- Git
- Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ozgedurna/ai-chat-assistant.git
cd ai-chat-assistant
code .
```

### 2. Configure API Key

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your Gemini API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run with Docker

```bash
docker-compose up --build
```

The application will start:
- **Frontend (Streamlit):** http://localhost:8501
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs

### 4. Stop the Application

```bash
# Press Ctrl + C in terminal, or:
docker-compose down
```

## Project Structure

```
ai-chat-assistant/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile
├── frontend/
│   ├── streamlit_app.py    # Streamlit UI
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .env.example            # API key template
├── .gitignore
└── README.md
```

## Features

- Google Gemini AI integration
- Modern responsive UI with Streamlit
- RESTful API with FastAPI
- Docker containerization for easy deployment
- Chat history support
- Adjustable AI parameters (temperature, max tokens)
- Interactive API documentation (Swagger/OpenAPI)
- Hot reload for development

## Development

### Edit Backend

Open `backend/app.py` in VS Code. Changes auto-reload with Docker.

### Edit Frontend

Open `frontend/streamlit_app.py` in VS Code. Changes auto-reload with Streamlit.

### View Logs

```bash
docker-compose logs -f
```

## Troubleshooting

### Docker Issues

```bash
docker-compose down
docker-compose up --build
```

### Port Already in Use

Edit `docker-compose.yml` to change ports:
- Change `8000:8000` to `8001:8000`
- Change `8501:8501` to `8502:8501`

### API Key Errors

- Verify `.env` file exists in project root
- Check API key is valid
- Restart Docker: `docker-compose restart`

## Technology Stack

- **Backend:** FastAPI, Python 3.11, Uvicorn
- **Frontend:** Streamlit
- **AI:** Google Gemini API
- **Deployment:** Docker, Docker Compose

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Docker Documentation](https://docs.docker.com/)

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Open a Pull Request

## License

MIT License - feel free to use this project for learning and development.

## Author

Built with FastAPI, Streamlit, and Docker.
