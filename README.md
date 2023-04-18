# Unclick
* turn any of your python module into a cli tool
* save your chores to turn your functions into cli tool with library like click in most cases.

## Usecases
### execute a function in a module
```
unclick funcs.py add 23 90
```
### show all function names in a module
```
unclick funcs.py show
```
### show args of a function in a module
```
unclick funcs.py args <add | n_hello>
```
### execute a function with optional args
```
unclick funcs.py n_hello --x 10

```
