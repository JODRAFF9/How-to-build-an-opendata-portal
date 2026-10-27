# Construire des portails nationaux de type Open Data for Africa

Ce guide prolonge le tutoriel. Il s'adresse à ceux qui veulent mettre en place, pour un ou plusieurs pays africains, des portails de données nationaux comparables à **Open Data for Africa**, la plateforme lancée par la Banque africaine de développement (BAD).

## 1. Comprendre le modèle Open Data for Africa

Open Data for Africa est un réseau de portails : un portail régional et un portail par pays, souvent sous la forme `<pays>.opendataforafrica.org`. Chaque portail national est en principe administré avec l'institut national de la statistique (INS) du pays.

Sa différence avec un portail de type CKAN :

| | Portail catalogue (CKAN, udata) | Portail statistique (Open Data for Africa) |
|---|---|---|
| Unité de base | Un fichier (CSV, PDF, GeoJSON) | Un indicateur dans le temps et l'espace |
| Exemple | « Liste des écoles 2025.csv » | « Taux de scolarisation, par région, 2000 à 2025 » |
| Fonctions clés | Recherche, téléchargement, API | Séries temporelles, graphiques, cartes, comparaisons entre pays |
| Producteurs | Tous les services de l'État | Surtout l'INS et les ministères sectoriels |
| Standard d'échange | DCAT | SDMX |

Un portail national complet combine souvent **les deux** : un portail statistique pour les indicateurs et un catalogue pour les autres données (géographiques, budgétaires, administratives).

La plateforme historique d'Open Data for Africa repose sur une solution propriétaire (Knoema). Pour construire vos propres portails, vous pouvez soit travailler avec la BAD sur ce réseau, soit déployer une pile open source équivalente, décrite ci-dessous.

## 2. Les acteurs à impliquer dans chaque pays

| Acteur | Rôle |
|---|---|
| Institut national de la statistique | Producteur principal, garant de la qualité, souvent hébergeur |
| Ministère du numérique ou agence numérique | Infrastructure, hébergement, politique open data |
| Ministères sectoriels (santé, éducation, agriculture, finances) | Producteurs de données administratives |
| Banque centrale (BCEAO, BEAC ou nationale) | Données monétaires et financières |
| Partenaires : BAD, Banque mondiale, PARIS21, Afristat, UNECA | Financement, méthodes, renforcement des capacités |
| Société civile, universités, presse | Réutilisateurs, relais de la demande |

Avant toute technique, faites une **ODRA** par pays (voir [`grille-odra.md`](grille-odra.md)). Les situations varient beaucoup d'un pays à l'autre, notamment sur le cadre juridique, le financement et la connectivité.

## 3. Une pile open source pour un portail national

```
              Public, développeurs, médias
                         |
              Portail national (un domaine)
               /                       \
   Portail statistique            Catalogue de données
   .Stat Suite (SDMX)                 CKAN (DCAT)
   indicateurs, séries,          fichiers, géodonnées,
   tableaux, graphiques           budget, administration
               \                       /
         Entrepôt de données (PostgreSQL)
                         |
     Pipelines d'intégration et de validation
                         |
   INS, ministères, banque centrale, enquêtes
```

| Brique | Outil open source conseillé | Pourquoi |
|---|---|---|
| Portail statistique | **.Stat Suite** (communauté SIS-CC, OCDE) | Diffusion SDMX native, utilisé par plusieurs INS |
| Catalogue | **CKAN** | Voir le tutoriel principal |
| Données géographiques | GeoServer ou pg_featureserv, avec PostGIS | Cartes par région, limites administratives |
| Visualisations | Apache Superset, Metabase ou des pages statiques | Tableaux de bord pour le grand public |
| Micro-données d'enquêtes | **NADA** (Banque mondiale, IHSN) | Catalogue d'enquêtes avec documentation DDI |
| Pipelines | Python, Frictionless, Airflow ou Dagster | Mises à jour automatiques et validées |

NADA mérite une mention particulière : de nombreux INS africains l'utilisent déjà pour leurs enquêtes (recensements, enquêtes ménages). Le portail national peut s'appuyer sur l'existant au lieu de tout reconstruire.

## 4. Les standards à adopter

- **SDMX** : le standard international des données statistiques, utilisé par la BAD, le FMI, la Banque mondiale et les Nations unies. Adopter SDMX permet d'échanger automatiquement avec ces institutions.
- **DCAT** : pour le catalogue, afin d'être moissonné par d'autres portails.
- **DDI** : pour documenter les enquêtes (via NADA).
- **Codes communs** : ISO 3166 pour les pays, codes officiels des régions et communes, et la liste des indicateurs des Objectifs de développement durable (ODD) et de l'Agenda 2063 de l'Union africaine.

## 5. Le contenu prioritaire d'un portail national

Commencez par les indicateurs que les utilisateurs cherchent le plus et que les partenaires demandent déjà :

1. population et démographie (recensement, projections) ;
2. comptes nationaux (PIB, croissance, inflation) ;
3. indicateurs des ODD ;
4. éducation (effectifs, taux de scolarisation) ;
5. santé (couverture vaccinale, mortalité) ;
6. agriculture et sécurité alimentaire (production, prix des marchés) ;
7. finances publiques (budget voté et exécuté) ;
8. commerce extérieur ;
9. énergie et accès à l'électricité ;
10. données géographiques de référence (limites administratives).

## 6. Les contraintes propres au contexte africain

| Contrainte | Réponse |
|---|---|
| Connectivité limitée ou coûteuse | Pages légères, téléchargements compressés, cache CDN, export hors ligne |
| Coupures d'électricité dans les centres de données | Hébergement redondant, sauvegardes hors site |
| Équipes techniques réduites | Solutions standard plutôt que sur mesure, documentation, formation |
| Usage majoritaire sur téléphone mobile | Interface pensée d'abord pour le mobile |
| Langues | Interface en français, anglais, portugais, arabe selon le pays, et langues nationales si possible |
| Souveraineté des données | Hébergement national ou régional quand c'est possible |
| Dépendance aux financements extérieurs | Budget national inscrit dans la loi de finances dès la deuxième année |

## 7. Passer de un pays à plusieurs pays

Si vous visez plusieurs pays, standardisez pour ne pas reconstruire à chaque fois :

1. **Un socle commun** : les mêmes images Docker, la même configuration de base, les mêmes schémas d'indicateurs (structures SDMX partagées).
2. **Une personnalisation par pays** : nom de domaine, langue, logo, liste des producteurs, codes géographiques.
3. **Un dépôt de configuration par pays**, avec un déploiement automatisé (Ansible, Terraform ou Kubernetes).
4. **Un portail régional** qui agrège les données de tous les pays via SDMX et DCAT, pour les comparaisons.
5. **Une communauté de pratique** entre les équipes nationales : formations communes, partage des pipelines, entraide.

## 8. Feuille de route type pour un pays

| Phase | Durée | Livrables |
|---|---|---|
| Diagnostic | 2 mois | ODRA, cartographie des acteurs, inventaire des données |
| Cadrage | 1 mois | Gouvernance, licence, choix techniques, budget sur 3 ans |
| Pilote | 3 mois | Portail avec 50 indicateurs clés et 20 jeux de données |
| Lancement | 1 mois | Ouverture publique, formation des producteurs et des journalistes |
| Montée en charge | 6 mois | Automatisation, ajout des ministères sectoriels, premier hackathon |
| Pérennisation | Continu | Budget national, mises à jour, nouvelle ODRA à 2 ou 3 ans |

## 9. Votre parcours d'apprentissage

1. Suivez le tutoriel principal ([`tutoriel.md`](tutoriel.md)) pour maîtriser CKAN.
2. Étudiez deux portails existants : un portail Open Data for Africa et un portail d'INS basé sur .Stat Suite ou NADA. Notez ce qu'ils publient, comment, et à quelle fréquence.
3. Apprenez les bases de SDMX (structures de données, listes de codes, API REST).
4. Installez .Stat Suite en local à partir de sa documentation officielle (sis-cc.gitlab.io/dotstatsuite-documentation).
5. Réalisez une ODRA pour un pays cible.
6. Construisez un prototype national : 10 indicateurs dans .Stat Suite, 10 jeux de données dans CKAN, une page d'accueil commune.
7. Présentez le prototype à l'INS ou au ministère concerné, avec le rapport ODRA.

## Ressources

- Banque africaine de développement, Open Data for Africa : https://dataportal.opendataforafrica.org
- Banque mondiale, Open Data Toolkit : https://www.banquemondiale.org/fr/data/opendatatoolkit/home
- .Stat Suite : https://sis-cc.gitlab.io/dotstatsuite-documentation/
- NADA : https://nada.ihsn.org
- SDMX : https://sdmx.org
- PARIS21 (renforcement des systèmes statistiques) : https://www.paris21.org
- Afristat : https://www.afristat.org
- Open Data Inventory (évaluation des données des INS) : https://odin.opendatawatch.com
