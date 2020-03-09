= Image Renamer Tool =

Cet outil a pour but de lister un ensemble d'image dans un dossier et de les renommer selon leur date de prise de vue.

== Utilisation ==

```bash
$ python renamer.py INPUT_FOLER OUTPUT_FOLDER
```

== Resultat attendu ==

Suite à un appel `python renamer.py input output`, 
l'image `input/image1.jpg` est renommée en `output/2020-01-23_10-11-59.jpg`
si image1.jpg est présente dans le dossier input est a été capturée le 23 janvier 2020 à 10:11:59.

== Bonus ==

- Ajouter l'option '--prefix' qui permet d'ajouter un prefixe au nom de fichier de sortie.
- Ajouter une option '--frame_index' permettant de renommer les fichiers avec un index selon l'ordre de capture des images.
