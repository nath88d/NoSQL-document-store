/* global use, db */

const database = 'projeto';

// Conecta ao banco
use(database);



// histórico escolar de qualquer aluno, 
// retornando o código e nome da disciplina, 
// semestre e ano que a disciplina foi cursada e nota final

db.aluno.aggregate([
  {
    $match: { // Trocar ID pelo valor do aluno que deseja pesquisar
      id: 8 //  id: <ID_DO_ALUNO>
    }
  },
  {
    $lookup: {
      from: "historico_aluno",
      localField: "id",
      foreignField: "id_aluno",
      as: "historico_do_aluno",
    }
  },
  {
  $lookup: {
    from: "disciplina",
    localField: "historico_do_aluno.id_disciplina",
    foreignField: "id",
    as: "disciplina",
  }
  },
  {
    $addFields: {
      "historico_do_aluno": {
        $map: {
          input: "$historico_do_aluno",  
          as: "historico",        
          in: {
            $mergeObjects: [
              "$$historico",          
              { $arrayElemAt: ["$disciplina", 0] }  
            ]
          }
        }
      }
    }
  },

  {
    $project: { // Remove dados irrelevantes
      _id:0,
      "historico_do_aluno._id":0,
      "historico_do_aluno.id_aluno":0,
      "disciplina":0
    }
  }
])

// histórico de disciplinas
// ministradas por qualquer professor,
// com semestre e ano

db.professor.aggregate([
  {
    $match: {
      id: 8
    }
  },
  {
    $lookup: {
      from: "historico_professor",
      localField: "id",
      foreignField: "id_professor",
      as: "historico_do_professor",
    }
  },
  {
  $lookup: {
    from: "disciplina",
    localField: "historico_do_professor.id_disciplina",
    foreignField: "id",
    as: "disciplina",
  }
  },
  {
    $addFields: {
      "historico_do_professor": {
        $map: {
          input: "$historico_do_professor",  
          as: "historico",        
          in: {
            $mergeObjects: [
              "$$historico",          
              { $arrayElemAt: ["$disciplina", 0] }  
            ]
          }
        }
      }
    }
  },

  {
    $project: { // Remove dados irrelevantes
      _id:0,
      "historico_do_professor._id":0,
      "historico_do_professor.id_professor":0,
      "disciplina":0
    }
  }
])

// listar alunos que já se formaram 
// (foram aprovados em todos os cursos de uma matriz curricular) 
// em um determinado semestre de um ano

db.aluno.aggregate([
  {
    $match: {
      formado: "True"
    }
  },
  {
    $lookup: {
      from: "matriz_curricular",
      localField: "id",
      foreignField: "id_aluno",
      as: "matriz_do_aluno",
    }
  },
  {
  $lookup: {
    from: "curso",
    localField: "matriz_do_aluno.id_curso",
    foreignField: "id",
    as: "curso",
  }
  },
  {
    $addFields: {
      "matriz_do_aluno": {
        $map: {
          input: "$matriz_do_aluno",  
          as: "historico",        
          in: {
            $mergeObjects: [
              "$$historico",          
              { $arrayElemAt: ["$curso", 0] }  
            ]
          }
        }
      }
    }
  },

  {
    $project: { // Remove dados irrelevantes
      _id:0,
      "matriz_do_aluno._id":0,
      "matriz_do_aluno.id_aluno":0,
      "matriz_do_aluno.id":0,
      "curso":0
    }
  }
])


// listar todos os professores que são 
// chefes de departamento, junto
// com o nome do departamento

db.departamento.aggregate([
  {
    $lookup: {
      from: "professor",
      localField: "id_chefe_departamento",
      foreignField: "id",
      as: "chefe_departamento",
    }
  },
  {
    $project: { // Remove dados irrelevantes
      _id:0,
      "chefe_departamento._id":0,
      "chefe_departamento.id":0,
      "chefe_departamento.departamento":0,
    }
  }
])

// saber quais alunos formaram 
// um grupo de TCC e qual
// professor foi o orientador

db.aluno.aggregate([ 
  {
    $match: {
      formado:"True"
    }
  }
  
  ,{
    $lookup: {
      from: "grupo_tcc",
      localField: "grupo_tcc",
      foreignField: "id_grupo",
      as: "grupo_tcc",
    }
  },
  {
  $lookup: {
    from: "professor",
    localField: "grupo_tcc.id_professor",
    foreignField: "id",
    as: "professor_orientador",
  }
  },

  {
    $project: { // Remove dados irrelevantes
      _id:0,
      "grupo_tcc._id":0,
      "grupo_tcc.id":0,
      "professor_orientador._id":0,
      "professor_orientador.id":0,
    }
  }
])
