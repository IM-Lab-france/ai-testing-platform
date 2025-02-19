#!/bin/bash

# Construire l'image Docker pour le backend
docker build -t ai-testing-platform-backend -f docker/Dockerfile.backend ../backend

# Vérifier que l'image a été construite correctement
if [ $? -ne 0 ]; then
    echo "Failed to build the Docker image."
    exit 1
fi

# Exécuter un conteneur à partir de l'image
docker run -d -p 8000:8000 ai-testing-platform-backend

# Attendre que le conteneur soit prêt
sleep 10

# Vérifier que le backend est accessible
if curl -s --head http://localhost:8000; then
    echo "Backend is up and running."
else
    echo "Backend is not accessible."
    exit 1
fi

# Arrêter et supprimer le conteneur
docker rm -f $(docker ps -aq --filter "ancestor=ai-testing-platform-backend")


#### UTILISATION ####
# chmod +x docker/tests/test_dockerfile_backend.sh
# docker/tests/test_dockerfile_backend.sh