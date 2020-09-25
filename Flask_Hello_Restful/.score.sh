tn=2
tp=`python3 -m unittest test_app.py > testout.txt 2>&1; head -1 testout.txt | awk -F"." '{print NF-1}'`
rm testout.txt

FS_SCORE=`awk -v tests_passed="$tp" -v tests_total="$tn" 'BEGIN {print tests_passed / tests_total * 100}'`
echo "FS_SCORE:$FS_SCORE%"
#echo "FS_SCORE:10%" 
