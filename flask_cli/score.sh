tn=12
tp=`python3 -m unittest discover myflaskproj > testout.txt 2>&1; head -1 testout.txt | awk -F"." '{print NF-1}'`
rm testout.txt

FS_SCORE=`awk -v tests_passed="$tp" -v tests_total="$tn" 'BEGIN {print tests_passed / tests_total * 100}'`
echo "This custom script can run any bash command, and perform tests."
echo "It needs to only output on1 line in the format 'FS_SCORE:xx%', where xx is the percentage score for the solution."
echo "FS_SCORE:$FS_SCORE%"
