Geek Brains
===========

Development
----------

```shell
docker build -t ai-learn .
docker run -it -p 8888:8888 -v $(pwd):/code ai-learn start-notebook.sh --NotebookApp.password='' --NotebookApp.token=''
```
