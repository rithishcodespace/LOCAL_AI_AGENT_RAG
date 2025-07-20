1. create virtual env by python -m venv venv -> to keep the project dependencies seperate from others, this avoids mismatch of same dependencies of different versions
2. to activate virtual env -> ./venv/Scripts/activate
3.  pip install langchain langchain-ollama langchain-chroma -> dependencies
4. download ollama -> install the required model using cmd
  ollama pull llama3.2
  ollama pull mxbai-embed-large
5. configure chroma db
    Term Meanings:
    Embedding    -	A numeric representation of text (meaning-based)
    Vector	     -  A list of numbers that represents an embedding
    Vector Store -	A place to store text + its vector + metadata
    ChromaDB	 -  A fast, open-source vector store you use locally
    LangChain + Chroma + Ollama	A powerful combo to build your own ChatGPT for PDFs, reviews, etc.

