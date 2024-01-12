This project hosts casino images for the various casinos found on https://www.bravopokerlive.com. The list of casinos was fetched using their API and is stored in `casinos.json`

1. `python3 extract_casinos.py`
    Used to extra the id / name / city of each casino into `casinos.txt`

2. `python3 normalize.py`
    Used to normalize all .jpeg / .jpg files to use .jpg

3. `python3 resize.py`
    Used to resize images using the [convert](https://legacy.imagemagick.org/script/convert.php) command from ImageMagick

4. `python3 sql.py`
    Used to generate sql to insert the ids of all supported images into a database