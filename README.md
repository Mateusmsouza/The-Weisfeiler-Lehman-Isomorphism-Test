# The Weisfeiler Lehman Isomorphism Test

# How does that work?

The core idea of the Weisfeiler-Lehman isomorphism test is to find for each node in each graph a signature based on the neighborhood around the node. These signatures can then be used to find the correspondance between nodes in the two graphs, which can be used to check for isomorphism. [1]

# How can I run it?

I strongly recommend you to run this project using [Pipenv](https://pipenv.pypa.io/en/latest/) + [pyenv](https://github.com/pyenv/pyenv), as you can activate pipenv shell and easily get dependencies by running:

```bash
$ pipenv shell
$(pipenv active) pipenv install
$(pipenv active) python3 main.py
..
...
```

# Important Files

[main.py](http://main.py) >> main file to run algo

service_graph.py >> wrapper to graph library

wl_algo >> file that contains wl algo

[data.graphs.py](http://data.graphs.py) >> file that holds default example graphs

# Dependencies

- jgraph
- *igraph*
- python-igraph
- *cairocffi*
- scikit-learn

References:

[1] The Weisfeiler-Lehman Isomorphism Test, David Bieber available [here](https://davidbieber.com/post/2019-05-10-weisfeiler-lehman-isomorphism-test/).