I) installer docker avec la commande "sudo apt-get install docker.io"
II) installer docker-compose "sudo apt-get install docker-compose"
III) creer un fichier docker-compose.yml pour definir les services odoo et postgrsSQL
version: '3.1'
services:
  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
    volumes:
      - odoo-db-data:/var/lib/postgresql/data

  odoo:
    image: odoo:17.0
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./custom-addons:/mnt/extra-addons
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo

volumes:
  odoo-db-data:
  odoo-web-data:
  
IV) Executez la commande "docker-compose up -d" pour demarrer les services  
V) comamnde pour redemarrer le conteneur  "docker-compose restart"
VI) Allez dans Odoo (http://localhost:8069),Activez le mode développeur.

Allez dans Applications > Mettre à jour la liste des modules
