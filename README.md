# PyDerogator 


Automatiser en Python la **generation de l'attestation de déplacement dérogatoire** (France, confinement 2)

Avec delta de temps, impression automatique et une citation pour le plaisir.


```
python derogator.py --reason mission
derogation mission (+15m) : file:///tmp/derogation.txt
printed :)

 ____________________________________
/ An honest tale speeds best being   \
| plainly told.                      |
|                                    |
\ -- William Shakespeare, "Henry VI" /
 ------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```



```
python derogator.py --help


Usage: deragator.py [OPTIONS]

Options:
  --reason TEXT  Veuillez choisir entre : pro, achats, soins, famille, sport,
                 handicap, judiciaire, mission, enfant

  --help         Show this message and exit.

```






## Justifications

- Facile a personnaliser avec Python
- Terminal is beautiful (tout en local, une seule commande reutilisable dans l'historique)


## Ce qu'il fait

- Utilise en template Jinja **l'attestation officielle** au format txt du 30/10/2020 (https://www.interieur.gouv.fr/Actualites/L-actu-du-Ministere/Attestations-de-deplacement)
- **Remplit le document** avec les informations de nom et d'adresse
- Ajoute la date et l'heure avec un **delta de +x minutes** (pour compter le temps de sortir effectivement)
- **Coche la justification** en fonction de l'option
- Genere le fichier dans /tmp (Linux) et **fournit son lien** pour l'afficher et l'imprimer manuellement si besoin dans le browser
- Si possible, envoie le fichier a **l'imprimante** (Linux)
- Si possible, fournit une **citation** pour egayer votre sortie




## Configuration


### Virtualenv


Necessite Python3.6

Creer un virtualenv et installer le requirements :
```
python -m venv venv

pip install -r requirements.txt

source venv/bin/activate
```

Il faut au prealable configurer ces variables d'environnement (ex en les mettant dans .bashrc) contenant les informations necessaires a la derogation :

### Obligatoires

```
export DEROG_NAME=""  # M/Mme Prenom Nom
export DEROG_BIRTH_DATE=""  # Date de naissance
export DEROG_BIRTH_PLACE=""  # Lieu de naissance
export DEROG_ADDRESS=""  # Adresse complete
export DEROG_SIGN_PLACE=""  # Lieu de la signature
```

### Optionnelles

Ajouter un nombre de minutes, pour compter le temps de effectivement sortir de chez soi (par defaut 5minutes)

```
export DEROG_DELTA_MINUTES=10  # Minutes a ajouter au temps courant pour l'heure de signature
```

Definir l'imprimante pour imprimer le document avec lpr

```
export DEROG_PRINTER="Samsung-M2020-Series"  # Nom de l'imprimante installee
```

Pour avoir le nom de votre imprimante, vous pouvez utiliser
```
lpoptions
```


### Citation

Pour afficher une citation, il faut installer les generateurs
- https://doc.ubuntu-fr.org/fortune 
- https://debian-facile.org/doc:jeux:cowsay


## Usage

Executer le programme avec
```
python derogator.py --reason sport

```

## Limitations

Concu pour
- Une seule personne, pour plusieurs il faudrait un fichier de settings et pouvoir saisir la personne concernee en option
- Linux (voir les commentaires Linux pour le rendre compatible windows)


### Avertissement

- Je suis informaticien et non juriste
- Aucune garantie juridique, technique ou autre n'est associee a ce projet, partage comme un exemple personnel du Python que j'aime.
- Vous l'utilisez donc sous votre entiere responsabilite 
