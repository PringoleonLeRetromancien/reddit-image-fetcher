# reddit-image-fetcher

# EN-Instruction

This is a small script to that downloads images from a list of subreddits. To make it work on your machine, you have to follow these steps : 

- go to https://www.reddit.com/prefs/apps/ to create an app, this will give you a client_id and a client_secret

- after you downloaded the script, go in the gitmain.py file and put the client id and secret in the correct place (line 4 and 5) and create a user agent <like this>

- on line 10, specify the path of "url.txt" in the "images" folder 
  
- on line 11, modify the "limit" variable to specify how many posts do you want to fetch. Keep in my mind that not all post contain images, hence there will be less images than the limit
  
- finally, on line 16, add the path of the "images" folder to the functions argument. 

- you can now run the script ! 

When running, if you followed the steps correctly, it will put all the images into the images folder. 
  
  
# FR-Instruction
  
C'est un petit programme capable de télécharger des images depuis plusieurs sous-reddits. Pour le faire fonctionner, veuillez suivre ces étapes : 

- va sur https://www.reddit.com/prefs/apps/ pour créer une app reddit pour récupérer le client id et le client secret de ton application nouvellement créer

- télécharge le script en conservant la hiérarchie des fichiers, renseigne le client id et secret aux lignes 4 et 5, et créé un user agent <comme ça>

- à la ligne 10, resenseigne l'emplacement de "url.txt" dans le dossier "images"

- à la ligne 11, modifie la variable "limi" pour ajuster le nombre de posts que le programme va tester. Tu n'obtiendras pas autant d'images, pour la bonne et simple raison que touts les posts de contiennent pas des images

- à la ligne 16, renseignes l'emplacement du fichier "images" au bon endroit (là où c'est écrit "voir README")

- et normallement ça marches ! 
  
Les images devraient alors commencer à apparaitre dans le fichier "images". 
