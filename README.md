Simple example of using flask for creating a RESTful API\
Based on linked-in learning tutorial "Building Web APIs with Flask", chapter 1.1\
\
To use it:\
Start virtual python environment and install flask using pip, then try it out\
> virtualenv venv\
> source venv/bin/activate\
> pip install flask\
> python app.py\
...
> deactivate \
\
To run in Docker:\
> docker build -t simpleflask . \
> docker run -p 5000:5000 simpleflask
\
To try it out, use this endpoint for an example:
http://localhost:5000/api/funny
