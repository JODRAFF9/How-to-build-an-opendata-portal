# Construire un portail open data

Tutoriel complet, en français, pour concevoir et mettre en place un portail de données ouvertes. Il combine deux approches :

- la méthode de la Banque mondiale (Open Data Toolkit et Open Data Readiness Assessment, ou ODRA) pour la stratégie, la gouvernance et l'écosystème ;
- CKAN, la plateforme open source la plus utilisée au monde, pour la partie technique.

## Contenu

| Fichier | Rôle |
|---|---|
| [`docs/tutoriel.md`](docs/tutoriel.md) | Le tutoriel, en 10 modules |
| [`docs/grille-odra.md`](docs/grille-odra.md) | Grille d'évaluation ODRA prête à remplir |
| [`docs/open-data-for-africa.md`](docs/open-data-for-africa.md) | Guide pour construire des portails nationaux de type Open Data for Africa |
| [`docs/ressources.md`](docs/ressources.md) | Bibliothèque de ressources : méthodes, écosystème africain, logiciels, standards, données, formations, financements |
| [`docs/beamer/`](docs/beamer/) | Présentation Beamer (source LaTeX et PDF) : revue de la littérature sur les portails open data |
| [`ckan/`](ckan/) | Instructions et configuration pour lancer CKAN avec Docker |
| [`scripts/publier.py`](scripts/publier.py) | Pipeline qui valide un CSV puis le publie via l'API CKAN |
| [`exemples/`](exemples/) | Jeu de données d'exemple pour les exercices |

## Par où commencer

1. Lire les modules 1 à 3 du tutoriel (stratégie).
2. Remplir la grille ODRA pour une organisation réelle.
3. Suivre les modules 4 à 8 pour installer CKAN et publier vos premières données.
4. Terminer avec les modules 9 et 10 (animation, pérennité).

## Sources

- Banque mondiale, Open Data Toolkit : https://www.banquemondiale.org/fr/data/opendatatoolkit/home
- Documentation CKAN : https://docs.ckan.org
- Dépôt Docker officiel de CKAN : https://github.com/ckan/ckan-docker

## Licence

Contenu sous licence CC-BY 4.0. Le code est sous licence MIT.
