# cart-service

📦 Installation

# Cloner le repo
git clone git@github.com:eshop-backend/cart-service.git
cd cart-service

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate


# Installer les dépendances

pip install -r requirements.txt


🐳 Lancer Redis avec Docker

docker run -d -p 6379:6379 --name redis-cart redis


🚀 Lancer le service FastAPI

uvicorn main:app --reload --port 4002


🧪 Endpoints disponibles

Méthode	URL	Description
GET	/cart/{user_id}	Récupérer un panier
POST	/cart	Ajouter un produit
DELETE	/cart/{user_id}/{product_id}	Supprimer un produit
