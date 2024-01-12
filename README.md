This project hosts images for the casinos found on [BravoPokerLive](https://www.bravopokerlive.com/venues)

1. `extract_casinos.py`: used to extract the id / name / city from `casinos.json` into `casinos.txt`

2. `normalize.py`: used to normalize all `.jpeg` / `.jpg` files to use `.jpg`

3. `resize.py`: used to resize images using the [convert](https://legacy.imagemagick.org/script/convert.php) command

4. `sql.py`: used to generate sql to insert the ids of all supported images into a database