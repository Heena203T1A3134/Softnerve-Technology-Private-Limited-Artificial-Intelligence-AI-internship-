# Softnerve-Technology-Private-Limited-Artificial-Intelligence-AI-internship-
# Student Management System - LLM Agent

# Project Overview
The Student Management System is an AI-powered application that uses a Large Language Model (LLM) agent to handle student queries related to books and academic topics. This system provides quick and relevant answers to questions, recommends books, papers, or articles based on the student's queries, and can handle follow-up questions to maintain context.

Features:

Query Handling: The system responds to book and topic-related questions using an LLM.
Context Awareness: The agent can maintain context and handle follow-up questions effectively.
Recommendations: Based on the student's query, the system suggests relevant books, papers, and articles.
Logging: All interactions are logged for future analysis and improvement.
Modular Design: Clean code structure with a supervisor layer, adapter layer, and LLM layer.

Setup Instructions
1. Prerequisites
Python 3.8+: Make sure you have Python installed.
Git: For cloning the repository.
Virtual Environment: (Optional but recommended) for isolated dependency management.

2. Clone the Repository
git clone https://github.com/yourusername/student-management-system-llm.git
cd student-management-system-llm

3. Create a Virtual Environment and Activate It

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install Dependencies

pip install -r requirements.txt

5. Setup Logging
Ensure the logs directory exists:
mkdir logs

6. Run the Application
Using Streamlit, you can start the application with:

streamlit run app/main.py

# Usage Instructions
Access the Application: Once the application is running, open your web browser and navigate to http://localhost:8501.

Ask a Question: Use the text input box to ask questions related to books or academic topics. For example:

"What are the best books for learning Python?"
"Can you recommend a good article on Machine Learning?"
Receive Answers: The LLM agent will process your question and provide a relevant response. Follow-up questions will be understood in context, allowing for a natural conversation flow.

Logging: Check the logs/app.log file for a record of all interactions. This is useful for debugging and analyzing user queries.

# Example Queries
General Book Inquiry: "What are some good books on data science?"
Topic-Specific Query: "Can you suggest books on neural networks?"
Academic Help: "What is supervised learning?"
Follow-up Question: "What are some popular algorithms in supervised learning?"

# Notes on Architecture and Code Structure
The project follows a modular architecture to ensure scalability and maintainability:

Supervisor Layer: (supervisor.py) This layer is responsible for handling user inputs, managing session states, and interfacing with the adapter layer.

Adapter Layer: (adapter.py) This acts as a mediator between the supervisor and the LLM, formatting the input queries and handling the responses from the LLM.

LLM Layer: (llm_model.py) This is where the interaction with the chosen LLM occurs. The LLMModel class loads the specific model (e.g., Llama-3.1, Phi 3.5) and generates responses based on the input queries.

Logging Configuration: (logging_config.py) Handles the logging setup, ensuring all user interactions are recorded for analysis and improvement.

Frontend: (main.py) Uses Streamlit to provide a simple, interactive UI where users can enter their queries and view responses.

# Conclusion
The Student Management System using an LLM agent is a robust application that showcases the use of AI to enhance academic support systems. By leveraging open-source LLMs and modern deployment practices, this project can scale effectively and adapt to the evolving needs of students and educators. Feel free to contribute to the project or use it as a base to build more specialized systems!

