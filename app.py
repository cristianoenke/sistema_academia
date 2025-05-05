from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/academia'
db = SQLAlchemy(app)

# Classe Instrutor
class Instrutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_instrutor= db.Column(db.String(50))
    fone_instrutor = db.Column(db.String(50))
    email_instrutor= db.Column(db.String(140))
    sexo_instrutor= db.Column(db.String(50))
    nasc_instrutor= db.Column(db.Date)

# Classe Exercicio
class Exercicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_exerc= db.Column(db.String(50))
    categ_exer = db.Column(db.String(50))
    descr_exerc= db.Column(db.String(140))

# Classe Treino
class Treino(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    numero_series = db.Column(db.Integer)
    repeticoes = db.Column(db.Integer)
    grupo_muscular = db.Column(db.String(50))
    membro_corpo = db.Column(db.String(50))
    exercicios = db.relationship('Exercicio', secondary='exercicios_no_treino', backref='treinos')
    instrutores = db.relationship('Instrutor', secondary='treinos_do_instrutor', backref='instrutor')

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_aluno = db.Column(db.String(100), nullable=False)
    fone_aluno = db.Column(db.String(15))
    nasc_aluno = db.Column(db.Date)
    sexo_aluno = db.Column(db.String(1))
    email_aluno = db.Column(db.String(100))
    instrutores = db.relationship('Instrutor', secondary='instrutor_do_aluno', backref='alunos')
    treinos = db.relationship('Treino', secondary='treinos_do_aluno', backref='alunos', cascade="all, delete")

# Tabela associativa para Instrutor e Aluno
instrutor_do_aluno = db.Table('instrutor_do_aluno',
    db.Column('instrutor_id', db.Integer, db.ForeignKey('instrutor.id'), primary_key=True),
    db.Column('aluno_id', db.Integer, db.ForeignKey('aluno.id'), primary_key=True)
)

# Tabela associativa para Exercicio e Treino
exercicios_no_treino = db.Table('exercicios_no_treino',
    db.Column('treino_id', db.Integer, db.ForeignKey('treino.id', ondelete="cascade"), primary_key=True),
    db.Column('exercicio_id', db.Integer, db.ForeignKey('exercicio.id', ondelete="cascade"), primary_key=True)
)

# Tabela associativa para Aluno e Treino
treinos_do_aluno = db.Table('treinos_do_aluno',
    db.Column('aluno_id', db.Integer, db.ForeignKey('aluno.id', ondelete="cascade"), primary_key=True),
    db.Column('treino_id', db.Integer, db.ForeignKey('treino.id'), primary_key=True),
    db.Column('dia_semana', db.String(10), primary_key=True),  # Ex: 'segunda', 'terça', etc.
    db.Column('periodo', db.String(10), primary_key=True)  # Ex: 'manhã', 'tarde', 'noite'
)


# Tabela associativa para Instrutor e Treino
treinos_do_instrutor = db.Table('treinos_do_instrutor',
    db.Column('instrutor_id', db.Integer, db.ForeignKey('instrutor.id', ondelete="cascade"), primary_key=True),
    db.Column('treino_id', db.Integer, db.ForeignKey('treino.id'), primary_key=True)
)


# with app.app_context():
#     db.create_all() 


@app.route('/')
def index():
    return render_template('index.html')

# # Rota para adicionar um Aluno
@app.route('/add_aluno', methods=['GET', 'POST'])
def add_aluno():
    if request.method == 'POST':
        # Captura dos dados do aluno
        nome_aluno = request.form['nome_aluno']
        fone_aluno = request.form['fone_aluno']
        nasc_aluno = request.form['nasc_aluno']
        sexo_aluno = request.form['sexo_aluno']
        email_aluno = request.form['email_aluno']
        novo_aluno = Aluno(nome_aluno=nome_aluno, fone_aluno=fone_aluno, nasc_aluno=nasc_aluno, sexo_aluno=sexo_aluno, email_aluno=email_aluno)
        db.session.add(novo_aluno)
        db.session.commit()  # Salvar o aluno no banco de dados

        instrutores_selecionados = request.form.getlist('instrutores')
        for instrutor_id in instrutores_selecionados:
            pass
        dias_da_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
        for dia in dias_da_semana:
            treinos_selecionados = request.form.getlist(f'treinos_{dia}')
            for treino_id in treinos_selecionados:
                periodo = request.form.get(f'periodo_{dia}_{treino_id}')
                # Criar a associação com a tabela associativa
                db.session.execute(
                    treinos_do_aluno.insert().values(
                        aluno_id=novo_aluno.id,
                        treino_id=treino_id,
                        dia_semana=dia,
                        periodo=periodo
                    )
                )
        db.session.commit()  # Salvar todas as associações
        return redirect(url_for('index'))  # Redirecionar para a página inicial ou onde for apropriado
    instrutores = Instrutor.query.all()  # Ajuste conforme seu modelo de instrutor
    treinos = Treino.query.all()  # Ajuste conforme seu modelo de treino
    return render_template('aluno_form.html', instrutores=instrutores, treinos=treinos)




# Rota para adicionar um instrutor
@app.route('/add_instrutor', methods=['GET', 'POST'])
def add_instrutor():
    if request.method == 'POST':
        nome_instrutor = request.form['nome_instrutor']
        fone_instrutor = request.form['fone_instrutor']
        email_instrutor = request.form['email_instrutor']
        sexo_instrutor = request.form['sexo_instrutor']
        nasc_instrutor = request.form['nasc_instrutor']
        novo_instrutor = Instrutor(nome_instrutor=nome_instrutor, fone_instrutor=fone_instrutor, email_instrutor=email_instrutor,sexo_instrutor=sexo_instrutor,nasc_instrutor=nasc_instrutor)
        db.session.add(novo_instrutor)
        db.session.commit()
        return redirect(url_for('add_instrutor'))
    return render_template('instrutor_form.html')

# Rota para adicionar uma exercicio
@app.route('/add_exercicio', methods=['GET', 'POST'])
def add_exercicio():
    if request.method == 'POST':
        nome_exerc = request.form['nome_exerc']
        categ_exer = request.form['categ_exerc']
        descr_exerc= request.form['descr_exerc']
        novo_exerc = Exercicio(nome_exerc=nome_exerc, categ_exer=categ_exer, descr_exerc=descr_exerc)
        db.session.add(novo_exerc)
        db.session.commit()
        return redirect(url_for('add_exercicio'))
    return render_template('exercicio_form.html')

# # Rota para adicionar um Treino
@app.route('/add_treino', methods=['GET', 'POST'])
def add_treino():
    exercicios = Exercicio.query.all()
    instrutores = Instrutor.query.all()
    if request.method == 'POST':
        nome = request.form['nome_treino']
        selected_exercicios_ids = request.form.getlist('exercicios')
        selected_instrutor_id = request.form.getlist('instrutores')
        novo_treino = Treino(nome=nome)
        for exercicio_id in selected_exercicios_ids:
            exercicio = Exercicio.query.get(exercicio_id)
            novo_treino.exercicios.append(exercicio)
        
        for instrutor_id in selected_instrutor_id:
            instrutor = Instrutor.query.get(instrutor_id)
            novo_treino.instrutores.append(instrutor)
            
        db.session.add(novo_treino)
        db.session.commit()
        return redirect(url_for('add_treino'))
    return render_template('treino_form.html', exercicios=exercicios, instrutores=instrutores)


@app.route('/visualizar_treinos')
def visualizar_treinos():
    treinos = Treino.query.all()
    return render_template('visualizar_treinos.html', treinos=treinos)

@app.route('/visualizar_exercicios')
def visualizar_exercicios():
    exercicios = Exercicio.query.all()
    return render_template('visualizar_exercicios.html', exercicios=exercicios)

@app.route('/visualizar_instrutores')
def visualizar_instrutores():
    instrutores = Instrutor.query.all()
    return render_template('visualizar_instrutores.html', instrutores=instrutores)

@app.route('/visualizar_alunos')
def visualizar_alunos():
    alunos = Aluno.query.all()
    return render_template('visualizar_alunos.html', alunos=alunos)

@app.route('/ficha_aluno/<int:aluno_id>')
def ficha_aluno(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)
    treinos_associados = db.session.query(
        Treino.nome,
        treinos_do_aluno.c.dia_semana,
        treinos_do_aluno.c.periodo
    ).join(treinos_do_aluno).filter(treinos_do_aluno.c.aluno_id == aluno.id).all()
    
    return render_template('ficha_aluno.html', aluno=aluno, treinos_associados=treinos_associados)

@app.route('/excluir_aluno', methods=['GET', 'POST'])
def excluir_aluno():
    if request.method == 'POST':
        aluno_ids = request.form.getlist('aluno_ids')
        if aluno_ids:
            Aluno.query.filter(Aluno.id.in_(aluno_ids)).delete(synchronize_session='fetch')
            db.session.commit()
        return redirect(url_for('index'))  # Redireciona para a página inicial após exclusão

    alunos = Aluno.query.all()
    return render_template('excluir_aluno.html', alunos=alunos)

@app.route('/excluir_instrutor', methods=['GET', 'POST'])
def excluir_instrutor():
    if request.method == 'POST':
        instrutor_ids = request.form.getlist('instrutor_ids')
        if instrutor_ids:
            Instrutor.query.filter(Instrutor.id.in_(instrutor_ids)).delete(synchronize_session='fetch')
            db.session.commit()
        return redirect(url_for('index'))  # Redireciona para a página inicial após exclusão

    instrutores = Instrutor.query.all()
    return render_template('excluir_instrutor.html', instrutores=instrutores)

@app.route('/excluir_treino', methods=['GET', 'POST'])
def excluir_treino():
    if request.method == 'POST':
        treino_ids = request.form.getlist('treino_ids')
        if treino_ids:
            Treino.query.filter(Treino.id.in_(treino_ids)).delete(synchronize_session='fetch')
            db.session.commit()
        return redirect(url_for('index'))  # Redireciona para a página inicial após exclusão

    treinos = Treino.query.all()
    return render_template('excluir_treino.html', treinos=treinos)

@app.route('/excluir_exercicio', methods=['GET', 'POST'])
def excluir_exercicio():
    if request.method == 'POST':
        exercicio_ids = request.form.getlist('exercicio_ids')
        if exercicio_ids:
            Exercicio.query.filter(Exercicio.id.in_(exercicio_ids)).delete(synchronize_session='fetch')
            db.session.commit()
        return redirect(url_for('index'))  # Redireciona para a página inicial após exclusão

    exercicios = Exercicio.query.all()
    return render_template('excluir_exercicio.html', exercicios=exercicios)

if __name__ == '__main__':
    app.run(debug=True)