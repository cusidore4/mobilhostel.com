from flask import Flask, render_template
import os
from supabase import create_client, Client

# Variabili d'ambiente per il database
supabase_url: str = os.environ.get("https://plspverzyqbobpfijixv.supabase.co")
supabase_key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBsc3B2ZXJ6eXFib2JwZmlqaXh2Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NjkxODEzOCwiZXhwIjoyMDcyNDk0MTM4fQ.nUrbtZohUHnGTS0QqdwgMENr0ZEHg5a0cy6TrXjko3w")

# Aggiungi questa linea per debug:
print(f"URL Supabase: {supabase_url}")

supabase: Client = create_client(supabase_url, supabase_key)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)