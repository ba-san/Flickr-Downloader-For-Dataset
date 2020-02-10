#!/usr/bin/bash/

start_date="2010-01-01"
end_date=`date -d $start_date' 2 months' '+%Y-%m-%d'`
end_date=`date -d $end_date' 1 days ago' '+%Y-%m-%d'`

echo $start_date
echo $end_date
echo '############'

sed -i -e '36,36d' downloader.py
sed -i -e '36,36d' downloader.py

sed -i '36i \min_upload_date = '\'$start_date\'',' downloader.py
sed -i '37i \max_upload_date = '\'$end_date\'',' downloader.py

python3 downloader.py $start_date'_'$end_date


############################################################################

for year in `seq 239` # months - 1
do

start_date=`date -d $end_date' 1 days' '+%Y-%m-%d'`
end_date=`date -d $start_date' 2 months' '+%Y-%m-%d'`
end_date=`date -d $end_date' 1 days ago' '+%Y-%m-%d'`

echo $start_date
echo $end_date
echo '############'

sed -i -e '36,36d' downloader.py
sed -i -e '36,36d' downloader.py

sed -i '36i \min_upload_date = '\'$start_date\'',' downloader.py
sed -i '37i \max_upload_date = '\'$end_date\'',' downloader.py

python3 downloader.py $start_date'_'$end_date

done
