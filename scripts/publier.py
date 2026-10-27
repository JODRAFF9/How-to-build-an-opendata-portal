"""Valide un fichier CSV contre un schéma Frictionless puis le publie sur CKAN.

Crée le jeu de données s'il n'existe pas, puis crée ou remplace la ressource
portant le même nom de fichier. Rien n'est publié si la validation échoue.
"""

import argparse
import os
import sys
from pathlib import Path

from ckanapi import NotFound, RemoteCKAN
from frictionless import Resource, Schema


def valider(fichier: Path, schema: Path) -> bool:
    rapport = Resource(path=str(fichier), schema=Schema(str(schema))).validate()
    if rapport.valid:
        print(f"Validation réussie : {fichier.name}")
        return True
    print(f"Validation échouée : {fichier.name}", file=sys.stderr)
    for erreur in rapport.flatten(["rowNumber", "fieldName", "message"]):
        ligne, colonne, message = erreur
        print(f"  ligne {ligne}, colonne {colonne} : {message}", file=sys.stderr)
    return False


def obtenir_jeu(ckan: RemoteCKAN, nom: str, titre: str, organisation: str, licence: str) -> dict:
    try:
        return ckan.action.package_show(id=nom)
    except NotFound:
        print(f"Création du jeu de données {nom}")
        return ckan.action.package_create(
            name=nom, title=titre, owner_org=organisation, license_id=licence
        )


def publier(ckan: RemoteCKAN, jeu: dict, fichier: Path) -> None:
    existante = next((r for r in jeu.get("resources", []) if r["name"] == fichier.name), None)
    with fichier.open("rb") as contenu:
        if existante:
            ckan.action.resource_update(id=existante["id"], upload=contenu, format="CSV")
            print(f"Ressource mise à jour : {fichier.name}")
        else:
            ckan.action.resource_create(
                package_id=jeu["id"], name=fichier.name, upload=contenu, format="CSV"
            )
            print(f"Ressource créée : {fichier.name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fichier", type=Path, required=True)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--organisation", required=True, help="Identifiant de l'organisation CKAN")
    parser.add_argument("--jeu", required=True, help="Identifiant du jeu de données")
    parser.add_argument("--titre", required=True)
    parser.add_argument("--licence", default="cc-by")
    parser.add_argument("--valider-seulement", action="store_true")
    args = parser.parse_args()

    if not valider(args.fichier, args.schema):
        return 1
    if args.valider_seulement:
        return 0

    url = os.environ.get("CKAN_URL")
    jeton = os.environ.get("CKAN_API_TOKEN")
    if not url or not jeton:
        print("Définissez CKAN_URL et CKAN_API_TOKEN.", file=sys.stderr)
        return 2

    ckan = RemoteCKAN(url, apikey=jeton)
    jeu = obtenir_jeu(ckan, args.jeu, args.titre, args.organisation, args.licence)
    publier(ckan, jeu, args.fichier)
    return 0


if __name__ == "__main__":
    sys.exit(main())
