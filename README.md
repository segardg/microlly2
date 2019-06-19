## Comment faire fonctionner Microlly ?

1. `git clone`
2. `pipenv --python 3`
3. `pipenv install`
4. `flask initdb`
5.  `flask fakedata`
6.  `flask run`
7. Et go sur [127.0.0.1:5000](http://127.0.0.1:5000)

Une page sur le login va s'ouvrir.
Pour vous enregister, cliquez sur Register et renseignez tous les champs.
Ensuite vous pourrez voir les publications de tous les utilisateurs.
Pour voir les publictions d'un seul utilisateur, vous pouvez soit cliquer sur son nom sur la publication, soit aller dans Users pour voir les différents Users existants et leurs publications.

Les publications éditables et avec une corbeille (suppression) sont vos publications.
Pour revenir à la page d'accueil, cliquez sur le logo Microlly.
Pour vous déconnecter, veuillezcliquer sur le logo de déconnexion en haut à droite.

## Tests ?

Nous avons essayé d'effectué quelques tests, comme pour la création des utilisateurs et des publications pour voir si tout fonctionnait correctement.
Mais lors des tests, nous sommes restés bloqués sur l'erreur du status code.
Après quelques essais sans succès même en ayant commenté cette partie, les tests ne se faisaient pas correctement.

## Auteurs

> [Gaëtan SEGARD]
> [Donatien SEGARD]
