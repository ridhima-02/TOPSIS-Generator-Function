## TOPSIS




Made both Python library and a web service for dealing with Multiple Criteria Decision Making(MCDM) problems by using Technique for Order of Preference by Similarity to Ideal Solution(TOPSIS).


## Installation

Use the package manager pip to install topsis

```sh
pip install Topsis-Ridhima-102017100==1.0.0.4
```

## Usage
Enter csv filename followed by .csv extentsion, then enter the weights vector with vector values separated by commas, followed by the impacts vector with comma separated signs (+,-), followed by result filename
```sh
topsis sample.csv "1,1,1,1" "+,-,+,+" result.csv
```
Impact and weight should not contain spaces in between them.

## Example
##### sample.csv
A csv file showing data for different mobile handsets having varying features.

| Model |	Storage space(in gb)|	Camera(in MP)|	Price(in $)|Looks(out of 5)
| ------|-----------------------|----------------|-------------|---------
| M1    |16|	12|	250|	5
| M2    |16|	8|	200|	3
| M3    |32|	16|	300|	4
| M4    |32|	8|	275|	4
| M5    |16|	16|	225|	2

weights vector = [ 0.25 , 0.25 , 0.25 , 0.25 ]
impacts vector = [ + , + , - , + ]

### Input:
```sh
topsis sample.csv "1,1,1,1" "+,+,-,+" result.csv
```

### Output:
Topsis Result:

| | Model |	Storage space(in gb)|	Camera(in MP)|	Price(in $)|Looks(out of 5)|Performance Score|Rank|
|--| ------|-----------------------|----------------|-------------|---------|-------|----|
|1| M1    |16|	12|	250|	5|0.534277|3|
|2| M2    |16|	8|	200|	3|0.308368|5|
|3| M3    |32|	16|	300|	4|0.691632|1|
|4| M4    |32|	8|	275|	4|0.534737|2|
|5| M5    |16|	16|	225|	2|0.401046|4|


## Other notes
- The first column and first row are removed by the library before processing, in attempt to remove indices and headers. So make sure the csv follows the format as shown in sample.csv.
- Make sure the csv does not contain categorical values




## License

MIT


