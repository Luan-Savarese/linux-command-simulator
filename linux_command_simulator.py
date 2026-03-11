# Linux Command Simulator

# Dictionary with Linux commands and descriptions
commands = {
    "ls": "lista arquivos e diretorios",
    "cd": "altera o diretorio atual",
    "pwd": "mostra o caminho do diretorio atual",
    "mkdir": "cria um novo diretorio",
}

# Read command from user
entrada = input().strip()

# Get command description
descricao = commands.get(entrada, "comando invalido")

print(descricao)
