#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages statiques du site A2CMieux à partir d'un gabarit commun."""
import os

OUT = os.path.join(os.path.dirname(__file__), "site")

# Pages HelloAsso officielles de l'association (fiables et à jour) — les
# formulaires datés ayant été retirés/redirigés, on pointe vers la page du compte.
HELLOASSO_BASE = "https://www.helloasso.com/associations/a2cmieux-sports-et-loisirs-en-duo"
HELLOASSO_ADH = HELLOASSO_BASE
HELLOASSO_DON = HELLOASSO_BASE
EMAIL = "contact.a2cmieux@gmail.com"
FFH = "https://www.handisport.org/"
INJA = "https://injalouisbraille.fr/"

INSTAGRAM = "https://www.instagram.com/a2cmieux.paris"
FACEBOOK = "https://www.facebook.com/a2cmieuxsports"
YOUTUBE = "https://www.youtube.com/channel/UCHil4jJGYPGS2OwvpxKMLXA/featured"

# Icônes SVG des réseaux sociaux (inline, sans dépendance externe)
_SVG_INSTA = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2Zm0 1.8c-3.1 0-3.5 0-4.7.1-1.1.1-1.7.2-2.1.4-.5.2-.9.4-1.2.8-.4.3-.6.7-.8 1.2-.2.4-.3 1-.4 2.1-.1 1.2-.1 1.6-.1 4.7s0 3.5.1 4.7c.1 1.1.2 1.7.4 2.1.2.5.4.9.8 1.2.3.4.7.6 1.2.8.4.2 1 .3 2.1.4 1.2.1 1.6.1 4.7.1s3.5 0 4.7-.1c1.1-.1 1.7-.2 2.1-.4.5-.2.9-.4 1.2-.8.4-.3.6-.7.8-1.2.2-.4.3-1 .4-2.1.1-1.2.1-1.6.1-4.7s0-3.5-.1-4.7c-.1-1.1-.2-1.7-.4-2.1-.2-.5-.4-.9-.8-1.2-.3-.4-.7-.6-1.2-.8-.4-.2-1-.3-2.1-.4-1.2-.1-1.6-.1-4.7-.1Zm0 3.1a4.9 4.9 0 1 1 0 9.8 4.9 4.9 0 0 1 0-9.8Zm0 8.1a3.2 3.2 0 1 0 0-6.4 3.2 3.2 0 0 0 0 6.4Zm6.3-8.3a1.15 1.15 0 1 1-2.3 0 1.15 1.15 0 0 1 2.3 0Z"/></svg>'
_SVG_FB = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path fill="currentColor" d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12Z"/></svg>'
_SVG_YT = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path fill="currentColor" d="M23 7.5a3 3 0 0 0-2.1-2.1C19 4.9 12 4.9 12 4.9s-7 0-8.9.5A3 3 0 0 0 1 7.5 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.5a3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 23.5 12 31 31 0 0 0 23 7.5ZM9.8 15.3V8.7l5.7 3.3-5.7 3.3Z"/></svg>'


def social_links(classname="social", labelled=False):
    items = [
        (INSTAGRAM, "Instagram", "Instagram", _SVG_INSTA),
        (FACEBOOK, "Facebook", "Facebook", _SVG_FB),
        (YOUTUBE, "YouTube", "Chaîne YouTube", _SVG_YT),
    ]
    out = ['<div class="{c}">'.format(c=classname)]
    for url, name, aria, svg in items:
        text = '<span>{n}</span>'.format(n=name) if labelled else ''
        out.append(
            '<a href="{u}" target="_blank" rel="noopener" aria-label="{a} (nouvel onglet)" class="social-{k}">{svg}{t}</a>'.format(
                u=url, a=aria, k=name.lower(), svg=svg, t=text)
        )
    out.append('</div>')
    return "".join(out)


NAV = [
    ("Accueil", "index.html", None),
    ("L'association", None, [
        ("Nos missions", "nos-missions.html"),
        ("Qui sommes-nous ?", "qui-sommes-nous.html"),
        ("Nos partenaires", "nos-partenaires.html"),
    ]),
    ("Les sports", "les-sports.html", None),
    ("Événements", "les-evenements.html", None),
    ("Nous soutenir", None, [
        ("Adhésions", "adhesions.html"),
        ("Faire un don", "faire-un-don.html"),
        ("Devenir bénévole", "devenir-benevole.html"),
    ]),
    ("Contact", "contact.html", None),
]


def menu_html(active):
    items = []
    for label, href, sub in NAV:
        if sub:
            open_child = any(active == s[1] for s in sub)
            subitems = "".join(
                '<li><a href="{h}"{cur}>{l}</a></li>'.format(
                    h=s[1], l=s[0], cur=' aria-current="page"' if active == s[1] else "")
                for s in sub
            )
            items.append(
                '<li class="has-sub" data-open="false">'
                '<button type="button" aria-expanded="false" aria-haspopup="true">{l} <span aria-hidden="true">▾</span></button>'
                '<ul class="submenu">{sub}</ul></li>'.format(l=label, sub=subitems)
            )
        else:
            cur = ' aria-current="page"' if active == href else ""
            items.append('<li><a href="{h}"{cur}>{l}</a></li>'.format(h=href, l=label, cur=cur))
    items.append('<li><a class="btn-nav" href="adhesions.html">Adhérer</a></li>')
    return "\n        ".join(items)


def header(active):
    return """  <a class="skip-link" href="#main">Aller au contenu principal</a>

  <div class="a11y-bar" role="region" aria-label="Options d'accessibilité et réseaux sociaux">
    <div class="container">
      <span class="a11y-bar-label">Suivez-nous</span>
      """ + social_links("social social--bar") + """
      <button type="button" id="a11y-open" class="a11y-btn" aria-expanded="false" aria-controls="a11y-panel">
        <span aria-hidden="true">&#9855;</span> Options d'accessibilité
      </button>
    </div>
  </div>

  <div class="a11y-overlay" id="a11y-overlay" hidden></div>
  <aside class="a11y-panel" id="a11y-panel" role="dialog" aria-modal="true" aria-labelledby="a11y-title" hidden>
    <div class="a11y-panel-head">
      <h2 id="a11y-title"><span aria-hidden="true">&#9855;</span> Accessibilité</h2>
      <button type="button" id="a11y-close" class="a11y-close" aria-label="Fermer le panneau d'accessibilité">&#10005;</button>
    </div>
    <p class="a11y-panel-intro">Adaptez l'affichage à votre confort. Vos réglages sont mémorisés sur cet appareil.</p>
    <div class="a11y-grid">
      <button type="button" class="a11y-tool" data-a11y="text-plus"><span class="ico" aria-hidden="true">A+</span> Augmenter le texte</button>
      <button type="button" class="a11y-tool" data-a11y="text-minus"><span class="ico" aria-hidden="true">A&minus;</span> Diminuer le texte</button>
      <button type="button" class="a11y-tool" data-a11y="grayscale" aria-pressed="false"><span class="ico" aria-hidden="true">&#9681;</span> Niveaux de gris</button>
      <button type="button" class="a11y-tool" data-a11y="contrast" aria-pressed="false"><span class="ico" aria-hidden="true">&#9680;</span> Haut contraste</button>
      <button type="button" class="a11y-tool" data-a11y="negative" aria-pressed="false"><span class="ico" aria-hidden="true">&#9635;</span> Contraste négatif</button>
      <button type="button" class="a11y-tool" data-a11y="lightbg" aria-pressed="false"><span class="ico" aria-hidden="true">&#9723;</span> Arrière-plan clair</button>
      <button type="button" class="a11y-tool" data-a11y="underline" aria-pressed="false"><span class="ico" aria-hidden="true">&#95;</span> Liens soulignés</button>
      <button type="button" class="a11y-tool" data-a11y="readable" aria-pressed="false"><span class="ico" aria-hidden="true">&#9633;A</span> Police lisible</button>
    </div>
    <button type="button" class="a11y-reset" data-a11y="reset"><span aria-hidden="true">&#8635;</span> Réinitialiser</button>
  </aside>

  <header class="site-header">
    <nav class="container nav" aria-label="Navigation principale">
      <a class="brand" href="index.html" aria-label="A2CMieux, retour à l'accueil">
        <img src="assets/img/logo.png" alt="" width="48" height="48">
        <span><b>A2CMieux</b><small>Sports en duo · Paris</small></span>
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="primary-menu">
        <span aria-hidden="true">☰</span> Menu
      </button>
      <ul class="menu" id="primary-menu">
        {menu}
      </ul>
    </nav>
  </header>
""".format(menu=menu_html(active))


def footer():
    return """  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="assets/img/logo.png" alt="Logo A2CMieux">
          <p>A2CMieux — Sports et Loisirs en Duo. Club sportif parisien affilié à la Fédération Française Handisport, rendant le sport accessible aux personnes déficientes visuelles.</p>
          <p class="footer-follow"><strong>Suivez-nous&nbsp;:</strong></p>
          """ + social_links("social social--footer", labelled=True) + """
        </div>
        <div>
          <h4>Naviguer</h4>
          <ul>
            <li><a href="nos-missions.html">Nos missions</a></li>
            <li><a href="qui-sommes-nous.html">Qui sommes-nous ?</a></li>
            <li><a href="les-sports.html">Les sports</a></li>
            <li><a href="les-evenements.html">Événements</a></li>
          </ul>
        </div>
        <div>
          <h4>S'engager</h4>
          <ul>
            <li><a href="adhesions.html">Adhérer</a></li>
            <li><a href="faire-un-don.html">Faire un don</a></li>
            <li><a href="devenir-benevole.html">Devenir bénévole</a></li>
            <li><a href="nos-partenaires.html">Nos partenaires</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:{email}">{email}</a></li>
            <li><a href="contact.html">Formulaire de contact</a></li>
            <li>Paris, France</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span id="year">2026</span> A2CMieux — Association loi 1901. Tous droits réservés.</span>
        <span><a href="politique-de-confidentialite.html">Politique de confidentialité</a></span>
      </div>
    </div>
  </footer>

  <script src="assets/js/main.js"></script>
</body>
</html>""".format(email=EMAIL)


def page(active, title, description, body):
    return """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta name="theme-color" content="#FF7235">
  <link rel="icon" href="assets/img/logo.png">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{header}
  <main id="main">
{body}
  </main>
{footer}""".format(title=title, desc=description, header=header(active), body=body, footer=footer())


def page_head(crumb, h1, intro):
    return """    <section class="page-head">
      <div class="container">
        <p class="crumb"><a href="index.html">Accueil</a> › {crumb}</p>
        <h1>{h1}</h1>
        <p class="reveal">{intro}</p>
      </div>
    </section>
""".format(crumb=crumb, h1=h1, intro=intro)


def cta_block():
    return """    <section class="section">
      <div class="container">
        <div class="callout reveal">
          <h2>Prêt·e à nous rejoindre&nbsp;?</h2>
          <p>Que vous soyez déficient·e visuel·le, guide bénévole ou simplement motivé·e, il y a une place pour vous chez A2CMieux. Le sport, ça se vit mieux à deux&nbsp;!</p>
          <div class="btn-group" style="justify-content:center">
            <a class="btn btn-primary btn-lg" href="adhesions.html">Adhérer à l'association</a>
            <a class="btn btn-outline btn-lg" href="contact.html">Nous contacter</a>
          </div>
        </div>
      </div>
    </section>
"""


PAGES = {}

# ------------------------------------------------------------------ ACCUEIL
PAGES["index.html"] = dict(
    active="index.html",
    title="A2CMieux — Sports et Loisirs en Duo",
    description="A2CMieux, club sportif parisien affilié à la Fédération Française Handisport, rend le sport accessible aux personnes déficientes visuelles grâce à des Duos Sportifs guide + sportif.",
    body="""    <section class="hero">
      <div class="container">
        <div class="reveal">
          <span class="eyebrow"><span class="dot"></span> Club affilié à la Fédération Française Handisport</span>
          <h1>Le sport, ça se vit <span>mieux à deux</span>.</h1>
          <p class="lead">A2CMieux forme des <strong>Duos Sportifs</strong> — un guide et une personne déficiente visuelle — pour rendre le vélo, la natation, la course à pied et le triathlon accessibles à toutes et à tous.</p>
          <div class="btn-group">
            <a class="btn btn-primary btn-lg" href="adhesions.html">Rejoindre l'association</a>
            <a class="btn btn-outline btn-lg" href="les-sports.html">Découvrir les sports</a>
          </div>
        </div>
        <div class="hero-media reveal">
          <img src="assets/img/gallery/photo-01.png" alt="Deux sportives de l'association A2CMieux, en maillot orange, souriant pendant une séance de vélo.">
          <div class="badge">
            <span class="ic" aria-hidden="true">🤝</span>
            <span><b>+50%</b><small>d'adhérentes femmes</small></span>
          </div>
        </div>
      </div>
    </section>

    <section class="stripe section">
      <div class="container">
        <div class="stat-grid reveal">
          <div class="stat"><b>4</b><span>disciplines sportives</span></div>
          <div class="stat"><b>100%</b><span>bénévole &amp; solidaire</span></div>
          <div class="stat"><b>Gratuit</b><span>pour les participants</span></div>
          <div class="stat"><b>Paris</b><span>et Île-de-France</span></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="center narrow reveal">
          <p class="tag-line">Notre raison d'être</p>
          <h2>Rendre le sport accessible à toutes et à tous</h2>
          <p>A2CMieux est une association, mais c'est avant tout un club sportif qui favorise toute activité sportive ou de loisir organisée par ou pour des personnes atteintes de déficience visuelle. Quels que soient votre niveau, vos besoins ou votre projet, nous vous accompagnons.</p>
        </div>
        <div class="grid grid-3" style="margin-top:2.4rem">
          <article class="card reveal">
            <div class="ic" aria-hidden="true">👁️</div>
            <h3>Des Duos Sportifs</h3>
            <p>Chaque duo associe un guide bénévole et une personne déficiente visuelle, dans un binôme harmonieux et adapté au niveau de chacun·e.</p>
          </article>
          <article class="card reveal">
            <div class="ic" aria-hidden="true">🎯</div>
            <h3>Du loisir à la compétition</h3>
            <p>Initiation, pratique loisir, reprise d'activité, entraînements réguliers ou préparation aux compétitions : à vous de choisir.</p>
          </article>
          <article class="card reveal">
            <div class="ic" aria-hidden="true">💛</div>
            <h3>Une communauté</h3>
            <p>Une équipe soudée, bienveillante et 100% bénévole, ouverte à toutes et à tous, adolescents comme adultes.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split reveal">
          <div class="split-media"><img src="assets/img/gallery/photo-08.png" alt="Un duo de cyclistes A2CMieux posant avec leur tandem devant la basilique du Sacré-Cœur à Paris."></div>
          <div>
            <p class="tag-line">Nos sports</p>
            <h2>Quatre disciplines, un même esprit</h2>
            <p>Nous formons des duos adaptés dans plusieurs disciplines. Envie de tester&nbsp;? Nous mettons tout en œuvre pour réaliser votre projet sportif.</p>
            <ul class="ticks">
              <li>Cyclisme en tandem</li>
              <li>Natation</li>
              <li>Course à pied</li>
              <li>Triathlon &amp; duathlon</li>
            </ul>
            <div class="btn-group">
              <a class="btn btn-primary" href="les-sports.html">Voir toutes les activités</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="split reverse reveal">
          <div class="split-media"><img src="assets/img/gallery/photo-15.png" alt="Groupe de coureurs et de guides A2CMieux réunis sur une piste d'athlétisme à Paris."></div>
          <div>
            <p class="tag-line">Devenez guide</p>
            <h2>Nous avons besoin de vous</h2>
            <p>Nos Duos Sportifs ne peuvent exister sans guides. Pour ne pas solliciter constamment les mêmes personnes et composer des binômes harmonieux, il est primordial d'avoir de nouveaux guides, dans toutes les disciplines.</p>
            <p>Aucune expérience particulière n'est requise : nous formons et accompagnons chaque guide.</p>
            <div class="btn-group">
              <a class="btn btn-primary" href="adhesions.html">Devenir guide</a>
              <a class="btn btn-outline" href="devenir-benevole.html">Autres façons d'aider</a>
            </div>
          </div>
        </div>
      </div>
    </section>

""" + cta_block(),
)

# ------------------------------------------------------------------ NOS MISSIONS
PAGES["nos-missions.html"] = dict(
    active="nos-missions.html",
    title="Nos missions — A2CMieux",
    description="A2CMieux forme des Duos Sportifs adaptés au niveau de chacun pour permettre aux personnes déficientes visuelles de pratiquer un sport.",
    body=page_head("Nos missions", "Nos missions",
        "Permettre à des personnes atteintes de déficience visuelle de faire du sport au travers d'un Duo Sportif, formé de manière harmonieuse et adaptée au niveau de chacun·e.") +
"""    <section class="section">
      <div class="container">
        <div class="split reveal">
          <div class="split-media"><img src="assets/img/gallery/photo-20.png" alt="Quatre membres d'A2CMieux devant un atelier vélo, présentant un maillot orange du club et un tandem."></div>
          <div>
            <p class="tag-line">Un accompagnement sur mesure</p>
            <h2>Des duos adaptés à chacun·e</h2>
            <p>Un Duo Sportif est composé d'un guide et d'une personne déficiente visuelle. Nous prêtons une attention particulière aux binômes&nbsp;: chaque guide est formé et accompagné, et nous disposons de coachs professionnels pour certaines de nos activités.</p>
            <p>A2CMieux est ouvert à toutes et à tous (plus de 50% d'adhérentes), adolescents ou adultes, débutants ou sportifs confirmés, pratiquants réguliers ou non. Vous avez un projet&nbsp;? Nous mettrons tout en œuvre pour le réaliser.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="center narrow reveal">
          <p class="tag-line">Ce que nous proposons</p>
          <h2>Du premier essai à la compétition</h2>
        </div>
        <div class="grid grid-3 reveal" style="margin-top:2rem">
          <article class="card"><div class="ic" aria-hidden="true">✨</div><h3>Initiations découvertes</h3><p>Des séances d'initiation pour découvrir chacun des sports que nous pratiquons.</p></article>
          <article class="card"><div class="ic" aria-hidden="true">🚴</div><h3>Pratique loisir</h3><p>Une pratique axée loisir, de manière occasionnelle ou régulière, selon vos envies.</p></article>
          <article class="card"><div class="ic" aria-hidden="true">🔄</div><h3>Reprise d'activité</h3><p>Une aide à la reprise d'une activité sportive, en douceur et en confiance.</p></article>
          <article class="card"><div class="ic" aria-hidden="true">🏋️</div><h3>Entraînements réguliers</h3><p>Des entraînements réguliers pour progresser et se dépasser.</p></article>
          <article class="card"><div class="ic" aria-hidden="true">🏅</div><h3>Compétitions</h3><p>La préparation et la participation aux compétitions sportives.</p></article>
          <article class="card"><div class="ic" aria-hidden="true">🎓</div><h3>Actions jeunesse</h3><p>Des actions avec l'Institut National des Jeunes Aveugles (INJA) pour inciter les jeunes à faire du sport.</p></article>
        </div>
      </div>
    </section>

""" + cta_block(),
)

# ------------------------------------------------------------------ QUI SOMMES-NOUS
PAGES["qui-sommes-nous.html"] = dict(
    active="qui-sommes-nous.html",
    title="Qui sommes-nous ? — A2CMieux",
    description="Découvrez A2CMieux, association loi 1901 et club sportif affilié à la Fédération Française Handisport, et l'équipe de bénévoles qui l'anime.",
    body=page_head("Qui sommes-nous&nbsp;?", "Qui sommes-nous ?",
        "Une association loi 1901, un club sportif affilié à la Fédération Française Handisport, et surtout une équipe de bénévoles passionnés.") +
"""    <section class="section">
      <div class="container">
        <div class="split reveal">
          <div>
            <p class="tag-line">Notre histoire</p>
            <h2>Le sport comme trait d'union</h2>
            <p>A2CMieux — « Association pour Cyclisme, Course, Mieux » — est née de la conviction que le sport doit être accessible à toutes et à tous. Club sportif affilié à la <a href="{ffh}" target="_blank" rel="noopener">Fédération Française Handisport</a>, l'association a pour objet de favoriser toute activité sportive ou de loisir type multisport organisée par ou pour des personnes atteintes de déficience visuelle, grâce à la formation de Duos Sportifs.</p>
            <p>Nous accompagnons chaque personne, quels que soient son niveau, ses besoins et son projet, pour découvrir, débuter, s'entraîner ou se perfectionner.</p>
          </div>
          <div class="split-media"><img src="assets/img/gallery/tandem-groupe.jpg" alt="Un groupe de cyclistes de l'association A2CMieux à l'entraînement sur des tandems."></div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="center narrow reveal">
          <p class="tag-line">L'équipe</p>
          <h2>Des bénévoles engagés</h2>
          <p>Le bureau et les bénévoles font vivre l'association au quotidien&nbsp;: organisation des créneaux, formation des guides, événements et vie du club.</p>
        </div>
        <div class="grid grid-3 reveal" style="margin-top:2rem">
          <article class="card team-card"><div class="avatar" aria-hidden="true">L</div><h3>Ludovic</h3><p class="role">Bureau de l'association</p><p>Membre du bureau, impliqué dans la coordination des activités et l'accompagnement des duos.</p></article>
          <article class="card team-card"><div class="avatar" aria-hidden="true">S</div><h3>Stéphane</h3><p class="role">Bureau de l'association</p><p>Membre du bureau, engagé dans l'organisation des sorties et la vie du club.</p></article>
          <article class="card team-card"><div class="avatar" aria-hidden="true">S</div><h3>Salomé</h3><p class="role">Bureau de l'association</p><p>Membre du bureau, active dans l'animation de la communauté et l'accueil des nouveaux membres.</p></article>
          <article class="card team-card"><div class="avatar" aria-hidden="true">D</div><h3>Dany</h3><p class="role">Guide historique</p><p>Guide historique de l'association, présent depuis les débuts pour accompagner les duos et transmettre son expérience.</p></article>
          <article class="card team-card"><div class="avatar" aria-hidden="true">T</div><h3>Thibaut</h3><p class="role">Guide bénévole · Communication</p><p>Guide bénévole, il aide notamment sur la communication de l'association pour la faire rayonner.</p></article>
          <article class="card team-card"><div class="avatar" aria-hidden="true">É</div><h3>Éloïse</h3><p class="role">Bénévole · Compétitions</p><p>Bénévole, elle aide à l'inscription des duos aux compétitions sportives.</p></article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid grid-3 reveal">
          <article class="card"><div class="ic" aria-hidden="true">🤝</div><h3>Solidarité</h3><p>Composer des binômes harmonieux et ne jamais laisser quelqu'un de côté.</p></article>
          <article class="card"><div class="ic" aria-hidden="true">♿</div><h3>Accessibilité</h3><p>Rendre le sport possible pour toutes et tous, gratuitement pour les participants.</p></article>
          <article class="card"><div class="ic" aria-hidden="true">🌟</div><h3>Dépassement</h3><p>Accompagner chacun vers son propre objectif, du loisir à la compétition.</p></article>
        </div>
      </div>
    </section>

""".format(ffh=FFH) + cta_block(),
)

# ------------------------------------------------------------------ LES SPORTS
PAGES["les-sports.html"] = dict(
    active="les-sports.html",
    title="Les sports — A2CMieux",
    description="Vélo en tandem, natation, course à pied, triathlon et duathlon : découvrez les activités sportives d'A2CMieux pour personnes déficientes visuelles.",
    body=page_head("Les sports", "Les sports",
        "A2CMieux organise plusieurs activités sportives pour les personnes déficientes visuelles et leurs guides. Découvrez-les ci-dessous.") +
"""    <section class="section">
      <div class="container">
        <div class="grid grid-2 reveal">
          <article class="card sport-card">
            <img src="assets/img/gallery/tandem-super.jpg" alt="Deux tandems de l'association A2CMieux en pleine course sur route, pilotes et équipiers en maillot orange et noir.">
            <div class="body">
              <span class="tag">Cyclisme</span>
              <h3>Vélo en tandem</h3>
              <p>Sur un tandem, le guide pilote à l'avant et le·la sportif·ve déficient·e visuel·le pédale à l'arrière. Sorties conviviales et entraînements, de la balade à la performance.</p>
            </div>
          </article>
          <article class="card sport-card">
            <img src="assets/img/gallery/natation.jpg" alt="Un entraîneur A2CMieux encourage une nageuse au bord du bassin, front contre front, tous deux souriants.">
            <div class="body">
              <span class="tag">Aquatique</span>
              <h3>Natation</h3>
              <p>Sur nos créneaux piscine, encadrés par des maîtres-nageurs, débutants et confirmés progressent en sécurité, chacun à son rythme.</p>
            </div>
          </article>
          <article class="card sport-card">
            <img src="assets/img/gallery/course-guide.jpg" alt="Un guide et une coureuse d'A2CMieux reliés par un cordon de guidage lors d'une course à pied ensoleillée.">
            <div class="body">
              <span class="tag">Athlétisme</span>
              <h3>Course à pied</h3>
              <p>Reliés par un cordon de guidage, coureur et guide avancent ensemble. Du footing loisir aux courses officielles, à votre allure.</p>
            </div>
          </article>
          <article class="card sport-card">
            <img src="assets/img/gallery/podium-duathlon.jpg" alt="L'équipe A2CMieux réunie et souriante derrière une banderole de course, après une épreuve de duathlon.">
            <div class="body">
              <span class="tag">Endurance</span>
              <h3>Triathlon &amp; duathlon</h3>
              <p>Enchaîner natation, vélo et course (ou course et vélo pour le duathlon) : nos coachs préparent les duos aux épreuves multisports.</p>
            </div>
          </article>
        </div>
        <div class="center reveal" style="margin-top:2.4rem">
          <p class="lead">Un autre sport vous tente&nbsp;? Parlons-en&nbsp;! Nous formons des duos selon les envies de nos membres.</p>
          <a class="btn btn-primary btn-lg" href="contact.html">Proposer une activité</a>
        </div>
      </div>
    </section>

""" + cta_block(),
)

# ------------------------------------------------------------------ EVENEMENTS
PAGES["les-evenements.html"] = dict(
    active="les-evenements.html",
    title="Événements — A2CMieux",
    description="Retrouvez les temps forts d'A2CMieux : sorties, entraînements, courses et notre duathlon 2026 en vidéo.",
    body=page_head("Événements", "Nos événements",
        "Sorties, entraînements, compétitions et rendez-vous conviviaux rythment la vie d'A2CMieux tout au long de l'année.") +
"""    <section class="section">
      <div class="container">
        <div class="narrow center reveal">
          <p class="tag-line">À la une</p>
          <h2>Notre duathlon 2026 en vidéo</h2>
          <p>Revivez l'ambiance de notre duathlon 2026 : l'énergie des duos, l'entraide et le plaisir de partager le sport ensemble.</p>
        </div>
        <div class="reveal" style="max-width:900px;margin:2rem auto 0">
          <div class="video-frame">
            <iframe src="https://www.youtube-nocookie.com/embed/ug8ZdynpOYw?start=24"
              title="Duathlon avec A2CMieux — vidéo 2026"
              loading="lazy"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              referrerpolicy="strict-origin-when-cross-origin"
              allowfullscreen></iframe>
          </div>
          <p class="center" style="margin-top:1rem">
            <a class="btn btn-outline" href="https://www.youtube.com/watch?v=ug8ZdynpOYw&t=24s" target="_blank" rel="noopener">Voir la vidéo sur YouTube</a>
          </p>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="center narrow reveal">
          <p class="tag-line">Galerie</p>
          <h2>Retour en images</h2>
          <p>Quelques instants partagés lors de nos sorties et rendez-vous sportifs.</p>
        </div>
        <div class="gallery reveal" style="margin-top:2rem">
""" + "".join(
        '          <a href="assets/img/gallery/{f}" target="_blank" rel="noopener"><img src="assets/img/gallery/{f}" alt="{alt}" loading="lazy"></a>\n'.format(f=f, alt=alt)
        for f, alt in [
            ("marine.jpg", "Deux coureuses A2CMieux devant la tour Eiffel illuminée en soirée."),
            ("dany.jpg", "Un duo de coureurs A2CMieux, guide et sportif reliés, lors d'une course urbaine."),
            ("podium.jpg", "Des membres d'A2CMieux sur un podium de compétition avec de jeunes participants."),
            ("arrivee-team.jpg", "L'équipe A2CMieux franchissant l'arche d'arrivée d'une course, bras levés."),
            ("alexandre.jpg", "Un coureur A2CMieux accompagné de son guide lors d'une course en ville."),
            ("lepouce.jpg", "Un coureur A2CMieux lève le pouce en plein effort pendant une course."),
            ("rico.jpg", "Deux coureurs A2CMieux souriants avec leurs dossards après une épreuve."),
            ("louise.jpg", "Des coureuses A2CMieux à l'entraînement sur une piste d'athlétisme au crépuscule."),
            ("yasmine.jpg", "Deux coureuses A2CMieux sur une avenue arborée parisienne."),
            ("joelette.jpg", "Sortie A2CMieux avec une joëlette tout-terrain, ambiance de course de Noël."),
            ("mathieu.jpg", "Un duo de coureurs A2CMieux souriants, paysage de nature en arrière-plan."),
            ("ludo-stade-de-france.jpg", "Des membres d'A2CMieux devant la pelouse du Stade de France."),
            ("ludo-heureux.jpg", "Un coureur A2CMieux tout sourire en selfie pendant une course à Paris."),
            ("guillaume-bouchou.jpg", "Deux cyclistes A2CMieux casqués avec leur vélo avant un départ."),
            ("versailles.jpg", "Cyclistes et tandem A2CMieux devant le château de Versailles."),
        ]
    ) +
"""        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="callout reveal">
          <h2>Envie de participer à nos prochains rendez-vous&nbsp;?</h2>
          <p>Contactez-nous pour connaître les prochaines dates de sorties, d'entraînements et d'événements. Et pour ne rien manquer, suivez toutes nos aventures sur les réseaux sociaux&nbsp;!</p>
          <div class="btn-group" style="justify-content:center">
            <a class="btn btn-primary btn-lg" href="contact.html">Nous contacter</a>
            <a class="btn btn-outline btn-lg" href="adhesions.html">Adhérer</a>
          </div>
          """ + social_links("social social--callout", labelled=True) + """
        </div>
      </div>
    </section>
""",
)

# ------------------------------------------------------------------ ADHESIONS
PAGES["adhesions.html"] = dict(
    active="adhesions.html",
    title="Adhésions — A2CMieux",
    description="Adhérez à A2CMieux en tant que guide ou personne déficiente visuelle et rejoignez nos Duos Sportifs.",
    body=page_head("Adhésions", "Adhérer à A2CMieux",
        "Guide bénévole ou sportif·ve déficient·e visuel·le, votre adhésion fait vivre l'association et permet de composer de nouveaux Duos Sportifs.") +
"""    <section class="section">
      <div class="container">
        <div class="grid grid-2 reveal">
          <article class="card">
            <div class="ic" aria-hidden="true">🧑‍🦯</div>
            <h3>Vous êtes déficient·e visuel·le</h3>
            <p>Rejoignez un Duo Sportif adapté à votre niveau et à votre projet. Nos guides et coachs vous accompagnent, du premier essai à la compétition.</p>
          </article>
          <article class="card">
            <div class="ic" aria-hidden="true">🤝</div>
            <h3>Vous voulez devenir guide</h3>
            <p>Nous avons besoin de guides dans toutes les disciplines&nbsp;! Aucune expérience requise&nbsp;: nous vous formons et vous accompagnons.</p>
          </article>
        </div>

        <div class="narrow reveal" style="margin-top:2.6rem">
          <h2>Comment adhérer&nbsp;?</h2>
          <p>L'adhésion se fait en ligne, de manière simple et sécurisée, via la plateforme HelloAsso de l'association. Le tarif comprend l'adhésion à l'association A2CMieux.</p>
          <ul class="ticks">
            <li>Une adhésion valable pour la saison sportive.</li>
            <li>Une formule adaptée pour les guides et les personnes déficientes visuelles qui ne viennent pas aux créneaux piscine.</li>
            <li>Des conditions particulières si vous êtes déjà membre d'un club partenaire (Expatriés Triathlon, RMA Triathlon, Stade Français Triathlon).</li>
          </ul>
          <div class="btn-group">
            <a class="btn btn-primary btn-lg" href="{adh}" target="_blank" rel="noopener">Adhérer sur HelloAsso</a>
            <a class="btn btn-outline btn-lg" href="contact.html">Une question ? Contactez-nous</a>
          </div>
          <p style="margin-top:1rem;font-size:.9rem">Le lien ci-dessus ouvre la page sécurisée HelloAsso de l'association dans un nouvel onglet.</p>
        </div>
      </div>
    </section>
""".format(adh=HELLOASSO_ADH),
)

# ------------------------------------------------------------------ FAIRE UN DON
PAGES["faire-un-don.html"] = dict(
    active="faire-un-don.html",
    title="Faire un don — A2CMieux",
    description="Soutenez A2CMieux par un don. Tous nos événements sont gratuits pour les participants ; vos dons financent le matériel, les tandems et les créneaux.",
    body=page_head("Faire un don", "Faire un don",
        "Chez A2CMieux, nous sommes tous bénévoles et faisons face à des dépenses régulières, nécessaires au bon fonctionnement de l'association.") +
"""    <section class="section">
      <div class="container">
        <div class="split reveal">
          <div>
            <p class="tag-line">Pourquoi donner&nbsp;?</p>
            <h2>Votre soutien fait la différence</h2>
            <p>Tous nos événements sont <strong>gratuits</strong> pour les participants, et nous mettons un point d'honneur à les rendre accessibles à toutes et à tous. Mais cela engendre inévitablement des coûts. Grâce à vos dons, vous contribuez à la continuité de ce beau projet.</p>
            <div class="btn-group">
              <a class="btn btn-primary btn-lg" href="{don}" target="_blank" rel="noopener">Faire un don sur HelloAsso</a>
            </div>
          </div>
          <div class="card">
            <h3>À quoi servent vos dons&nbsp;?</h3>
            <ul class="ticks">
              <li>Organisation des événements (maître-nageur, location de bassin, etc.)</li>
              <li>Location du local pour entreposer les tandems</li>
              <li>Révision régulière du matériel</li>
              <li>Achat de nouveaux équipements et tandems</li>
              <li>Hébergement du site web</li>
              <li>Frais bancaires</li>
            </ul>
          </div>
        </div>
        <div class="narrow reveal" style="margin-top:2.4rem">
          <p>Par exemple, la révision des tandems est essentielle&nbsp;: ils sont partagés entre les guides et les personnes déficientes visuelles de l'association. De nombreux réglages garantissent des conditions de sécurité optimales lors de nos événements, et un usage fréquent impose une maintenance régulière.</p>
        </div>
      </div>
    </section>
""".format(don=HELLOASSO_DON),
)

# ------------------------------------------------------------------ DEVENIR BENEVOLE
PAGES["devenir-benevole.html"] = dict(
    active="devenir-benevole.html",
    title="Devenir bénévole — A2CMieux",
    description="Rejoignez l'équipe bénévole d'A2CMieux : communication, community management, communication visuelle ou administratif, toute aide est la bienvenue.",
    body=page_head("Devenir bénévole", "Devenir bénévole",
        "Chez A2CMieux, nous sommes tous et toutes bénévoles. Toute aide est la bienvenue, quels que soient vos disponibilités et le temps que vous pouvez nous consacrer.") +
"""    <section class="section">
      <div class="container">
        <div class="narrow reveal">
          <p>Il est important de nous faire connaître afin de chercher des guides, des partenariats et des subventions. Nous avons aussi besoin d'aide pour la gestion du club&nbsp;: les événements, les adhérents, et bien plus.</p>
        </div>
        <div class="grid grid-2 reveal" style="margin-top:2rem">
          <article class="card"><div class="ic" aria-hidden="true">📣</div><h3>Communication digitale</h3><p>Améliorer et développer notre communication vers nos partenaires sportifs et associatifs, futurs sponsors, médias, etc.</p></article>
          <article class="card"><div class="ic" aria-hidden="true">💬</div><h3>Community management</h3><p>Promouvoir et rendre visible l'association sur le web et les réseaux sociaux, gestion de l'e-mailing, etc.</p></article>
          <article class="card"><div class="ic" aria-hidden="true">🎨</div><h3>Communication visuelle</h3><p>Concevoir affiches, panneaux, flyers et supports pour faire rayonner l'association.</p></article>
          <article class="card"><div class="ic" aria-hidden="true">🗂️</div><h3>Administratif</h3><p>Demandes de subventions, gestion des adhérents et suivi de la vie associative.</p></article>
        </div>
        <div class="center reveal" style="margin-top:2.4rem">
          <h2>A2CMieux compte sur vous&nbsp;!</h2>
          <p>La meilleure façon de nous rejoindre et de faire vivre l'association, c'est d'<strong>adhérer</strong>. Votre adhésion nous permet de composer de nouveaux duos et de développer nos actions.</p>
          <div class="btn-group" style="justify-content:center">
            <a class="btn btn-primary btn-lg" href="adhesions.html">Adhérer à l'association</a>
            <a class="btn btn-outline btn-lg" href="faire-un-don.html">Faire un don</a>
          </div>
          <p style="margin-top:1.2rem;font-size:.95rem">Une question avant de vous engager&nbsp;? <a href="contact.html">Contactez-nous</a>.</p>
        </div>
      </div>
    </section>
""".format(email=EMAIL),
)

# ------------------------------------------------------------------ PARTENAIRES
PAGES["nos-partenaires.html"] = dict(
    active="nos-partenaires.html",
    title="Nos partenaires — A2CMieux",
    description="Découvrez les clubs et partenaires qui accompagnent A2CMieux dans sa mission d'accès au sport pour les personnes déficientes visuelles.",
    body=page_head("Nos partenaires", "Nos partenaires",
        "A2CMieux avance grâce à un réseau de clubs et de partenaires engagés à nos côtés pour rendre le sport accessible.") +
"""    <section class="section">
      <div class="container">
        <div class="partners reveal">
          <div class="partner"><div class="ic" aria-hidden="true" style="margin:0 auto 14px">🏊</div><b>RMA Triathlon</b><p>Club partenaire triathlon.</p></div>
          <div class="partner"><div class="ic" aria-hidden="true" style="margin:0 auto 14px">🏉</div><b>Stade Français Triathlon</b><p>Club partenaire triathlon.</p></div>
          <div class="partner"><div class="ic" aria-hidden="true" style="margin:0 auto 14px">🌍</div><b>Expatriés Triathlon</b><p>Club partenaire triathlon.</p></div>
        </div>
        <div class="narrow reveal" style="margin-top:2.4rem">
          <h2>Nos soutiens institutionnels</h2>
          <p>A2CMieux est un club sportif affilié à la <a href="{ffh}" target="_blank" rel="noopener">Fédération Française Handisport</a>. Nous menons également des actions avec l'<a href="{inja}" target="_blank" rel="noopener">Institut National des Jeunes Aveugles (INJA Louis Braille)</a> pour inciter les jeunes à pratiquer un sport.</p>
        </div>
        <div class="center reveal" style="margin-top:2rem">
          <h3>Devenir partenaire</h3>
          <p>Votre entreprise ou votre club souhaite nous soutenir&nbsp;? Parlons de ce que nous pouvons construire ensemble.</p>
          <a class="btn btn-primary btn-lg" href="contact.html">Devenir partenaire</a>
        </div>
      </div>
    </section>
""".format(ffh=FFH, inja=INJA),
)

# ------------------------------------------------------------------ CONTACT
PAGES["contact.html"] = dict(
    active="contact.html",
    title="Contact — A2CMieux",
    description="Contactez A2CMieux pour rejoindre l'association, devenir guide, proposer un partenariat ou poser vos questions.",
    body=page_head("Contact", "Nous contacter",
        "Une question, une envie de rejoindre l'aventure ou de nous soutenir ? Écrivez-nous, nous serons ravis de vous répondre.") +
"""    <section class="section">
      <div class="container">
        <div class="split reveal">
          <div>
            <h2>Parlons de votre projet</h2>
            <p>Que vous soyez une personne déficiente visuelle, un futur guide, un partenaire ou un média, n'hésitez pas à nous écrire.</p>
            <div class="card" style="margin-bottom:18px">
              <h3>E-mail</h3>
              <p><a href="mailto:contact.a2cmieux@gmail.com">contact.a2cmieux@gmail.com</a></p>
            </div>
            <div class="card" style="margin-bottom:18px">
              <h3>Où nous trouver</h3>
              <p>Paris et Île-de-France, France.</p>
            </div>
            <div class="card">
              <h3>Nous soutenir</h3>
              <p><a href="adhesions.html">Adhérer</a> · <a href="faire-un-don.html">Faire un don</a> · <a href="devenir-benevole.html">Devenir bénévole</a></p>
            </div>
            <div class="card">
              <h3>Suivez-nous</h3>
              <p>Retrouvez nos actualités et nos aventures sur les réseaux&nbsp;:</p>
              """ + social_links("social social--card", labelled=True) + """
            </div>
          </div>
          <div>
            <form class="form card" action="mailto:{email}" method="post" enctype="text/plain" aria-label="Formulaire de contact">
              <h3 class="mt-0">Formulaire de contact</h3>
              <div class="field">
                <label for="nom">Nom et prénom <span class="req" aria-hidden="true">*</span></label>
                <input id="nom" name="nom" type="text" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="email">Adresse e-mail <span class="req" aria-hidden="true">*</span></label>
                <input id="email" name="email" type="email" autocomplete="email" required>
              </div>
              <div class="field">
                <label for="sujet">Sujet</label>
                <select id="sujet" name="sujet">
                  <option>Devenir guide bénévole</option>
                  <option>Pratiquer un sport (déficient·e visuel·le)</option>
                  <option>Proposer un partenariat</option>
                  <option>Faire un don</option>
                  <option>Autre</option>
                </select>
              </div>
              <div class="field">
                <label for="message">Votre message <span class="req" aria-hidden="true">*</span></label>
                <span class="hint" id="msg-hint">Décrivez votre demande en quelques lignes.</span>
                <textarea id="message" name="message" rows="6" aria-describedby="msg-hint" required></textarea>
              </div>
              <button class="btn btn-primary btn-lg" type="submit">Envoyer le message</button>
              <p class="hint">Les champs marqués d'un astérisque (*) sont obligatoires. À l'envoi, votre logiciel de messagerie s'ouvre pour transmettre votre message à l'association.</p>
            </form>
          </div>
        </div>
      </div>
    </section>
""".format(email=EMAIL),
)

# ------------------------------------------------------------------ CONFIDENTIALITE
PAGES["politique-de-confidentialite.html"] = dict(
    active=None,
    title="Politique de confidentialité — A2CMieux",
    description="Politique de confidentialité et de protection des données personnelles du site A2CMieux.",
    body=page_head("Politique de confidentialité", "Politique de confidentialité",
        "A2CMieux s'engage à protéger la vie privée et les données personnelles des visiteurs de son site et de ses membres.") +
"""    <section class="section">
      <div class="container narrow reveal">
        <h2>Données collectées</h2>
        <p>Le site A2CMieux ne collecte des données personnelles que lorsque vous nous les transmettez volontairement, par exemple via le formulaire de contact ou par e-mail (nom, adresse e-mail, contenu de votre message). Ces informations servent uniquement à répondre à votre demande et à la vie associative.</p>
        <h2>Utilisation des données</h2>
        <p>Vos données ne sont ni vendues, ni louées, ni cédées à des tiers. Elles sont conservées le temps nécessaire au traitement de votre demande et à la gestion de votre éventuelle adhésion.</p>
        <h2>Vidéo et contenus externes</h2>
        <p>Certaines pages intègrent des contenus tiers (vidéo YouTube en mode « sans cookie », plateforme HelloAsso pour les adhésions et les dons). Ces services disposent de leurs propres politiques de confidentialité, que nous vous invitons à consulter.</p>
        <h2>Vos droits</h2>
        <p>Conformément au Règlement Général sur la Protection des Données (RGPD), vous disposez d'un droit d'accès, de rectification et de suppression de vos données. Pour exercer ces droits, écrivez-nous à <a href="mailto:{email}">{email}</a>.</p>
        <h2>Cookies</h2>
        <p>Ce site n'utilise pas de cookies de suivi publicitaire. Vos préférences d'accessibilité (contraste, taille du texte) sont enregistrées localement dans votre navigateur et ne sont jamais transmises.</p>
      </div>
    </section>
""".format(email=EMAIL),
)


def build():
    for filename, data in PAGES.items():
        html = page(data["active"], data["title"], data["description"], data["body"])
        with open(os.path.join(OUT, filename), "w", encoding="utf-8") as fh:
            fh.write(html)
        print("écrit :", filename)


if __name__ == "__main__":
    build()
