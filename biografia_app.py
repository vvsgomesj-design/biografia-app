import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Biografia App", layout="wide")
st.title("📘 Minha Biografia")

# Inicializa o estado para o livro gerado
if 'livro_gerado' not in st.session_state:
    st.session_state.livro_gerado = ""

# Criação das abas
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

    # ==================================================
    # CAPÍTULO 1 – NEUROPLASTICIDADE E MINDSET
    # ==================================================
    with st.expander("Cap. 1 – Neuroplasticidade e Mudança de Mindset"):
        c1_mudanca = st.radio(
            "Você acredita que é possível mudar padrões de pensamento?",
            ["Sim", "Não", "Não tenho certeza"],
            key="c1_mudanca"
        )

        c1_aprendizado = st.selectbox(
            "Com que frequência você busca aprender algo novo?",
            ["Diariamente", "Semanalmente", "Raramente", "Nunca"],
            key="c1_aprendizado"
        )

        c1_reacao = st.radio(
            "Quando enfrenta um desafio, você tende a:",
            [
                "Desistir facilmente",
                "Persistir e buscar novas estratégias",
                "Esperar que alguém resolva"
            ],
            key="c1_reacao"
        )

        c1_habitos = st.radio(
            "Você já percebeu mudanças positivas após criar novos hábitos?",
            ["Sim", "Não", "Ainda estou tentando"],
            key="c1_habitos"
        )

        c1_motiva = st.text_input("Em uma palavra, o que mais te motiva a mudar?", key="c1_motiva")

        c1_renovar = st.text_area("O que significa para você 'renovar a mente'?", key="c1_renovar")

    # ==================================================
    # CAPÍTULO 2 – IDENTIDADE EM CRISTO (HERDEIRO)
    # ==================================================
    with st.expander("Cap. 2 – Identidade em Cristo e Herança"):
        c2_heranca = st.radio(
            "Como você se vê em relação à herança espiritual?",
            [
                "Sinto-me herdeiro(a) de Deus",
                "Às vezes me esqueço",
                "Ainda não compreendo"
            ],
            key="c2_heranca"
        )

        c2_desafios = st.radio(
            "Como você costuma encarar os desafios da vida?",
            [
                "Como oportunidade de crescimento",
                "Com medo ou insegurança",
                "Com dificuldade de enxergar propósito"
            ],
            key="c2_desafios"
        )

        c2_promessas = st.radio(
            "Qual sua relação com as promessas bíblicas?",
            [
                "Conheço e procuro viver",
                "Conheço, mas não aplico sempre",
                "Não costumo refletir sobre isso"
            ],
            key="c2_promessas"
        )

        c2_eternidade = st.radio(
            "Você pensa no seu futuro eterno?",
            ["Sim, com convicção", "Às vezes", "Raramente"],
            key="c2_eternidade"
        )

        c2_reflexao = st.text_area(
            "De que forma seus desafios revelam sua identidade e herança?",
            key="c2_reflexao"
        )

    # ==================================================
    # CAPÍTULO 3 – ORGANIZAÇÃO (CORPO E ESPÍRITO)
    # ==================================================
    with st.expander("Cap. 3 – Organização do Corpo e do Espírito"):
        c3_corpo = st.multiselect(
            "Quais práticas você mantém para cuidar do corpo?",
            [
                "Rotina diária",
                "Atividade física",
                "Alimentação equilibrada",
                "Sono regulado",
                "Disciplina"
            ],
            key="c3_corpo"
        )

        c3_espirito = st.multiselect(
            "Quais práticas fortalecem seu espírito?",
            [
                "Oração",
                "Meditação",
                "Leitura espiritual",
                "Intuição",
                "Paz com propósito"
            ],
            key="c3_espirito"
        )

        c3_equilibrio = st.text_area(
            "Como você percebe o equilíbrio (ou desequilíbrio) entre corpo e espírito?",
            key="c3_equilibrio"
        )

    # ==================================================
    # CAPÍTULO 4 – POSIÇÃO VERTICAL E HORIZONTAL
    # ==================================================
    with st.expander("Cap. 4 – Autoconhecimento e Posição na Vida"):
        c4_autentico = st.text_area(
            "Descreva um momento em que você se sentiu verdadeiramente autêntico(a):",
            key="c4_autentico"
        )

        c4_talentos = st.text_input("Quais são seus três maiores talentos?", key="c4_talentos")

        c4_desafio = st.text_area("Relate um desafio significativo que você superou:", key="c4_desafio")

        c4_aprendizado = st.text_area(
            "O que esse desafio te ensinou sobre você mesmo(a)?",
            key="c4_aprendizado"
        )

    # ==================================================
    # CAPÍTULO 5 – POSIÇÃO LOCAL, REGIONAL E INTERNACIONAL
    # ==================================================
    with st.expander("Cap. 5 – Alcance da Sua História"):
        c5_local = st.radio(
            "Você acredita que sua história impacta pessoas ao seu redor?",
            ["Sim", "Não"],
            key="c5_local"
        )

        c5_regional = st.radio(
            "Você acredita que sua trajetória pode inspirar pessoas fora do seu círculo?",
            ["Sim", "Não"],
            key="c5_regional"
        )

        c5_internacional = st.radio(
            "Você acredita que sua história pode inspirar diferentes culturas ou países?",
            ["Sim", "Não"],
            key="c5_internacional"
        )

        c5_reflexao = st.text_area(
            "Por que você acredita que sua história merece ser contada?",
            key="c5_reflexao"
        )

    # ==================================================
    # CAPÍTULO 6 – POSIÇÃO CONFORME A BÍBLIA
    # ==================================================
    with st.expander("Cap. 6 – Posição Conforme a Bíblia"):
        c6_crise = st.radio(
            "Em momentos de crise, você costuma buscar aprendizado?",
            ["Sim", "Não", "Às vezes"],
            key="c6_crise"
        )

        c6_carater = st.radio(
            "Você acredita que suas decisões revelam seu caráter?",
            ["Sim", "Não"],
            key="c6_carater"
        )

        c6_emocoes = st.radio(
            "Você presta atenção às suas emoções antes de agir?",
            ["Sim", "Não", "Raramente"],
            key="c6_emocoes"
        )

        c6_arrependimento = st.radio(
            "Você pratica arrependimento como mudança real de atitude?",
            ["Sim", "Não", "Ainda estou aprendendo"],
            key="c6_arrependimento"
        )

        c6_fidelidade = st.radio(
            "Você se mantém fiel aos seus compromissos mesmo quando ninguém está olhando?",
            ["Sim", "Não"],
            key="c6_fidelidade"
        )

        c6_reflexao = st.text_area(
            "Como os princípios bíblicos influenciam suas decisões diárias?",
            key="c6_reflexao"
        )

    # ==================================================
    # CAPÍTULO 7 – SITUAÇÃO ATUAL (TRAMPOLIM)
    # ==================================================
    with st.expander("Cap. 7 – Situação Atual e Impulso para o Trampolim"):
        c7_proativo = st.radio(
            "Você se considera uma pessoa proativa?",
            ["Sim", "Não"],
            key="c7_proativo"
        )

        c7_estagnacao = st.radio(
            "Você sente que está estagnado(a) em alguma área da vida?",
            ["Sim", "Não"],
            key="c7_estagnacao"
        )

        c7_area = st.text_input(
            "Se sim, em qual área você sente maior estagnação?",
            key="c7_area"
        )

        c7_decisao = st.radio(
            "Você sente que chegou o momento de mudar?",
            ["Sim", "Não", "Ainda estou refletindo"],
            key="c7_decisao"
        )

        c7_reflexao = st.text_area(
            "O que hoje funciona como trampolim para o seu próximo nível?",
            key="c7_reflexao"
        )

    # ==================================================
    # CAPÍTULO 8 – COMEMORAÇÃO E MARCOS
    # ==================================================
    with st.expander("Cap. 8 – Comemoração e Reconhecimento de Conquistas"):
        c8_celebra = st.selectbox(
            "Você costuma celebrar pequenas vitórias?",
            ["Sempre", "Às vezes", "Raramente", "Nunca"],
            key="c8_celebra"
        )

        c8_motivo = st.radio(
            "Por que você acha importante (ou difícil) comemorar conquistas?",
            [
                "Reconhece o esforço",
                "Evita frustração",
                "Nunca parei para pensar",
                "Tenho dificuldade em comemorar"
            ],
            key="c8_motivo"
        )

        c8_memoria = st.text_area("Descreva uma conquista que marcou sua vida:", key="c8_memoria")

        c8_aprendizado = st.text_area("O que essa conquista te ensinou?", key="c8_aprendizado")

    # ==================================================
    # CAPÍTULO 9 – PRA QUEM, POR QUÊ E COMO
    # ==================================================
    with st.expander("Cap. 9 – Público, Propósito e Forma"):
        c9_publico = st.multiselect(
            "Para quem esta biografia é direcionada?",
            ["Família", "Amigos", "Estudantes", "Líderes", "Público em geral"],
            key="c9_publico"
        )

        c9_por_que = st.multiselect(
            "Por que você deseja contar sua história?",
            [
                "Inspirar pessoas",
                "Registrar minha trajetória",
                "Ensinar aprendizados",
                "Curar feridas",
                "Deixar legado"
            ],
            key="c9_por_que"
        )

        c9_como = st.multiselect(
            "Como você gostaria que sua história fosse sentida pelo leitor?",
            ["Acolhedora", "Inspiradora", "Realista", "Transformadora", "Leve"],
            key="c9_como"
        )

        c9_reflexao = st.text_area(
            "Qual impacto você espera causar em quem ler sua biografia?",
            key="c9_reflexao"
        )

    # ==================================================
    # CAPÍTULO 10 – ANÁLISE CURRICULAR E HISTÓRICO
    # ==================================================
    with st.expander("Cap. 10 – Análise Curricular e Experiências"):
        c10_formacao = st.text_area(
            "Formações acadêmicas, cursos ou treinamentos relevantes:",
            key="c10_formacao"
        )

        c10_experiencias = st.text_area(
            "Experiências profissionais ou ministeriais marcantes:",
            key="c10_experiencias"
        )

        c10_competencias = st.text_area(
            "Quais competências você desenvolveu ao longo da vida?",
            key="c10_competencias"
        )

        c10_reflexao = st.text_area(
            "Como sua trajetória prepara você para o futuro?",
            key="c10_reflexao"
        )

# ==================================================
# BLOCO B – CAPÍTULOS 11 A 20
# ==================================================
with tab_b:
    st.header("Bloco B: Seleção, Legado, Talento e Relações")

    # ==================================================
    # CAPÍTULO 11 – TÉCNICAS DE SELEÇÃO
    # ==================================================
    with st.expander("Cap. 11 – Técnicas de Seleção e Critérios"):
        c11_etica = st.radio(
            "Para você, ética é determinante em qualquer escolha importante?",
            ["Sim", "Não"],
            key="c11_etica"
        )

        c11_contratacoes = st.multiselect(
            "Você considera contratar apoio para este projeto?",
            ["Editora", "Ghost Writer", "Designer", "Gráfica", "Nenhum"],
            key="c11_contratacoes"
        )

        c11_criterios = st.text_area(
            "Quais critérios você considera essenciais ao selecionar pessoas ou projetos?",
            key="c11_criterios"
        )

    # ==================================================
    # CAPÍTULO 12 – TÉCNICAS DE TREINAMENTO
    # ==================================================
    with st.expander("Cap. 12 – Treinamento, Aprendizado e Virada"):
        c12_virada = st.text_area("Descreva um momento decisivo de virada na sua vida:", key="c12_virada")

        c12_aprendeu = st.text_area("O que esse momento te ensinou?", key="c12_aprendeu")

        c12_aplicacao = st.radio(
            "Você costuma aplicar rapidamente o que aprende?",
            ["Sim", "Não", "Depende da situação"],
            key="c12_aplicacao"
        )

    # ==================================================
    # CAPÍTULO 13 – LEGADO
    # ==================================================
    with st.expander("Cap. 13 – Legado e Postura Pessoal"):
        c13_procrastina = st.radio(
            "Você se considera mais proativo(a) ou procrastinador(a)?",
            ["Proativo(a)", "Procrastinador(a)"],
            key="c13_procrastina"
        )

        c13_tempo = st.text_area("O que costuma roubar seu tempo e energia?", key="c13_tempo")

        c13_mudanca = st.text_area(
            "O que você sente que precisa mudar para deixar um legado melhor?",
            key="c13_mudanca"
        )

    # ==================================================
    # CAPÍTULO 14 – TALENTO E HOBBY
    # ==================================================
    with st.expander("Cap. 14 – Talento, Hobby e Fonte de Paz"):
        c14_hobby = st.text_input("Qual talento ou hobby faz parte da sua história?", key="c14_hobby")

        c14_origem = st.text_area(
            "Como esse talento ou hobby surgiu e quem te influenciou?",
            key="c14_origem"
        )

        c14_paz = st.text_area(
            "Relate um momento em que esse hobby trouxe paz, cura ou alegria:",
            key="c14_paz"
        )

        c14_frase_capa = st.text_input(
            "Crie uma frase curta sobre esse talento para a capa do livro:",
            key="c14_frase_capa"
        )

    # ==================================================
    # CAPÍTULO 15 – POSIÇÃO SOCIAL E RELACIONAL
    # ==================================================
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

        c15_escolhidos = st.multiselect(
            "Quais papéis você exerce hoje em sua vida?",
            papeis_list,
            key="c15_escolhidos"
        )

        c15_reflexao = st.text_area("Como esses papéis influenciam quem você é?", key="c15_reflexao")

    # ==================================================
    # CAPÍTULO 16 – VIRTUDES
    # ==================================================
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

        c16_virtudes = st.multiselect(
            "Quais virtudes você reconhece em si ou deseja desenvolver?",
            virtudes_list,
            key="c16_virtudes"
        )

        c16_exemplo = st.text_area(
            "Cite uma situação em que uma virtude fez diferença na sua vida:",
            key="c16_exemplo"
        )

    # ==================================================
    # CAPÍTULO 17 – GALARDÃO
    # ==================================================
    with st.expander("Cap. 17 – Galardão e Motivação"):
        c17_motivo = st.radio(
            "O que mais te motiva na vida?",
            [
                "Agradar a Deus",
                "Ser reconhecido(a) pelas pessoas",
                "Deixar um legado",
                "Cumprir meu propósito"
            ],
            key="c17_motivo"
        )

        c17_reflexao = st.text_area(
            "Como essa motivação influencia suas decisões diárias?",
            key="c17_reflexao"
        )

    # ==================================================
    # CAPÍTULO 18 – TERCEIRIZAÇÃO
    # ==================================================
    with st.expander("Cap. 18 – Terceirização e Confiança"):
        c18_delega = st.selectbox(
            "Como você se sente ao delegar tarefas?",
            ["Alívio", "Insegurança", "Medo de perder o controle", "Entusiasmo"],
            key="c18_delega"
        )

        c18_dificuldade = st.text_area(
            "O que mais dificulta para você confiar tarefas a outras pessoas?",
            key="c18_dificuldade"
        )

        c18_aprendizado = st.text_area(
            "O que você já aprendeu ao delegar ou tentar fazer tudo sozinho(a)?",
            key="c18_aprendizado"
        )

    # ==================================================
    # CAPÍTULO 19 – FASES DA VIDA
    # ==================================================
    with st.expander("Cap. 19 – Fases da Vida"):
        c19_infancia = st.text_area(
            "Quais brincadeiras ou atividades marcaram sua infância ou o que vc fazia quando bebê se vc for criança?",
            key="c19_infancia"
        )

        c19_adolescencia = st.text_area("O que mais marcou sua adolescência ou o que vc faz na infância se vc for criança?", key="c19_adolescencia")

        c19_adulta = st.text_area("Qual foi (ou é) o auge da sua fase adulta?", key="c19_adulta")

        c19_aprendizado = st.text_area(
            "Que aprendizado cada fase da vida te trouxe?",
            key="c19_aprendizado"
        )

    # ==================================================
    # CAPÍTULO 20 – PEQUENAS AÇÕES E CONSTÂNCIA
    # ==================================================
    with st.expander("Cap. 20 – Pequenas Ações e Perseverança"):
        c20_habito = st.radio(
            "Você consegue manter um hábito por pelo menos 21 dias?",
            ["Sim", "Tentando", "Não"],
            key="c20_habito"
        )

        c20_exemplo = st.text_area("Cite um pequeno hábito que já trouxe grande mudança:", key="c20_exemplo")

        c20_dificuldade = st.text_area("O que mais dificulta sua constância?", key="c20_dificuldade")

# ==================================================
# BLOCO C – CAPÍTULOS 21 A 26
# ==================================================
with tab_c:
    st.header("Bloco C: Estrutura do Livro, Vendas e Experiência")

    # ==================================================
    # CAPÍTULO 21 – PLANEJAMENTO E VISÃO DE FUTURO
    # ==================================================
    with st.expander("Cap. 21 – Planejamento, Tempo e Futuro"):
        c21_foco = st.radio(
            "Você tende a viver mais focado em:",
            ["Passado", "Presente", "Futuro"],
            key="c21_foco"
        )

        c21_aprende = st.radio(
            "Você aprende mais com:",
            ["Erros", "Acertos", "Observando outras pessoas"],
            key="c21_aprende"
        )

        c21_sonho = st.text_area("Qual é o principal sonho ou objetivo para os próximos anos?", key="c21_sonho")

        c21_plano = st.text_area(
            "Que passos práticos você acredita que precisa dar a partir de agora?",
            key="c21_plano"
        )

    # ==================================================
    # CAPÍTULO 22 – FLUXOGRAMA EDITORIAL
    # ==================================================
    with st.expander("Cap. 22 – Estrutura e Fluxograma do Livro"):
        c22_elementos = st.multiselect(
            "Quais elementos você deseja incluir no livro?",
            [
                "Título com essência",
                "Capa profissional",
                "Orelhas / Sinopse",
                "Folha de rosto",
                "Epígrafe",
                "Dedicatória",
                "Sumário",
                "Corpo do texto",
                "Apêndices",
                "Fotos",
                "Ficha catalográfica",
                "QR Code com música",
                "Agradecimentos finais"
            ],
            key="c22_elementos"
        )

        c22_reflexao = st.text_area("Por que esses elementos são importantes para você?", key="c22_reflexao")

    # ==================================================
    # CAPÍTULO 23 – ORGANIZAÇÃO E DISTRIBUIÇÃO
    # ==================================================
    with st.expander("Cap. 23 – Organização e Distribuição"):
        c23_formato = st.multiselect(
            "Em quais formatos você imagina sua biografia?",
            [
                "Livro físico",
                "E-book (PDF)",
                "Audiobook",
                "Curso",
                "Material terapêutico",
                "Material ministerial"
            ],
            key="c23_formato"
        )

        c23_publicacao = st.radio(
            "Como você pretende publicar?",
            ["Independente", "Plataformas digitais", "Editoras", "Ainda não sei"],
            key="c23_publicacao"
        )

        c23_reflexao = st.text_area(
            "O que mais te anima (ou preocupa) sobre a publicação?",
            key="c23_reflexao"
        )

    # ==================================================
    # CAPÍTULO 24 – EXPERIÊNCIA VISUAL E APOIOS
    # ==================================================
    with st.expander("Cap. 24 – Experiência Visual e Apoios"):
        c24_mapas = st.radio(
            "Você deseja incluir mapas mentais ou esquemas visuais no livro?",
            ["Sim", "Não"],
            key="c24_mapas"
        )

        c24_estetica = st.text_area("Como você imagina a estética visual do livro?", key="c24_estetica")

        c24_apoios = st.multiselect(
            "Quais recursos visuais ou de apoio você gostaria de incluir?",
            [
                "Ilustrações",
                "Fotos pessoais",
                "Gráficos",
                "Checklists",
                "Exercícios práticos",
                "Espaço para anotações"
            ],
            key="c24_apoios"
        )

    # ==================================================
    # CAPÍTULO 25 – VENDA, DIVULGAÇÃO E ALCANCE
    # ==================================================
    with st.expander("Cap. 25 – Vendas, Divulgação e Alcance"):
        c25_vendas = st.multiselect(
            "Quais etapas de venda você pretende estruturar?",
            [
                "E-mail profissional",
                "Página de vendas",
                "Cadastro em plataforma (ex: Kiwify)",
                "Link na bio do Instagram",
                "Conteúdo de divulgação",
                "Renda passiva"
            ],
            key="c25_vendas"
        )

        c25_reflexao = st.text_area(
            "Como você imagina que esse livro pode alcançar pessoas?",
            key="c25_reflexao"
        )

    # ==================================================
    # CAPÍTULO 26 – EXPERIÊNCIA SINESTÉSICA E LEGADO FINAL
    # ==================================================
    with st.expander("Cap. 26 – Experiência Sinestésica e Legado"):
        c26_sinestesia = st.multiselect(
            "Quais sentidos você gostaria que seu livro despertasse?",
            [
                "Visão (design, marca-páginas)",
                "Tato (papel, textura)",
                "Olfato (aroma, memória afetiva)",
                "Audição (playlist, áudio)",
                "Paladar (brinde simbólico)",
                "Experiência de entrega (caixa especial)"
            ],
            key="c26_sinestesia"
        )

        c26_legado = st.text_area("Qual mensagem final você deseja deixar como legado?", key="c26_legado")

# ==================================================
# FUNÇÕES DE GERAÇÃO (VERSÃO ENRIQUECIDA)
# ==================================================

def get_safe(key, default=""):
    valor = st.session_state.get(key, default)
    if valor is None:
        return default
    if isinstance(default, list) and not isinstance(valor, list):
        return default
    if isinstance(default, str) and not isinstance(valor, str):
        return default
    return valor

def gerar_biografia_hobby():
    nome = get_safe('nome_autor', 'Autor Desconhecido')
    data = datetime.now().strftime("%d/%m/%Y")

    texto = f"""# OS PASSATEMPOS DE {nome.upper()}
## Uma Jornada de Descoberta, Paixão e Sentido
*Gerado em {data}*

---

### INTRODUÇÃO

Cada pessoa carrega dentro de si um universo particular de interesses e talentos. Para **{nome}**, os passatempos não são meras distrações; são verdadeiras fontes de vida, momentos em que a alma se reconecta consigo mesma e com o mundo de forma leve e autêntica. Nesta biografia, vamos mergulhar nesse universo e descobrir o que faz o coração de {nome} bater mais forte.

---

"""

    # --- CAPÍTULO 14: MEU HOBBY FAVORITO (origem e significado) ---
    hobby = get_safe('c14_hobby')
    if hobby:
        texto += "## 🌟 CAPÍTULO 14: MEU HOBBY FAVORITO\n\n"
        texto += f"O grande amor de {nome} é **{hobby}**. "
        origem = get_safe('c14_origem')
        if origem:
            texto += f"Essa paixão surgiu {origem}. "
        paz = get_safe('c14_paz')
        if paz:
            texto += f"Em momentos difíceis, essa atividade trouxe paz e alegria: \"{paz}\". "
        frase = get_safe('c14_frase_capa')
        if frase:
            texto += f"Se fosse resumir em uma frase: **\"{frase}\"**. "
        texto += "\n\n"

    # --- CAPÍTULO 4: TALENTOS E AUTENTICIDADE ---
    talentos = get_safe('c4_talentos')
    autentico = get_safe('c4_autentico')
    if talentos or autentico:
        texto += "## ✨ CAPÍTULO 4: TALENTOS QUE ME DEFINEM\n\n"
        if talentos:
            texto += f"Além do hobby, {nome} possui talentos especiais: {talentos}. "
        if autentico:
            texto += f"Um momento em que se sentiu verdadeiramente autêntico(a) foi quando {autentico}. "
        texto += "\n\n"

    # --- CAPÍTULO 8: CONQUISTAS MARCANTES (relacionadas ao hobby ou não) ---
    memoria = get_safe('c8_memoria')
    aprendizado_conquista = get_safe('c8_aprendizado')
    if memoria or aprendizado_conquista:
        texto += "## 🏆 CAPÍTULO 8: CONQUISTAS MARCANTES\n\n"
        if memoria:
            texto += f"Uma conquista inesquecível foi {memoria}. "
        if aprendizado_conquista:
            texto += f"Essa experiência ensinou que {aprendizado_conquista}. "
        texto += "\n\n"

    # --- CAPÍTULO 16: VIRTUDES QUE ILUMINAM O CAMINHO ---
    virtudes = get_safe('c16_virtudes')
    exemplo_virtude = get_safe('c16_exemplo')
    if virtudes or exemplo_virtude:
        texto += "## 💎 CAPÍTULO 16: VIRTUDES QUE ILUMINAM O CAMINHO\n\n"
        if virtudes:
            if isinstance(virtudes, list):
                virtudes_str = ", ".join(virtudes).lower()
            else:
                virtudes_str = str(virtudes).lower()
            texto += f"Ao longo da vida, {nome} cultivou virtudes como {virtudes_str}. "
        if exemplo_virtude:
            texto += f"Certa vez, {exemplo_virtude}. "
        texto += "\n\n"

    # --- CAPÍTULO 19: FASES DA VIDA E A RELAÇÃO COM O HOBBY ---
    infancia = get_safe('c19_infancia')
    adolescencia = get_safe('c19_adolescencia')
    adulta = get_safe('c19_adulta')
    if infancia or adolescencia or adulta:
        texto += "## 🌱 CAPÍTULO 19: O HOBBY AO LONGO DAS FASES DA VIDA\n\n"
        if infancia:
            texto += f"Na infância, {nome} já demonstrava interesse por {infancia}. "
        if adolescencia:
            texto += f"Na adolescência, {adolescencia}. "
        if adulta:
            texto += f"Na fase adulta, {adulta}. "
        texto += "Essas experiências foram moldando sua relação com o hobby e consigo mesmo.\n\n"

    # --- CAPÍTULO 20: PEQUENOS HÁBITOS, GRANDES TRANSFORMAÇÕES ---
    habito_exemplo = get_safe('c20_exemplo')
    if habito_exemplo:
        texto += "## 🌿 CAPÍTULO 20: PEQUENOS HÁBITOS, GRANDES TRANSFORMAÇÕES\n\n"
        texto += f"{nome} descobriu que um pequeno hábito – {habito_exemplo} – podia trazer uma grande mudança. "
        dificuldade = get_safe('c20_dificuldade')
        if dificuldade:
            texto += f"Mas manter a constância nem sempre é fácil: a maior dificuldade é {dificuldade}. "
        texto += "\n\n"

    # --- CAPÍTULO 21: SONHOS E PROJETOS FUTUROS (relacionados ao hobby) ---
    sonho = get_safe('c21_sonho')
    plano = get_safe('c21_plano')
    if sonho or plano:
        texto += "## 🔮 CAPÍTULO 21: SONHOS PARA O FUTURO\n\n"
        if sonho:
            texto += f"Seu principal sonho é {sonho}. "
        if plano:
            texto += f"Para realizá-lo, planeja {plano}. "
        texto += "\n\n"

    # --- CAPÍTULO 1: MINDSET E APRENDIZADO (como o hobby influencia o crescimento) ---
    mudanca = get_safe('c1_mudanca')
    aprendizado_freq = get_safe('c1_aprendizado')
    reacao_desafio = get_safe('c1_reacao')
    if mudanca or aprendizado_freq or reacao_desafio:
        texto += "## 🧠 CAPÍTULO 1: O PODER DO APRENDIZADO CONTÍNUO\n\n"
        if mudanca == "Sim":
            texto += f"{nome} acredita que é possível mudar padrões de pensamento, e o hobby é prova disso. "
        if aprendizado_freq and aprendizado_freq != "Nunca":
            texto += f"Busca aprender algo novo {aprendizado_freq.lower()}, sempre em busca de evolução. "
        if "Persistir" in str(reacao_desafio):
            texto += f"Quando enfrenta desafios, persiste e busca novas estratégias – exatamente como faz ao praticar seu hobby. "
        texto += "\n\n"

    # --- CAPÍTULO 26: LEGADO E MENSAGEM FINAL ---
    legado = get_safe('c26_legado')
    if legado:
        texto += "## 💖 CAPÍTULO 26: O LEGADO QUE DEIXO\n\n"
        texto += f"{legado}\n\n"

    # --- CONCLUSÃO ---
    texto += "---\n"
    texto += "## PARA SEMPRE...\n\n"
    texto += f"A história de {nome} é feita de pequenos e grandes momentos, de hobbies que aquecem a alma e talentos que iluminam o caminho. Que esta biografia sirva como um lembrete de que cada passatempo, cada conquista e cada desafio são peças preciosas no mosaico da vida. Que venham muitos novos capítulos, repletos de criatividade, alegria e propósito!\n\n"
    texto += f"*Com admiração e carinho,\n{nome}*"

    return texto


def gerar_biografia_profissional():
    nome = get_safe('nome_autor', 'Autor Desconhecido')
    data = datetime.now().strftime("%d/%m/%Y")

    texto = f"""# PERFIL PROFISSIONAL DE {nome.upper()}
## Trajetória, Competências e Realizações
*Gerado em {data}*

---

### APRESENTAÇÃO

**{nome}** é um profissional cuja trajetória reflete dedicação, aprendizado contínuo e busca por excelência. Ao longo dos anos, construiu uma carreira sólida, baseada em valores éticos e na paixão pelo que faz. Este perfil reúne as principais experiências, formações e competências que o(a) tornam um profissional diferenciado.

---
"""

    # --- CAPÍTULO 10: FORMAÇÃO E EXPERIÊNCIAS ---
    formacao = get_safe('c10_formacao')
    experiencias = get_safe('c10_experiencias')
    competencias = get_safe('c10_competencias')
    
    if formacao or experiencias or competencias:
        texto += "## 📚 CAPÍTULO 10: FORMAÇÃO E TRAJETÓRIA\n\n"
        if formacao:
            texto += f"Sua formação inclui {formacao}. "
        if experiencias:
            texto += f"Ao longo da carreira, viveu experiências marcantes como {experiencias}. "
        if competencias:
            texto += f"Desenvolveu competências essenciais: {competencias}. "
        texto += "\n\n"

    # --- CAPÍTULO 4: TALENTOS E AUTENTICIDADE (aplicados ao contexto profissional) ---
    talentos = get_safe('c4_talentos')
    autentico = get_safe('c4_autentico')
    if talentos or autentico:
        texto += "## ✨ CAPÍTULO 4: TALENTOS QUE IMPULSIONAM A CARREIRA\n\n"
        if talentos:
            texto += f"Seus três maiores talentos – {talentos} – são pilares de sua atuação profissional. "
        if autentico:
            texto += f"Um momento em que se sentiu verdadeiramente autêntico(a) foi quando {autentico}. "
        texto += "\n\n"

    # --- CAPÍTULO 4 (desafio) e CAPÍTULO 6: SUPERAÇÃO E CARÁTER ---
    desafio = get_safe('c4_desafio')
    aprendizado = get_safe('c4_aprendizado')
    crise = get_safe('c6_crise')
    carater = get_safe('c6_carater')
    
    if desafio or crise or carater:
        texto += "## 🚀 CAPÍTULOS 4 E 6: SUPERAÇÃO E CARÁTER\n\n"
        if desafio:
            texto += f"Um desafio significativo que superou foi {desafio}. "
        if aprendizado:
            texto += f"Essa experiência ensinou que {aprendizado}. "
        if crise == "Sim":
            texto += f"Em momentos de crise, sempre busca aprendizado. "
        if carater == "Sim":
            texto += f"Acredita que suas decisões revelam seu caráter. "
        texto += "\n\n"

    # --- CAPÍTULO 1: MINDSET E APRENDIZADO CONTÍNUO ---
    mudanca = get_safe('c1_mudanca')
    freq_aprendizado = get_safe('c1_aprendizado')
    reacao = get_safe('c1_reacao')
    if mudanca or freq_aprendizado or reacao:
        texto += "## 🧠 CAPÍTULO 1: MINDSET E APRENDIZADO CONTÍNUO\n\n"
        if mudanca == "Sim":
            texto += f"{nome} acredita firmemente na capacidade de mudar padrões de pensamento. "
        if freq_aprendizado and freq_aprendizado != "Nunca":
            texto += f"Busca aprender algo novo {freq_aprendizado.lower()}. "
        if "Persistir" in str(reacao):
            texto += f"Diante de desafios, persiste e busca novas estratégias. "
        texto += "\n\n"

    # --- CAPÍTULO 7: SITUAÇÃO ATUAL E PROATIVIDADE ---
    proativo = get_safe('c7_proativo')
    estagnacao = get_safe('c7_estagnacao')
    area_estagnacao = get_safe('c7_area')
    decisao_mudar = get_safe('c7_decisao')
    if proativo or estagnacao or decisao_mudar:
        texto += "## 🔄 CAPÍTULO 7: SITUAÇÃO ATUAL E IMPULSO PARA MUDANÇA\n\n"
        if proativo == "Sim":
            texto += f"Considera-se uma pessoa proativa. "
        if estagnacao == "Sim" and area_estagnacao:
            texto += f"Sente estagnação na área de {area_estagnacao}. "
        if decisao_mudar == "Sim":
            texto += f"Acredita que chegou o momento de mudar. "
        elif decisao_mudar == "Ainda estou refletindo":
            texto += f"Ainda reflete sobre o momento certo para mudar. "
        texto += "\n\n"

    # --- CAPÍTULO 13: LEGADO E POSTURA PESSOAL ---
    procrastina = get_safe('c13_procrastina')
    tempo = get_safe('c13_tempo')
    mudanca_legado = get_safe('c13_mudanca')
    if procrastina or tempo or mudanca_legado:
        texto += "## 🏛️ CAPÍTULO 13: LEGADO E POSTURA PESSOAL\n\n"
        if procrastina == "Proativo(a)":
            texto += f"{nome} se considera mais proativo(a) do que procrastinador(a). "
        else:
            texto += f"Reconhece que às vezes procrastina. "
        if tempo:
            texto += f"O que costuma roubar seu tempo e energia: {tempo}. "
        if mudanca_legado:
            texto += f"Sente que precisa mudar {mudanca_legado} para deixar um legado melhor. "
        texto += "\n\n"

    # --- CAPÍTULO 18: TERCEIRIZAÇÃO E TRABALHO EM EQUIPE ---
    delega = get_safe('c18_delega')
    dificuldade_delegar = get_safe('c18_dificuldade')
    aprendizado_delegar = get_safe('c18_aprendizado')
    if delega or dificuldade_delegar or aprendizado_delegar:
        texto += "## 🤝 CAPÍTULO 18: TERCEIRIZAÇÃO E CONFIANÇA\n\n"
        if delega:
            texto += f"Ao delegar tarefas, sente {delega.lower()}. "
        if dificuldade_delegar:
            texto += f"Dificuldade em confiar: {dificuldade_delegar}. "
        if aprendizado_delegar:
            texto += f"Aprendeu que {aprendizado_delegar}. "
        texto += "\n\n"

    # --- CAPÍTULO 11: TÉCNICAS DE SELEÇÃO E CRITÉRIOS (para projetos) ---
    etica = get_safe('c11_etica')
    contratacoes = get_safe('c11_contratacoes')
    criterios = get_safe('c11_criterios')
    if etica or contratacoes or criterios:
        texto += "## 📋 CAPÍTULO 11: TÉCNICAS DE SELEÇÃO E CRITÉRIOS\n\n"
        if etica == "Sim":
            texto += f"Para {nome}, ética é determinante em qualquer escolha importante. "
        if contratacoes:
            if isinstance(contratacoes, list):
                contratacoes_str = ", ".join(contratacoes)
            else:
                contratacoes_str = str(contratacoes)
            texto += f"Considera contratar {contratacoes_str} para projetos. "
        if criterios:
            texto += f"Critérios essenciais: {criterios}. "
        texto += "\n\n"

    # --- CAPÍTULO 21: VISÃO DE FUTURO ---
    sonho = get_safe('c21_sonho')
    plano = get_safe('c21_plano')
    if sonho or plano:
        texto += "## 🔮 CAPÍTULO 21: VISÃO DE FUTURO\n\n"
        if sonho:
            texto += f"Seu principal sonho profissional é {sonho}. "
        if plano:
            texto += f"Para realizá-lo, planeja {plano}. "
        texto += "\n\n"

    # --- CAPÍTULO 26: LEGADO FINAL ---
    legado = get_safe('c26_legado')
    if legado:
        texto += "## 💬 CAPÍTULO 26: MENSAGEM DE LEGADO\n\n"
        texto += f"{legado}\n\n"

    # --- CAPÍTULO 9 (propósito) e CAPÍTULO 17 (motivação) ---
    publico = get_safe('c9_publico')
    por_que = get_safe('c9_por_que')
    impacto = get_safe('c9_reflexao')
    motivo = get_safe('c17_motivo')
    if publico or por_que or impacto or motivo:
        texto += "## ❤️ CAPÍTULOS 9 E 17: PROPÓSITO E MOTIVAÇÃO\n\n"
        if publico:
            if isinstance(publico, list):
                publico_str = ", ".join(publico)
            else:
                publico_str = str(publico)
            texto += f"Esta biografia é direcionada a {publico_str}. "
        if por_que:
            if isinstance(por_que, list):
                por_que_str = ", ".join(por_que)
            else:
                por_que_str = str(por_que)
            texto += f"Deseja contar sua história para {por_que_str}. "
        if impacto:
            texto += f"Espera causar o impacto: {impacto}. "
        if motivo:
            texto += f"Sua maior motivação na vida é {motivo.lower()}. "
        texto += "\n\n"

    # --- CAPÍTULO 23 e 25: PUBLICAÇÃO E ALCANCE ---
    formato = get_safe('c23_formato')
    publicacao = get_safe('c23_publicacao')
    etapas_venda = get_safe('c25_vendas')
    if formato or publicacao or etapas_venda:
        texto += "## 📖 CAPÍTULOS 23 E 25: PUBLICAÇÃO E ALCANCE\n\n"
        if formato:
            if isinstance(formato, list):
                formato_str = ", ".join(formato)
            else:
                formato_str = str(formato)
            texto += f"Imagina sua biografia nos formatos: {formato_str}. "
        if publicacao:
            texto += f"Pretende publicar de forma {publicacao.lower()}. "
        if etapas_venda:
            if isinstance(etapas_venda, list):
                etapas_str = ", ".join(etapas_venda)
            else:
                etapas_str = str(etapas_venda)
            texto += f"Planeja estruturar {etapas_str}. "
        texto += "\n\n"

    # --- CAPÍTULO 8: COMEMORAÇÃO DE CONQUISTAS ---
    celebra = get_safe('c8_celebra')
    motivo_celebra = get_safe('c8_motivo')
    if celebra or motivo_celebra:
        texto += "## 🎉 CAPÍTULO 8: COMEMORAÇÃO DE CONQUISTAS\n\n"
        if celebra:
            texto += f"{nome} costuma celebrar pequenas vitórias {celebra.lower()}. "
        if motivo_celebra:
            texto += f"A importância de comemorar: {motivo_celebra}. "
        texto += "\n\n"

    # --- CAPÍTULO 12: MOMENTO DE VIRADA ---
    virada = get_safe('c12_virada')
    aprendeu_virada = get_safe('c12_aprendeu')
    if virada:
        texto += "## 🌠 CAPÍTULO 12: MOMENTO DE VIRADA\n\n"
        texto += f"Um momento decisivo em sua vida foi {virada}. "
        if aprendeu_virada:
            texto += f"Com ele, aprendeu que {aprendeu_virada}. "
        texto += "\n\n"

    # --- CAPÍTULO 16 (virtudes) já foi incluído? Vamos incluir de forma mais abrangente ---
    # (já incluímos no capítulo 16, mas podemos reforçar)
    # Para evitar duplicação, vou manter apenas o bloco acima.

    texto += "---\n"
    texto += "## CONSIDERAÇÕES FINAIS\n\n"
    texto += f"A trajetória de {nome} é um exemplo de como a determinação, o aprendizado constante e a paixão pelo trabalho podem construir uma carreira significativa. Que este perfil sirva de inspiração e de registro para as futuras conquistas que ainda virão.\n\n"
    texto += f"*{nome}*"

    return texto


def gerar_biografia_infantil(genero):
    nome = get_safe('nome_autor', 'Autor Desconhecido')
    data = datetime.now().strftime("%d/%m/%Y")

    # Configuração de gênero e pronomes
    if genero == "Menina":
        artigo, sujeito, objeto, poss, art_def = "uma", "ela", "a", "sua", "a"
        personagem = "princesa"
    else:
        artigo, sujeito, objeto, poss, art_def = "um", "ele", "o", "seu", "o"
        personagem = "príncipe"

    # Início da narrativa
    texto = f"""# 🌈 A GRANDE JORNADA DE {nome.upper()}
## Uma história de descobertas, coragem e sonhos
*Gerado em {data}*

---

### 🌟 ERA UMA VEZ...

Era uma vez {artigo} {personagem} muito especial chamad{art_def} **{nome}**. {sujeito.capitalize()} vivia em um lugar onde cada dia era uma nova aventura, e {poss} coração batia no ritmo da curiosidade. {sujeito.capitalize()} adorava explorar, perguntar e aprender – e foi assim que {poss} história começou a ser escrita.

---

"""

    # --- CAPÍTULO 1: O PODER DE APRENDER ---
    conteudo_c1 = ""
    mudanca = get_safe('c1_mudanca')
    if mudanca == "Sim":
        conteudo_c1 += f"{nome} descobriu que podia treinar {poss} mente para ficar mais forte a cada dia. "
    freq = get_safe('c1_aprendizado')
    if freq and freq != "Nunca":
        conteudo_c1 += f"{sujeito.capitalize()} adorava aprender coisas novas {freq.lower()}. "
    reacao = get_safe('c1_reacao')
    if "Persistir" in str(reacao):
        conteudo_c1 += f"Quando um desafio aparecia, {sujeito} não desistia: respirava fundo, pensava em uma nova ideia e tentava de novo. "

    if conteudo_c1:
        texto += "## 📖 CAPÍTULO 1: O PODER DE APRENDER\n\n"
        texto += f"No começo de {poss} jornada, {nome} já sabia que aprender era {artigo} aventura incrível. "
        texto += conteudo_c1 + "\n\n"

    # --- CAPÍTULO 2: QUEM EU SOU DE VERDADE ---
    conteudo_c2 = ""
    heranca = get_safe('c2_heranca')
    if "herdeiro" in str(heranca).lower():
        conteudo_c2 += f"{nome} sentia no coração que era filh{art_def} amad{art_def} do Rei do Universo, e isso {objeto} fazia muito especial. "
    desafios = get_safe('c2_desafios')
    if "oportunidade" in str(desafios).lower():
        conteudo_c2 += f"Os desafios, para {objeto}, eram como degraus para crescer e ficar mais forte. "

    if conteudo_c2:
        texto += "## 👑 CAPÍTULO 2: QUEM EU SOU DE VERDADE\n\n"
        texto += f"{nome} sabia que {poss} identidade era {artigo} joia rara. " + conteudo_c2 + "\n\n"

    # --- CAPÍTULO 3: CUIDANDO DO MEU TESOURO ---
    conteudo_c3 = ""
    corpo = get_safe('c3_corpo')
    if corpo:
        # converte lista em string amigável
        if isinstance(corpo, list):
            corpo_str = ", ".join(corpo).lower()
        else:
            corpo_str = str(corpo).lower()
        conteudo_c3 += f"{nome} cuidava de {poss} corpo com carinho, praticando {corpo_str}. "
    espirito = get_safe('c3_espirito')
    if espirito:
        if isinstance(espirito, list):
            espirito_str = ", ".join(espirito).lower()
        else:
            espirito_str = str(espirito).lower()
        conteudo_c3 += f"Para fortalecer {poss} espírito, gostava de {espirito_str}. "

    if conteudo_c3:
        texto += "## ❤️ CAPÍTULO 3: CUIDANDO DO MEU TESOURO\n\n"
        texto += conteudo_c3 + "\n\n"

    # --- CAPÍTULO 4: MEUS DONS ESPECIAIS ---
    conteudo_c4 = ""
    talentos = get_safe('c4_talentos')
    if talentos:
        conteudo_c4 += f"Seus três maiores talentos eram {talentos}. "
    autentico = get_safe('c4_autentico')
    if autentico:
        conteudo_c4 += f"Um dia, {sujeito} sentiu-se verdadeiramente feliz quando {autentico}. "

    if conteudo_c4:
        texto += "## ✨ CAPÍTULO 4: MEUS DONS ESPECIAIS\n\n"
        texto += conteudo_c4 + "\n\n"

    # --- CAPÍTULO 5: UMA HISTÓRIA PARA CONTAR ---
    reflexao_c5 = get_safe('c5_reflexao')
    if reflexao_c5:
        texto += "## 🌍 CAPÍTULO 5: UMA HISTÓRIA PARA CONTAR\n\n"
        texto += f"{nome} acreditava que {poss} história merecia ser contada porque {reflexao_c5}.\n\n"

    # --- CAPÍTULO 8: CONQUISTAS MARCANTES ---
    memoria_c8 = get_safe('c8_memoria')
    if memoria_c8:
        texto += "## 🏆 CAPÍTULO 8: CONQUISTAS MARCANTES\n\n"
        texto += f"Uma conquista que marcou {poss} vida foi {memoria_c8}. "
        aprendizado_c8 = get_safe('c8_aprendizado')
        if aprendizado_c8:
            texto += f"Com ela, aprendeu que {aprendizado_c8}. "
        texto += "\n\n"

    # --- CAPÍTULO 12: MOMENTO DE VIRADA ---
    virada_c12 = get_safe('c12_virada')
    if virada_c12:
        texto += "## 🚀 CAPÍTULO 12: MOMENTO DE VIRADA\n\n"
        texto += f"Um dia, algo especial aconteceu: {virada_c12}. "
        aprendeu_c12 = get_safe('c12_aprendeu')
        if aprendeu_c12:
            texto += f"Esse momento ensinou {objeto} que {aprendeu_c12}. "
        texto += "\n\n"

    # --- CAPÍTULO 14: MEU HOBBY FAVORITO ---
    hobby = get_safe('c14_hobby')
    if hobby:
        texto += "## 🎨 CAPÍTULO 14: MEU HOBBY FAVORITO\n\n"
        texto += f"{nome} adorava {hobby}. "
        origem = get_safe('c14_origem')
        if origem:
            texto += f"Essa paixão começou {origem}. "
        paz = get_safe('c14_paz')
        if paz:
            texto += f"Em um momento difícil, essa atividade trouxe paz: \"{paz}\". "
        frase = get_safe('c14_frase_capa')
        if frase:
            texto += f"Se fosse resumir em uma frase: \"{frase}\". "
        texto += "\n\n"

    # --- CAPÍTULO 15: PESSOAS IMPORTANTES ---
    papeis = get_safe('c15_escolhidos')
    if papeis:
        if isinstance(papeis, list):
            papeis_str = ", ".join(papeis).lower()
        else:
            papeis_str = str(papeis).lower()
        texto += "## 👨‍👩‍👧 CAPÍTULO 15: PESSOAS IMPORTANTES\n\n"
        texto += f"Na vida, {nome} exercia papéis especiais: {papeis_str}. Cada um {objeto} ajudava a ser quem {sujeito} era.\n\n"

    # --- CAPÍTULO 16: VIRTUDES QUE BRILHAM ---
    virtudes = get_safe('c16_virtudes')
    if virtudes:
        if isinstance(virtudes, list):
            virtudes_str = ", ".join(virtudes).lower()
        else:
            virtudes_str = str(virtudes).lower()
        texto += "## 💎 CAPÍTULO 16: VIRTUDES QUE BRILHAM\n\n"
        texto += f"Seu coração guardava virtudes como {virtudes_str}. "
        exemplo = get_safe('c16_exemplo')
        if exemplo:
            texto += f"Certa vez, {exemplo}. "
        texto += "\n\n"

    # --- CAPÍTULO 17: O QUE MOVE MEU CORAÇÃO ---
    motivo = get_safe('c17_motivo')
    if motivo:
        texto += "## 🌟 CAPÍTULO 17: O QUE MOVE MEU CORAÇÃO\n\n"
        texto += f"O que mais motivava {nome} era {motivo.lower()}. Isso guiava {poss} caminho todos os dias.\n\n"

    # --- CAPÍTULO 19: AS FASES DA infÂncia ---
    infancia = get_safe('c19_infancia')
    
    if bebê or criança:
        texto += "## 🌱 CAPÍTULO 19: AS FASES DA infância\n\n"
        if bebê:
            texto += f"quando era bebê, {nome} brincava de {infancia}. "
        if infância:
            texto += f"Na infância, {adolescência}. "
                texto += "\n\n"

    # --- CAPÍTULO 20: PEQUENOS HÁBITOS, GRANDES MUDANÇAS ---
    habito_ex = get_safe('c20_exemplo')
    if habito_ex:
        texto += "## 🌿 CAPÍTULO 20: PEQUENOS HÁBITOS, GRANDES MUDANÇAS\n\n"
        texto += f"{nome} descobriu que {artigo} pequena atitude – {habito_ex} – podia trazer {artigo} grande transformação.\n\n"

    # --- CAPÍTULO 21: SONHOS PARA O FUTURO ---
    sonho = get_safe('c21_sonho')
    plano = get_safe('c21_plano')
    if sonho or plano:
        texto += "## 🔮 CAPÍTULO 21: SONHOS PARA O FUTURO\n\n"
        if sonho:
            texto += f"Seu maior sonho era {sonho}. "
        if plano:
            texto += f"Para realizá-lo, planejava {plano}. "
        texto += "\n\n"

    # --- CAPÍTULO 26: MENSAGEM FINAL ---
    legado = get_safe('c26_legado')
    if legado:
        texto += "## 💖 MENSAGEM FINAL\n\n"
        texto += f"{legado}\n\n"

    # --- CONCLUSÃO ---
    texto += "---\n"
    texto += f"## 🌈 A JORNADA CONTINUA...\n\n"
    texto += f"Esta é {artigo} história de {nome}, {artigo} {personagem} que nos ensina que, com fé, coragem e amor, cada um de nós pode escrever {artigo} história tão especial quanto a {poss}.\n\n"
    texto += f"*Fim (por enquanto…) – Com carinho para {nome}*"

    return texto

# ==================================================
# BARRA LATERAL COM SELEÇÃO DE ESTILO
# ==================================================
st.sidebar.markdown("---")
st.sidebar.header("📖 Gerar livro")

estilo = st.sidebar.selectbox(
    "Escolha o estilo da narrativa:",
    ["Hobby / Passatempo", "Profissional", "Infantil"]
)

genero = None
if estilo == "Infantil":
    genero = st.sidebar.radio("Gênero da criança:", ["Menina", "Menino"])

if st.sidebar.button("Gerar biografia"):
    if estilo == "Hobby / Passatempo":
        st.session_state.livro_gerado = gerar_biografia_hobby()
    elif estilo == "Profissional":
        st.session_state.livro_gerado = gerar_biografia_profissional()
    else:
        st.session_state.livro_gerado = gerar_biografia_infantil(genero)
    st.sidebar.success("Biografia gerada! Vá para a aba '📖 Livro Gerado'.")

# ==================================================
# ABA DO LIVRO GERADO
# ==================================================
with tab_d:
    st.header("Minha Biografia")
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





















