cd out
rm index.html
for d in sg*html
do
	echo "<a href='$d' target='_new'>$d</a><br>" >> index.html
done
