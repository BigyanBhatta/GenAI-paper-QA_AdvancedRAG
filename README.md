# GenAI-paper-QA_AdvancedRAG

This project is designed to facilitate the extraction and querying of research papers related to Generative AI. The application uses a combination of local and online tools to fetch, parse, and query research papers from a specified directory and Arxiv.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Components](#components)

## Installation


### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/GenAI-paper-QA_AdvancedRAG.git
    cd GenAI-paper-QA_AdvancedRAG
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your `.env` file with the necessary environment variables. Create a `.env` file in the root directory of the project and add the following:

    ```env
    LLAMA_PARSE_KEY=your_llama_parse_key
    ```

## Usage

1. Start the application by running:

    ```bash
    python main.py
    ```

2. You will be prompted to enter a query. Type your question related to Generative AI research papers and press Enter. To quit, type `q` and press Enter.

## Configuration

The application uses environment variables for sensitive information and configuration. Ensure you have a `.env` file in the root directory with the following content:

```env
LLAMA_PARSE_KEY=your_llama_parse_key
```

## Components

1. `main.py`
This is the main entry point of the application. It initializes the LLM, document parser, embedding model, vector store index, and the agent. It also handles the interactive prompt loop.

2. `paper_extractor.py`
This module defines a function to search for research papers on Arxiv based on a given topic. The function returns a list of papers with their title, abstract, authors, and PDF URL.

3. `prompt.py`
This module contains the context used by the agent during the query processing.