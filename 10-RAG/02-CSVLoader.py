
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="resources/02-17-load.csv",
)

print(loader.load())

