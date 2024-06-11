from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent

from paper_extractor import paper_extractor



from prompt import context
from dotenv import load_dotenv
import os 

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
load_dotenv()


llm = Ollama(model = 'llama3', request_timeout = 1000.0,  server_url='http://localhost:11434')



parser = LlamaParse(result_type='markdown', api_key= os.environ['LLAMA_PARSE_KEY'])

documents = SimpleDirectoryReader("./data", file_extractor= {'.pdf': parser}).load_data()


embed_model = resolve_embed_model('local:BAAI/bge-m3')
vector_index = VectorStoreIndex.from_documents(documents= documents, embed_model = embed_model)


query_engine = vector_index.as_query_engine(llm = llm)

tools = [
    QueryEngineTool(
        query_engine= query_engine,
        metadata= ToolMetadata(
            name= 'Generative AI',
            description= """These are the ground breaking research papers in the field of AI. They contain Generative AI advancement and methods.
            Use these to extract information related to Generative AI questions."""
        )
    ),
    paper_extractor
]


agent = ReActAgent.from_tools(tools, llm = llm, verbose = True, context = context)

while (prompt := input("Enter a prompt (q to quit):")) != "q":
    result = agent.query(prompt)
    print(result)