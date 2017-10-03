### Pulse DSS (Data-Science Scoring Service)

#### Idea

To build a Data Science Scoring service that can deploy models, rules
and custom algorithms for the purposes of anomaly detection in the
guise of Jupyter Notebooks.

### Notebooks

**Running Jupyter Notebook Server**

Simply run the following command in the base of the repository:
```bash
$ ./launch_notebook_server
```
This should open a new window with the server running on
http://localhost:8888. From here you can navigate through the notebooks
package, edit and save changes to notebooks.

**Editing Notebooks**

Remember the following when editing notebooks
 -  All notebooks should follow the example given in
    ean-pulse-dss/notebooks/user/example.ipynb
 -  Notebook files are saved to .py files as well as .ipynb by default
 - In the application, notebooks are simply treated as Python modules

### The API

**Running the Service**

Ensure all prerequisites from requirements.txt are installed and then
execute
```bash
$ python main.py
```
From here you can call POST to http://localhost:5000/score. To see a
typical request shape then see example.json. All data should be given
in a JSON format that can be interpreted by Pandas read_json() function
with orient='split', see https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_json.html
for further details.

### Feedback

**Pros**

 -  Organise software by use-case i.e. a notebook is some form of anomaly
    detection for a user
 -  Very easy to move from prototyping to production
 -  Can easily get new users to contribute
 -  Detailed configuration files dropped in favour of actual code
 -  Testing all current use cases in production becomes simple - don't
    run all possible combinations from a config, just run all notebooks
    against golden data
 -  Removes need for super high-level abstraction removing unwanted
    dependencies
 -  Can setup in a short space of time

**Cons**

 -  Have to write a lot of boiler plate code
 -  Not completely smooth switching from running code within the Notebook
    to being called by the application itself e.g.
     -  Have to restart kernel to pick up local changes to dss codebase
     -  Importing modules from relative locations can be fiddly
 -  Unclear how to organise the Notebooks package
 -  Have to write more code which may make maintaining code at scale
    challenging
 -  Fiddly to understand how to configure Jupyter