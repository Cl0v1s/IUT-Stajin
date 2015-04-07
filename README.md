# Stajin
## Manuel D'utilisation



### Préface
    
Stajin est une application de gestion de Stage développée pour le compte de l'Institut Universitaire de Technologie de Bordeaux.  
Il se découpe en deux modules distincts (DataUtils et Client) qui seront eux-même traité ici séparemment.  

Stajin a été développé dans un but universitaire et reste l'entière propriété de ses concepteurs susnommés:  

* Eliott Vincent (Chef de projet)
* Loup Salles (Assistant chef de projet)
* Jérome Pham (Chargé de conception du modèle de données)
* Clovis Portron (Développement du logiciel statistique)

<hr>

### Index

#### 1. Installation
    * 1.a Installer Python
    * 1.b Installer Bottle
    * 1.c Installer pymssql

#### 2. DataUtils et traitement de fichiers csv
    * 2.a Objectifs
    * 2.b Fournir les données
    * 2.c Traitement des erreurs
    * 2.d Importation des données dans la base
    * 2.e Aide 

#### 3. Client et affichage des données statistiques 
    * 3.a Objectifs
    * 3.b Lancement du service Client
    * 3.c Consultation de la page de données statistiques


<hr>


### 1.Installation

Stajin requiert un ensemble de prérequis sans lesquels il ne pourra se comporter de manière normale et remplir sa tâche.  
En voici la liste:

* Le langage Python dans sa version 3.4
* Le framework python [Bottle](http://bottlepy.org/docs/dev/index.html)
* L'interface de connexion à SQL Server [pymssql](http://www.pymssql.org/en/stable/)

Vous trouverez ci-dessous les instructions d'installation de ces élements.



#### 1.a Installer Python 

**Installer Python sous Windows**  
Afin de pouvoir disposer de Python dans votre environnement Windows, vous pouvez le récupérer [ici](https://www.python.org/downloads/release/python-343/).  
Il vous suffira ensuite d'exécuter l'installateur et de vous laisser guider par celui-ci.

**Installer Python sous Debian-based**

Dans l'optique d'installer Python sur votre système Debian (ou basé sur Debian), il vous suffira d'exécuter la commande suivante:  

    sudo apt-get install python

Et vous devriez profiter de la dernière version (3.5) de l'interpréteur du fameux langage de programmation.  
Vous pouvez vérifier que l'installation s'est bien déroulée en lançant un interpréteur de commande et en tapant la commande suivante:  

    python

Votre système devrait ainsi vous présenter un écran semblable à celui ci:
![python sample](http://i.imgur.com/DtIXT2K.png)



####1.b Installer Bottle

Bottle est un framework Python destiné à mettre facilement en route un serveur de page dynamique sous Python.  
Il est requis par Stajin afin de fournir la page de données statistiques.  

Vous pouvez facilement l'installer à l'aide de la commande pip fournie avec python et disponible aussi bien sous Windows que sous Debian-based.  

Bottle s'installe rapidement et facilement avec son aide de la manière suivante:

    pip install bottle 

Bottle s'installera de lui-même sans aucun problème particulier.



####1.c Installer pymssql

Pymssql permet à python de joindre une base de données SQL Server de Microsoft.  
Ce module est donc essentiel au bon fonctionnement de Stajin. Vous pouvez vous le procurer aisément grâce à la commande pip précedemment introduite.  

    pip install pymssql


<hr>

### 2. DataUtils et traitement de fichiers csv

#### 2.a Objectifs

Le module nommé DataUtils est chargé de lire les fichiers CSV fournis par le client, de détecter les erreurs et incohérences qui y sont présentes puis, le cas échéant de fournir un script SQL (compatible SQL Server) permettant au client de transférer ses données dans une base.



#### 2.b Fournir les données

Afin d'être en mesure d'user de la fonctionnalité d'analyse de DataUtils, vous devez placer les fichiers à traiter dans le répertoire de Stajin et les nommer de la manière suivante:   

|Données contenues dans le fichier | Nom du fichier requis |
|----------------------------------|-----------------------|
|Liste des enseignants | fichier_enseignants.csv |
|Liste des entreprises | fichier_entreprises.csv |
|Liste des étudiants | fichier_etudiants.csv |
|Liste des stages | fichier_stages.csv |

**Vous devez impérativement respecter cette nomenclature.**

![fichiers](http://i.imgur.com/PV8J1b7.png)

Une fois le placement des fichiers effectué et correct, vous serez en mesure de lancer le traitement des erreurs.



#### 2.c Traitement des erreurs

Afin de lancer l'exécution du module vous devez vous placer dans le répertoire DataUtils situé dans le dossier de Stajin à l'aide de l'interprète de commande et lancer la commande suivante:  

    python datautils.py

(Notez que vous pouvez passer cette phase d'analyse à l'aide de l'option --force)

Vous lancerez ainsi le traitement des données et la détection des erreurs.  

Lorsque DataUtils rencontre des erreurs dans les fichiers csv, il génère un fichier erreurs.log (dans le répertoire DataUtils de Stajin) dans lequel vous pourrez retrouver l'ensemble des erreurs rencontrées associées à leur code et à la ligne à laquelle elle furent détectée.

Vous trouverez ci-dessous le descriptif des erreurs possibles associées à leur code.

* (P1) Chaque enseignant du fichier enseignants doit disposer d'un nom, prénom et surnom.

* (P2) Chaque entreprise du fichier entreprises doit disposer d'un nom d'entreprise, du nom,
prénom et adresse email du responsable. L'adresse de l'entreprise et son secteur sont
optionnels.

* (P3) Chaque étudiant du fichier étudiants doit disposer d'un nom, prénom, et adresse
email.

* (P4) Chaque stage du fichier stages doit disposer d'un nom d'entreprise, du nom, prénom
et adresse email du responsable de stage, du nom et prénom de l'étudiant, d'une année
universitaire, et du surnom de l'enseignant encadrant le stage. Le titre du stage ainsi que
les dates de début et fin sont optionnels.

* (P5) Chaque entreprise mentionnée dans le fichier stages doit être présente dans le fichier
entreprises.

* (P6) Chaque étudiant (nom, prénom) mentionné dans le fichier stages doit être présent
dans le fichier étudiants.

* (P7) Chaque enseignant (surnom) mentionné dans le fichier stages doit être présent dans le
fichier enseignants.

* (P8) Chaque fichier CSV est bien formé, c'est-à-dire que chaque ligne dispose du bon
nombre de colonnes (via le séparateur point-virgule).

* (P9) Dans le fichier enseignants, il ne doit pas y avoir deux enseignants avec le même
surnom.

* (P10) Dans le fichier entreprises, il ne doit pas y avoir deux entreprises avec le même nom.

* (P11) Dans le fichier étudiants, il ne doit pas y avoir deux étudiants avec les mêmes noms et
prénoms (sinon on ne peut pas les identifier dans le fichier stages).



#### 2.d Importation des données dans la base

Lorsque aucune erreur n'a été détectée par DataUtils (ou que l'option --force a été utilisée), celui-ci produire un script sql vous permettant d'importer les données présentes dans les fichiers CSV dans votre base de données. 

Ce fichier intitulé "data.sql" sera placé dans le répertoire DataUtils de Stajin. 

En l'important dans SQL server vous serez donc en mesure de retrouver toutes les données corrigées et triées dans votre base de données.

**A noter que la base de données de Stajin devra être nommée PT2_PPSV afin d'être compatible avec le module Client.**



#### 2.e Aide 

Vous trouverez ci-dessous le récapitulatif des options utilisable avec DataUtils.

|Syntaxe de l'option | Effet |
|---------------------|------|
| -h, --help | Affiche l'aide |
| -f, --force | Force la génération du script SQL, que des erreurs soient présentent dans les fichiers CSV ou non. |



<hr>

### 3. Client et affichage des données statistiques 

#### 3.a Objectifs

Stajin fournit également un outil de visionnage des statistiques sobrement intitulé Client.  
Cet outil statistique prend dans les faits la forme d'une page Web consultable en local depuis le navigateur.


#### 3.b Lancement du service Client

Le système client de consultation des données peut facilement être instancié en lançant un interprète de commande,en vous plaçant dans le répertoire Client situé dans les fichiers de Stajin puis en exécutant la commande suivante:

    python client.py

Ceci aura pour effet de lancer un serveur Web en local permettant à l'utilisateur de visionner ultérieurement ces données statistiques.


#### 3.c Consultation de la page de données statistique

Une fois le serveur local lancé (voir section 3.b) la page de statistiques peut être consultée en tapant dans la barre URL de votre navigateur l'adresse suivante:

    http://localhost/






