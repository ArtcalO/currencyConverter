find -name *.pyc -exec rm {} +
echo "Removed"

find -name 000?_*.py -exec rm {} +

echo "Removed"
find -name *.sqlite3 -exec rm {} +