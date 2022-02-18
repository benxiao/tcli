# tcli
* turn any of your python module into a cli tool
* save your chores to turn your functions into cli tool with library like click in most cases.

## Usecases
### execute a function in a module
```
python tcli.py funcs.py add 23 90
```
### show all function names in a module
```
python tcli.py funcs.py show
```
### show args of a function in a module
```
python tcli.py funcs.py args 
```
### execute a function with optional args
```
python tcli.py funcs.py n_hello --x 10

```