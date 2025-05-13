
# 🧠💚🖥️ NVIDIA LLM PDF Chatbot

A powerful and interactive chatbot built with **LangChain**, **Streamlit**, and **NVIDIA NIM** that lets you ask questions based on the content of PDF files in real-time. 📄🤖

---

## 🚀 Features

- 🔍 Extracts and embeds text from PDFs using `NVIDIAEmbeddings`
- 🧠 Uses `nvidia/llama-3.1-nemotron-ultra-253b-v1` model for intelligent Q&A
- 💾 Caches vector embeddings using FAISS for fast retrieval
- 🧩 Built with modular LangChain components
- 🌐 User-friendly interface with Streamlit

---

## 📂 Folder Structure

```

📁 project-root/
┣ 📁 data/
┃ ┗ 📄 your-pdfs-here.pdf
┣ 📄 app.py
┗ 📄 README.md

````

---

## ⚙️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/nvidia-llm-pdf-chatbot.git
cd nvidia-llm-pdf-chatbot
````

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set your NVIDIA API key** in the code or your environment:

```python
os.environ['NVIDIA_API_KEY'] = "your-nvidia-api-key"
```

---

## ▶️ Run the App

```bash
streamlit run final_app.py
```

Open your browser at `http://localhost:8501` and start chatting! 🧠💬

---

## 📘 How It Works

1. Upload or place your PDF files inside the `./data` folder.
2. Click **"Document Embeddings"** to process the documents.
3. Ask any question related to the content of your PDFs.
4. Get accurate answers along with document excerpts used for answering.

---

## 🛠️ Built With

* [LangChain](https://www.langchain.com/)
* [Streamlit](https://streamlit.io/)
* [NVIDIA NIM + LLM](https://developer.nvidia.com/)
* [FAISS](https://github.com/facebookresearch/faiss)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to ⭐ the repo if you find it useful!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> Made with 💚 using NVIDIA tech & LangChain magic.
