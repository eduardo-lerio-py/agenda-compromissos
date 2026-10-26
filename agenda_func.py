from datetime import datetime
import json

formatacao = '%d/%m/%Y %H:%M'
ARQUIVO = "compromissos.json"


def pegarcomp(mensagem):
    while True:
        comp = str(input(mensagem)).strip()
        if comp == '':
            print('Adicione um compromisso')
            continue
        else:
            return comp


def ler_inteiro(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            return int(entrada)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def pegardata(mensagem, formato=formatacao):
    while True:
        data = input(mensagem).strip()
        try:
            return datetime.strptime(data, formato)
        except ValueError:
            print('Escreva uma data válida')
            continue


def gerarid(idantigo):
    iid = 1
    while iid in idantigo:
        iid += 1
    return iid


def salvar(compromissos):
    para_salvar = []
    for c in compromissos:
        copia = c.copy()
        copia["Data"] = c["Data"].strftime(formatacao)
        para_salvar.append(copia)

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(para_salvar, f, ensure_ascii=False, indent=2)


def carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    for c in dados:
        c["Data"] = datetime.strptime(c["Data"], formatacao)

    return dados


def addcomp(compromissos, idantigo):
    texto = pegarcomp('Título do compromisso: ')
    data = pegardata('Digite a data do compromisso '
                     '(dd/mm/aaaa hh:mm): ', formatacao)

    iid = gerarid(idantigo)
    idantigo.add(iid)

    compromisso = {'id': iid, 'Título': texto, 'Data': data}
    compromissos.append(compromisso)
    salvar(compromissos)
    print("compromisso criado com sucesso")


def formatar_comp(c):
    data_str = c["Data"].strftime(formatacao)
    return f'{c["id"]:>3} | {data_str} | {c["Título"]}'


def listar(compromissos, apenasf = False):
    if not compromissos:
        print('Sem compromissos!')
        return

    agora = datetime.now()

    if apenasf:
        filtrados = [c for c in compromissos if c['Data'] >= agora]
    else:
        filtrados = list(compromissos)

    if not filtrados:
        print('Sem compromissos!')
        return

    ordenados = sorted(filtrados, key=lambda c: c['Data'])

    print("ID  | Data/Hora         | Título")
    print("-------------------------------------------")
    for c in ordenados:
        print(formatar_comp(c))


def remover(compromissos, idantigo):
    if not compromissos:
        print('Sem compromissos!')
        return

    comp_id = ler_inteiro('Qual compromisso remover?: ')

    indice_para_remover = None
    for i, c in enumerate(compromissos):
        if c["id"] == comp_id:
            indice_para_remover = i
            break

    if indice_para_remover is None:
        print('id não encontrado!')
        return

    removido = compromissos.pop(indice_para_remover)
    salvar(compromissos)
    idantigo.discard(removido["id"])
    print(f"🗑️ Compromisso removido: {removido['Título']} (id={removido['id']})")

