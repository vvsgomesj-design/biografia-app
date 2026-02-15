import streamlit as st
from datetime import datetime

# --- 1. CONFIGURAÇÃO E INICIALIZAÇÃO ---
st.set_page_config(page_title="Gerador Trampolim", layout="wide")
# --- SISTEMA DE SENHA SIMPLES ---
def check_password():
    if "password_correct" not in st.session_state:
        st.text_input("Digite a senha do livro para acessar:", type="password", key="password")
        if st.button("Entrar"):
            if st.session_state["password"] == "BIOGRAFIA2024": # Sua senha aqui
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("Senha incorreta!")
        return False
    return True

if not check_password():
    st.stop() # Interrompe o código aqui se a senha não estiver correta
# --- RESTANTE DO SEU CÓDIGO ABAIXO ---

# Inicializa o estado para evitar erro de página em branco
if 'livro_gerado' not in st.session_state:
    st.session_state.livro_gerado = ""

# --- 2. FUNÇÃO DE SEGURANÇA (BUSCA DADOS NO SESSION STATE) ---
def buscar_dados(key, mensagem_padrao="[informação não preenchida]"):
    """
    Retorna o valor da chave no session_state de forma segura.
    Se for lista vazia ou None, retorna a mensagem padrão.
    Se for lista com itens, retorna uma string com os itens separados por vírgula.
    """
    valor = st.session_state.get(key)
    if valor is None or valor == "" or valor == []:
        return mensagem_padrao
    if isinstance(valor, list):
        return ", ".join(str(v) for v in valor)
    return str(valor)

# Criação das abas (deve vir antes de usar as tabs)
tab_a, tab_b, tab_c, tab_d = st.tabs([
    "Bloco A: Fundamentos",
    "Bloco B: Legado e Relações",
    "Bloco C: Estrutura",
    "📖 Livro Gerado"
])

# ==================================================
# BLOCO A – CAPÍTULOS 1 A 10
# ==================================================
with tab_a:
    st.header("Bloco A: Fundamentos, Identidade e Organização")
    nome_autor = st.text_input("Nome Completo:", "Autor Desconhecido", key="nome_autor")

    # Capítulo 1
    with st.expander("Cap. 1 – Neuroplasticidade e Mudança de Mindset"):
        st.radio("Você acredita que é possível mudar padrões de pensamento?",
                 ["Sim", "Não", "Não tenho certeza"], key="c1_mudanca")
        st.selectbox("Com que frequência você busca aprender algo novo?",
                     ["Diariamente", "Semanalmente", "Raramente", "Nunca"], key="c1_aprendizado")
        st.radio("Quando enfrenta um desafio, você tende a:",
                 ["Desistir facilmente", "Persistir e buscar novas estratégias", "Esperar que alguém resolva"],
                 key="c1_reacao")
        st.radio("Você já percebeu mudanças positivas após criar novos hábitos?",
                 ["Sim", "Não", "Ainda estou tentando"], key="c1_habitos")
        st.text_input("Em uma palavra, o que mais te motiva a mudar?", key="c1_motiva")
        st.text_area("O que significa para você 'renovar a mente'?", key="c1_renovar")

    # Capítulo 2
    with st.expander("Cap. 2 – Identidade em Cristo e Herança"):
        st.radio("Como você se vê em relação à herança espiritual?",
                 ["Sinto-me herdeiro(a) de Deus", "Às vezes me esqueço", "Ainda não compreendo"],
                 key="c2_heranca")
        st.radio("Como você costuma encarar os desafios da vida?",
                 ["Como oportunidade de crescimento", "Com medo ou insegurança", "Com dificuldade de enxergar propósito"],
                 key="c2_desafios")
        st.radio("Qual sua relação com as promessas bíblicas?",
                 ["Conheço e procuro viver", "Conheço, mas não aplico sempre", "Não costumo refletir sobre isso"],
                 key="c2_promessas")
        st.radio("Você pensa no seu futuro eterno?",
                 ["Sim, com convicção", "Às vezes", "Raramente"], key="c2_eternidade")
        st.text_area("De que forma seus desafios revelam sua identidade e herança?", key="c2_reflexao")

    # Capítulo 3
    with st.expander("Cap. 3 – Organização do Corpo e do Espírito"):
        st.multiselect("Quais práticas você mantém para cuidar do corpo?",
                       ["Rotina diária", "Atividade física", "Alimentação equilibrada", "Sono regulado", "Disciplina"],
                       key="c3_corpo")
        st.multiselect("Quais práticas fortalecem seu espírito?",
                       ["Oração", "Meditação", "Leitura espiritual", "Intuição", "Paz com propósito"],
                       key="c3_espirito")
        st.text_area("Como você percebe o equilíbrio (ou desequilíbrio) entre corpo e espírito?", key="c3_equilibrio")

    # Capítulo 4
    with st.expander("Cap. 4 – Autoconhecimento e Posição na Vida"):
        st.text_area("Descreva um momento em que você se sentiu verdadeiramente autêntico(a):", key="c4_autentico")
        st.text_input("Quais são seus três maiores talentos?", key="c4_talentos")
        st.text_area("Relate um desafio significativo que você superou:", key="c4_desafio")
        st.text_area("O que esse desafio te ensinou sobre você mesmo(a)?", key="c4_aprendizado")

    # Capítulo 5
    with st.expander("Cap. 5 – Alcance da Sua História"):
        st.radio("Você acredita que sua história impacta pessoas ao seu redor?", ["Sim", "Não"], key="c5_local")
        st.radio("Você acredita que sua trajetória pode inspirar pessoas fora do seu círculo?", ["Sim", "Não"], key="c5_regional")
        st.radio("Você acredita que sua história pode inspirar diferentes culturas ou países?", ["Sim", "Não"], key="c5_internacional")
        st.text_area("Por que você acredita que sua história merece ser contada?", key="c5_reflexao")

    # Capítulo 6
    with st.expander("Cap. 6 – Posição Conforme a Bíblia"):
        st.radio("Em momentos de crise, você costuma buscar aprendizado?", ["Sim", "Não", "Às vezes"], key="c6_crise")
        st.radio("Você acredita que suas decisões revelam seu caráter?", ["Sim", "Não"], key="c6_carater")
        st.radio("Você presta atenção às suas emoções antes de agir?", ["Sim", "Não", "Raramente"], key="c6_emocoes")
        st.radio("Você pratica arrependimento como mudança real de atitude?", ["Sim", "Não", "Ainda estou aprendendo"], key="c6_arrependimento")
        st.radio("Você se mantém fiel aos seus compromissos mesmo quando ninguém está olhando?", ["Sim", "Não"], key="c6_fidelidade")
        st.text_area("Como os princípios bíblicos influenciam suas decisões diárias?", key="c6_reflexao")

    # Capítulo 7
    with st.expander("Cap. 7 – Situação Atual e Impulso para o Trampolim"):
        st.radio("Você se considera uma pessoa proativa?", ["Sim", "Não"], key="c7_proativo")
        st.radio("Você sente que está estagnado(a) em alguma área da vida?", ["Sim", "Não"], key="c7_estagnacao")
        st.text_input("Se sim, em qual área você sente maior estagnação?", key="c7_area")
        st.radio("Você sente que chegou o momento de mudar?", ["Sim", "Não", "Ainda estou refletindo"], key="c7_decisao")
        st.text_area("O que hoje funciona como trampolim para o seu próximo nível?", key="c7_reflexao")

    # Capítulo 8
    with st.expander("Cap. 8 – Comemoração e Reconhecimento de Conquistas"):
        st.selectbox("Você costuma celebrar pequenas vitórias?", ["Sempre", "Às vezes", "Raramente", "Nunca"], key="c8_celebra")
        st.radio("Por que você acha importante (ou difícil) comemorar conquistas?",
                 ["Reconhece o esforço", "Evita frustração", "Nunca parei para pensar", "Tenho dificuldade em comemorar"],
                 key="c8_motivo")
        st.text_area("Descreva uma conquista que marcou sua vida:", key="c8_memoria")
        st.text_area("O que essa conquista te ensinou?", key="c8_aprendizado")

    # Capítulo 9
    with st.expander("Cap. 9 – Público, Propósito e Forma"):
        st.multiselect("Para quem esta biografia é direcionada?",
                       ["Família", "Amigos", "Estudantes", "Líderes", "Público em geral"], key="c9_publico")
        st.multiselect("Por que você deseja contar sua história?",
                       ["Inspirar pessoas", "Registrar minha trajetória", "Ensinar aprendizados", "Curar feridas", "Deixar legado"],
                       key="c9_por_que")
        st.multiselect("Como você gostaria que sua história fosse sentida pelo leitor?",
                       ["Acolhedora", "Inspiradora", "Realista", "Transformadora", "Leve"], key="c9_como")
        st.text_area("Qual impacto você espera causar em quem ler sua biografia?", key="c9_reflexao")

    # Capítulo 10
    with st.expander("Cap. 10 – Análise Curricular e Experiências"):
        st.text_area("Formações acadêmicas, cursos ou treinamentos relevantes:", key="c10_formacao")
        st.text_area("Experiências profissionais ou ministeriais marcantes:", key="c10_experiencias")
        st.text_area("Quais competências você desenvolveu ao longo da vida?", key="c10_competencias")
        st.text_area("Como sua trajetória prepara você para o futuro?", key="c10_reflexao")

# ==================================================
# BLOCO B – CAPÍTULOS 11 A 20
# ==================================================
with tab_b:
    st.header("Bloco B: Seleção, Legado, Talento e Relações")

    # Capítulo 11
    with st.expander("Cap. 11 – Técnicas de Seleção e Critérios"):
        st.radio("Para você, ética é determinante em qualquer escolha importante?", ["Sim", "Não"], key="c11_etica")
        st.multiselect("Você considera contratar apoio para este projeto?",
                       ["Editora", "Ghost Writer", "Designer", "Gráfica", "Nenhum"], key="c11_contratacoes")
        st.text_area("Quais critérios você considera essenciais ao selecionar pessoas ou projetos?", key="c11_criterios")

    # Capítulo 12
    with st.expander("Cap. 12 – Treinamento, Aprendizado e Virada"):
        st.text_area("Descreva um momento decisivo de virada na sua vida:", key="c12_virada")
        st.text_area("O que esse momento te ensinou?", key="c12_aprendeu")
        st.radio("Você costuma aplicar rapidamente o que aprende?", ["Sim", "Não", "Depende da situação"], key="c12_aplicacao")

    # Capítulo 13
    with st.expander("Cap. 13 – Legado e Postura Pessoal"):
        st.radio("Você se considera mais proativo(a) ou procrastinador(a)?", ["Proativo(a)", "Procrastinador(a)"], key="c13_procrastina")
        st.text_area("O que costuma roubar seu tempo e energia?", key="c13_tempo")
        st.text_area("O que você sente que precisa mudar para deixar um legado melhor?", key="c13_mudanca")

    # Capítulo 14
    with st.expander("Cap. 14 – Talento, Hobby e Fonte de Paz"):
        st.text_input("Qual talento ou hobby faz parte da sua história?", key="c14_hobby")
        st.text_area("Como esse talento ou hobby surgiu e quem te influenciou?", key="c14_origem")
        st.text_area("Relate um momento em que esse hobby trouxe paz, cura ou alegria:", key="c14_paz")
        st.text_input("Crie uma frase curta sobre esse talento para a capa do livro:", key="c14_frase_capa")

    # Capítulo 15
    with st.expander("Cap. 15 – Posição Social, Família e Relações"):
        papeis_list = [
            "Mãe", "Pai", "Filha", "Filho", "Irmã", "Irmão",
            "Avó", "Avô", "Neta", "Neto", "Tia", "Tio",
            "Sobrinha", "Sobrinho", "Prima", "Primo",
            "Madrinha", "Padrinho", "Esposa", "Marido",
            "Companheira", "Companheiro", "Noiva", "Noivo",
            "Sogra", "Sogro", "Nora", "Genro",
            "Cunhada", "Cunhado", "Madrasta", "Padrasto",
            "Enteada", "Enteado", "Amiga", "Amigo",
            "Vizinha", "Vizinho", "Colega", "Parceira", "Parceiro"
        ]
        st.multiselect("Quais papéis você exerce hoje em sua vida?", papeis_list, key="c15_escolhidos")
        st.text_area("Como esses papéis influenciam quem você é?", key="c15_reflexao")

    # Capítulo 16
    with st.expander("Cap. 16 – Virtudes (Caráter em Construção)"):
        virtudes_list = [
            "Perdão", "Honra", "Gratidão", "Cortesia", "Perseverança",
            "Tato", "Paciência", "Flexibilidade", "Bom Humor", "Simpatia",
            "Contentamento", "Justiça", "Responsabilidade", "Verdade",
            "Bondade", "Consideração", "Compaixão", "Lealdade", "Gentileza",
            "Excelência", "Prestatividade", "Generosidade", "Dedicação",
            "Disciplina", "Independência", "Propósito", "Organização",
            "Tolerância", "Determinação", "União", "Idealismo",
            "Assertividade", "Criatividade", "Confiança", "Autenticidade",
            "Diligência", "Respeito", "Modéstia", "Comprometimento",
            "Entusiasmo", "Moderação"
        ]
        st.multiselect("Quais virtudes você reconhece em si ou deseja desenvolver?", virtudes_list, key="c16_virtudes")
        st.text_area("Cite uma situação em que uma virtude fez diferença na sua vida:", key="c16_exemplo")

    # Capítulo 17
    with st.expander("Cap. 17 – Galardão e Motivação"):
        st.radio("O que mais te motiva na vida?",
                 ["Agradar a Deus", "Ser reconhecido(a) pelas pessoas", "Deixar um legado", "Cumprir meu propósito"],
                 key="c17_motivo")
        st.text_area("Como essa motivação influencia suas decisões diárias?", key="c17_reflexao")

    # Capítulo 18
    with st.expander("Cap. 18 – Terceirização e Confiança"):
        st.selectbox("Como você se sente ao delegar tarefas?",
                     ["Alívio", "Insegurança", "Medo de perder o controle", "Entusiasmo"], key="c18_delega")
        st.text_area("O que mais dificulta para você confiar tarefas a outras pessoas?", key="c18_dificuldade")
        st.text_area("O que você já aprendeu ao delegar ou tentar fazer tudo sozinho(a)?", key="c18_aprendizado")

    # Capítulo 19
    with st.expander("Cap. 19 – Fases da Vida"):
        st.text_area("Quais brincadeiras ou atividades marcaram sua infância?", key="c19_infancia")
        st.text_area("O que mais marcou sua adolescência?", key="c19_adolescencia")
        st.text_area("Qual foi (ou é) o auge da sua fase adulta?", key="c19_adulta")
        st.text_area("Que aprendizado cada fase da vida te trouxe?", key="c19_aprendizado")

    # Capítulo 20
    with st.expander("Cap. 20 – Pequenas Ações e Perseverança"):
        st.radio("Você consegue manter um hábito por pelo menos 21 dias?", ["Sim", "Tentando", "Não"], key="c20_habito")
        st.text_area("Cite um pequeno hábito que já trouxe grande mudança:", key="c20_exemplo")
        st.text_area("O que mais dificulta sua constância?", key="c20_dificuldade")

# ==================================================
# BLOCO C – CAPÍTULOS 21 A 26
# ==================================================
with tab_c:
    st.header("Bloco C: Estrutura do Livro, Vendas e Experiência")

    # Capítulo 21
    with st.expander("Cap. 21 – Planejamento, Tempo e Futuro"):
        st.radio("Você tende a viver mais focado em:", ["Passado", "Presente", "Futuro"], key="c21_foco")
        st.radio("Você aprende mais com:", ["Erros", "Acertos", "Observando outras pessoas"], key="c21_aprende")
        st.text_area("Qual é o principal sonho ou objetivo para os próximos anos?", key="c21_sonho")
        st.text_area("Que passos práticos você acredita que precisa dar a partir de agora?", key="c21_plano")

    # Capítulo 22
    with st.expander("Cap. 22 – Estrutura e Fluxograma do Livro"):
        st.multiselect("Quais elementos você deseja incluir no livro?",
                       ["Título com essência", "Capa profissional", "Orelhas / Sinopse", "Folha de rosto",
                        "Epígrafe", "Dedicatória", "Sumário", "Corpo do texto", "Apêndices", "Fotos",
                        "Ficha catalográfica", "QR Code com música", "Agradecimentos finais"], key="c22_elementos")
        st.text_area("Por que esses elementos são importantes para você?", key="c22_reflexao")

    # Capítulo 23
    with st.expander("Cap. 23 – Organização e Distribuição"):
        st.multiselect("Em quais formatos você imagina sua biografia?",
                       ["Livro físico", "E-book (PDF)", "Audiobook", "Curso", "Material terapêutico", "Material ministerial"],
                       key="c23_formato")
        st.radio("Como você pretende publicar?", ["Independente", "Plataformas digitais", "Editoras", "Ainda não sei"],
                 key="c23_publicacao")
        st.text_area("O que mais te anima (ou preocupa) sobre a publicação?", key="c23_reflexao")

    # Capítulo 24
    with st.expander("Cap. 24 – Experiência Visual e Apoios"):
        st.radio("Você deseja incluir mapas mentais ou esquemas visuais no livro?", ["Sim", "Não"], key="c24_mapas")
        st.text_area("Como você imagina a estética visual do livro?", key="c24_estetica")
        st.multiselect("Quais recursos visuais ou de apoio você gostaria de incluir?",
                       ["Ilustrações", "Fotos pessoais", "Gráficos", "Checklists", "Exercícios práticos", "Espaço para anotações"],
                       key="c24_apoios")

    # Capítulo 25
    with st.expander("Cap. 25 – Vendas, Divulgação e Alcance"):
        st.multiselect("Quais etapas de venda você pretende estruturar?",
                       ["E-mail profissional", "Página de vendas", "Cadastro em plataforma (ex: Kiwify)",
                        "Link na bio do Instagram", "Conteúdo de divulgação", "Renda passiva"], key="c25_vendas")
        st.text_area("Como você imagina que esse livro pode alcançar pessoas?", key="c25_reflexao")

    # Capítulo 26
    with st.expander("Cap. 26 – Experiência Sinestésica e Legado"):
        st.multiselect("Quais sentidos você gostaria que seu livro despertasse?",
                       ["Visão (design, marca-páginas)", "Tato (papel, textura)", "Olfato (aroma, memória afetiva)",
                        "Audição (playlist, áudio)", "Paladar (brinde simbólico)", "Experiência de entrega (caixa especial)"],
                       key="c26_sinestesia")
        st.text_area("Qual mensagem final você deseja deixar como legado?", key="c26_legado")

# ==================================================
# FUNÇÕES DE GERAÇÃO (USAM buscar_dados)
# ==================================================

def gerar_biografia_hobby():
    nome = buscar_dados('nome_autor', 'Autor Desconhecido').upper()
    data = datetime.now().strftime("%d/%m/%Y")

    texto = f"""# OS PASSATEMPOS DE {nome}
## Uma Jornada de Descoberta, Paixão e Sentido
*Gerado em {data}*

---

### INTRODUÇÃO

Cada pessoa carrega dentro de si um universo particular de interesses e talentos. Para **{nome}**, os passatempos não são meras distrações; são verdadeiras fontes de vida, momentos em que a alma se reconecta consigo mesma e com o mundo de forma leve e autêntica. Nesta biografia, vamos mergulhar nesse universo e descobrir o que faz o coração de {nome} bater mais forte.

---

"""

    # Capítulo 14
    hobby = buscar_dados('c14_hobby')
    if hobby != "[informação não preenchida]":
        texto += "## 🌟 CAPÍTULO 14: MEU HOBBY FAVORITO\n\n"
        texto += f"O grande amor de {nome} é **{hobby}**. "
        origem = buscar_dados('c14_origem')
        if origem != "[informação não preenchida]":
            texto += f"Essa paixão surgiu {origem}. "
        paz = buscar_dados('c14_paz')
        if paz != "[informação não preenchida]":
            texto += f"Em momentos difíceis, essa atividade trouxe paz e alegria: \"{paz}\". "
        frase = buscar_dados('c14_frase_capa')
        if frase != "[informação não preenchida]":
            texto += f"Se fosse resumir em uma frase: **\"{frase}\"**. "
        texto += "\n\n"

    # Capítulo 4
    talentos = buscar_dados('c4_talentos')
    autentico = buscar_dados('c4_autentico')
    if talentos != "[informação não preenchida]" or autentico != "[informação não preenchida]":
        texto += "## ✨ CAPÍTULO 4: TALENTOS QUE ME DEFINEM\n\n"
        if talentos != "[informação não preenchida]":
            texto += f"Além do hobby, {nome} possui talentos especiais: {talentos}. "
        if autentico != "[informação não preenchida]":
            texto += f"Um momento em que se sentiu verdadeiramente autêntico(a) foi quando {autentico}. "
        texto += "\n\n"

    # Capítulo 8
    memoria = buscar_dados('c8_memoria')
    aprendizado_conquista = buscar_dados('c8_aprendizado')
    if memoria != "[informação não preenchida]" or aprendizado_conquista != "[informação não preenchida]":
        texto += "## 🏆 CAPÍTULO 8: CONQUISTAS MARCANTES\n\n"
        if memoria != "[informação não preenchida]":
            texto += f"Uma conquista inesquecível foi {memoria}. "
        if aprendizado_conquista != "[informação não preenchida]":
            texto += f"Essa experiência ensinou que {aprendizado_conquista}. "
        texto += "\n\n"

    # Capítulo 16
    virtudes = buscar_dados('c16_virtudes')
    exemplo_virtude = buscar_dados('c16_exemplo')
    if virtudes != "[informação não preenchida]" or exemplo_virtude != "[informação não preenchida]":
        texto += "## 💎 CAPÍTULO 16: VIRTUDES QUE ILUMINAM O CAMINHO\n\n"
        if virtudes != "[informação não preenchida]":
            texto += f"Ao longo da vida, {nome} cultivou virtudes como {virtudes.lower()}. "
        if exemplo_virtude != "[informação não preenchida]":
            texto += f"Certa vez, {exemplo_virtude}. "
        texto += "\n\n"

    # Capítulo 19
    infancia = buscar_dados('c19_infancia')
    adolescencia = buscar_dados('c19_adolescencia')
    adulta = buscar_dados('c19_adulta')
    if any(v != "[informação não preenchida]" for v in [infancia, adolescencia, adulta]):
        texto += "## 🌱 CAPÍTULO 19: O HOBBY AO LONGO DAS FASES DA VIDA\n\n"
        if infancia != "[informação não preenchida]":
            texto += f"Na infância, {nome} já demonstrava interesse por {infancia}. "
        if adolescencia != "[informação não preenchida]":
            texto += f"Na adolescência, {adolescencia}. "
        if adulta != "[informação não preenchida]":
            texto += f"Na fase adulta, {adulta}. "
        texto += "Essas experiências foram moldando sua relação com o hobby e consigo mesmo.\n\n"

    # Capítulo 20
    habito_exemplo = buscar_dados('c20_exemplo')
    if habito_exemplo != "[informação não preenchida]":
        texto += "## 🌿 CAPÍTULO 20: PEQUENOS HÁBITOS, GRANDES TRANSFORMAÇÕES\n\n"
        texto += f"{nome} descobriu que um pequeno hábito – {habito_exemplo} – podia trazer uma grande mudança. "
        dificuldade = buscar_dados('c20_dificuldade')
        if dificuldade != "[informação não preenchida]":
            texto += f"Mas manter a constância nem sempre é fácil: a maior dificuldade é {dificuldade}. "
        texto += "\n\n"

    # Capítulo 21
    sonho = buscar_dados('c21_sonho')
    plano = buscar_dados('c21_plano')
    if sonho != "[informação não preenchida]" or plano != "[informação não preenchida]":
        texto += "## 🔮 CAPÍTULO 21: SONHOS PARA O FUTURO\n\n"
        if sonho != "[informação não preenchida]":
            texto += f"Seu principal sonho é {sonho}. "
        if plano != "[informação não preenchida]":
            texto += f"Para realizá-lo, planeja {plano}. "
        texto += "\n\n"

    # Capítulo 1
    mudanca = buscar_dados('c1_mudanca')
    aprendizado_freq = buscar_dados('c1_aprendizado')
    reacao_desafio = buscar_dados('c1_reacao')
    if any(v != "[informação não preenchida]" for v in [mudanca, aprendizado_freq, reacao_desafio]):
        texto += "## 🧠 CAPÍTULO 1: O PODER DO APRENDIZADO CONTÍNUO\n\n"
        if mudanca == "Sim":
            texto += f"{nome} acredita que é possível mudar padrões de pensamento, e o hobby é prova disso. "
        if aprendizado_freq not in ["[informação não preenchida]", "Nunca"]:
            texto += f"Busca aprender algo novo {aprendizado_freq.lower()}, sempre em busca de evolução. "
        if "Persistir" in reacao_desafio:
            texto += f"Quando enfrenta desafios, persiste e busca novas estratégias – exatamente como faz ao praticar seu hobby. "
        texto += "\n\n"

    # Capítulo 26
    legado = buscar_dados('c26_legado')
    if legado != "[informação não preenchida]":
        texto += "## 💖 CAPÍTULO 26: O LEGADO QUE DEIXO\n\n"
        texto += f"{legado}\n\n"

    texto += "---\n"
    texto += "## PARA SEMPRE...\n\n"
    texto += f"A história de {nome} é feita de pequenos e grandes momentos, de hobbies que aquecem a alma e talentos que iluminam o caminho. Que esta biografia sirva como um lembrete de que cada passatempo, cada conquista e cada desafio são peças preciosas no mosaico da vida. Que venham muitos novos capítulos, repletos de criatividade, alegria e propósito!\n\n"
    texto += f"*Com admiração e carinho,\n{nome}*"

    return texto


def gerar_biografia_profissional():
    nome = buscar_dados('nome_autor', 'Autor Desconhecido').upper()
    data = datetime.now().strftime("%d/%m/%Y")

    texto = f"""# PERFIL PROFISSIONAL DE {nome}
## Trajetória, Competências e Realizações
*Gerado em {data}*

---

### APRESENTAÇÃO

**{nome}** é um profissional cuja trajetória reflete dedicação, aprendizado contínuo e busca por excelência. Ao longo dos anos, construiu uma carreira sólida, baseada em valores éticos e na paixão pelo que faz. Este perfil reúne as principais experiências, formações e competências que o(a) tornam um profissional diferenciado.

---
"""

    # Capítulo 10
    formacao = buscar_dados('c10_formacao')
    experiencias = buscar_dados('c10_experiencias')
    competencias = buscar_dados('c10_competencias')
    if any(v != "[informação não preenchida]" for v in [formacao, experiencias, competencias]):
        texto += "## 📚 CAPÍTULO 10: FORMAÇÃO E TRAJETÓRIA\n\n"
        if formacao != "[informação não preenchida]":
            texto += f"Sua formação inclui {formacao}. "
        if experiencias != "[informação não preenchida]":
            texto += f"Ao longo da carreira, viveu experiências marcantes como {experiencias}. "
        if competencias != "[informação não preenchida]":
            texto += f"Desenvolveu competências essenciais: {competencias}. "
        texto += "\n\n"

    # Capítulo 4
    talentos = buscar_dados('c4_talentos')
    autentico = buscar_dados('c4_autentico')
    if talentos != "[informação não preenchida]" or autentico != "[informação não preenchida]":
        texto += "## ✨ CAPÍTULO 4: TALENTOS QUE IMPULSIONAM A CARREIRA\n\n"
        if talentos != "[informação não preenchida]":
            texto += f"Seus três maiores talentos – {talentos} – são pilares de sua atuação profissional. "
        if autentico != "[informação não preenchida]":
            texto += f"Um momento em que se sentiu verdadeiramente autêntico(a) foi quando {autentico}. "
        texto += "\n\n"

    # Capítulo 4 (desafio) e Capítulo 6
    desafio = buscar_dados('c4_desafio')
    aprendizado = buscar_dados('c4_aprendizado')
    crise = buscar_dados('c6_crise')
    carater = buscar_dados('c6_carater')
    if any(v != "[informação não preenchida]" for v in [desafio, aprendizado, crise, carater]):
        texto += "## 🚀 CAPÍTULOS 4 E 6: SUPERAÇÃO E CARÁTER\n\n"
        if desafio != "[informação não preenchida]":
            texto += f"Um desafio significativo que superou foi {desafio}. "
        if aprendizado != "[informação não preenchida]":
            texto += f"Essa experiência ensinou que {aprendizado}. "
        if crise == "Sim":
            texto += "Em momentos de crise, sempre busca aprendizado. "
        if carater == "Sim":
            texto += "Acredita que suas decisões revelam seu caráter. "
        texto += "\n\n"

    # Capítulo 1
    mudanca = buscar_dados('c1_mudanca')
    freq_aprendizado = buscar_dados('c1_aprendizado')
    reacao = buscar_dados('c1_reacao')
    if any(v != "[informação não preenchida]" for v in [mudanca, freq_aprendizado, reacao]):
        texto += "## 🧠 CAPÍTULO 1: MINDSET E APRENDIZADO CONTÍNUO\n\n"
        if mudanca == "Sim":
            texto += f"{nome} acredita firmemente na capacidade de mudar padrões de pensamento. "
        if freq_aprendizado not in ["[informação não preenchida]", "Nunca"]:
            texto += f"Busca aprender algo novo {freq_aprendizado.lower()}. "
        if "Persistir" in reacao:
            texto += "Diante de desafios, persiste e busca novas estratégias. "
        texto += "\n\n"

    # Capítulo 7
    proativo = buscar_dados('c7_proativo')
    estagnacao = buscar_dados('c7_estagnacao')
    area_estagnacao = buscar_dados('c7_area')
    decisao_mudar = buscar_dados('c7_decisao')
    if any(v != "[informação não preenchida]" for v in [proativo, estagnacao, area_estagnacao, decisao_mudar]):
        texto += "## 🔄 CAPÍTULO 7: SITUAÇÃO ATUAL E IMPULSO PARA MUDANÇA\n\n"
        if proativo == "Sim":
            texto += "Considera-se uma pessoa proativa. "
        if estagnacao == "Sim" and area_estagnacao != "[informação não preenchida]":
            texto += f"Sente estagnação na área de {area_estagnacao}. "
        if decisao_mudar == "Sim":
            texto += "Acredita que chegou o momento de mudar. "
        elif decisao_mudar == "Ainda estou refletindo":
            texto += "Ainda reflete sobre o momento certo para mudar. "
        texto += "\n\n"

    # Capítulo 13
    procrastina = buscar_dados('c13_procrastina')
    tempo = buscar_dados('c13_tempo')
    mudanca_legado = buscar_dados('c13_mudanca')
    if any(v != "[informação não preenchida]" for v in [procrastina, tempo, mudanca_legado]):
        texto += "## 🏛️ CAPÍTULO 13: LEGADO E POSTURA PESSOAL\n\n"
        if procrastina == "Proativo(a)":
            texto += f"{nome} se considera mais proativo(a) do que procrastinador(a). "
        else:
            texto += "Reconhece que às vezes procrastina. "
        if tempo != "[informação não preenchida]":
            texto += f"O que costuma roubar seu tempo e energia: {tempo}. "
        if mudanca_legado != "[informação não preenchida]":
            texto += f"Sente que precisa mudar {mudanca_legado} para deixar um legado melhor. "
        texto += "\n\n"

    # Capítulo 18
    delega = buscar_dados('c18_delega')
    dificuldade_delegar = buscar_dados('c18_dificuldade')
    aprendizado_delegar = buscar_dados('c18_aprendizado')
    if any(v != "[informação não preenchida]" for v in [delega, dificuldade_delegar, aprendizado_delegar]):
        texto += "## 🤝 CAPÍTULO 18: TERCEIRIZAÇÃO E CONFIANÇA\n\n"
        if delega != "[informação não preenchida]":
            texto += f"Ao delegar tarefas, sente {delega.lower()}. "
        if dificuldade_delegar != "[informação não preenchida]":
            texto += f"Dificuldade em confiar: {dificuldade_delegar}. "
        if aprendizado_delegar != "[informação não preenchida]":
            texto += f"Aprendeu que {aprendizado_delegar}. "
        texto += "\n\n"

    # Capítulo 11
    etica = buscar_dados('c11_etica')
    contratacoes = buscar_dados('c11_contratacoes')
    criterios = buscar_dados('c11_criterios')
    if any(v != "[informação não preenchida]" for v in [etica, contratacoes, criterios]):
        texto += "## 📋 CAPÍTULO 11: TÉCNICAS DE SELEÇÃO E CRITÉRIOS\n\n"
        if etica == "Sim":
            texto += f"Para {nome}, ética é determinante em qualquer escolha importante. "
        if contratacoes != "[informação não preenchida]":
            texto += f"Considera contratar {contratacoes} para projetos. "
        if criterios != "[informação não preenchida]":
            texto += f"Critérios essenciais: {criterios}. "
        texto += "\n\n"

    # Capítulo 21
    sonho = buscar_dados('c21_sonho')
    plano = buscar_dados('c21_plano')
    if sonho != "[informação não preenchida]" or plano != "[informação não preenchida]":
        texto += "## 🔮 CAPÍTULO 21: VISÃO DE FUTURO\n\n"
        if sonho != "[informação não preenchida]":
            texto += f"Seu principal sonho profissional é {sonho}. "
        if plano != "[informação não preenchida]":
            texto += f"Para realizá-lo, planeja {plano}. "
        texto += "\n\n"

    # Capítulo 26
    legado = buscar_dados('c26_legado')
    if legado != "[informação não preenchida]":
        texto += "## 💬 CAPÍTULO 26: MENSAGEM DE LEGADO\n\n"
        texto += f"{legado}\n\n"

    # Capítulos 9 e 17
    publico = buscar_dados('c9_publico')
    por_que = buscar_dados('c9_por_que')
    impacto = buscar_dados('c9_reflexao')
    motivo = buscar_dados('c17_motivo')
    if any(v != "[informação não preenchida]" for v in [publico, por_que, impacto, motivo]):
        texto += "## ❤️ CAPÍTULOS 9 E 17: PROPÓSITO E MOTIVAÇÃO\n\n"
        if publico != "[informação não preenchida]":
            texto += f"Esta biografia é direcionada a {publico}. "
        if por_que != "[informação não preenchida]":
            texto += f"Deseja contar sua história para {por_que}. "
        if impacto != "[informação não preenchida]":
            texto += f"Espera causar o impacto: {impacto}. "
        if motivo != "[informação não preenchida]":
            texto += f"Sua maior motivação na vida é {motivo.lower()}. "
        texto += "\n\n"

    # Capítulos 23 e 25
    formato = buscar_dados('c23_formato')
    publicacao = buscar_dados('c23_publicacao')
    etapas_venda = buscar_dados('c25_vendas')
    if any(v != "[informação não preenchida]" for v in [formato, publicacao, etapas_venda]):
        texto += "## 📖 CAPÍTULOS 23 E 25: PUBLICAÇÃO E ALCANCE\n\n"
        if formato != "[informação não preenchida]":
            texto += f"Imagina sua biografia nos formatos: {formato}. "
        if publicacao != "[informação não preenchida]":
            texto += f"Pretende publicar de forma {publicacao.lower()}. "
        if etapas_venda != "[informação não preenchida]":
            texto += f"Planeja estruturar {etapas_venda}. "
        texto += "\n\n"

    # Capítulo 8
    celebra = buscar_dados('c8_celebra')
    motivo_celebra = buscar_dados('c8_motivo')
    if any(v != "[informação não preenchida]" for v in [celebra, motivo_celebra]):
        texto += "## 🎉 CAPÍTULO 8: COMEMORAÇÃO DE CONQUISTAS\n\n"
        if celebra != "[informação não preenchida]":
            texto += f"{nome} costuma celebrar pequenas vitórias {celebra.lower()}. "
        if motivo_celebra != "[informação não preenchida]":
            texto += f"A importância de comemorar: {motivo_celebra}. "
        texto += "\n\n"

    # Capítulo 12
    virada = buscar_dados('c12_virada')
    aprendeu_virada = buscar_dados('c12_aprendeu')
    if virada != "[informação não preenchida]":
        texto += "## 🌠 CAPÍTULO 12: MOMENTO DE VIRADA\n\n"
        texto += f"Um momento decisivo em sua vida foi {virada}. "
        if aprendeu_virada != "[informação não preenchida]":
            texto += f"Com ele, aprendeu que {aprendeu_virada}. "
        texto += "\n\n"

    texto += "---\n"
    texto += "## CONSIDERAÇÕES FINAIS\n\n"
    texto += f"A trajetória de {nome} é um exemplo de como a determinação, o aprendizado constante e a paixão pelo trabalho podem construir uma carreira significativa. Que este perfil sirva de inspiração e de registro para as futuras conquistas que ainda virão.\n\n"
    texto += f"*{nome}*"

    return texto


def gerar_biografia_infantil(genero):
    nome = buscar_dados('nome_autor', 'Autor Desconhecido')
    data = datetime.now().strftime("%d/%m/%Y")

    # Configuração de gênero e pronomes
    if genero == "Menina":
        artigo, sujeito, objeto, poss, art_def = "uma", "ela", "a", "sua", "a"
        personagem = "princesa"
    else:
        artigo, sujeito, objeto, poss, art_def = "um", "ele", "o", "seu", "o"
        personagem = "príncipe"

    texto = f"""# 🌈 A GRANDE JORNADA DE {nome.upper()}
## Uma história de descobertas, coragem e sonhos
*Gerado em {data}*

---

### 🌟 ERA UMA VEZ...

Era uma vez {artigo} {personagem} muito especial chamad{art_def} **{nome}**. {sujeito.capitalize()} vivia em um lugar onde cada dia era uma nova aventura, e {poss} coração batia no ritmo da curiosidade. {sujeito.capitalize()} adorava explorar, perguntar e aprender – e foi assim que {poss} história começou a ser escrita.

---

"""

    # Capítulo 1
    conteudo_c1 = ""
    mudanca = buscar_dados('c1_mudanca')
    if mudanca == "Sim":
        conteudo_c1 += f"{nome} descobriu que podia treinar {poss} mente para ficar mais forte a cada dia. "
    freq = buscar_dados('c1_aprendizado')
    if freq not in ["[informação não preenchida]", "Nunca"]:
        conteudo_c1 += f"{sujeito.capitalize()} adorava aprender coisas novas {freq.lower()}. "
    reacao = buscar_dados('c1_reacao')
    if "Persistir" in reacao:
        conteudo_c1 += f"Quando um desafio aparecia, {sujeito} não desistia: respirava fundo, pensava em uma nova ideia e tentava de novo. "
    if conteudo_c1:
        texto += "## 📖 CAPÍTULO 1: O PODER DE APRENDER\n\n"
        texto += f"No começo de {poss} jornada, {nome} já sabia que aprender era {artigo} aventura incrível. " + conteudo_c1 + "\n\n"

    # Capítulo 2
    conteudo_c2 = ""
    heranca = buscar_dados('c2_heranca')
    if "herdeiro" in heranca.lower():
        conteudo_c2 += f"{nome} sentia no coração que era filh{art_def} amad{art_def} do Rei do Universo, e isso {objeto} fazia muito especial. "
    desafios = buscar_dados('c2_desafios')
    if "oportunidade" in desafios.lower():
        conteudo_c2 += f"Os desafios, para {objeto}, eram como degraus para crescer e ficar mais forte. "
    if conteudo_c2:
        texto += "## 👑 CAPÍTULO 2: QUEM EU SOU DE VERDADE\n\n"
        texto += f"{nome} sabia que {poss} identidade era {artigo} joia rara. " + conteudo_c2 + "\n\n"

    # Capítulo 3
    conteudo_c3 = ""
    corpo = buscar_dados('c3_corpo')
    if corpo != "[informação não preenchida]":
        conteudo_c3 += f"{nome} cuidava de {poss} corpo com carinho, praticando {corpo.lower()}. "
    espirito = buscar_dados('c3_espirito')
    if espirito != "[informação não preenchida]":
        conteudo_c3 += f"Para fortalecer {poss} espírito, gostava de {espirito.lower()}. "
    if conteudo_c3:
        texto += "## ❤️ CAPÍTULO 3: CUIDANDO DO MEU TESOURO\n\n" + conteudo_c3 + "\n\n"

    # Capítulo 4
    conteudo_c4 = ""
    talentos = buscar_dados('c4_talentos')
    if talentos != "[informação não preenchida]":
        conteudo_c4 += f"Seus três maiores talentos eram {talentos}. "
    autentico = buscar_dados('c4_autentico')
    if autentico != "[informação não preenchida]":
        conteudo_c4 += f"Um dia, {sujeito} sentiu-se verdadeiramente feliz quando {autentico}. "
    if conteudo_c4:
        texto += "## ✨ CAPÍTULO 4: MEUS DONS ESPECIAIS\n\n" + conteudo_c4 + "\n\n"

    # Capítulo 5
    reflexao_c5 = buscar_dados('c5_reflexao')
    if reflexao_c5 != "[informação não preenchida]":
        texto += "## 🌍 CAPÍTULO 5: UMA HISTÓRIA PARA CONTAR\n\n"
        texto += f"{nome} acreditava que {poss} história merecia ser contada porque {reflexao_c5}.\n\n"

    # Capítulo 8
    memoria_c8 = buscar_dados('c8_memoria')
    if memoria_c8 != "[informação não preenchida]":
        texto += "## 🏆 CAPÍTULO 8: CONQUISTAS MARCANTES\n\n"
        texto += f"Uma conquista que marcou {poss} vida foi {memoria_c8}. "
        aprendizado_c8 = buscar_dados('c8_aprendizado')
        if aprendizado_c8 != "[informação não preenchida]":
            texto += f"Com ela, aprendeu que {aprendizado_c8}. "
        texto += "\n\n"

    # Capítulo 12
    virada_c12 = buscar_dados('c12_virada')
    if virada_c12 != "[informação não preenchida]":
        texto += "## 🚀 CAPÍTULO 12: MOMENTO DE VIRADA\n\n"
        texto += f"Um dia, algo especial aconteceu: {virada_c12}. "
        aprendeu_c12 = buscar_dados('c12_aprendeu')
        if aprendeu_c12 != "[informação não preenchida]":
            texto += f"Esse momento ensinou {objeto} que {aprendeu_c12}. "
        texto += "\n\n"

    # Capítulo 14
    hobby = buscar_dados('c14_hobby')
    if hobby != "[informação não preenchida]":
        texto += "## 🎨 CAPÍTULO 14: MEU HOBBY FAVORITO\n\n"
        texto += f"{nome} adorava {hobby}. "
        origem = buscar_dados('c14_origem')
        if origem != "[informação não preenchida]":
            texto += f"Essa paixão começou {origem}. "
        paz = buscar_dados('c14_paz')
        if paz != "[informação não preenchida]":
            texto += f"Em um momento difícil, essa atividade trouxe paz: \"{paz}\". "
        frase = buscar_dados('c14_frase_capa')
        if frase != "[informação não preenchida]":
            texto += f"Se fosse resumir em uma frase: \"{frase}\". "
        texto += "\n\n"

    # Capítulo 15
    papeis = buscar_dados('c15_escolhidos')
    if papeis != "[informação não preenchida]":
        texto += "## 👨‍👩‍👧 CAPÍTULO 15: PESSOAS IMPORTANTES\n\n"
        texto += f"Na vida, {nome} exercia papéis especiais: {papeis.lower()}. Cada um {objeto} ajudava a ser quem {sujeito} era.\n\n"

    # Capítulo 16
    virtudes = buscar_dados('c16_virtudes')
    if virtudes != "[informação não preenchida]":
        texto += "## 💎 CAPÍTULO 16: VIRTUDES QUE BRILHAM\n\n"
        texto += f"Seu coração guardava virtudes como {virtudes.lower()}. "
        exemplo = buscar_dados('c16_exemplo')
        if exemplo != "[informação não preenchida]":
            texto += f"Certa vez, {exemplo}. "
        texto += "\n\n"

    # Capítulo 17
    motivo = buscar_dados('c17_motivo')
    if motivo != "[informação não preenchida]":
        texto += "## 🌟 CAPÍTULO 17: O QUE MOVE MEU CORAÇÃO\n\n"
        texto += f"O que mais motivava {nome} era {motivo.lower()}. Isso guiava {poss} caminho todos os dias.\n\n"

    # Capítulo 19
    infancia = buscar_dados('c19_infancia')
    adolescencia = buscar_dados('c19_adolescencia')
    if infancia != "[informação não preenchida]" or adolescencia != "[informação não preenchida]":
        texto += "## 🌱 CAPÍTULO 19: AS FASES DA INFÂNCIA\n\n"
        if infancia != "[informação não preenchida]":
            texto += f"Quando era bebê, {nome} brincava de {infancia}. "
        if adolescencia != "[informação não preenchida]":
            texto += f"Na infância, {adolescencia}. "
        texto += "\n\n"

    # Capítulo 20
    habito_ex = buscar_dados('c20_exemplo')
    if habito_ex != "[informação não preenchida]":
        texto += "## 🌿 CAPÍTULO 20: PEQUENOS HÁBITOS, GRANDES MUDANÇAS\n\n"
        texto += f"{nome} descobriu que {artigo} pequena atitude – {habito_ex} – podia trazer {artigo} grande transformação.\n\n"

    # Capítulo 21
    sonho = buscar_dados('c21_sonho')
    plano = buscar_dados('c21_plano')
    if sonho != "[informação não preenchida]" or plano != "[informação não preenchida]":
        texto += "## 🔮 CAPÍTULO 21: SONHOS PARA O FUTURO\n\n"
        if sonho != "[informação não preenchida]":
            texto += f"Seu maior sonho era {sonho}. "
        if plano != "[informação não preenchida]":
            texto += f"Para realizá-lo, planejava {plano}. "
        texto += "\n\n"

    # Capítulo 26
    legado = buscar_dados('c26_legado')
    if legado != "[informação não preenchida]":
        texto += "## 💖 MENSAGEM FINAL\n\n"
        texto += f"{legado}\n\n"

    texto += "---\n"
    texto += f"## 🌈 A JORNADA CONTINUA...\n\n"
    texto += f"Esta é {artigo} história de {nome}, {artigo} {personagem} que nos ensina que, com fé, coragem e amor, cada um de nós pode escrever {artigo} história tão especial quanto a {poss}.\n\n"
    texto += f"*Fim (por enquanto…) – Com carinho para {nome}*"

    return texto

# ==================================================
# BARRA LATERAL COM SELEÇÃO DE ESTILO E BOTÃO ÚNICO
# ==================================================
with st.sidebar:
    st.markdown("---")
    st.header("📖 Gerar livro")

    estilo = st.selectbox(
        "Escolha o estilo da narrativa:",
        ["Hobby / Passatempo", "Profissional", "Infantil"]
    )

    genero = None
    if estilo == "Infantil":
        genero = st.radio("Gênero da criança:", ["Menina", "Menino"])

    if st.button("Gerar biografia", type="primary"):
        if estilo == "Hobby / Passatempo":
            st.session_state.livro_gerado = gerar_biografia_hobby()
        elif estilo == "Profissional":
            st.session_state.livro_gerado = gerar_biografia_profissional()
        else:  # Infantil
            if genero is None:
                genero = "Menina"  # fallback, mas nunca deve acontecer
            st.session_state.livro_gerado = gerar_biografia_infantil(genero)
        st.success("Biografia gerada! Vá para a aba '📖 Livro Gerado'.")

# ==================================================
# ABA DO LIVRO GERADO
# ==================================================
with tab_d:
    st.header("Sua Biografia")
    if st.session_state.livro_gerado:
        st.markdown(st.session_state.livro_gerado)
        st.download_button(
            label="📥 Baixar biografia",
            data=st.session_state.livro_gerado,
            file_name=f"biografia_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )
    else:
        st.info("Clique no botão na barra lateral para gerar sua biografia.")























