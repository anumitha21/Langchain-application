# 🌍 LangTrans 


LangChain LCEL Translation Chain using Groq

This project demonstrates the use of LangChain Expression Language (LCEL) to build a translation pipeline. It takes a text input and a target language, then uses Groq's language model to generate an accurate and context-aware translation.

This project provides a **FastAPI-based translation server** powered by **LangChain**, **LangServe**, and **Groq's Gemma model**. It also includes a **Jupyter Notebook (LCEL.ipynb)** that demonstrates the same functionality interactively.

---

## 📚 Contents

- ✅ API Server using FastAPI and LangServe
- ✅ Interactive LangChain Chain via Jupyter Notebook (`LCEL.ipynb`)
- ✅ Uses `gemma2-9b-it` from Groq
- ✅ Chain created using LangChain Expression Language (LCEL)

---

## 🛠️ Technologies Used

- Python
- FastAPI
- LangChain
- LangServe
- Groq Model via `langchain_groq`
- Python-dotenv
- Uvicorn
- Jupyter Notebook

---

## 📁 Folder Structure

```

.
├── LCEL.ipynb              # Jupyter notebook demo of the LangChain chain
├── main.py                 # FastAPI application to expose the chain
├── .env                    # Contains GROQ\_API\_KEY
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

````

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/langchain-translation-api.git
cd langchain-translation-api
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

Add the following to `requirements.txt` if not already present:

```txt
fastapi
langchain
langserve
langchain-groq
python-dotenv
uvicorn
notebook
```

---

## 🔐 Environment Variables

Create a `.env` file with your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Visit Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔄 API Endpoint

### `POST /chain/invoke`

#### Example Input:

```json
{
  "input": {
    "language": "French",
    "text": "Good morning"
  }
}
```

#### Example Output:

```json
{
  "output": "Bonjour"
}
```

---

## 🧪 Jupyter Notebook Usage

To run interactively:

```bash
jupyter notebook LCEL.ipynb
```

* The notebook demonstrates creating a LangChain chain using LCEL.
* It accepts a language and text input to generate a translation using Groq's model.

---

## 📬 License

MIT License

---

## 🙌 Acknowledgments

* [LangChain](https://www.langchain.com/)
* [Groq](https://groq.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [LangServe](https://github.com/langchain-ai/langserve)



