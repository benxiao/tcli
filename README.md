# Unclick
* turn any of your python module into a cli tool
* save your chores to turn your functions into cli tool with library like click in most cases.

## Usecases
```
cd unclick
```
### execute a function in a module
```
unclick examples.funcs.py add 23 90
```
### show all function names in a module
```
unclick examples.funcs.py show
```
### show args of a function in a module
```
unclick examples.funcs.py args <add | n_hello>
```
### execute a function with optional args
```
unclick examples.funcs.py n_hello --x 10

```
