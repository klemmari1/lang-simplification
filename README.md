# lang-simplification

Lang simplification algorithm created with python. More information about the algorithm can be found [here](http://psimpl.sourceforge.net/lang.html).

## Usage with Docker

1. Run `docker image build --tag lang .`

2. Run the algorithm with `docker container run -it --rm lang <input> <tolerance> <look_ahead>`

## Usage without Docker

1. Create a virtual environment.

2. Run `pip install -r requirements.txt`

3. `python lang_simplification.py <input> <tolerance> <look_ahead>`

## Example input

Input data is an array of 2 or 3 dimensional points followed by the tolerance and look ahead parameters:

* `<input> <tolerance> <look_ahead>`

* `"[[0, 1], [1, 12], [2, 3], [4, 5], [6, 14], [7, 12], [8, 1]]" 2 3`
