# Getting started

You must have python-virtualenv installed (and obviously be connected to my DB ;))

Run
<pre> 
./setup.sh
</pre>

While developing
<pre>
env/bin/pserve development.ini --reload
</pre>

To install a new python module, first edit setup.py and then
<pre>
env/bin/python setup.py develop
</pre>
