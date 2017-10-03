### Pulse DSS (Data-Science Scoring Service)

**Idea**

To build a Data Science Scoring service that can deploy models, rules
and custom algorithms for the purposes of anomaly detection in the
guise of Jupyter Notebooks.


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