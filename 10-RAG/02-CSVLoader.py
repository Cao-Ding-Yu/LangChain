
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="resources/02-load.csv",
)

print(loader.load())

