document.addEventListener('DOMContentLoaded', function() {

const altoContrasteBtn = document.getElementById('alto-contraste-btn');

// Aplica alto contraste se estiver ativo no localStorage
if (localStorage.getItem('altoContrasteAtivo') === 'true') {
    document.body.classList.add('alto-contraste');
}

// Alterna o modo de alto contraste ao clicar no botão
altoContrasteBtn.addEventListener('click', function() {
    document.body.classList.toggle('alto-contraste');
    
    // Salva o estado no localStorage
    const contrasteAtivo = document.body.classList.contains('alto-contraste');
    localStorage.setItem('altoContrasteAtivo', contrasteAtivo);
});

    const alunosBtn = document.getElementById('alunos-btn');
    const instrutoresBtn = document.getElementById('instrutores-btn');
    const treinosBtn = document.getElementById('treinos-btn');
    const exerciciosBtn = document.getElementById('exercicios-btn');
    
    const alunosSubBtn = document.getElementById('alunos-sub-buttons');
    const visualizaralunosBtn = document.getElementById('visualizar-alunos-btn');
    const inserirAlunoBtn = document.getElementById('inserir-aluno-btn');
    const excluirAlunoBtn = document.getElementById('excluir-aluno-btn');
    const alunoBackBtn = document.getElementById('aluno-back-btn');
   
    const instrutoresSubBtn = document.getElementById('instrutores-sub-buttons');
    const visuInstrutBtn = document.getElementById('visualizar-instrut-btn');
    const insertInstrutBtn = document.getElementById('inserir-instrut-btn');
    const excluirInstrutBtn = document.getElementById('excluir-instrut-btn');
    const instrutBackBtn = document.getElementById('instrut-back-btn');
 
    const treinosSubBtn = document.getElementById('treinos-sub-buttons');
    const visuTreinoBtn = document.getElementById('visualizar-treino-btn');
    const insertTreinoBtn = document.getElementById('inserir-treino-btn');
    const excluirTreinoBtn = document.getElementById('excluir-treino-btn');
    const treinoBackBtn = document.getElementById('treino-back-btn');
 
    const exercsSubBtn = document.getElementById('exercicios-sub-buttons');
    const visuexercsBtn = document.getElementById('visualizar-exercicios-btn');
    const insertexercsBtn = document.getElementById('inserir-exercicios-btn');
    const excluirexercsBtn = document.getElementById('excluir-exercicios-btn');
    const exercsBackBtn = document.getElementById('exerc-back-btn');
         
    instrutoresBtn.addEventListener('click', function() {
        toggleMainButtons(false);
        instrutoresSubBtn.style.display = 'block';
    });

    instrutBackBtn.addEventListener('click', function() {
        toggleMainButtons(true);
        instrutoresSubBtn.style.display = 'none';
    });
    
    alunosBtn.addEventListener('click', function() {
        toggleMainButtons(false);
        alunosSubBtn.style.display = 'block';
    });

    alunoBackBtn.addEventListener('click', function() {
        toggleMainButtons(true);
        alunosSubBtn.style.display = 'none';
    });

    treinosBtn.addEventListener('click', function() {
        toggleMainButtons(false);
        treinosSubBtn.style.display = 'block';
    });

    treinoBackBtn.addEventListener('click', function() {
        toggleMainButtons(true);
        treinosSubBtn.style.display = 'none';
    });

    exerciciosBtn.addEventListener('click', function() {
        toggleMainButtons(false);
        exercsSubBtn.style.display = 'block';
    });

    exercsBackBtn.addEventListener('click', function() {
        toggleMainButtons(true);
        exercsSubBtn.style.display = 'none';
    });
    
    insertInstrutBtn.addEventListener('click', function() {
        window.location.href = '/add_instrutor';
     });
     
    visuTreinoBtn.addEventListener('click', function() {
        window.location.href = '/visualizar_treinos';
    });
    
    visuexercsBtn.addEventListener('click', function() {
        window.location.href = '/visualizar_exercicios';
    });

    insertTreinoBtn.addEventListener('click', function() {
        window.location.href = '/add_treino';
    });

    visuexercsBtn.addEventListener('click', function() {
        window.location.href = '/visualizar_exercicios';
    });

    visuInstrutBtn.addEventListener('click', function() {
        window.location.href = '/visualizar_instrutores';
    });

    insertexercsBtn.addEventListener('click', function() {
        window.location.href = '/add_exercicio';
    });
    
    inserirAlunoBtn.addEventListener('click', function() {
        window.location.href = '/add_aluno';
    });
    
    visualizaralunosBtn.addEventListener('click', function() {
        window.location.href = '/visualizar_alunos';
    });
    
    excluirAlunoBtn.addEventListener('click', function() {
    window.location.href = '/excluir_aluno';
    });
    
    excluirInstrutBtn.addEventListener('click', function() {
    window.location.href = '/excluir_instrutor';
    });
    
    excluirTreinoBtn.addEventListener('click', function() {
    window.location.href = '/excluir_treino';
    });
    
    excluirexercsBtn.addEventListener('click', function() {
    window.location.href = '/excluir_exercicio';
    });
    
    function toggleMainButtons(show) {
        alunosBtn.style.display = show ? 'block' : 'none';
        instrutoresBtn.style.display = show ? 'block' : 'none';
        treinosBtn.style.display = show ? 'block' : 'none';
        exerciciosBtn.style.display = show ? 'block' : 'none';
    }
    
});


