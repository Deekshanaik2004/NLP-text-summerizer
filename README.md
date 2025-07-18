# NLP-text-summerizer (BERT or GPT-based)

## 📖 Project Overview

This project is a simple **Text Summarization web application** using Streamlit and Hugging Face Transformers.  
Users can input large text, and the app returns a summarized version using the **BART model** (`facebook/bart-large-cnn`) or GPT models optionally.

---

## 🚀 Technologies Used
- Python 3.9+
- Streamlit
- Hugging Face Transformers
- Pre-trained Model: `facebook/bart-large-cnn` (default)

---

## 📂 Project Structure
text_summarization_app/
├── summarizer_app.py
├── requirements.txt
├── README.md


## 💻 Installation & Running Instructions

1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/text_summarization_app.git
cd text_summarization_app
2️⃣ Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For Mac/Linux
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy
Edit
streamlit run summarizer_app.py
Open your browser and visit:
http://localhost:8501

✅ Notes
The first model download may take a few minutes depending on your internet speed.

For GPT-based summarization, integrating OpenAI API is optional and requires an API key.

✅ Author
Deeksha Naik

GitHub: https://github.com/Deekshanaik2004




