start=$PWD

# cd $start/out
# rm index.html
# for d in sg*html
# do
# 	echo "<a href='$d' target='_new'>$d</a><br>" >> index.html
# done

cd $start/maps
index=$start/maps/index.html
rm $index
for d in $(ls)
do
	echo $d
	echo "<a href='$d'>$d</a> | " >> $index
	cd $start/maps/$d

	rm index.html 2>/dev/null

	for f in *html
	do
		echo "<a href='$f' target='_new'>${f/.html/}</a> | " >> index.html
	done
done

