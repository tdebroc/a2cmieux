# A2CMieux — Sports et Loisirs en Duo

Site web de l'association **A2CMieux**, club sportif parisien affilié à la Fédération
Française Handisport, qui rend le sport accessible aux personnes déficientes visuelles
grâce à des **Duos Sportifs** (un guide + un·e sportif·ve).

## ✨ Caractéristiques

- Charte graphique moderne 2026 (orange du logo + bleu marine, dégradés, glassmorphism, animations au défilement)
- **Accessibilité** : mode contraste élevé, agrandissement du texte (préférences mémorisées),
  lien d'évitement, HTML sémantique + ARIA, focus visibles, support `prefers-reduced-motion`, textes alternatifs
- Site statique multi-pages (aucune dépendance runtime)

## 📂 Structure

```
site/                 # Site publié (racine GitHub Pages)
  index.html, ...     # Pages HTML
  assets/css|js|img   # Styles, scripts, images
build.py              # Génère les pages HTML depuis un gabarit commun
.github/workflows/    # Déploiement automatique sur GitHub Pages
```

## 🛠️ Développement

Régénérer les pages :

```bash
python3 build.py
```

Prévisualiser localement :

```bash
cd site && python3 -m http.server 8000
# puis http://localhost:8000
```

## 🚀 Déploiement

À chaque `push` sur `main`, le workflow GitHub Actions publie le dossier `site/`
sur **GitHub Pages**.
