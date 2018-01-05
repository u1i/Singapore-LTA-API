
hour=$(export TZ="Asia/Singapore";date +%H)

echo $hour

case $hour in
    06|07|08|09|10|11|12|13|14|15|16|17|18|19) echo yes;;
    *)             echo no;;
esac
