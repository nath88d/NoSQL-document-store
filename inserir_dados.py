import names
import random as rand
from pprint import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from key import connection_string


num_de_pessoas = int(input("Insira o numero de pessoas para inserir no banco: "))
depart = [453, 654, 236, 735]
formado = [True, False]
# Cria uma conexao cliente / servidor
client = MongoClient(connection_string, server_api=ServerApi('1'))
banco = client["projeto"]
try:
    tabela_aluno = banco["aluno"]
    client.admin.command('ping')
    
    print("Conectado ao MongoDB com sucesso!")
    print()
    resposta = tabela_aluno.find()
    for registro in list(resposta): 
        print(registro)
    
except Exception as e:
    print(e)

def inserir(collection, data):
    try:
        ((client["projeto"])[collection]).insert_one(data)
        print("Dado inserido!")
        pprint(data)
        # pass
    except Exception as e:
        print(e)

def atualizar(collection, filtro, data):
    ((client["projeto"])[collection]).find_one_and_update(
    { "id":filtro },  # Filtro
    { "$set": data }  # Dado a ser atualizado
    )
    print("Dado atualizado!")
    # pprint(data)


def delete_collection(collection):
    try:
        pprint(((client["projeto"])[collection]).delete_many({})); print(" Deletado")
    except Exception as e:
        print(e)
        
#   deleta dados
delete_collection("professor")
delete_collection("aluno")
delete_collection("grupo_tcc")
delete_collection("historico_professor")
delete_collection("disciplina")
delete_collection("matriz_curricular")
delete_collection("curso")
delete_collection("departamento")

# #departamento
inserir("departamento", { "id": 453, "nome_curso": "Computacao" , "id_chefe_departamento": 0});
inserir("departamento", { "id": 654, "nome_curso": "Engenharia" , "id_chefe_departamento": 0});
inserir("departamento", { "id": 236, "nome_curso": "Administracao" , "id_chefe_departamento": 0});
inserir("departamento", { "id": 735, "nome_curso": "Economia" , "id_chefe_departamento": 0});

# #cursos
inserir("curso", { "id": 0, "nome_curso": "Administração de Empresas" });
inserir("curso", { "id": 1, "nome_curso": "Gestão de Recursos Humanos" });
inserir("curso", { "id": 2, "nome_curso": "Engenharia Civil" });
inserir("curso", { "id": 3, "nome_curso": "Engenharia Elétrica" });
inserir("curso", { "id": 4, "nome_curso": "Ciência da Computação" });
inserir("curso", { "id": 5, "nome_curso": "Engenharia de Software" });
inserir("curso", { "id": 6, "nome_curso": "Economia" });
inserir("curso", { "id": 7, "nome_curso": "Finanças" });

# #disciplinas
inserir("disciplina", { "id": 0, "nome_disciplina": "Comp. Sci.", "id_departamento": 453, "semestre": 4 });
inserir("disciplina", { "id": 1, "nome_disciplina": "Finance", "id_departamento": 654, "semestre": 7 });
inserir("disciplina", { "id": 2, "nome_disciplina": "Eng. eletrica", "id_departamento": 236, "semestre": 3 });
inserir("disciplina", { "id": 3, "nome_disciplina": "Physics", "id_departamento": 735, "semestre": 4 });
inserir("disciplina", { "id": 4, "nome_disciplina": "Desenvolvimento Web", "id_departamento": 453, "semestre": 4 });
inserir("disciplina", { "id": 5, "nome_disciplina": "Mercado de Capitais", "id_departamento": 654, "semestre": 7 });
inserir("disciplina", { "id": 6, "nome_disciplina": "Eletromagnetismo", "id_departamento": 236, "semestre": 3 });
inserir("disciplina", { "id": 7, "nome_disciplina": "Astrofísica", "id_departamento": 735, "semestre": 4 });
inserir("disciplina", { "id": 8, "nome_disciplina": "Gestão de Recursos Humanos", "id_departamento": 453, "semestre": 0 });
inserir("disciplina", { "id": 9, "nome_disciplina": "Segurança da Informação", "id_departamento": 654, "semestre": 7 });
inserir("disciplina", { "id": 10, "nome_disciplina": "Gestão de Riscos", "id_departamento": 236, "semestre": 3 });
inserir("disciplina", { "id": 11, "nome_disciplina": "Energias Renováveis", "id_departamento": 735, "semestre": 4 });
inserir("disciplina", { "id": 12, "nome_disciplina": "Mecânica Quântica", "id_departamento": 453, "semestre": 4 });
inserir("disciplina", { "id": 13, "nome_disciplina": "Marketing Estratégico", "id_departamento": 654, "semestre": 7 });
inserir("disciplina", { "id": 14, "nome_disciplina": "Big Data Analytics", "id_departamento": 236, "semestre": 3 });
inserir("disciplina", { "id": 15, "nome_disciplina": "Derivativos Financeiros", "id_departamento": 735, "semestre": 7 });
inserir("disciplina", { "id": 16, "nome_disciplina": "Eletrônica de Potência", "id_departamento": 453, "semestre": 3 });
inserir("disciplina", { "id": 17, "nome_disciplina": "Física Nuclear", "id_departamento": 654, "semestre": 4 });
inserir("disciplina", { "id": 18, "nome_disciplina": "Empreendedorismo", "id_departamento": 236, "semestre": 0 });
inserir("disciplina", { "id": 19, "nome_disciplina": "Aprendizado de Máquina", "id_departamento": 735, "semestre": 4 });
inserir("disciplina", { "id": 20, "nome_disciplina": "Finanças Corporativas", "id_departamento": 453, "semestre": 7 });
inserir("disciplina", { "id": 21, "nome_disciplina": "Telecomunicações", "id_departamento": 654, "semestre": 5 });
inserir("disciplina", { "id": 22, "nome_disciplina": "Óptica Avançada", "id_departamento": 236, "semestre": 3 });
inserir("disciplina", { "id": 23, "nome_disciplina": "Gestão da Qualidade", "id_departamento": 735, "semestre": 0 });


num = 0
for i in range(num_de_pessoas):  # Insere professores
    inserir("professor", { 
        "id": num, 
        "nome": names.get_full_name(), 
        "departamento": str(depart[rand.randint(0, 3)]) 
    })
    num += 1

num = 0
for i in range(num_de_pessoas):  # Insere aluno
    inserir("aluno", { 
        "id": num, 
        "nome": names.get_full_name(), 
        "formado": formado[rand.randint(0, 1)]
    })
    num += 1

num = 0
for i in range(num_de_pessoas):  # Insere histórico do professor
    for h in range(1, 4):
        inserir("historico_professor", { 
            "id_professor": num, 
            "id_disciplina": rand.randint(0, 23), 
            "semestre": rand.randint(1, 8), 
            "ano": rand.randint(2000, 2024) 
        })
    num += 1

num = 0
for i in range(round(0.2 * num_de_pessoas)):  # Insere grupo TCC
    inserir("grupo_tcc", { 
        "id_grupo": num, 
        "id_aluno": rand.randint(0, num_de_pessoas) 
    })
    num += 1
num = 0
for i in range(num_de_pessoas):  # Insere histórico do aluno / Matriz curricular / verificar nota e alterar formado
    nota = rand.uniform(0, 10)
    print(nota)
    curso = rand.randint(0, 7)
    data_inicial = rand.randint(2000, 2024)
    sem_inicial = rand.randint(1, 8)
    
    # Inserir na matriz curricular
    inserir("matriz_curricular", { 
        "id_aluno": num, 
        "id_curso": curso, 
        "ano": data_inicial, 
        "semestre": 8 
    })
    
    # Selecionar disciplinas
    disciplinas = ((client["projeto"])["disciplina"]).find({ "id": curso })
    lista_disciplinas = [disciplina["id"] for disciplina in disciplinas]
    limite_disciplinas = len(lista_disciplinas) - rand.randint(0, 4)
    
    type(disciplinas)
    # pprint(disciplinas)
    semestre = 0
    for m in range(limite_disciplinas):
        semestre += 1
        inserir("historico_aluno", { 
            "id_aluno": num, 
            "id_disciplina": lista_disciplinas[m], 
            "semestre": semestre, 
            "ano": data_inicial, 
            "nota": round(nota, 2) 
        })
        print(lista_disciplinas[m])
        data_inicial += 1
    
    # Atualizar estado de formado
    if (nota >= 5 and sem_inicial == 8):
        atualizar("aluno", num,{ 
            "id": num, 
            "formado": 'True', 
            "grupo_tcc": rand.randint(0, round(0.2 * num_de_pessoas)) 
        })
        print("formado")
    else:
        atualizar("aluno", num, { 
            "id": num, 
            "formado": 'False' 
        })
        print("não formado")
    
    num += 1

### Atualizar departamento e alunos 
atualizar("departamento", 453, {"id_chefe_departamento" : rand.randint(0,(num_de_pessoas-1))});
atualizar("departamento", 654, {"id_chefe_departamento" : rand.randint(0,(num_de_pessoas-1))});
atualizar("departamento", 236, {"id_chefe_departamento" : rand.randint(0,(num_de_pessoas-1))});
atualizar("departamento", 735, {"id_chefe_departamento" : rand.randint(0,(num_de_pessoas-1))});
# executa("\
#     UPDATE departamentos SET id_chefe_departamento = %d where id_departamento = '453';\
#     UPDATE departamentos SET id_chefe_departamento = %d where id_departamento = 654;\
#     UPDATE departamentos SET id_chefe_departamento = %d where id_departamento = 236;\
#     UPDATE departamentos SET id_chefe_departamento = %d where id_departamento = 735;\
#     "%(
#         rand.randint(0,num_de_pessoas-1),
#         rand.randint(0,num_de_pessoas-1),
#         rand.randint(0,num_de_pessoas-1),
#         rand.randint(0,num_de_pessoas-1)))
client.close()