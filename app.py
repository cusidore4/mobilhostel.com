from flask import Flask, render_template
import os
from supabase import create_client, Client

# Variabili d'ambiente per il database
SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_KEY: str = os.environ.get("SUPABASE_KEY")

# Inizializza l'app di Flask
app = Flask(__name__)

# Inizializza il client di Supabase all'interno di una funzione per assicurarci che l'app sia pronta
def get_supabase_client():
    if not SUPABASE_URL or not SUPABASE_KEY:
        # Questo messaggio apparirà nei log di Heroku se le chiavi non sono impostate
        print("Errore: Le variabili d'ambiente SUPABASE_URL o SUPABASE_KEY non sono impostate.")
        return None
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# Connessione al database, ora gestita dopo l'inizializzazione dell'app
supabase: Client = get_supabase_client()

@app.route('/')
def index():
    if supabase is None:
        return "Errore di connessione al database. Controlla i log di Heroku per maggiori dettagli."
    
    # QUI ANDRA' IL CODICE PER INTERAGIRE CON IL DATABASE
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)