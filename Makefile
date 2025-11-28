.PHONY: dev up down logs build restart

# Lancer en mode attach (utile pour le dev)
dev:
	docker compose up --build

# Lancer en detached
up:
	docker compose up -d --build

# Arrêter et supprimer containers + volumes liés
down:
	docker compose down --volumes --remove-orphans

# Voir logs en temps réel
logs:
	docker compose logs -f

# Rebuild sans cache (si besoin)
build:
	docker compose build --no-cache

restart: down up
