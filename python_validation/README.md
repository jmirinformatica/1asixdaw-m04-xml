# Validació de DTD i XSD amb python

## Setup

Fem servir [Python Virtual Environment](https://docs.python.org/3/library/venv.html).

Crea l'entorn:

    python3 -m venv .venv

Activa'l:

    source .venv/bin/activate

Instal·la el requisits:

    pip install -r requirements.txt

Per a generar el fitxer de requiriments:

    pip freeze > requirements.txt

Per desactivar l'entorn:

    deactivate

## Execució:

Pots provar els diferents exemples:

    python validator.py exemples/exemple.xml
    python validator.py exemples/exemple.xml exemples/exemple.dtd
    python validator.py exemples/exemple.xml exemples/exemple.xsd
