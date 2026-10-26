# agenda-compromissos
Recebe compromissos e os guarda em um arquivo.

# Agenda de Compromissos

Programa de terminal em Python para gerenciar compromissos: adicionar, listar (todos ou só os futuros) e remover. Os dados ficam salvos em arquivo, então não se perdem ao fechar o programa.

## Requisitos

Python 3.6 ou superior. Não precisa instalar nenhuma biblioteca.

## Como rodar

```
python agenda_main.py
```

## Funcionalidades

- Adicionar compromisso com título e data/hora (`dd/mm/aaaa hh:mm`)
- Listar todos os compromissos, ordenados por data
- Listar apenas os compromissos futuros
- Remover compromisso pelo id
- Validação de datas inválidas e de títulos vazios
- Salvamento automático em `compromissos.json` e carregamento ao abrir

## Exemplo de uso

```
==============================
📅 Agenda de Compromissos (CLI)
==============================
1) Adicionar compromisso
2) Listar compromissos (todos)
3) Listar compromissos (apenas futuros)
4) Remover compromisso
0) Sair
Escolha uma opção: 2
Sem compromissos!

==============================
📅 Agenda de Compromissos (CLI)
==============================
1) Adicionar compromisso
2) Listar compromissos (todos)
3) Listar compromissos (apenas futuros)
4) Remover compromisso
0) Sair
Escolha uma opção: 1
Título do compromisso: Natal
Digite a data do compromisso (dd/mm/aaaa hh:mm): 25/12/2026 12:30
compromisso criado com sucesso

==============================
📅 Agenda de Compromissos (CLI)
==============================
1) Adicionar compromisso
2) Listar compromissos (todos)
3) Listar compromissos (apenas futuros)
4) Remover compromisso
0) Sair
Escolha uma opção: 2
ID  | Data/Hora         | Título
-------------------------------------------
  1 | 25/12/2026 12:30 | Natal

==============================
📅 Agenda de Compromissos (CLI)
==============================
1) Adicionar compromisso
2) Listar compromissos (todos)
3) Listar compromissos (apenas futuros)
4) Remover compromisso
0) Sair
Escolha uma opção: 0
Saindo do programa

```

## Como os dados são salvos

Os compromissos ficam no arquivo `compromissos.json`, criado automaticamente na primeira vez que você adiciona algo. As datas são guardadas como texto e convertidas de volta ao abrir o programa. 

## Estrutura do projeto

- `agenda_main.py`: menu e laço principal
- `agenda_func.py`: funções de adicionar, listar, remover, salvar e carregar
