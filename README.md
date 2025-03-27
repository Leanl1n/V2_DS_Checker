# DeepSeek Text Processor

A Streamlit application for processing text using the DeepSeek API.

## Project Structure
```
deepseek-streamlit-app
├── src
│   ├── app.py
│   ├── services
│   │   └── deepseek_service.py
│   ├── utils
│   │   └── file_handler.py
│   └── config
│       └── settings.py
├── requirements.txt
└── README.md
```

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in your DeepSeek API credentials
4. Run the app: `streamlit run src/app.py`