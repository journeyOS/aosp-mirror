ASOP="aosp"
REPO="repo.sh"
for ((i=1; i<=4; i++)); do
	curl https://github.com/aosp-mirror?page=$i > $ASOP.$i.html;
done

cat /dev/null > $REPO
for page in `ls $ASOP.*`; do
	python3 fetch_aosp.py < $page >> $REPO;
	rm -rf $page
done
chmod 777 $REPO