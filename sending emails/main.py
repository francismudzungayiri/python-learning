import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("API_KEY")

print(password)