**Disc:<br>**
This project was created to complete the final project of the AI Python Bootcamp Batch 2 organized by Skill Academy Pro by Ruangguru!.

# AI-Powered Social Media Content Generator

## Project Overview

The AI-Powered Social Media Content Generator is designed to empower small business owners and content creators by streamlining and enhancing their social media presence. This application aims to bridge the gap by providing an intuitive, AI-driven platform for generating diverse social media content, leveraging artificial intelligence to generate text, suggest relevant hashtags, and provide ideas for accompanying visuals.



## Application Architecture

The AI-Powered Social Media Content Generator follows a client-server architecture, with Streamlit serving as the primary framework for the frontend and a Python-based backend handling AI model interactions and data processing. The architecture is designed to be modular, scalable, and maintainable, emphasizing clear separation of concerns.

### Frontend (Streamlit)

The frontend is built entirely using Streamlit, simplifying the creation of interactive web applications in Python. Key aspects include:

*   **User Interface (UI):** Streamlit widgets are used to create an intuitive and responsive user interface for inputting content ideas, selecting content types, specifying target platforms, and viewing generated content.
*   **Session State Management:** Streamlit's session state is utilized to maintain user inputs, application settings, and intermediate results across reruns.
*   **Layout and Styling:** Streamlit provides basic layout options, with custom CSS for advanced styling.
*   **User Feedback:** Progress indicators, success messages, and error notifications provide clear feedback to the user.

### Backend (Python with AI Models)

The backend primarily consists of Python scripts and modules responsible for handling the core logic, AI model inference, and data management. This includes:

*   **Content Generation Module:** Houses the logic for interacting with various AI models, responsible for text generation (using Large Language Models), hashtag suggestion, and content idea generation.
*   **Data Processing and Storage Module:** Handles data persistence for features like saving user preferences, content history, or analytics. SQLite is used for initial development, with options for PostgreSQL/MySQL or NoSQL databases for future scalability.
*   **Utility Module:** A collection of helper functions and classes for common tasks such as input validation, text formatting, and API key management.

### Data Storage

For initial development, a lightweight, file-based database like **SQLite** is used for storing user preferences and content history. API keys for external AI services are securely managed using Streamlit's secrets management or environment variables.




## Feature List

This section outlines the key features of the AI-Powered Social Media Content Generator, detailing their functionality, required input forms, and interactive elements. The design emphasizes user-friendliness and leverages Object-Oriented Programming (OOP) principles, appropriate data structures, and efficient looping techniques for robust and maintainable code.

### 3.1. Content Generation Module

This is the core functionality, allowing users to generate various types of social media content.

#### 3.1.1. Text Post Generation

*   **Description:** Generates text-based social media posts (e.g., for Twitter, Facebook, LinkedIn) based on user-defined parameters.
*   **Input Forms/Interactive Elements:**
    *   **Topic/Keywords (Text Input):** A `st.text_area` or `st.text_input` widget for users to enter the main subject or keywords for the post.
    *   **Content Type (Dropdown/Radio Buttons):** A `st.selectbox` or `st.radio` widget to choose the type of content (e.g., promotional, informative, question, announcement, storytelling).
    *   **Target Platform(s) (Multi-select):** A `st.multiselect` widget to select one or more social media platforms (e.g., Facebook, Twitter, Instagram, LinkedIn).
    *   **Tone of Voice (Dropdown):** A `st.selectbox` widget to specify the desired tone (e.g., formal, casual, humorous, professional, empathetic).
    *   **Call to Action (Optional Text Input):** A `st.text_input` for users to provide a specific call to action.
    *   **Generate Button (Button):** A `st.button` to trigger the AI text generation process.

#### 3.1.2. Hashtag Suggestion

*   **Description:** Generates relevant and trending hashtags based on the generated text or user-provided keywords.
*   **Input Forms/Interactive Elements:**
    *   **Text Input (Automatic/Manual):** This can be automatically populated with the generated text post or allow manual input via `st.text_area`.
    *   **Number of Hashtags (Slider):** A `st.slider` to specify the desired number of hashtags.
    *   **Generate Hashtags Button (Button):** A `st.button` to initiate hashtag generation.

#### 3.1.3. Image Idea Generation

*   **Description:** Provides creative prompts or descriptions for images that complement the generated text post. *Note: Actual image generation (using tools like DALL-E or Stable Diffusion) would require significant computational resources and potentially higher subscription tiers. This feature focuses on generating ideas/prompts for images, not the images themselves.*
*   **Input Forms/Interactive Elements:**
    *   **Text Post (Display Only):** The previously generated text post will be displayed for context.
    *   **Generate Image Ideas Button (Button):** A `st.button` to trigger the idea generation.

### 3.2. Content Management and History

This module allows users to review, save, and manage their generated content.

#### 3.2.1. Save/Edit Generated Content

*   **Description:** Enables users to save their generated text posts and associated hashtags, and make minor edits before saving.
*   **Input Forms/Interactive Elements:**
    *   **Editable Text Area:** A `st.text_area` pre-populated with the generated text, allowing users to modify it.
    *   **Editable Hashtag Input:** A `st.text_input` or `st.text_area` for editing the suggested hashtags.
    *   **Save Button (Button):** A `st.button` to commit the content to storage.

#### 3.2.2. Content History Display

*   **Description:** Displays a list of previously generated and saved content, allowing users to view, edit, or delete entries.
*   **Input Forms/Interactive Elements:**
    *   **Filter Options (Dropdowns/Multi-select):** `st.selectbox` or `st.multiselect` for filtering by platform, date range, or content type.
    *   **Search Bar (Text Input):** A `st.text_input` for searching content by keywords.
    *   **Display Table/List:** `st.dataframe` or `st.expander` within a loop to display each post. Each entry would have:
        *   **View/Edit Button (Button):** A `st.button` next to each post to load it into the editor.
        *   **Delete Button (Button):** A `st.button` next to each post for removal.

### 3.3. User Preferences and Settings

*   **Description:** Allows users to configure default settings for content generation and manage their API keys.
*   **Input Forms/Interactive Elements:**
    *   **Default Tone (Dropdown):** `st.selectbox` for setting a default tone.
    *   **Default Platforms (Multi-select):** `st.multiselect` for setting default target platforms.
    *   **API Key Input (Text Input):** A `st.text_input` for users to enter their API keys for external AI services. This input should be masked (`type=\'password\'`).
    *   **Save Settings Button (Button):** A `st.button` to save preferences.




## Installation

To set up the AI-Powered Social Media Content Generator locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd AI-PoweredSocialMediaContentGenerator
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *Note: A `requirements.txt` file should be created containing all necessary Python packages, such as `streamlit`, `sqlite3` (usually built-in), `requests`, etc. Based on the provided `Social_Media_Content_Generator.py`, the key dependencies are `streamlit` and `requests`.*

4.  **Set up API Key (for LLM Service):**

    The application uses an LLM service (OpenRouter.ai is mentioned in the code). You will need an API key for this service. It is recommended to manage this securely using Streamlit's secrets management or environment variables.

    *   **Using Streamlit Secrets:** Create a `.streamlit/secrets.toml` file in your project directory (if it doesn't exist) and add your API key:

        ```toml
        # .streamlit/secrets.toml
        OPENROUTER_API_KEY = "your_openrouter_api_key_here"
        ```

    *   **Using Environment Variables:** Set the `OPENROUTER_API_KEY` environment variable before running the application.

        ```bash
        export OPENROUTER_API_KEY="your_openrouter_api_key_here"
        ```




## Usage

To run the Streamlit application, navigate to the project root directory in your terminal and execute:

```bash
streamlit run Social_Media_Content_Generator.py
```

This will open the application in your web browser. You can then interact with the various features:

*   **Generate Text Posts:** Input your topic, select content type, platform, tone, and an optional call to action, then click 'Generate'.
*   **Get Hashtag Suggestions:** After generating a text post, you can get relevant hashtag suggestions.
*   **Generate Image Ideas:** Obtain creative prompts for images that complement your generated text posts.
*   **Manage Content History:** Save, edit, or delete your generated content from the history section.
*   **Configure Settings:** Adjust default tones, platforms, and manage your API key in the settings section.




## Project Structure

```
AI-PoweredSocialMediaContentGenerator/
├── Social_Media_Content_Generator.py  # Main Streamlit application file
├── README.md                          # Project README file
├── requirements.txt                   # Python dependencies
└── .streamlit/                        # Streamlit configuration (optional)
    └── secrets.toml                   # For secure API key management
```

### Key Files and Directories:

*   `Social_Media_Content_Generator.py`: This is the main application script. It contains the Streamlit UI definition, the core logic for content generation, hashtag suggestion, image idea generation, and interactions with the database and LLM service.
*   `README.md`: This file provides an overview of the project, instructions for installation and usage, and other relevant information.
*   `requirements.txt`: Lists all the Python packages required to run the application. These can be installed using `pip install -r requirements.txt`.
*   `.streamlit/secrets.toml`: (Optional) This directory and file are used by Streamlit to securely store sensitive information like API keys, preventing them from being hardcoded directly into the application script.



## Classes and Modules

The `Social_Media_Content_Generator.py` file is structured using Object-Oriented Programming (OOP) principles, with several key classes encapsulating specific functionalities:

*   **`SocialMediaPost` (Data Class):**
    *   A dataclass representing a single social media post. It holds attributes such as `id`, `text`, `hashtags` (list of strings), `platform`, `tone`, `content_type`, and `timestamp`.
    *   It includes a `__post_init__` method to set default values for `hashtags` and `timestamp` if not provided.

*   **`UserSettings` (Data Class):**
    *   A dataclass for storing user preferences and settings, including `default_tone`, `default_platforms` (list of strings), and `api_key`.
    *   The `__post_init__` method ensures `default_platforms` has a default value if not specified.

*   **`ContentGenerator` (Core Class):**
    *   Responsible for generating social media content using AI models (simulated with templates for demonstration).
    *   Manages `platform_limits` (character limits for different social media platforms) and `content_templates` (pre-defined text structures for various content types).
    *   The `generate_text_post` method takes `topic`, `content_type`, `platform`, `tone`, and an optional `cta` (call to action) to produce a text post, applying tone modifications and ensuring it fits platform limits.

*   **`HashtagSuggester` (Core Class):**
    *   Responsible for suggesting relevant hashtags based on input text.
    *   Uses a `hashtag_database` (simulated) and `trending_hashtags`.
    *   The `suggest_hashtags` method extracts keywords from the input text and returns a list of unique, relevant, and trending hashtags, ensuring the requested count is met.

*   **`ImageIdeaGenerator` (Core Class):**
    *   Generates creative prompts or descriptions for images that complement a given text post.
    *   Uses `image_styles` and `image_elements` to construct diverse image ideas.
    *   The `generate_ideas` method analyzes the text post for keywords and combines them with styles and elements to produce a list of image idea descriptions.

*   **`PostRepository` (Core Class - Repository Pattern):**
    *   Handles all database operations, abstracting the data access layer.
    *   Initializes an SQLite database (`social_media_posts.db`) with `posts` and `user_settings` tables.
    *   Provides methods for `save_post`, `get_all_posts`, `delete_post`, `save_settings`, and `load_settings`, ensuring data persistence and retrieval.

*   **`LLMService` (Core Class):**
    *   Manages interaction with the Large Language Model (LLM) service, specifically OpenRouter AI for free LLM access.
    *   The `generate_content` method sends a prompt to the configured LLM model (`deepseek/deepseek-chat-v3-0324`) and returns the generated content.

*   **`main()` Function:**
    *   The entry point of the Streamlit application.
    *   Configures the Streamlit page, sets up custom themes, and orchestrates the UI elements and interactions with the core classes.
    *   Manages session state for theme toggling and other UI-related functionalities.




## Prompt Example

Generate a creative social media package for the topic 'Remote Work Productivity'.

Return the result in the following STRICT format (do not add extra lines or change the structure):
1. Caption: 
   Description: 
2. Post Idea: 
   Description: 
3. Hashtags: 
   Description: 
4. Visual/Design Suggestion: 
   Description: 

Content type: informative, Tone: professional, Call to action: Learn More.
Do NOT add any extra text, explanation, or blank lines. Only output the list in the format above.




## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.


## Demo

[app](https://socialmediacontentgenerator.streamlit.app/)

## Video

[Video](https://drive.google.com/drive/folders/1R7_rI_BfLm5CRQjZ7m7S1R9bXTVupq3X?usp=sharing)


## Connect, Support & Collaborate

[LinkedIn](https://www.linkedin.com/in/abizar-al-gifari/)
