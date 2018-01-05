ts=$(export TZ="Asia/Singapore";date +%Y-%m-%d/%H%M)
out="maps/$ts.html"
dir=$(dirname $out)
mkdir -p $dir 2>/dev/null
echo $out in $dir
