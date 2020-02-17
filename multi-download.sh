#!/usr/bin/bash/

start_date="2010-01-01" # set the initial date.
end_date=`date -d $start_date' 2 months' '+%Y-%m-%d'`
end_date=`date -d $end_date' 1 days ago' '+%Y-%m-%d'`

echo $start_date
echo $end_date
echo '############'

sed -i -e '34,34d' downloader.py
sed -i -e '34,34d' downloader.py

sed -i '34i \min_upload_date = '\'$start_date\'',' downloader.py
sed -i '35i \max_upload_date = '\'$end_date\'',' downloader.py

python3 downloader.py $start_date'_'$end_date


############################################################################

for year in `seq 119` # Set the months you want to search. (number should be 'months - 1')
do

start_date=`date -d $end_date' 1 days' '+%Y-%m-%d'`
end_date=`date -d $start_date' 2 months' '+%Y-%m-%d'`
end_date=`date -d $end_date' 1 days ago' '+%Y-%m-%d'`

echo $start_date
echo $end_date
echo '############'

sed -i -e '34,34d' downloader.py
sed -i -e '34,34d' downloader.py

sed -i '34i \min_upload_date = '\'$start_date\'',' downloader.py
sed -i '35i \max_upload_date = '\'$end_date\'',' downloader.py

python3 downloader.py $start_date'_'$end_date

done
