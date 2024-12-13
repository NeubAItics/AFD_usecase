# **Virtual Finance Assistant**

A Streamlit-based application for analyzing financial documents using OpenAI's GPT API. This app allows users to upload balance sheets or other financial images, process their content, and get insightful analysis.

---

## **Live Demo**
🚀 Try the application now: [Virtual Finance Assistant App](https://virtual-finance-assistant.streamlit.app/)


---

## **Features**
- 📄 Upload financial documents as images.
- 💡 Leverage OpenAI's GPT models for intelligent analysis.
- 📊 Get meaningful insights into financial ratios and metrics.
- 🔒 Securely handle API keys using Streamlit secrets.

---

## **Requirements**
- Python 3.9 or higher.
- OpenAI API key for GPT model access.
- Virtual environment for dependency management.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/Analyze-Financial-Documents.git
cd Analyze-Financial-Documents
```

### **2. Create and Activate a Virtual Environment**
- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **Setup**

### **1. Obtain OpenAI API Key**
- Visit [OpenAI's API page](https://platform.openai.com/account/api-keys) to generate your API key.

### **2. Configure API Key**
- Add your API key to the `secrets.toml` file for secure storage:
  - Create the `.streamlit` directory if it doesn't exist:
    ```bash
    mkdir .streamlit
    ```
  - Create a `secrets.toml` file inside the `.streamlit` directory:
    ```plaintext
    [general]
    OPENAI_API_KEY = "your_openai_api_key_here"
    ```

### **3. Verify `.gitignore`**
Ensure the `.streamlit/secrets.toml` file is excluded from version control. This is handled in `.gitignore`:
```plaintext
# Add this line to .gitignore
.streamlit/secrets.toml
```

---

## **Running the Application**

### **1. Start the Streamlit App**
Run the application locally using Streamlit:
```bash
streamlit run app.py
```

### **2. Access the Application**
- Open your browser and navigate to the URL provided by Streamlit (e.g., `http://localhost:8501`).

---

## **Project Structure**

```
Analyze-Financial-Documents/
├── .gitignore                # Excludes sensitive files from version control
├── .streamlit/
│   └── secrets.toml          # Secure storage for OpenAI API key
├── app.py                    # Main application script
├── requirements.txt          # List of required Python dependencies
├── venv/                     # Virtual environment directory
└── README.md                 # Project documentation
```

---

## **Notes**
1. **API Usage**: Be mindful of OpenAI API usage limits and billing.
2. **Environment Variables**: For deployment, ensure the API key is securely stored in the hosting environment.
3. **Dependencies**: Use `requirements.txt` to ensure compatibility across environments.

---

## **License**

This project is licensed under the [MIT License](LICENSE).