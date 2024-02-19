import os
import json
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

nome_arquivo = 'tasks.json'
caminho_completo = os.path.join(os.getcwd(), nome_arquivo)
memory_task_list = []
current_task_list = []

if os.path.exists(caminho_completo):
    with open(caminho_completo, 'r+', encoding='utf-8') as arquivo:
        tasks_dist = json.load(arquivo)
        memory_task_list = [task for task in tasks_dist['memory_task_list']]
        current_task_list = [task for task in tasks_dist['current_task_list']]
else:
    tasks_dist = {
        'memory_task_list': [],
        'current_task_list': []
    }
    with open(caminho_completo, 'w+', encoding='utf-8') as arquivo:
        json.dump(tasks_dist, arquivo, ensure_ascii=False, indent=2)


def clear_terminal():
    os.system('clear')


def undo_task():
    if len(current_task_list) == 0:
        clear_terminal()
        print('nada para desfazer!!!')
        print()
    else:
        deleted_task = current_task_list.pop()
        memory_task_list.append(deleted_task)
        list_tasks()


def undo_task_forever():
    if len(current_task_list) == 0:
        clear_terminal()
        print('nada para desfazer!!!')
        print()
    else:
        current_task_list.pop()
        list_tasks()


def redo_task():
    if len(memory_task_list) == 0:
        clear_terminal()
        print('nada para refazer!!!')
        print()
    else:
        deleted_task = memory_task_list.pop()
        current_task_list.append(deleted_task)
        list_tasks()


def list_tasks():
    if not current_task_list:
        clear_terminal()
        print('Nenhuma tarefa para ser listada!!!!')
        print()
    else:
        clear_terminal()
        print('lista de tarefas:')
        print()
        print(*current_task_list, sep='\n')
        print()


while True:
    print(
        'digite uma tarefa ou [desfazer], [desfazer para sempre], [refazer], [listar] ou [sair]')
    action = input()

    action_lower = action.lower()

    if action_lower == 'desfazer':
        undo_task()
    elif action_lower == 'desfazer para sempre':
        undo_task_forever()
    elif action_lower == 'refazer':
        redo_task()
    elif action_lower == 'listar':
        list_tasks()
    elif action_lower == 'sair':
        break
    else:
        current_task_list.append(action)

tasks_dist = {
    'memory_task_list': memory_task_list,
    'current_task_list': current_task_list
}
with open(caminho_completo, 'w+', encoding='utf-8') as arquivo:
    json.dump(tasks_dist, arquivo, ensure_ascii=False, indent=2)
