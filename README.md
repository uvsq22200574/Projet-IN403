
# Projet Python: Tables de routage

  - Il s'agit ici de produire un petit texte de 10 - 15 lignes decrivant et expliquant les principaux termes techniques utilisés dans ce projet (transit IP, backbone, niveau des opérateurs (Tier), peering, ...). Vous êtes vivement encouragés a utiliser pour ce faire un agent conversationnel (ChatGPT ou un autre chatbot). Si le texte produit pouvait être un peu humoristique, ce serait un plus.
  - Il convient ici de creer la topologie d'interconnexion d'un réseau de 100 nœud de la forme indiquée sur le schéma figurant sur la page suivante. Les liens et les temps de communication sur chacun de ces liens vont être crées de manière aléatoire selon les règles suivantes :
    - le backbone ou coeur du reseau (Tier1 sur le schéma) composé de 10 nœud très connectés entre eux par des lignes de communication a très haut débit. On va considérer que pour chaque lien possible entre ces nœud (non orienté), il y a 75% de chance qu'il existe. Par ailleurs, si le lien existe, il sera valué par une valeur tirée aléatoirement entre 5 et 10 (représentant le temps unitaire moyen de communication sur cette ligne).
    ![Figure1](embed/Figure%201.jpg)
    - Les opérateurs de niveau 2 (Tier 2) souvent appelés opérateurs de transit. 20 nœud qui seront chacun connectés à 1 ou 2 nœud du backbone tiré(s) aléatoirement et à 2 ou 3 nœud de niveau 2 (tirés également aléatoirement). Chacun de ces liens sera valué par une valeur comprise entre 10 et 20.
    - Les operateurs de niveau 3 (Tier3). 70 nœuds reliés chacun à 2 nœud de niveau 2. Les liens seront valués par une valeur comprise entre 20 et 50. 
  - Il faudra également dans cette partie déterminer la structure de données qui vous parait la plus adéquate pour représenter et mémoriser le graphe correspondant à ce réseau.
  - Même s'il est très probable que le réseau créé soit connexe, le tirage aléatoire des liens peut faire qu'exceptionnellement il ne le soit pas. Le but de cette partie est de developper une procédure pour vérifier que tous les sommets peuvent bien être atteints à partir d'un sommet de départ quelconque. Si ce n'est pas le cas, il convient de relancer la création d'un nouveau réseau.
  - La table de routage d'un nœud doit indiquer pour chaque destination possible (les 99 autres nœud) à quel voisin il convient de router un message (un paquet) compte tenu de la destination finale. C'est donc le prochain nœud sur un plus court chemin vers cette destination car le message doit suivre le cheminement le plus court en temps de communication (les temps de routage en chaque noeud intermediaire sont considérés comme negligeables). Il convient donc dans cette partie de developper l’algorithme qui calcule ces 100 tables de routage.
  - Il faut dans cette partie permettre a l'utilisateur de saisir 2 nœud : un nœud émetteur de message et un nœud destinataire et a l'aide des tables de routage (il ne faut pas refaire ici le calcul de plus court chemin mais juste utiliser les tables de routage établies dans la partie précédente) reconstituer le chemin que va suivre ce message. Ce chemin devra être indiqué (affiché) à l'utilisateur.

  - Texte ![](https://img.shields.io/badge/Status-todo-red)
  - Nœuds Backbone ![](https://img.shields.io/badge/Status-completed-green)
  - Nœuds Transit ![](https://img.shields.io/badge/Status-half_completed-yellow)
  - Nœuds Regulier ![](https://img.shields.io/badge/Status-todo-red)
  - Connexité ![](https://img.shields.io/badge/Status-todo-red)
  - Table de Routage ![](https://img.shields.io/badge/Status-todo-red)
  - Chemin ![](https://img.shields.io/badge/Status-todo-red)
  - Interface ![](https://img.shields.io/badge/Status-Optional-purple)

# Contacts
  - Chargé de TD: N/A
  - Chargé du Github: hugoassis.crh@protonmail.com
  - Collaborateurs : N/A
