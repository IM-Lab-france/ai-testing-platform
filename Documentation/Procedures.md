Procédures pour la Plateforme de Test d'IAs
1. Procédure de Configuration de l'Environnement
Objectif : Préparer l'environnement pour le développement et le déploiement de l'application.

Étapes :

Installer Docker : Assurez-vous que Docker est installé sur votre machine. Vous pouvez télécharger Docker depuis docker.com.
Configurer Docker Compose : Installez Docker Compose en suivant les instructions sur docs.docker.com.
Cloner le Dépôt : Clonez le dépôt de l'application depuis votre système de gestion de version (par exemple, Git).
Configurer les Variables d'Environnement : Créez un fichier .env à la racine du projet avec les variables nécessaires (par exemple, DATABASE_URL, OPENAI_API_KEY, etc.).
2. Procédure d'Installation de l'Application
Objectif : Installer l'application et ses dépendances.

Étapes :

Naviguer vers le Répertoire du Projet : Ouvrez un terminal et naviguez vers le répertoire racine du projet.
Construire les Images Docker : Exécutez la commande suivante pour construire les images Docker pour le backend et le frontend :

docker-compose build
Démarrer les Services : Utilisez Docker Compose pour démarrer les services :

docker-compose up -d
Vérifier les Services : Assurez-vous que les services backend et frontend sont accessibles en vérifiant les ports 8000 et 3000 respectivement.
3. Procédure d'Exploitation
Objectif : Gérer l'application en production.

Étapes :

Surveiller les Logs : Utilisez Docker pour surveiller les logs des conteneurs :

docker-compose logs -f
Mettre à Jour l'Application : Pour mettre à jour l'application, arrêtez les services, tirez les dernières modifications du dépôt, construisez les images Docker, et redémarrez les services :

docker-compose down
git pull origin main
docker-compose build
docker-compose up -d
Scaler les Services : Si nécessaire, scalez les services en utilisant Docker Compose :

docker-compose up --scale backend=3 -d
4. Procédure d'Utilisation
Objectif : Utiliser l'application pour gérer les fournisseurs d'IA et les campagnes.

Étapes :

Accéder à l'Interface Utilisateur : Ouvrez un navigateur et accédez à http://localhost:3000 pour utiliser l'application.
Ajouter un Fournisseur d'IA : Utilisez le formulaire dans la section "Provider Management" pour ajouter un nouveau fournisseur d'IA.
Créer une Campagne : Utilisez la section "Campaign Management" pour créer une nouvelle campagne.
Lancer une Campagne : Sélectionnez une campagne existante et lancez-la pour évaluer les performances des IAs.
Supprimer des Données : Utilisez les options de suppression dans l'interface pour supprimer des fournisseurs d'IA ou des campagnes.
5. Procédure de Sauvegarde des Données
Objectif : Sauvegarder les données de l'application.

Étapes :

Sauvegarder la Base de Données : Utilisez pg_dump pour sauvegarder la base de données PostgreSQL :

docker exec -t <db_container_id> pg_dump -U user -F c -b -v -f /backups/db_backup.sql
Sauvegarder les Données des Conteneurs : Utilisez Docker pour sauvegarder les volumes de données :

docker run --rm --volumes-from <db_container_id> -v $(pwd)/backup:/backup ubuntu bash -c "cd /var/lib/postgresql/data && tar cvf /backup/db_data_backup.tar ."
Stocker les Sauvegardes : Transférez les fichiers de sauvegarde vers un stockage sécurisé.
Procédures Supplémentaires
Procédure de Débogage : Utilisez des outils comme docker logs et docker exec pour déboguer les conteneurs en cas de problème.
Procédure de Sécurité : Assurez-vous que les communications entre les conteneurs sont sécurisées et que les secrets sont gérés de manière sécurisée.
Procédure de Documentation : Maintenez une documentation à jour pour chaque composant de l'application.
Procédure de Tests : Exécutez régulièrement les tests unitaires et d'intégration pour assurer la stabilité de l'application.
Ces procédures couvrent les aspects essentiels de la configuration, de l'installation, de l'exploitation, de l'utilisation, et de la sauvegarde de l'application. Vous pouvez adapter ces procédures en fonction des besoins spécifiques de votre environnement et de votre organisation.