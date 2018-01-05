start=$PWD

cd $start/out
rm index.html
for d in sg*html
do
	echo "<a href='$d' target='_new'>$d</a><br>" >> index.html
done

cd $start/maps

rm index.html
for d in $(ls)
do
	echo "<a href='$d'>$d</a><br>" >> index.html
done

