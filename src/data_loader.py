from  pathlib import Path
from typing import List , Any
from langchain_community.document_loaders import PyPDFLoader , TextLoader , CSVLoader
from langchain_community.document_loaders import Docx2txtLoader 
from langchain_community.document_loaders.excel import  UnstructuredExcelLoader
from langchain_community.document_loaders import UnstructuredPowerPointLoader
from langchain_community.document_loaders import JSONLoader
# from langchain_community.document_loaders import SQLLoader


def load_all_doc(data_dir : str) -> List[Any]:
    """Load documents from various file types in the specified directory.
    Supported file types: PDF, TXT, CSV, DOCX, XLSX, JSON.
    """
    
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Loading documents from: {data_path}")
    documents = []
    
    # Load PDF files
    pdf_files = list(data_path.rglob("**/*.pdf"))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files.{ [str(f) for f in pdf_files] }")
    for pf in pdf_files:
      print(f"[DEBUG] Loading PDF file: {pf}")
      try :
          loader = PyPDFLoader(str(pf))
          loader = loader.load()
          print(f"[DEBUG] Loaded {len(loader)} pages from {pf}")
          documents.extend(loader)  
      except Exception as e:
            print(f"[ERROR] Failed to load PDF file {pf}: {e}")
            
            
    # Load TXT files
    txt_files = list(data_path.rglob("**/*.txt"))
    print(f"[DEBUG] Found {len(txt_files)} TXT files.{ [str(f) for f in txt_files] }")
    for tf in txt_files:
      print(f"[DEBUG] Loading TXT file: {tf}")
      try :
          loader = TextLoader(str(tf))
          loader = loader.load()
          print(f"[DEBUG] Loaded {len(loader)} documents from {tf}")
          documents.extend(loader)  
      except Exception as e:
            print(f"[ERROR] Failed to load TXT file {tf}: {e}")
            
    # Load CSV files
    csv_files = list(data_path.rglob("**/*.csv"))
    print(f"[DEBUG] Found {len(csv_files)} CSV files.{ [str(f) for f in csv_files] }")
    for cf in csv_files:
      print(f"[DEBUG] Loading CSV file: {cf}")
      try :
          loader = CSVLoader(str(cf))
          loader = loader.load()
          print(f"[DEBUG] Loaded {len(loader)} documents from {cf}")
          documents.extend(loader)  
      except Exception as e:
            print(f"[ERROR] Failed to load CSV file {cf}: {e}")
            
            
            
     # Load DOCX files
    docx_files = list(data_path.rglob("**/*.docx"))
    print(f"[DEBUG] Found {len(docx_files)} DOCX files.{ [str(f) for f in docx_files] }")
    for dxf in docx_files:
      print(f"[DEBUG] Loading DOCX file: {dxf}")
      try :
          loader = Docx2txtLoader(str(dxf))
          loader = loader.load()
          print(f"[DEBUG] Loaded {len(loader)} documents from {dxf}")
          documents.extend(loader)  
      except Exception as e:
            print(f"[ERROR] Failed to load DOCX file {dxf}: {e}")
            
            
            
     # Load XLSX files
    xlsx_files = list(data_path.rglob("**/*.xlsx"))
    print(f"[DEBUG] Found {len(xlsx_files)} XLSX files.{ [str(f) for f in xlsx_files] }")
    for xlf in xlsx_files:
      print(f"[DEBUG] Loading XLSX file: {xlf}")
      try :
          loader = UnstructuredExcelLoader(str(xlf))
          loader = loader.load()
          print(f"[DEBUG] Loaded {len(loader)} documents from {xlf}")
          documents.extend(loader)  
      except Exception as e:
            print(f"[ERROR] Failed to load XLSX file {xlf}: {e}")
            
            
     # Load JSON files
    json_files = list(data_path.rglob("**/*.json"))
    print(f"[DEBUG] Found {len(json_files)} JSON files.{ [str(f) for f in json_files] }")
    for jf in json_files:
      print(f"[DEBUG] Loading JSON file: {jf}")
      try :
          loader = JSONLoader(str(jf))
          loader = loader.load()
          print(f"[DEBUG] Loaded {len(loader)} documents from {jf}")
          documents.extend(loader)  
      except Exception as e:
            print(f"[ERROR] Failed to load JSON file {jf}: {e}")
            
            
      # Load sql files
    sql_files = list(data_path.rglob("**/*.sql"))
    print(f"[DEBUG] Found {len(sql_files)} SQL files.{ [str(f) for f in sql_files] }")
    for sf in sql_files:
        print(f"[DEBUG] Loading SQL file: {sf}")
        try :
            loader = TextLoader(str(sf))
            loader = loader.load()
            print(f"[DEBUG] Loaded {len(loader)} documents from {sf}")
            documents.extend(loader)  
        except Exception as e:
                print(f"[ERROR] Failed to load SQL file {sf}: {e}")      
                
    
    # # load pptx files
    pptx_files = list(data_path.rglob("**/*.pptx"))
    print(f"[DEBUG] Found {len(pptx_files)} PPTX files.{ [str(f) for f in pptx_files] }")
    for ppf in pptx_files:
        print(f"[DEBUG] Loading PPTX file: {ppf}")
        try :
            loader = UnstructuredPowerPointLoader(str(ppf))
            loader = loader.load()
            print(f"[DEBUG] Loaded {len(loader)} documents from {ppf}")
            documents.extend(loader)  
        except Exception as e:
                print(f"[ERROR] Failed to load PPTX file {ppf}: {e}")
                
                
    return documents
                
            