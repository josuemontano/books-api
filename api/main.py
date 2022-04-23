from dotenv import load_dotenv
from fastapi import FastAPI

# Add code that uses environment variables AFTER THE NEXT LINE
load_dotenv()

app = FastAPI()
