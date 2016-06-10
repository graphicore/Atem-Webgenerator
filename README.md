# Atem-Webgenerator

A static site generator like [Jekyll](https://jekyllrb.com/) and [Hyde](http://hyde.github.io/) but targeted specifically at a git/Github based workflow to run FLOSS project sites. Made in Python based on [Flask](http://flask.pocoo.org/) and [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/).

 * Templates with [Jinja2](http://jinja.pocoo.org/docs/dev/).
 * Markdown content with [misaka](http://misaka.61924.nl/) and [Pygments](http://pygments.org) for  syntax highlighting.
 * Sensibly updating the deployment directory.
 * Transforms the directory structure when mapping source to target.
 * Atom feed included.
 * Expects source to be a git repository, to gather metadata.

This is just the first pass I had on this code. In a further iteration the code will become more object oriented to be prepared for subclassing. I think I'll make an Atem-Project specific version and one that is a more general useful base version. The latter may end up in another repository, but for the moment the code has no Atem-Project specific parts.

### Git

The generator currently tries to ask git for creation and updated dates, especially for the Atom-feed generator. In the future I want to have a much deeper integration of git data, e.g. to generate API documentation from source files and include (github/bitbucket) links and commit-hashes or to create initial outlines for changelog information with the commit messages from between two git tag releases.

The use case I envision is that this runs on travis to continiously update a [gh-pages](https://pages.github.com/) branch when pushing to `master`. I'll leave the how-to documentation here when ready.

## Documentation

There's no documentation yet, feel free to help out though ;-)

**TODO:** *Make a well commented sample project in here!*

But, there is a page in production, fetch the sources from https://github.com/graphicore/Atem-Project

Most important is the [webgenerator.yaml](https://github.com/graphicore/Atem-Project/blob/master/webgenerator.yaml) file in the root directory of the source, it configures all of the page. The generated page is in the [gh-pages branch](https://github.com/graphicore/Atem-Project/tree/gh-pages). By looking at all of this you should figure out a lot. Also, [read the source, Luke](https://blog.codinghorror.com/learn-to-read-the-source-luke/).

## Usage

```
# Create a pythonvirtual environment
# I used python 3.5, you'll need 3.something `pyenv` may be the right command
# on your system, for me it was pyvenv-3.5
Atem-Webgenerator$ pyvenv-3.5

# activate the virtual environment
Atem-Webgenerator$ . venv/bin/activate

# install the dependencies
(venv) Atem-Webgenerator$ pip install -r requirements.txt

# run the development server, the virtual environment must be activated
# visit http://localhost:5000
(venv) ~/somewhere$ ./path/to/Atem-Webgenerator/webgenerator.py path/to/website-source-dir
# OR, inside of the website-source-dir
(venv) path/to/website-source-dir$ ./path/to/Atem-Webgenerator/webgenerator.py

# generate a static version of the site and update a previously generated site
(venv) ~/somewhere$ ./path/to/Atem-Webgenerator/webgenerator.py path/to/website-source-dir path/to/target-dir
# OR, inside of the website-source-dir
(venv) path/to/website-source-dir$ ./path/to/Atem-Webgenerator/webgenerator.py . path/to/target-dir

# serve the generated dir for testing
# vistit http://localhost:8080
(venv) path/to/target-dir$ python -m http.server 8080
```

Enjoy!
