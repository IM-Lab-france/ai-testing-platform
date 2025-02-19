#!/bin/bash

# Démarrer les services avec docker-compose
docker-compose up -d

# Attendre que les services soient prêts
sleep 10

# Vérifier que le backend est accessible
if curl -s --head http://localhost:8000; then
    echo "Backend is up and running."
else
    echo "Backend is not accessible."
    exit 1
fi

# Vérifier que le frontend est accessible
if curl -s --head http://localhost:3000; then
    echo "Frontend is up and running."
else
    echo "Frontend is not accessible."
    exit 1
fi

# Arrêter les services
docker-compose down



##### UTILISATION #####
# chmod +x docker/tests/test_docker_compose.sh
# docker/tests/test_docker_compose.sh