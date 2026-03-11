# Desafio 2 — Task to Command

This program receives a task description and returns the appropriate Linux command.

## Supported Tasks

| Task Example | Command |
|-------------|---------|
| listar arquivos | ls |
| criar nova pasta | mkdir |
| remover arquivo | rm |
| mostrar conteudo | cat |

If the task is not recognized, the program returns:

```
comando desconhecido
```

## Example

Input
```
remover arquivo antigo
```

Output
```
rm
```
