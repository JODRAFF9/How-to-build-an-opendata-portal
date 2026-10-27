# Tutoriel : construire un portail open data avec le Toolkit de la Banque mondiale et CKAN

Ce tutoriel vous accompagne de l'idée jusqu'à un portail en production. Il suit la logique du Open Data Toolkit de la Banque mondiale (évaluer, décider, construire, animer) et l'applique concrètement avec CKAN.

Durée indicative : 6 semaines à raison de quelques heures par semaine.

Prérequis techniques : savoir utiliser un terminal, avoir Docker et Python 3.10 ou plus récent installés.

---

## Sommaire

**Partie A : stratégie (Toolkit Banque mondiale)**

1. [Les fondamentaux de l'open data](#module-1--les-fondamentaux-de-lopen-data)
2. [Évaluer la maturité avec l'ODRA](#module-2--évaluer-la-maturité-avec-lodra)
3. [Lancer l'initiative : gouvernance et plan d'action](#module-3--lancer-linitiative--gouvernance-et-plan-daction)

**Partie B : technique (CKAN)**

4. [Choisir la plateforme](#module-4--choisir-la-plateforme)
5. [Installer CKAN avec Docker](#module-5--installer-ckan-avec-docker)
6. [Organiser le catalogue et publier](#module-6--organiser-le-catalogue-et-publier)
7. [API, DataStore et interopérabilité DCAT](#module-7--api-datastore-et-interopérabilité-dcat)
8. [Automatiser la publication](#module-8--automatiser-la-publication)

**Partie C : faire vivre le portail**

9. [Demande et engagement des réutilisateurs](#module-9--demande-et-engagement-des-réutilisateurs)
10. [Mise en production et pérennité](#module-10--mise-en-production-et-pérennité)

---

# Partie A : stratégie

## Module 1 : les fondamentaux de l'open data

### Définition

Une donnée est ouverte quand elle est :

- **juridiquement ouverte** : publiée sous une licence qui autorise la réutilisation, y compris commerciale ;
- **techniquement ouverte** : dans un format lisible par une machine, non propriétaire, téléchargeable en entier et gratuitement.

Un tableau dans un PDF n'est donc pas une donnée ouverte au sens strict. Le même tableau en CSV, sous Licence Ouverte, l'est.

### Les bénéfices mis en avant par la Banque mondiale

| Bénéfice | Exemple |
|---|---|
| Transparence et redevabilité | Publication du budget exécuté, des marchés publics |
| Efficacité de l'administration | Les services partagent leurs données au lieu de se les redemander |
| Croissance économique | Applications de transport, de météo agricole, d'immobilier |
| Participation citoyenne | Signalement de problèmes, suivi des projets locaux |

### Les licences

| Licence | Obligation pour le réutilisateur | Usage typique |
|---|---|---|
| Licence Ouverte Etalab 2.0 | Citer la source | Administrations françaises et francophones |
| CC-BY 4.0 | Citer la source | International, recherche |
| ODbL | Citer la source et repartager les bases dérivées sous la même licence | OpenStreetMap, certaines collectivités |
| CC0 | Aucune | Données de référence, domaine public |

Conseil : choisissez **une licence par défaut** pour tout le portail. Multiplier les licences complique la réutilisation.

### Ce qu'on n'ouvre pas

- Les données personnelles non anonymisées (RGPD ou loi locale de protection des données).
- Les données couvertes par le secret statistique, le secret des affaires ou la sécurité nationale.
- Les données dont l'administration ne détient pas les droits.

### Exercice

Allez sur trois portails (data.gouv.fr, data.worldbank.org et le portail national de votre pays s'il existe). Pour chacun, notez la licence, les formats proposés et la présence d'une API.

---

## Module 2 : évaluer la maturité avec l'ODRA

L'**Open Data Readiness Assessment** est la méthode de diagnostic de la Banque mondiale. Elle répond à une question : *cette organisation est-elle prête à lancer une initiative open data, et que doit-elle faire en priorité ?*

### Les 8 dimensions

1. **Leadership politique** : un responsable de haut niveau porte-t-il publiquement le projet ?
2. **Cadre politique et juridique** : loi d'accès à l'information, protection des données, droit d'auteur sur les données publiques, licences.
3. **Structures institutionnelles, responsabilités et compétences** : qui pilote ? Les services ont-ils des référents données ?
4. **Politiques et procédures de gestion des données** : inventaire, qualité, formats, archivage.
5. **Demande** : qui demande des données aujourd'hui, et lesquelles ?
6. **Écosystème civique et entrepreneurial** : développeurs, journalistes de données, universités, startups, communautés OpenStreetMap.
7. **Financement** : budget dédié au portail, aux formations et à l'animation, sur plusieurs années.
8. **Infrastructure technologique et compétences** : connectivité, hébergement, compétences en interne.

### La méthode

1. **Préparation** : identifier les interlocuteurs (ministères, agence statistique, société civile, secteur privé).
2. **Collecte** : entretiens, questionnaires, analyse des textes et des sites existants.
3. **Notation** : pour chaque dimension, attribuer un niveau.
   - *Prêt* : les conditions sont réunies.
   - *Partiellement prêt* : des bases existent mais avec des lacunes.
   - *Pas prêt* : obstacle majeur à lever avant de lancer.
4. **Recommandations** : pour chaque dimension, des actions concrètes, chiffrées et datées.
5. **Restitution** : présentation aux décideurs, publication du rapport.

### Exercice

Remplissez la grille [`grille-odra.md`](grille-odra.md) pour une organisation que vous connaissez. Comparez ensuite avec un rapport ODRA publié par la Banque mondiale (plusieurs pays d'Afrique, du Maghreb et d'Amérique latine en disposent).

---

## Module 3 : lancer l'initiative : gouvernance et plan d'action

### La gouvernance minimale

| Rôle | Responsabilité |
|---|---|
| Sponsor politique | Porte le projet, arbitre, débloque le budget |
| Équipe projet (2 à 5 personnes) | Pilote le portail, forme, anime |
| Référents données dans chaque service | Identifient, préparent et mettent à jour les jeux de données |
| Comité des utilisateurs | Remonte les besoins, teste le portail |
| Délégué à la protection des données | Valide l'absence de données personnelles |

### L'inventaire des données

Pour chaque service, créez une fiche par jeu de données :

| Champ | Exemple |
|---|---|
| Nom | Liste des écoles primaires |
| Service producteur | Direction de l'éducation |
| Système source | Base de gestion scolaire |
| Format actuel | Excel |
| Fréquence de mise à jour | Annuelle |
| Contient des données personnelles | Non |
| Demandé par | ONG éducation, journalistes |
| Effort de préparation | Faible |

### Prioriser

Placez chaque jeu de données sur deux axes : **valeur pour les utilisateurs** et **facilité d'ouverture**. Commencez par les jeux à forte valeur et faciles à ouvrir. Les catégories souvent prioritaires selon le Toolkit et la directive européenne sur les données à forte valeur :

- budget et dépenses publiques ;
- marchés publics ;
- données géographiques de référence (limites administratives, adresses) ;
- statistiques démographiques ;
- éducation et santé (liste des établissements) ;
- transport ;
- environnement et météo.

### Le plan d'action

Un plan réaliste sur 12 mois :

| Période | Objectif |
|---|---|
| Mois 1 à 2 | ODRA, gouvernance, choix de la licence |
| Mois 3 à 4 | Inventaire, choix de la plateforme, installation |
| Mois 5 | Publication des 20 premiers jeux de données, lancement public |
| Mois 6 à 9 | Automatisation des mises à jour, premier hackathon |
| Mois 10 à 12 | Bilan, mesure de l'usage, plan de l'année 2 |

---

# Partie B : technique

## Module 4 : choisir la plateforme

Le Toolkit de la Banque mondiale distingue trois familles.

| Famille | Exemples | Avantages | Inconvénients |
|---|---|---|---|
| Open source auto-hébergé | CKAN, udata, DKAN | Pas de licence, contrôle total, communauté | Demande des compétences techniques |
| Logiciel en tant que service | Opendatasoft, Socrata, ArcGIS Hub | Rapide à lancer, visualisations intégrées | Coût annuel, dépendance au fournisseur |
| Solution maison | Site statique et dépôt Git | Très peu coûteux | Fonctionnalités limitées, peu standard |

### Critères de choix

- Compétences disponibles en interne pour maintenir la solution.
- Budget sur 3 à 5 ans (pas seulement le lancement).
- Interopérabilité : export DCAT, API, moissonnage par les portails régionaux.
- Souveraineté : où sont hébergées les données ?
- Langues de l'interface.

Ce tutoriel utilise **CKAN** : gratuit, utilisé par data.gov (États-Unis), data.europa.eu, le portail open data du Canada et de nombreux pays, avec une API complète et une interface traduite en français.

### Architecture de CKAN

```
                Navigateur / client API
                          |
                     Nginx (HTTPS)
                          |
                  CKAN (application Python)
            /             |              \
     PostgreSQL         Solr            Redis
   (métadonnées et   (moteur de      (cache et files
     DataStore)       recherche)       de tâches)
                          |
                 Stockage des fichiers
```

---

## Module 5 : installer CKAN avec Docker

L'installation se base sur le dépôt officiel `ckan-docker`. Les détails sont dans [`../ckan/README.md`](../ckan/README.md).

### Étape 1 : récupérer le projet

```bash
git clone https://github.com/ckan/ckan-docker.git
cd ckan-docker
cp .env.example .env
```

### Étape 2 : configurer

Dans le fichier `.env`, modifiez au minimum :

```ini
CKAN_SITE_URL=https://localhost:8443
CKAN_SYSADMIN_NAME=admin
CKAN_SYSADMIN_PASSWORD=un_mot_de_passe_long_et_unique
CKAN_SYSADMIN_EMAIL=admin@exemple.org
CKAN__LOCALE_DEFAULT=fr
CKAN__PLUGINS="image_view text_view datatables_view datastore datapusher envvars"
```

### Étape 3 : démarrer

```bash
docker compose build
docker compose up -d
docker compose ps
```

Attendez que tous les conteneurs soient à l'état `healthy`, puis ouvrez https://localhost:8443. Le navigateur affichera un avertissement de certificat, c'est normal en local.

### Étape 4 : vérifier

```bash
curl -k https://localhost:8443/api/3/action/status_show
```

La réponse JSON doit contenir `"success": true` et la version de CKAN.

### Problèmes fréquents

| Symptôme | Cause probable | Solution |
|---|---|---|
| Le conteneur CKAN redémarre en boucle | Solr ou PostgreSQL pas encore prêts | Attendre, puis `docker compose logs ckan` |
| Erreur 502 | CKAN n'a pas fini de démarrer | Patienter une à deux minutes |
| Interface en anglais | Langue non configurée | Vérifier `CKAN__LOCALE_DEFAULT=fr` puis redémarrer |

---

## Module 6 : organiser le catalogue et publier

### Les concepts de CKAN

| Concept CKAN | Signification |
|---|---|
| Organisation | Le producteur (un ministère, un service). Chaque jeu de données appartient à une organisation. |
| Jeu de données (*dataset*) | La fiche descriptive : titre, description, licence, mots-clés, fréquence. |
| Ressource | Un fichier ou un lien attaché au jeu de données (CSV, JSON, API). |
| Groupe | Un regroupement thématique transversal (Éducation, Santé). |
| Mots-clés (*tags*) | Pour la recherche. |

### Les métadonnées à toujours renseigner

Une donnée sans métadonnées est inutilisable. Exigez au minimum :

- un titre explicite (« Écoles primaires publiques, 2025 » plutôt que « ecoles_v3 ») ;
- une description qui dit ce que contient le fichier, comment il a été produit et ses limites ;
- la licence ;
- le producteur et un contact ;
- la fréquence de mise à jour et la date de dernière mise à jour ;
- la couverture géographique et temporelle ;
- la signification de chaque colonne (dictionnaire des données).

### Publier à la main

1. Connectez-vous avec le compte administrateur.
2. Menu **Organisations**, puis **Ajouter une organisation**.
3. Dans l'organisation, **Ajouter un jeu de données**.
4. Remplissez les métadonnées, puis ajoutez une ressource : téléversez [`../exemples/ecoles.csv`](../exemples/ecoles.csv).
5. Ouvrez la ressource : CKAN affiche un aperçu tabulaire.

### Les rôles

| Rôle dans une organisation | Droits |
|---|---|
| Membre | Voir les jeux de données privés |
| Éditeur | Créer et modifier les jeux de données |
| Administrateur | Gérer aussi les membres de l'organisation |

Donnez le rôle d'éditeur aux référents données de chaque service : ce sont eux qui publient, pas l'équipe projet.

---

## Module 7 : API, DataStore et interopérabilité DCAT

### L'API CKAN

Tout ce que fait l'interface est disponible par l'API, à l'adresse `/api/3/action/<nom_action>`.

```bash
# Lister les jeux de données
curl -k https://localhost:8443/api/3/action/package_list

# Rechercher
curl -k "https://localhost:8443/api/3/action/package_search?q=ecoles&rows=5"

# Détail d'un jeu de données
curl -k "https://localhost:8443/api/3/action/package_show?id=ecoles-primaires"
```

Les actions d'écriture demandent un jeton d'API : dans l'interface, menu de votre profil, **Jetons d'API**, puis **Créer un jeton**.

### Le DataStore

Le DataStore charge le contenu des CSV dans PostgreSQL. Les données deviennent alors interrogeables ligne par ligne :

```bash
curl -k "https://localhost:8443/api/3/action/datastore_search?resource_id=<ID>&q=Ouagadougou&limit=10"
```

C'est ce qui permet aux développeurs de construire des applications sans télécharger tout le fichier. Le chargement automatique est assuré par DataPusher ou, mieux, par l'extension `ckanext-xloader`, plus rapide.

### DCAT : être visible au-delà de son portail

DCAT est le vocabulaire standard du W3C pour décrire des catalogues de données. Avec lui, votre catalogue peut être moissonné par des portails nationaux, régionaux ou par data.europa.eu.

Installation de l'extension `ckanext-dcat` (dans l'image Docker de CKAN) :

```dockerfile
RUN pip install -e git+https://github.com/ckan/ckanext-dcat.git#egg=ckanext-dcat && \
    pip install -r ${APP_DIR}/src/ckanext-dcat/requirements.txt
```

Puis ajoutez `dcat structured_data` à la variable `CKAN__PLUGINS`. Le catalogue est alors disponible à :

```
https://localhost:8443/catalog.ttl
https://localhost:8443/dataset/<nom>.rdf
```

Le plugin `structured_data` ajoute aussi des métadonnées Schema.org dans les pages, ce qui permet à Google Dataset Search de référencer vos données.

### Autres extensions utiles

| Extension | Utilité |
|---|---|
| `ckanext-xloader` | Chargement rapide des CSV dans le DataStore |
| `ckanext-scheming` | Personnaliser les champs de métadonnées (ajouter « couverture géographique », etc.) |
| `ckanext-harvest` | Moissonner d'autres catalogues |
| `ckanext-spatial` | Recherche géographique et aperçu cartographique |
| `ckanext-showcase` | Présenter les réutilisations (applications, articles) |
| `ckanext-validation` | Valider les fichiers contre un schéma Frictionless |

---

## Module 8 : automatiser la publication

Un portail mis à jour à la main finit toujours par se figer. L'objectif est que chaque jeu de données soit publié par un script qui :

1. récupère les données depuis le système source ;
2. les nettoie ;
3. les **valide** contre un schéma ;
4. les publie via l'API, en créant ou en mettant à jour la ressource.

### Le script fourni

[`../scripts/publier.py`](../scripts/publier.py) fait les étapes 3 et 4. Installation :

```bash
cd scripts
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Utilisation :

```bash
export CKAN_URL=https://localhost:8443
export CKAN_API_TOKEN=<votre_jeton>

python publier.py \
  --fichier ../exemples/ecoles.csv \
  --schema ../exemples/ecoles.schema.json \
  --organisation ministere-education \
  --jeu ecoles-primaires \
  --titre "Écoles primaires publiques"
```

Si le fichier ne respecte pas le schéma (colonne manquante, valeur non numérique, identifiant en double), le script s'arrête et affiche les erreurs : rien n'est publié.

### Planifier

Pour une mise à jour quotidienne, une simple tâche `cron` suffit au début :

```cron
0 3 * * * cd /opt/pipelines && .venv/bin/python publier.py --fichier /data/ecoles.csv ...
```

Quand les pipelines se multiplient, passez à un orchestrateur (Airflow, Dagster, Prefect) ou à GitHub Actions avec un déclenchement planifié.

### Décrire ses données avec un schéma

Le schéma [`../exemples/ecoles.schema.json`](../exemples/ecoles.schema.json) suit la spécification Table Schema de Frictionless Data. Publier le schéma à côté des données sert deux fois : il valide les données avant publication et documente chaque colonne pour les réutilisateurs.

---

# Partie C : faire vivre le portail

## Module 9 : demande et engagement des réutilisateurs

Le Toolkit insiste sur ce point : **un portail sans réutilisateurs est un échec, quel que soit le nombre de jeux publiés.**

### Connaître ses utilisateurs

| Public | Ce qu'il attend |
|---|---|
| Développeurs et startups | API stables, données à jour, documentation |
| Journalistes | Données fiables, contact rapide avec le producteur |
| Chercheurs | Historique, méthodologie, citations |
| Société civile et ONG | Données locales, formats simples |
| Administrations | Données des autres services, sans procédure |

### Les actions d'animation

- **Formulaire de demande de données** visible sur la page d'accueil, avec une réponse publique à chaque demande.
- **Page des réutilisations** (extension `ckanext-showcase`) : applications, visualisations, articles qui utilisent vos données.
- **Hackathons et concours** autour d'un thème (budget, transport, agriculture).
- **Partenariats** avec les universités et les écoles d'ingénieurs.
- **Formations** pour les journalistes et les associations.
- **Lettre d'information** annonçant les nouveaux jeux de données.

### Mesurer

| Indicateur | Source |
|---|---|
| Visites et téléchargements | Outil d'audience (Matomo, respectueux de la vie privée) |
| Appels à l'API | Journaux Nginx |
| Réutilisations recensées | Page des réutilisations |
| Fraîcheur | Part des jeux mis à jour dans les délais annoncés |
| Demandes de données traitées | Formulaire de demande |

---

## Module 10 : mise en production et pérennité

### Liste de vérification avant l'ouverture publique

- Nom de domaine et certificat HTTPS (Let's Encrypt).
- Mots de passe et clés secrètes uniques, hors du dépôt Git.
- Sauvegardes automatiques de PostgreSQL et du stockage des fichiers, avec un test de restauration.
- Supervision : disponibilité du site et de l'API, espace disque.
- Mises à jour de sécurité de CKAN et des images Docker planifiées.
- Conditions générales d'utilisation publiées.
- Politique de confidentialité publiée (cookies, mesure d'audience, comptes utilisateurs).
- Page de contact et mentions légales.
- Accessibilité de l'interface vérifiée (RGAA ou WCAG).

### Sauvegarde de la base

```bash
docker compose exec db pg_dump -U ckandbuser ckandb > sauvegarde_$(date +%F).sql
```

### Dimensionnement indicatif

| Taille du portail | Serveur |
|---|---|
| Jusqu'à 500 jeux de données | 2 processeurs, 4 Go de mémoire, 50 Go de disque |
| Jusqu'à 5 000 jeux de données | 4 processeurs, 8 à 16 Go de mémoire, Solr et PostgreSQL séparés |
| Au-delà | Services gérés pour la base, stockage objet, plusieurs instances CKAN |

### La pérennité selon le Toolkit

Les initiatives open data échouent rarement pour des raisons techniques. Elles échouent quand :

- le sponsor politique change et personne ne reprend le projet ;
- le budget couvre le lancement mais pas les années suivantes ;
- la publication repose sur une seule personne ;
- les données ne sont plus mises à jour.

Les parades : inscrire l'ouverture des données dans un texte (décret, politique officielle), intégrer la publication aux processus métiers des services, et refaire une ODRA tous les deux ou trois ans pour mesurer les progrès.

---

## Projet final

Construisez un mini-portail thématique :

1. une ODRA simplifiée de l'organisation choisie ;
2. une instance CKAN avec deux organisations et dix jeux de données documentés ;
3. au moins trois jeux publiés automatiquement par un script avec validation ;
4. le catalogue exposé en DCAT ;
5. une page des réutilisations avec un premier exemple (une visualisation que vous aurez réalisée) ;
6. les CGU et la politique de confidentialité.

## Pour aller plus loin

- Banque mondiale, Open Data Toolkit : https://www.banquemondiale.org/fr/data/opendatatoolkit/home
- Documentation CKAN : https://docs.ckan.org
- Frictionless Data : https://frictionlessdata.io
- Guides Etalab : https://guides.data.gouv.fr
- Open Data Handbook : https://opendatahandbook.org
- Spécification DCAT du W3C : https://www.w3.org/TR/vocab-dcat-3/
