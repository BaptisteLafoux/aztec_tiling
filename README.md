# Domino tiling generator for aztec diamonds
This code generates random tiling of dominoes (2x1 or 1x2 rectangle) for aztec diamond grids. It is based on random "shuffling" algorithm described in [Elkies *et al.* (1992) [1]](#1).

For a useful introduction to domino tilings, see [this excellent video](https://youtu.be/Yy7Q8IWNfHM) from the Mathologer YouTube channel. 

## Getting started 
### Prerequisit 
The code runs on Python 3. It relies on the package [shapely](https://pypi.org/project/Shapely/) for the manipulation of geometric objects. 
```
pip install shapely
```
### Run example 
Clone the git repository and run [example.py](example.py) like this 
```
git clone https://github.com/BaptisteLafoux/aztec_tiling.git
cd aztec_tiling
python example.py
```
This will create a .png file in the current directory, representing the generated tiling. 
The image below is an example of what you could get (tiling of an aztec diamond of order 22) 
![Domino tiling for aztec diamond of order 20](https://github.com/BaptisteLafoux/aztec_tiling/blob/main/aztec_diamond_domino_tiling_order22.png?raw=true)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## References
<a id="1">[1]</a> 
Elkies, N., Kuperberg, G., Larsen, M., & Propp, J. (1992). 
[Alternating-sign matrices and domino tilings (Part I)](https://link.springer.com/article/10.1023/A:1022420103267). 
*Journal of Algebraic Combinatorics*, 1(2), 111-132.
