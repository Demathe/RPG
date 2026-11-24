import sqlite3

conn = sqlite3.connect('musicas.db')

def criar_tabelas():
    conn.executescript(
    """CREATE TABLE IF NOT EXISTS artista(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    genero TEXT, 
    historia TEXT);
    CREATE TABLE IF NOT EXISTS albuns(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    datalancamento DATE,
    contexto TEXT,
    artista_id INTEGER NOT NULL REFERENCES artista(id));
    CREATE TABLE IF NOT EXISTS musicas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    letra text
    
    """
    )

criar_tabelas()