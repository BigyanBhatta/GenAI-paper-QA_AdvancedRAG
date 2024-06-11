import arxiv
from llama_index.core.tools import FunctionTool

def extract_arxiv_papers(topic: str, max_results: int = 5):
    search = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    papers = []
    for result in search.results():
        paper_info = {
            'title': result.title,
            'abstract': result.summary,
            'authors': ', '.join([author.name for author in result.authors]),
            'pdf_url': result.pdf_url
        }
        papers.append(paper_info)
    return papers

# # Example usage
# papers = extract_arxiv_papers('convolutional layers')
# for paper in papers:
#     print(f"Title: {paper['title']}")
#     print(f"Authors: {paper['authors']}")
#     print(f"Abstract: {paper['abstract']}")
#     print(f"PDF URL: {paper['pdf_url']}\n")

paper_extractor = FunctionTool.from_defaults(
    fn = extract_arxiv_papers,
    name = 'paper extractor',
    description="""It can search the paper. It return title, abstract and url of the selected paper as per the search.
    Use this when you need to search the relevant paper.""",
)
