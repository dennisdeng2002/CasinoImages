This project hosts images for the casinos found on [BravoPokerLive](https://www.bravopokerlive.com/venues)

1. `extract_casinos.py`: extract the id / name / city from `casinos.json` into `casinos.txt`

2. `normalize.py`: normalize all `.jpeg` / `.jpg` files to `.jpg`

3. `resize.py`: resize images using the [convert](https://legacy.imagemagick.org/script/convert.php) command

4. `validate.py`: 

5. `sql.py`: generate sql to insert the ids of all supported images into a database