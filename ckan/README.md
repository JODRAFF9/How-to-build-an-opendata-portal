# Lancer CKAN en local

Ce dossier complète le module 5 du tutoriel. Il s'appuie sur le dépôt officiel https://github.com/ckan/ckan-docker.

## Installation

```bash
git clone https://github.com/ckan/ckan-docker.git
cd ckan-docker
cp .env.example .env
```

Ajoutez ou remplacez dans `.env` les valeurs de [`env.exemple`](env.exemple), puis :

```bash
docker compose build
docker compose up -d
```

Le portail est disponible sur https://localhost:8443.

## Ajouter l'extension DCAT

Dans `ckan/Dockerfile` du dépôt `ckan-docker`, ajoutez :

```dockerfile
RUN pip install -e git+https://github.com/ckan/ckanext-dcat.git#egg=ckanext-dcat && \
    pip install -r ${APP_DIR}/src/ckanext-dcat/requirements.txt
```

Ajoutez `dcat structured_data` à `CKAN__PLUGINS`, puis reconstruisez :

```bash
docker compose build ckan && docker compose up -d
```

## Commandes utiles

```bash
docker compose logs -f ckan          # journaux de CKAN
docker compose exec ckan ckan sysadmin add <utilisateur>   # nommer un administrateur
docker compose exec ckan ckan search-index rebuild         # reconstruire l'index Solr
docker compose down                  # arrêter
```
