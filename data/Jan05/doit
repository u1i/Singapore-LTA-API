echo time,green,yellow,red
for d in *dat
do
	green=$(cat $d | tr "," "\n" | grep "'green'" | wc -l)
	yellow=$(cat $d | tr "," "\n" | grep "'orange'" | wc -l)
	red=$(cat $d | tr "," "\n" | grep "'red'" | wc -l)
	
	echo ${d:0:2}:${d:2:2},$green,$yellow,$red
done
