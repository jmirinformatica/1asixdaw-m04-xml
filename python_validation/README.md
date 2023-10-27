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

```bash
python3 validator.py exemples/exemple.xml
python3 validator.py exemples/exemple.xml exemples/exemple.dtd
python3 validator.py exemples/exemple.xml exemples/exemple.xsd
python3 validator.py exemples/exemple.xml exemples/exemple.dtd exemples/exemple.xsd
```

La sortida de la darrera execuió haura de ser:

    Fitxer XML: exemples/exemple.xml
    Fitxer DTD: exemples/exemple.dtd
    Fitxer XSD: exemples/exemple.xsd
    -------------------------------------------------------
    XML CORRECTE!
    DTD CORRECTE!
    Validant l'XML amb el DTD... OK!
    XSD CORRECTE!
    Validant l'XML amb el XSD... OK!