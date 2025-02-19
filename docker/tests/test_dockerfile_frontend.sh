#!/bin/bash

# Construire l'image Docker pour le frontend
docker build -t ai-testing-platform-frontend -f docker/Dockerfile.frontend ../frontend

# Vérifier que l'image a été construite correctement
if [ $? -ne 0 ]; then
    echo "Failed to build the Docker image."
    exit 1
fi

# Exécuter un conteneur à partir de l'image
docker run -d -p 3000:3000 ai-testing-platform-frontend

# Attendre que le conteneur soit prêt
sleep 10

# Vérifier que le frontend est accessible
if curl -s --head http://localhost:3000; then
    echo "Frontend is up and running."
else
    echo "Frontend is not accessible."
    exit 1
fi

# Arrêter et supprimer le conteneur
docker rm -f $(docker ps -aq --filter "ancestor=ai-testing-platform-frontend")


#### UTILISATION ####
# chmod +x docker/tests/test_dockerfile_frontend.sh
# docker/tests/test_dockerfile_frontend.sh