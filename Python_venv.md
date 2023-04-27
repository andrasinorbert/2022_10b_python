# Hogyan használjuk a virtual environmenteket?

## telepítés/létrehozás

```bash
# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv myvenv
# macOS
python3 -m venv myvenv
# Windows
python -m venv myvenv
```

## telepített package-ek listázása

```bash
pip list
```

## venv használata

```bash
source myvenv/bin/activate
# kikapcsolás: deactivate
```

- Ez után a $pip list$ paranccsal más fogunk látni
- ez után már ebbe a "python"-ba tudunk package-et telepíteni

## annak lekérdezése melyik python-t használjuk épp

```bash
which python
```

## Telepített package verziók listázása

```bash
pip freeze
```

Kimentése fájlba:

```bash
pip freeze > requirements.txt
```

A fájl alapján a package-ek letöltése:

```bash
pip install -r requirements.txt
```
