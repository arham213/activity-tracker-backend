# activity-tracker-backend

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white&style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135.1-009688?logo=fastapi&logoColor=white&style=flat-square)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-Inference_API-FFD21E?logo=huggingface&logoColor=black&style=flat-square)
![Deployed on Railway](https://img.shields.io/badge/Deployed-Railway-0B0D0E?logo=railway&logoColor=white&style=flat-square)

FastAPI inference backend for the AI activity monitoring system. Receives base64-encoded frames from the frontend, submits them to the Hugging Face image-to-text inference API, and returns generated activity captions.

**Live:** [activity-tracker-backend.up.railway.app](https://activity-tracker-backend.up.railway.app) &nbsp;|&nbsp; **Frontend:** [activity-tracker-frontend](https://github.com/arham213/activity-tracker-frontend)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI, Python |
| Inference | Hugging Face Inference API (image-to-text) |
| Deployment | Railway |

---

## Local Setup

### Prerequisites
- Python 3.9+
- Hugging Face API key

```bash
git clone https://github.com/arham213/activity-tracker-backend.git
cd activity-tracker-backend
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_api_key
ALLOWED_ORIGINS=your_frontend_url
```

> `ALLOWED_ORIGINS` is a comma-separated list of allowed frontend URLs. For production, replace with your deployed frontend URL.

```bash
uvicorn main:app --reload
```

See the [frontend README](https://github.com/arham213/activity-tracker-frontend#readme) for full frontend setup instructions.

---

[LinkedIn](https://linkedin.com/in/arhamasjid) · arhamasjid213@gmail.com
