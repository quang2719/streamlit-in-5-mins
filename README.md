# Streamlit in 5 Minutes - From Basics to Real-world Applications

## 📝 Introduction

This is a comprehensive Streamlit tutorial project that takes you from beginner to advanced level in just 5 minutes. The project includes 3 web applications built with Streamlit, ranging from basic component familiarization to real-world applications with data analysis and user authentication features.

**Special Feature**: All applications are generated from a single Jupyter Notebook file (`main.ipynb`) using the `%%writefile` command - a brilliant approach for development and code organization!

## 🗂️ Project Structure

```
streamlit-in-5-mins/
├── README.md
├── basic_web_deploy_streamlib/
│   ├── main.ipynb          # Main file - Jupyter Notebook
│   ├── app.py              # App 1: Basic tutorial
│   ├── app2.py             # App 2: Student score analysis  
│   ├── app3.py             # App 3: Calculator with authentication
│   ├── assets/             # Images and media folder
│   └── data/               # Sample data folder
```

## 🎯 Main Objectives of `main.ipynb`

The `main.ipynb` file is the heart of this project, designed with 3 main purposes:

### 1️⃣ **Basic Streamlit Tutorial** 
Comprehensive description of Streamlit's basic functions with detailed comments. Try each code segment with different functionalities and observe the step-by-step changes in the web page.

### 2️⃣ **Real-world Data Analysis Application**
A simple web application for analyzing and visualizing student score distributions.

### 3️⃣ **Application with User Authentication** 
A web application with user authentication for user authorization and a simple factorial calculation feature.

---

## 🚀 I. Basic Streamlit Tutorial (app.py)

### Description
This first app introduces all the basic components of Streamlit:
- Text display (title, header, subheader, caption)
- Markdown and LaTeX
- Media display (images, audio, video)
- Input widgets (checkbox, radio, selectbox, slider)
- Basic charts

### Run the application
```bash
streamlit run app.py
```

### Key Features
- 📝 Text display with various formats
- 🎨 Markdown and mathematical formula support
- 🖼️ Media display (images, audio, video)
- 🎛️ Interactive widgets (checkbox, radio, slider, input)
- 📊 Basic data charts

---

## 📊 II. Student Score Analysis (app2.py)

![Pipeline](./basic_web_deploy_streamlib/assets/pipeline.png)

### Description
A web application for analyzing and visualizing student score distributions from Excel files.

![Demo](./basic_web_deploy_streamlib/assets/image1.png)

### Run the application
```bash
streamlit run app2.py
```

### Features
- 📁 Upload Excel files containing score data
- 📈 Calculate average scores
- 📊 Analyze score distribution by ranges:
  - ≥ 80: Excellent
  - 60-79: Good  
  - 40-59: Average
  - < 40: Poor
- 🥧 Display pie chart for score distribution

### Sample Data
Use the file `data/diem_hoc_sinh.xlsx` to test the application.

---

## 🔐 III. Calculator with Authentication (app3.py)

![Demo Calculator](./basic_web_deploy_streamlib/assets/image2.png)

### Description
A factorial calculator application with simple user authentication system.

![Calculator Interface](./basic_web_deploy_streamlib/assets/factorial.png)

### Run the application
```bash
streamlit run app3.py
```

### Features
- 🔐 **Login System**: Only authorized users can access
- 🧮 **Factorial Calculator**: Calculate factorial of numbers from 0-50
- 💾 **Caching**: Uses `@st.cache_data` for performance optimization  
- 👤 **Session State**: Manages login state
- 🚪 **Logout**: Safe logout functionality

### Test Accounts
- Username: `admin` or `manager`
- No password required (simple demo)

---

## 🛠️ Installation and Setup

### System Requirements
- Python 3.7+
- Streamlit
- Pandas
- Matplotlib
- Pillow

### Installation
```bash
# Clone repository
git clone <repository-url>
cd streamlit-in-5-mins

# Install dependencies
pip install streamlit pandas matplotlib pillow openpyxl

# Run Jupyter Notebook (optional)
jupyter notebook basic_web_deploy_streamlib/main.ipynb
```

### Run Individual Applications
```bash
cd basic_web_deploy_streamlib

# App 1: Basic tutorial
streamlit run app.py

# App 2: Score analysis
streamlit run app2.py  

# App 3: Calculator with auth
streamlit run app3.py
```

## 💡 Special Feature - Using `%%writefile`

A brilliant aspect of this project is the use of the `%%writefile` command in Jupyter Notebook to create Python files:

```python
%%writefile app.py
import streamlit as st
# Application content...
```

This approach provides:
- ✅ Scientific code organization
- ✅ Easy experimentation and editing
- ✅ Run and test directly in notebook
- ✅ Create independent files for deployment

## 🎓 Conclusion

This project provides a complete Streamlit learning path from basic to advanced. You will learn:

1. **Basic components** of Streamlit UI
2. **Building real applications** with data processing and visualization  
3. **State management and authentication** for web applications

Try each application and experience the power of Streamlit in creating web apps with just Python! 🐍✨

---

## 📞 Contact

If you have questions or want to contribute to the project, please create an issue or pull request.

**Happy Coding!** 🚀