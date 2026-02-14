import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Biografia App", layout="wide")
st.title("📘 Minha Biografia")

# Inicializa o estado para o livro gerado
if 'livro_gerado' not in st.session_state:
    st.session_state.livro_gerado = ""

# Criação das abas (deve vir antes de usar tab_a, tab_b...)
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

    nome_autor = st.text_input("Nome Completo:", "Autor Desconhecido")

    # ==================================================
    # CAPÍTULO 1 – NEUROPLASTICIDADE E MINDSET
    # ==================================================
    with st.expander("Cap. 1 – Neuroplasticidade e Mudança de Mindset"):
        c1_mudanca = st.radio(
            "Você acredita que é possível mudar padrões de pensamento?",
            ["Sim", "Não", "Não tenho certeza"]
        )

        c1_aprendizado = st.selectbox(
            "Com que frequência você busca aprender algo novo?",
            ["Diariamente", "Semanalmente", "Raramente", "Nunca"]
        )

        c1_reacao = st.radio(
            "Quando enfrenta um desafio, você tende a:",
            [
                "Desistir facilmente",
                "Persistir e buscar novas estratégias",
                "Esperar que alguém resolva"
            ]
        )

        c1_habitos = st.radio(
            "Você já percebeu mudanças positivas após criar novos hábitos?",
            ["Sim", "Não", "Ainda estou tentando"]
        )

        c1_motiva = st.text_input("Em uma palavra, o que mais te motiva a mudar?")

        c1_renovar = st.text_area("O que significa para você 'renovar a mente'?")

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
            ]
        )

        c2_desafios = st.radio(
            "Como você costuma encarar os desafios da vida?",
            [
                "Como oportunidade de crescimento",
                "Com medo ou insegurança",
                "Com dificuldade de enxergar propósito"
            ]
        )

        c2_promessas = st.radio(
            "Qual sua relação com as promessas bíblicas?",
            [
                "Conheço e procuro viver",
                "Conheço, mas não aplico sempre",
                "Não costumo refletir sobre isso"
            ]
        )

        c2_eternidade = st.radio(
            "Você pensa no seu futuro eterno?",
            ["Sim, com convicção", "Às vezes", "Raramente"]
        )

        c2_reflexao = st.text_area(
            "De que forma seus desafios revelam sua identidade e herança?"
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
            ]
        )

        c3_espirito = st.multiselect(
            "Quais práticas fortalecem seu espírito?",
            [
                "Oração",
                "Meditação",
                "Leitura espiritual",
                "Intuição",
                "Paz com propósito"
            ]
        )

        c3_equilibrio = st.text_area(
            "Como você percebe o equilíbrio (ou desequilíbrio) entre corpo e espírito?"
        )

    # ==================================================
    # CAPÍTULO 4 – POSIÇÃO VERTICAL E HORIZONTAL
    # ==================================================
    with st.expander("Cap. 4 – Autoconhecimento e Posição na Vida"):
        c4_autentico = st.text_area(
            "Descreva um momento em que você se sentiu verdadeiramente autêntico(a):"
        )

        c4_talentos = st.text_input("Quais são seus três maiores talentos?")

        c4_desafio = st.text_area("Relate um desafio significativo que você superou:")

        c4_aprendizado = st.text_area(
            "O que esse desafio te ensinou sobre você mesmo(a)?"
        )

    # ==================================================
    # CAPÍTULO 5 – POSIÇÃO LOCAL, REGIONAL E INTERNACIONAL
    # ==================================================
    with st.expander("Cap. 5 – Alcance da Sua História"):
        c5_local = st.radio(
            "Você acredita que sua história impacta pessoas ao seu redor?",
            ["Sim", "Não"]
        )

        c5_regional = st.radio(
            "Você acredita que sua trajetória pode inspirar pessoas fora do seu círculo?",
            ["Sim", "Não"]
        )

        c5_internacional = st.radio(
            "Você acredita que sua história pode inspirar diferentes culturas ou países?",
            ["Sim", "Não"]
        )

        c5_reflexao = st.text_area(
            "Por que você acredita que sua história merece ser contada?"
        )

    # ==================================================
    # CAPÍTULO 6 – POSIÇÃO CONFORME A BÍBLIA
    # ==================================================
    with st.expander("Cap. 6 – Posição Conforme a Bíblia"):
        c6_crise = st.radio(
            "Em momentos de crise, você costuma buscar aprendizado?",
            ["Sim", "Não", "Às vezes"]
        )

        c6_carater = st.radio(
            "Você acredita que suas decisões revelam seu caráter?",
            ["Sim", "Não"]
        )

        c6_emocoes = st.radio(
            "Você presta atenção às suas emoções antes de agir?",
            ["Sim", "Não", "Raramente"]
        )

        c6_arrependimento = st.radio(
            "Você pratica arrependimento como mudança real de atitude?",
            ["Sim", "Não", "Ainda estou aprendendo"]
        )

        c6_fidelidade = st.radio(
            "Você se mantém fiel aos seus compromissos mesmo quando ninguém está olhando?",
            ["Sim", "Não"]
        )

        c6_reflexao = st.text_area(
            "Como os princípios bíblicos influenciam suas decisões diárias?"
        )

    # ==================================================
    # CAPÍTULO 7 – SITUAÇÃO ATUAL (TRAMPOLIM)
    # ==================================================
    with st.expander("Cap. 7 – Situação Atual e Impulso para o Trampolim"):
        c7_proativo = st.radio(
            "Você se considera uma pessoa proativa?",
            ["Sim", "Não"]
        )

        c7_estagnacao = st.radio(
            "Você sente que está estagnado(a) em alguma área da vida?",
            ["Sim", "Não"]
        )

        c7_area = st.text_input(
            "Se sim, em qual área você sente maior estagnação?"
        )

        c7_decisao = st.radio(
            "Você sente que chegou o momento de mudar?",
            ["Sim", "Não", "Ainda estou refletindo"]
        )

        c7_reflexao = st.text_area(
            "O que hoje funciona como trampolim para o seu próximo nível?"
        )

    # ==================================================
    # CAPÍTULO 8 – COMEMORAÇÃO E MARCOS
    # ==================================================
    with st.expander("Cap. 8 – Comemoração e Reconhecimento de Conquistas"):
        c8_celebra = st.selectbox(
            "Você costuma celebrar pequenas vitórias?",
            ["Sempre", "Às vezes", "Raramente", "Nunca"]
        )

        c8_motivo = st.radio(
            "Por que você acha importante (ou difícil) comemorar conquistas?",
            [
                "Reconhece o esforço",
                "Evita frustração",
                "Nunca parei para pensar",
                "Tenho dificuldade em comemorar"
            ]
        )

        c8_memoria = st.text_area("Descreva uma conquista que marcou sua vida:")

        c8_aprendizado = st.text_area("O que essa conquista te ensinou?")

    # ==================================================
    # CAPÍTULO 9 – PRA QUEM, POR QUÊ E COMO
    # ==================================================
    with st.expander("Cap. 9 – Público, Propósito e Forma"):
        c9_publico = st.multiselect(
            "Para quem esta biografia é direcionada?",
            ["Família", "Amigos", "Estudantes", "Líderes", "Público em geral"]
        )

        c9_por_que = st.multiselect(
            "Por que você deseja contar sua história?",
            [
                "Inspirar pessoas",
                "Registrar minha trajetória",
                "Ensinar aprendizados",
                "Curar feridas",
                "Deixar legado"
            ]
        )

        c9_como = st.multiselect(
            "Como você gostaria que sua história fosse sentida pelo leitor?",
            ["Acolhedora", "Inspiradora", "Realista", "Transformadora", "Leve"]
        )

        c9_reflexao = st.text_area(
            "Qual impacto você espera causar em quem ler sua biografia?"
        )

    # ==================================================
    # CAPÍTULO 10 – ANÁLISE CURRICULAR E HISTÓRICO
    # ==================================================
    with st.expander("Cap. 10 – Análise Curricular e Experiências"):
        c10_formacao = st.text_area(
            "Formações acadêmicas, cursos ou treinamentos relevantes:"
        )

        c10_experiencias = st.text_area(
            "Experiências profissionais ou ministeriais marcantes:"
        )

        c10_competencias = st.text_area(
            "Quais competências você desenvolveu ao longo da vida?"
        )

        c10_reflexao = st.text_area(
            "Como sua trajetória prepara você para o futuro?"
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
            ["Sim", "Não"]
        )

        c11_contratacoes = st.multiselect(
            "Você considera contratar apoio para este projeto?",
            ["Editora", "Ghost Writer", "Designer", "Gráfica", "Nenhum"]
        )

        c11_criterios = st.text_area(
            "Quais critérios você considera essenciais ao selecionar pessoas ou projetos?"
        )

    # ==================================================
    # CAPÍTULO 12 – TÉCNICAS DE TREINAMENTO
    # ==================================================
    with st.expander("Cap. 12 – Treinamento, Aprendizado e Virada"):
        c12_virada = st.text_area("Descreva um momento decisivo de virada na sua vida:")

        c12_aprendeu = st.text_area("O que esse momento te ensinou?")

        c12_aplicacao = st.radio(
            "Você costuma aplicar rapidamente o que aprende?",
            ["Sim", "Não", "Depende da situação"]
        )

    # ==================================================
    # CAPÍTULO 13 – LEGADO
    # ==================================================
    with st.expander("Cap. 13 – Legado e Postura Pessoal"):
        c13_procrastina = st.radio(
            "Você se considera mais proativo(a) ou procrastinador(a)?",
            ["Proativo(a)", "Procrastinador(a)"]
        )

        c13_tempo = st.text_area("O que costuma roubar seu tempo e energia?")

        c13_mudanca = st.text_area(
            "O que você sente que precisa mudar para deixar um legado melhor?"
        )

    # ==================================================
    # CAPÍTULO 14 – TALENTO E HOBBY
    # ==================================================
    with st.expander("Cap. 14 – Talento, Hobby e Fonte de Paz"):
        c14_hobby = st.text_input("Qual talento ou hobby faz parte da sua história?")

        c14_origem = st.text_area(
            "Como esse talento ou hobby surgiu e quem te influenciou?"
        )

        c14_paz = st.text_area(
            "Relate um momento em que esse hobby trouxe paz, cura ou alegria:"
        )

        c14_frase_capa = st.text_input(
            "Crie uma frase curta sobre esse talento para a capa do livro:"
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
            papeis_list
        )

        c15_reflexao = st.text_area("Como esses papéis influenciam quem você é?")

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
            virtudes_list
        )

        c16_exemplo = st.text_area(
            "Cite uma situação em que uma virtude fez diferença na sua vida:"
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
            ]
        )

        c17_reflexao = st.text_area(
            "Como essa motivação influencia suas decisões diárias?"
        )

    # ==================================================
    # CAPÍTULO 18 – TERCEIRIZAÇÃO
    # ==================================================
    with st.expander("Cap. 18 – Terceirização e Confiança"):
        c18_delega = st.selectbox(
            "Como você se sente ao delegar tarefas?",
            ["Alívio", "Insegurança", "Medo de perder o controle", "Entusiasmo"]
        )

        c18_dificuldade = st.text_area(
            "O que mais dificulta para você confiar tarefas a outras pessoas?"
        )

        c18_aprendizado = st.text_area(
            "O que você já aprendeu ao delegar ou tentar fazer tudo sozinho(a)?"
        )

    # ==================================================
    # CAPÍTULO 19 – FASES DA VIDA
    # ==================================================
    with st.expander("Cap. 19 – Fases da Vida"):
        c19_infancia = st.text_area(
            "Quais brincadeiras ou atividades marcaram sua infância?"
        )

        c19_adolescencia = st.text_area("O que mais marcou sua adolescência?")

        c19_adulta = st.text_area("Qual foi (ou é) o auge da sua fase adulta?")

        c19_aprendizado = st.text_area(
            "Que aprendizado cada fase da vida te trouxe?"
        )

    # ==================================================
    # CAPÍTULO 20 – PEQUENAS AÇÕES E CONSTÂNCIA
    # ==================================================
    with st.expander("Cap. 20 – Pequenas Ações e Perseverança"):
        c20_habito = st.radio(
            "Você consegue manter um hábito por pelo menos 21 dias?",
            ["Sim", "Tentando", "Não"]
        )

        c20_exemplo = st.text_area("Cite um pequeno hábito que já trouxe grande mudança:")

        c20_dificuldade = st.text_area("O que mais dificulta sua constância?")

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
            ["Passado", "Presente", "Futuro"]
        )

        c21_aprende = st.radio(
            "Você aprende mais com:",
            ["Erros", "Acertos", "Observando outras pessoas"]
        )

        c21_sonho = st.text_area("Qual é o principal sonho ou objetivo para os próximos anos?")

        c21_plano = st.text_area(
            "Que passos práticos você acredita que precisa dar a partir de agora?"
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
            ]
        )

        c22_reflexao = st.text_area("Por que esses elementos são importantes para você?")

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
            ]
        )

        c23_publicacao = st.radio(
            "Como você pretende publicar?",
            ["Independente", "Plataformas digitais", "Editoras", "Ainda não sei"]
        )

        c23_reflexao = st.text_area(
            "O que mais te anima (ou preocupa) sobre a publicação?"
        )

    # ==================================================
    # CAPÍTULO 24 – EXPERIÊNCIA VISUAL E APOIOS
    # ==================================================
    with st.expander("Cap. 24 – Experiência Visual e Apoios"):
        c24_mapas = st.radio(
            "Você deseja incluir mapas mentais ou esquemas visuais no livro?",
            ["Sim", "Não"]
        )

        c24_estetica = st.text_area("Como você imagina a estética visual do livro?")

        c24_apoios = st.multiselect(
            "Quais recursos visuais ou de apoio você gostaria de incluir?",
            [
                "Ilustrações",
                "Fotos pessoais",
                "Gráficos",
                "Checklists",
                "Exercícios práticos",
                "Espaço para anotações"
            ]
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
            ]
        )

        c25_reflexao = st.text_area(
            "Como você imagina que esse livro pode alcançar pessoas?"
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
            ]
        )

        c26_legado = st.text_area("Qual mensagem final você deseja deixar como legado?")
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
## Uma Jornada de Descoberta e Prazer
*Gerado em {data}*

---

### INTRODUÇÃO

Cada um de nós carrega dentro de si um universo particular de interesses, talentos e paixões. Para **{nome}**, os passatempos não são meras distrações; são verdadeiras fontes de vida, momentos em que a alma se reconecta consigo mesma e com o mundo de forma leve e autêntica. Nesta biografia, vamos mergulhar nesse universo e descobrir o que faz o coração de {nome} bater mais forte.

---
"""

    # ---- CAPÍTULO 14: HOBBY PRINCIPAL ----
    conteudo_c14 = ""
    hobby = get_safe('c14_hobby')
    if hobby:
        conteudo_c14 += f"**{nome}** adora **{hobby}**. "
    origem = get_safe('c14_origem')
    if origem:
        conteudo_c14 += f"Essa paixão começou {origem}. "
    paz = get_safe('c14_paz')
    if paz:
        conteudo_c14 += f"Em um momento difícil, essa atividade trouxe paz: \"{paz}\". "
    frase = get_safe('c14_frase_capa')
    if frase:
        conteudo_c14 += f"Se fosse resumir em uma frase: **\"{frase}\"**. "

    if conteudo_c14:
        texto += "## 🌟 MEU HOBBY FAVORITO\n\n" + conteudo_c14 + "\n\n"

    # ---- CAPÍTULO 4: TALENTOS ----
    conteudo_c4 = ""
    talentos = get_safe('c4_talentos')
    if talentos:
        conteudo_c4 += f"Além do hobby, {nome} tem talentos especiais: {talentos}. "
    autentico = get_safe('c4_autentico')
    if autentico:
        conteudo_c4 += f"Um momento de autenticidade foi quando {autentico}. "
    desafio = get_safe('c4_desafio')
    if desafio:
        conteudo_c4 += f"Um desafio que enfrentou: {desafio}. "
    aprendizado = get_safe('c4_aprendizado')
    if aprendizado:
        conteudo_c4 += f"Com isso, aprendeu que {aprendizado}. "

    if conteudo_c4:
        texto += "## ✨ TALENTOS QUE BRILHAM\n\n" + conteudo_c4 + "\n\n"

    # ---- CAPÍTULO 19: FASES DA VIDA ----
    conteudo_c19 = ""
    infancia = get_safe('c19_infancia')
    adolescencia = get_safe('c19_adolescencia')
    adulta = get_safe('c19_adulta')
    if infancia:
        conteudo_c19 += f"Na infância, {infancia}. "
    if adolescencia:
        conteudo_c19 += f"Na adolescência, {adolescencia}. "
    if adulta:
        conteudo_c19 += f"Na vida adulta, {adulta}. "
    aprendizado_fases = get_safe('c19_aprendizado')
    if aprendizado_fases:
        conteudo_c19 += f"Cada fase trouxe o aprendizado: {aprendizado_fases}. "

    if conteudo_c19:
        texto += "## 🌱 AO LONGO DA VIDA\n\n" + conteudo_c19 + "\n\n"

    # ---- CAPÍTULO 8: CONQUISTAS MARCANTES ----
    conteudo_c8 = ""
    memoria = get_safe('c8_memoria')
    if memoria:
        conteudo_c8 += f"Uma conquista marcante: {memoria}. "
    aprendizado_conquista = get_safe('c8_aprendizado')
    if aprendizado_conquista:
        conteudo_c8 += f"Isso ensinou que {aprendizado_conquista}. "

    if conteudo_c8:
        texto += "## 🏆 CONQUISTAS MARCANTES\n\n" + conteudo_c8 + "\n\n"

    # ---- CAPÍTULO 20: PEQUENOS HÁBITOS ----
    conteudo_c20 = ""
    habito = get_safe('c20_habito')
    exemplo = get_safe('c20_exemplo')
    dificuldade = get_safe('c20_dificuldade')

    if habito:
        conteudo_c20 += f"{nome} {habito.lower()} consegue manter um hábito por 21 dias. "
    if exemplo:
        conteudo_c20 += f"Um pequeno hábito que trouxe grande mudança: {exemplo}. "
    if dificuldade:
        conteudo_c20 += f"A maior dificuldade para manter a constância é {dificuldade}. "

    if conteudo_c20:
        texto += "## 🌿 O PODER DOS PEQUENOS HÁBITOS\n\n" + conteudo_c20 + "\n\n"

    # ---- CAPÍTULO 21: SONHOS PARA O FUTURO ----
    conteudo_c21 = ""
    sonho = get_safe('c21_sonho')
    plano = get_safe('c21_plano')
    if sonho:
        conteudo_c21 += f"Seu principal sonho é {sonho}. "
    if plano:
        conteudo_c21 += f"Para realizá-lo, planeja {plano}. "

    if conteudo_c21:
        texto += "## 🔮 OLHANDO PARA O FUTURO\n\n" + conteudo_c21 + "\n\n"

    # ---- CAPÍTULO 26: LEGADO FINAL ----
    legado = get_safe('c26_legado')
    if legado:
        texto += "## 💖 MENSAGEM FINAL\n\n"
        texto += f"{legado}\n\n"

    # ---- CONCLUSÃO INSPIRADORA ----
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

    # ---- CAPÍTULO 10: FORMAÇÃO E CAPACITAÇÃO ----
    conteudo_c10 = ""
    formacao = get_safe('c10_formacao')
    cursos = get_safe('c10_cursos')
    graduacoes = get_safe('c10_graduacoes')
    certificacoes = get_safe('c10_certificacoes')

    if formacao:
        conteudo_c10 += f"• {formacao}\n"
    if cursos:
        conteudo_c10 += f"• Cursos: {cursos}\n"
    if graduacoes:
        conteudo_c10 += f"• Graduações: {graduacoes}\n"
    if certificacoes:
        conteudo_c10 += f"• Certificações: {certificacoes}\n"

    if conteudo_c10:
        texto += "## 📚 FORMAÇÃO ACADÊMICA E CAPACITAÇÃO\n\n" + conteudo_c10 + "\n"

    # ---- CAPÍTULO 10: EXPERIÊNCIAS PROFISSIONAIS ----
    experiencias = get_safe('c10_experiencias')
    if experiencias:
        texto += "## 💼 EXPERIÊNCIAS PROFISSIONAIS RELEVANTES\n\n"
        texto += f"{experiencias}\n\n"

    # ---- CAPÍTULO 4 E 10: COMPETÊNCIAS E HABILIDADES ----
    conteudo_comp = ""
    talentos = get_safe('c4_talentos')
    competencias = get_safe('c10_competencias')

    if talentos:
        conteudo_comp += f"• **Principais talentos:** {talentos}\n"
    if competencias:
        conteudo_comp += f"• **Competências desenvolvidas:** {competencias}\n"

    if conteudo_comp:
        texto += "## ⚡ COMPETÊNCIAS E HABILIDADES\n\n" + conteudo_comp + "\n"

    # ---- CAPÍTULO 4 E 10: DESAFIOS E SUPERAÇÕES ----
    conteudo_desafios = ""
    desafio = get_safe('c4_desafio')
    aprendizado = get_safe('c4_aprendizado')
    maiores_desafios = get_safe('c10_maiores_desafios')

    if desafio:
        conteudo_desafios += f"• **Desafio marcante:** {desafio}\n"
    if aprendizado:
        conteudo_desafios += f"• **Aprendizado:** {aprendizado}\n"
    if maiores_desafios:
        conteudo_desafios += f"• **Outros desafios:** {maiores_desafios}\n"

    if conteudo_desafios:
        texto += "## 🚀 DESAFIOS E SUPERAÇÕES\n\n" + conteudo_desafios + "\n"

    # ---- CAPÍTULO 10: APLICAÇÃO DO CONHECIMENTO ----
    aplicacao = get_safe('c10_aplicacao_conhecimento')
    if aplicacao:
        texto += "## 🧠 APLICAÇÃO DO CONHECIMENTO\n\n"
        texto += f"{aplicacao}\n\n"

    # ---- CAPÍTULO 10: RESULTADOS ALCANÇADOS ----
    resultados = get_safe('c10_resultados_concretos')
    if resultados:
        texto += "## 📈 RESULTADOS ALCANÇADOS\n\n"
        texto += f"{resultados}\n\n"

    # ---- CAPÍTULO 11: OBJETIVO PROFISSIONAL ----
    objetivo = get_safe('c11_objetivo_profissional')
    if objetivo:
        texto += "## 🎯 OBJETIVO PROFISSIONAL\n\n"
        texto += f"{objetivo}\n\n"

    # ---- CAPÍTULO 21: VISÃO DE FUTURO ----
    conteudo_futuro = ""
    sonho = get_safe('c21_sonho')
    plano = get_safe('c21_plano')

    if sonho:
        conteudo_futuro += f"• **Sonho/objetivo:** {sonho}\n"
    if plano:
        conteudo_futuro += f"• **Passos planejados:** {plano}\n"

    if conteudo_futuro:
        texto += "## 🔮 VISÃO DE FUTURO\n\n" + conteudo_futuro + "\n"

    # ---- CAPÍTULO 26: LEGADO FINAL ----
    legado = get_safe('c26_legado')
    if legado:
        texto += "## 💬 MENSAGEM DE LEGADO\n\n"
        texto += f"{legado}\n\n"

    # ---- CONSIDERAÇÕES FINAIS ----
    texto += "---\n"
    texto += "## CONSIDERAÇÕES FINAIS\n\n"
    texto += f"A trajetória de {nome} é um exemplo de como a determinação, o aprendizado constante e a paixão pelo trabalho podem construir uma carreira significativa. Que este perfil sirva de inspiração e de registro para as futuras conquistas que ainda virão.\n\n"
    texto += f"*{nome}*"

    return texto


def gerar_biografia_infantil(genero):
    nome = get_safe('nome_autor', 'Autor Desconhecido')
    data = datetime.now().strftime("%d/%m/%Y")

    if genero == "Menina":
        artigo = "uma"
        pronome_sujeito = "ela"
        pronome_objeto = "a"
        pronome_possessivo = "sua"
        artigo_definido = "a"
        personagem = "princesa"
    else:
        artigo = "um"
        pronome_sujeito = "ele"
        pronome_objeto = "o"
        pronome_possessivo = "seu"
        artigo_definido = "o"
        personagem = "príncipe"

    texto = f"""# A HISTÓRIA DE {nome.upper()}
## Contada de um jeito bem gostoso de ler
*Gerado em {data}*

---

### 🌟 ERA UMA VEZ...

Era uma vez {artigo} {personagem} muito especial chamad{artigo_definido} **{nome}**. {pronome_sujeito.capitalize()} morava em um lugar onde os sonhos podiam voar e a imaginação não tinha limites. Seu coração era cheio de bondade e {pronome_possessivo} mente vivia cheia de perguntas curiosas sobre o mundo. Vamos conhecer {pronome_possessivo} linda história?

---
"""

    # Capítulo 1 – Aprendizado
    conteudo_c1 = ""
    mudanca = get_safe('c1_mudanca')
    if mudanca == "Sim":
        conteudo_c1 += f"{nome} sabia que podia mudar e aprender coisas novas todos os dias. Para {pronome_objeto}, cada dia era uma nova aventura de aprendizado. "
    elif mudanca == "Não":
        conteudo_c1 += f"{nome} achava que não podia mudar, mas estava aprendendo que sim, é possível. "
    else:
        conteudo_c1 += f"{nome} estava descobrindo que aprender coisas novas é uma grande aventura, mesmo quando parece difícil. "

    freq = get_safe('c1_aprendizado')
    if freq and freq != "Nunca":
        conteudo_c1 += f"{pronome_sujeito.capitalize()} gostava de aprender {freq.lower()}, sempre curioso(a) para saber mais. "

    reacao = get_safe('c1_reacao')
    if reacao:
        if "Persistir" in reacao:
            conteudo_c1 += f"Quando um desafio aparecia, {pronome_sujeito} não desistia: respirava fundo e tentava de novo, de um jeito diferente. "
        elif "Desistir" in reacao:
            conteudo_c1 += f"Às vezes {pronome_sujeito} queria desistir, mas aprendia que pedir ajuda também é uma forma de vencer. "
        else:
            conteudo_c1 += f"Quando algo era difícil, {pronome_sujeito} aprendia a esperar e confiar. "

    habitos = get_safe('c1_habitos')
    if habitos == "Sim":
        conteudo_c1 += f"Já percebeu que, quando criava novos hábitos, coisas boas começavam a acontecer ao {pronome_possessivo} redor. "

    motiva = get_safe('c1_motiva')
    if motiva:
        conteudo_c1 += f"O que mais {pronome_objeto} motivava a mudar era {motiva}. "

    renovar = get_safe('c1_renovar')
    if renovar:
        conteudo_c1 += f"Para {pronome_objeto}, 'renovar a mente' significava {renovar}. "

    if conteudo_c1:
        texto += "## 📖 CAPÍTULO 1: A MENTE QUE APRENDE\n\n" + conteudo_c1 + "\n\n"

    # Capítulo 2 – Identidade
    conteudo_c2 = ""
    heranca = get_safe('c2_heranca')
    if heranca:
        if "herdeiro" in heranca.lower():
            conteudo_c2 += f"{nome} sabia que era muito especial: {pronome_sujeito} era filho amado de Deus, herdeiro de um grande Rei! Isso fazia {pronome_objeto} se sentir protegido(a) e amado(a) para sempre. "
        else:
            conteudo_c2 += f"{nome} estava aprendendo que cada pessoa é única e tem um valor imenso, assim como {pronome_sujeito}. "

    desafios = get_safe('c2_desafios')
    if desafios:
        if "oportunidades" in desafios.lower():
            conteudo_c2 += f"Quando enfrentava dificuldades, lembrava que podia crescer com elas, como uma árvore que fica mais forte depois da tempestade. "
        else:
            conteudo_c2 += f"Às vezes os desafios assustavam, mas {pronome_sujeito} nunca deixava de tentar. "

    promessas = get_safe('c2_promessas')
    if promessas and "promessas" in promessas.lower():
        conteudo_c2 += f"Guardava no coração as promessas de Deus, como um tesouro precioso. "

    eternidade = get_safe('c2_eternidade')
    if eternidade:
        conteudo_c2 += f"Pensar no futuro eterno {pronome_objeto} fazia sentir {eternidade.lower()}. "

    reflexao2 = get_safe('c2_reflexao')
    if reflexao2:
        conteudo_c2 += f"{nome} refletia: \"{reflexao2}\". "

    if conteudo_c2:
        texto += "## 👑 CAPÍTULO 2: QUEM EU SOU\n\n" + conteudo_c2 + "\n\n"

    # Capítulo 3 – Corpo e Espírito
    conteudo_c3 = ""
    corpo = get_safe('c3_corpo', [])
    if isinstance(corpo, list) and corpo:
        conteudo_c3 += f"{nome} cuidava do {pronome_possessivo} corpo como quem cuida de um jardim: {', '.join(corpo)}. "
    else:
        conteudo_c3 += f"{nome} estava aprendendo a cuidar melhor do corpo, que é a casa onde moramos. "

    espirito = get_safe('c3_espirito', [])
    if isinstance(espirito, list) and espirito:
        conteudo_c3 += f"Para o espírito, {pronome_sujeito} gostava de {', '.join(espirito)}. "

    equilibrio = get_safe('c3_equilibrio')
    if equilibrio:
        conteudo_c3 += f"Refletindo sobre o equilíbrio entre corpo e espírito, {nome} pensava: \"{equilibrio}\". "

    if conteudo_c3:
        texto += "## ❤️ CAPÍTULO 3: O CORPO E O CORAÇÃO\n\n" + conteudo_c3 + "\n\n"

    # Capítulo 4 – Talentos
    conteudo_c4 = ""
    talentos = get_safe('c4_talentos')
    if talentos:
        conteudo_c4 += f"{nome} tinha talentos incríveis, como {talentos}. Eram dons que faziam {pronome_objeto} brilhar. "

    autentico = get_safe('c4_autentico')
    if autentico:
        conteudo_c4 += f"Um momento em que se sentiu verdadeiramente autêntico(a) foi quando {autentico}. "

    desafio4 = get_safe('c4_desafio')
    if desafio4:
        conteudo_c4 += f"Um dia, enfrentou um desafio: {desafio4}. Mas, com coragem, seguiu em frente. "

    aprendizado4 = get_safe('c4_aprendizado')
    if aprendizado4:
        conteudo_c4 += f"Com isso, aprendeu que {aprendizado4}. "

    if conteudo_c4:
        texto += "## ✨ CAPÍTULO 4: TALENTOS ESPECIAIS\n\n" + conteudo_c4 + "\n\n"

    # Capítulo 5 – Alcance
    conteudo_c5 = ""
    alcance_local = get_safe('c5_local')
    alcance_regional = get_safe('c5_regional')
    alcance_internacional = get_safe('c5_internacional')
    if alcance_local == "Sim":
        conteudo_c5 += f"{nome} acreditava que sua história podia impactar as pessoas ao redor. "
    if alcance_regional == "Sim":
        conteudo_c5 += f"Sabia que sua trajetória podia inspirar pessoas fora do seu círculo. "
    if alcance_internacional == "Sim":
        conteudo_c5 += f"Imaginava que sua história podia até alcançar diferentes culturas e países! "
    reflexao5 = get_safe('c5_reflexao')
    if reflexao5:
        conteudo_c5 += f"Para {pronome_objeto}, sua história merecia ser contada porque {reflexao5}. "

    if conteudo_c5:
        texto += "## 🌍 CAPÍTULO 5: O ALCANCE DA SUA HISTÓRIA\n\n" + conteudo_c5 + "\n\n"

    # Capítulo 6 – Posição bíblica
    conteudo_c6 = ""
    crise = get_safe('c6_crise')
    if crise == "Sim":
        conteudo_c6 += f"Em momentos de crise, {nome} sempre buscava aprendizado. "
    carater = get_safe('c6_carater')
    if carater == "Sim":
        conteudo_c6 += f"Sabia que suas decisões revelavam seu caráter. "
    emocoes = get_safe('c6_emocoes')
    if emocoes == "Sim":
        conteudo_c6 += f"Prestava atenção às suas emoções antes de agir. "
    arrependimento = get_safe('c6_arrependimento')
    if arrependimento == "Sim":
        conteudo_c6 += f"Praticava o arrependimento como uma mudança real de atitude. "
    fidelidade = get_safe('c6_fidelidade')
    if fidelidade == "Sim":
        conteudo_c6 += f"Mantinha-se fiel aos seus compromissos mesmo quando ninguém estava olhando. "
    reflexao6 = get_safe('c6_reflexao')
    if reflexao6:
        conteudo_c6 += f"Sobre a influência dos princípios bíblicos, {nome} disse: \"{reflexao6}\". "

    if conteudo_c6:
        texto += "## 📖 CAPÍTULO 6: A BÍBLIA NA VIDA\n\n" + conteudo_c6 + "\n\n"

    # Capítulo 7 – Trampolim
    conteudo_c7 = ""
    proativo = get_safe('c7_proativo')
    if proativo == "Sim":
        conteudo_c7 += f"{nome} sempre foi uma pessoa proativa, que não esperava as coisas acontecerem. "
    estagnacao = get_safe('c7_estagnacao')
    if estagnacao == "Sim":
        area_estagnacao = get_safe('c7_area')
        if area_estagnacao:
            conteudo_c7 += f"Sentia que estava estagnado(a) em {area_estagnacao}, mas isso não o(a) paralisava. "
    decisao = get_safe('c7_decisao')
    if decisao:
        conteudo_c7 += f"Sabia que {decisao} era o momento de mudar. "
    reflexao7 = get_safe('c7_reflexao')
    if reflexao7:
        conteudo_c7 += f"O que funcionava como trampolim para o próximo nível era: {reflexao7}. "

    if conteudo_c7:
        texto += "## 🚀 CAPÍTULO 7: O MOMENTO DE DAR O SALTO\n\n" + conteudo_c7 + "\n\n"

    # Capítulo 8 – Conquistas
    conteudo_c8 = ""
    memoria = get_safe('c8_memoria')
    if memoria:
        conteudo_c8 += f"Um momento que marcou {pronome_possessivo} vida para sempre foi: {memoria}. "
    celebra = get_safe('c8_celebra')
    if celebra:
        conteudo_c8 += f"{nome} costumava celebrar suas vitórias {celebra.lower()}. "
    aprendizado_conquista = get_safe('c8_aprendizado')
    if aprendizado_conquista:
        conteudo_c8 += f"Com essa conquista, {pronome_sujeito} aprendeu que {aprendizado_conquista}. "

    if conteudo_c8:
        texto += "## 🏅 CAPÍTULO 8: UMA CONQUISTA MUITO ESPECIAL\n\n" + conteudo_c8 + "\n\n"

    # Capítulo 9 – Público e propósito
    conteudo_c9 = ""
    publico = get_safe('c9_publico', [])
    if isinstance(publico, list) and publico:
        conteudo_c9 += f"{nome} imaginava sua biografia sendo lida por {', '.join(publico)}. "
    por_que = get_safe('c9_por_que', [])
    if isinstance(por_que, list) and por_que:
        conteudo_c9 += f"Queria contar sua história para {', '.join(por_que)}. "
    como = get_safe('c9_como', [])
    if isinstance(como, list) and como:
        conteudo_c9 += f"Desejava que o leitor se sentisse {', '.join(como)}. "
    impacto = get_safe('c9_reflexao')
    if impacto:
        conteudo_c9 += f"O impacto esperado era: {impacto}. "

    if conteudo_c9:
        texto += "## 🎯 CAPÍTULO 9: PARA QUEM ESCREVO\n\n" + conteudo_c9 + "\n\n"

    # Capítulo 10 – Análise curricular
    conteudo_c10 = ""
    formacao = get_safe('c10_formacao')
    experiencias10 = get_safe('c10_experiencias')
    competencias10 = get_safe('c10_competencias')
    if formacao:
        conteudo_c10 += f"Sua formação incluiu: {formacao}. "
    if experiencias10:
        conteudo_c10 += f"Experiências marcantes: {experiencias10}. "
    if competencias10:
        conteudo_c10 += f"Competências desenvolvidas: {competencias10}. "
    reflexao10 = get_safe('c10_reflexao')
    if reflexao10:
        conteudo_c10 += f"Tudo isso {pronome_objeto} preparou para o futuro: {reflexao10}. "

    if conteudo_c10:
        texto += "## 📚 CAPÍTULO 10: CAMINHOS DE APRENDIZADO\n\n" + conteudo_c10 + "\n\n"

    # Capítulo 11 – Seleção
    conteudo_c11 = ""
    etica = get_safe('c11_etica')
    if etica == "Sim":
        conteudo_c11 += f"{nome} sempre priorizou a ética em suas escolhas. "
    contratacoes = get_safe('c11_contratacoes', [])
    if isinstance(contratacoes, list) and contratacoes:
        conteudo_c11 += f"Para seu projeto, considerou contratar {', '.join(contratacoes)}. "
    criterios = get_safe('c11_criterios')
    if criterios:
        conteudo_c11 += f"Seus critérios essenciais eram: {criterios}. "

    if conteudo_c11:
        texto += "## ⚖️ CAPÍTULO 11: ESCOLHAS COM ÉTICA\n\n" + conteudo_c11 + "\n\n"

    # Capítulo 12 – Virada
    conteudo_c12 = ""
    virada = get_safe('c12_virada')
    if virada:
        conteudo_c12 += f"{virada} "
    aprendeu12 = get_safe('c12_aprendeu')
    if aprendeu12:
        conteudo_c12 += f"Isso {pronome_objeto} ensinou que {aprendeu12}. "
    aplicacao = get_safe('c12_aplicacao')
    if aplicacao:
        conteudo_c12 += f"Depois disso, {pronome_sujeito} passou a aplicar o que aprendia {aplicacao.lower()}. "

    if conteudo_c12:
        texto += "## 🔄 CAPÍTULO 12: O DIA QUE TUDO MUDOU\n\n" + conteudo_c12 + "\n\n"

    # Capítulo 13 – Legado
    conteudo_c13 = ""
    procrastina = get_safe('c13_procrastina')
    if procrastina == "Proativo(a)":
        conteudo_c13 += f"{nome} se considerava mais proativo(a) do que procrastinador(a). "
    elif procrastina == "Procrastinador(a)":
        conteudo_c13 += f"{nome} admitia ser mais procrastinador(a), mas estava melhorando. "
    tempo = get_safe('c13_tempo')
    if tempo:
        conteudo_c13 += f"O que costumava roubar seu tempo era {tempo}. "
    mudanca13 = get_safe('c13_mudanca')
    if mudanca13:
        conteudo_c13 += f"Para deixar um legado melhor, sentia que precisava mudar {mudanca13}. "

    if conteudo_c13:
        texto += "## 🌳 CAPÍTULO 13: O LEGADO QUE QUERO DEIXAR\n\n" + conteudo_c13 + "\n\n"

    # Capítulo 14 – Hobby
    conteudo_c14 = ""
    hobby = get_safe('c14_hobby')
    if hobby:
        conteudo_c14 += f"{nome} adorava {hobby}. "
    origem14 = get_safe('c14_origem')
    if origem14:
        conteudo_c14 += f"Essa paixão começou {origem14}. "
    paz14 = get_safe('c14_paz')
    if paz14:
        conteudo_c14 += f"Em um momento difícil, isso {pronome_objeto} trouxe paz: {paz14}. "
    frase14 = get_safe('c14_frase_capa')
    if frase14:
        conteudo_c14 += f"Se fosse uma frase de capa, seria: \"{frase14}\". "

    if conteudo_c14:
        texto += "## 🎨 CAPÍTULO 14: O PASSATEMPO PREFERIDO\n\n" + conteudo_c14 + "\n\n"

    # Capítulo 15 – Papéis sociais
    conteudo_c15 = ""
    papeis = get_safe('c15_escolhidos', [])
    if isinstance(papeis, list) and papeis:
        conteudo_c15 += f"{nome} exercia os papéis de {', '.join(papeis)}. "
    reflexao15 = get_safe('c15_reflexao')
    if reflexao15:
        conteudo_c15 += f"Esses papéis influenciavam quem {pronome_sujeito} era porque {reflexao15}. "

    if conteudo_c15:
        texto += "## 👨‍👩‍👧 CAPÍTULO 15: OS PAPÉIS QUE EXERÇO\n\n" + conteudo_c15 + "\n\n"

    # Capítulo 16 – Virtudes
    conteudo_c16 = ""
    virtudes = get_safe('c16_virtudes', [])
    if isinstance(virtudes, list) and virtudes:
        conteudo_c16 += f"{nome} reconhecia em si virtudes como {', '.join(virtudes)}. "
    exemplo16 = get_safe('c16_exemplo')
    if exemplo16:
        conteudo_c16 += f"Um exemplo de quando uma virtude fez diferença: {exemplo16}. "

    if conteudo_c16:
        texto += "## 💎 CAPÍTULO 16: VIRTUDES QUE BRILHAM\n\n" + conteudo_c16 + "\n\n"

    # Capítulo 17 – Galardão
    conteudo_c17 = ""
    motivo17 = get_safe('c17_motivo')
    if motivo17:
        conteudo_c17 += f"O que mais motivava {nome} na vida era {motivo17.lower()}. "
    reflexao17 = get_safe('c17_reflexao')
    if reflexao17:
        conteudo_c17 += f"Isso influenciava suas decisões porque {reflexao17}. "

    if conteudo_c17:
        texto += "## 🌟 CAPÍTULO 17: O QUE ME MOVE\n\n" + conteudo_c17 + "\n\n"

    # Capítulo 18 – Terceirizar
    conteudo_c18 = ""
    delega = get_safe('c18_delega')
    if delega:
        conteudo_c18 += f"{nome} se sentia {delega.lower()} ao delegar tarefas. "
    dificuldade18 = get_safe('c18_dificuldade')
    if dificuldade18:
        conteudo_c18 += f"Sua maior dificuldade era {dificuldade18}. "
    aprendizado18 = get_safe('c18_aprendizado')
    if aprendizado18:
        conteudo_c18 += f"Já aprendeu que {aprendizado18}. "

    if conteudo_c18:
        texto += "## 🤝 CAPÍTULO 18: APRENDENDO A DELEGAR\n\n" + conteudo_c18 + "\n\n"

    # Capítulo 19 – Fases da vida
    conteudo_c19 = ""
    infancia = get_safe('c19_infancia')
    adolescencia = get_safe('c19_adolescencia')
    adulta = get_safe('c19_adulta')
    if infancia:
        conteudo_c19 += f"Na infância, {infancia}. "
    if adolescencia:
        conteudo_c19 += f"Na adolescência, {adolescencia}. "
    if adulta:
        conteudo_c19 += f"Na vida adulta, {adulta}. "
    aprendizado_fases = get_safe('c19_aprendizado')
    if aprendizado_fases:
        conteudo_c19 += f"Cada fase trouxe o aprendizado: {aprendizado_fases}. "

    if conteudo_c19:
        texto += "## 🕰️ CAPÍTULO 19: AS FASES DA VIDA\n\n" + conteudo_c19 + "\n\n"

    # Capítulo 20 – Pequenos hábitos
    conteudo_c20 = ""
    habito20 = get_safe('c20_habito')
    if habito20:
        conteudo_c20 += f"{nome} {habito20.lower()} conseguia manter um hábito por 21 dias. "
    exemplo20 = get_safe('c20_exemplo')
    if exemplo20:
        conteudo_c20 += f"Um pequeno hábito que trouxe grande mudança foi: {exemplo20}. "
    dificuldade20 = get_safe('c20_dificuldade')
    if dificuldade20:
        conteudo_c20 += f"Sua maior dificuldade para manter a constância era {dificuldade20}. "

    if conteudo_c20:
        texto += "## 🌱 CAPÍTULO 20: O PODER DOS PEQUENOS HÁBITOS\n\n" + conteudo_c20 + "\n\n"

    # Capítulo 21 – Sonhos
    conteudo_c21 = ""
    sonho = get_safe('c21_sonho')
    plano = get_safe('c21_plano')
    foco = get_safe('c21_foco')
    aprende = get_safe('c21_aprende')
    if foco:
        conteudo_c21 += f"{nome} vivia mais focado no {foco.lower()}. "
    if aprende:
        conteudo_c21 += f"Aprendia mais com {aprende.lower()}. "
    if sonho:
        conteudo_c21 += f"Seu principal sonho era {sonho}. "
    if plano:
        conteudo_c21 += f"Para realizá-lo, planejava {plano}. "

    if conteudo_c21:
        texto += "## 🌠 CAPÍTULO 21: SONHOS PARA O FUTURO\n\n" + conteudo_c21 + "\n\n"

    # Capítulo 22 – Estrutura do livro
    conteudo_c22 = ""
    elementos = get_safe('c22_elementos', [])
    if isinstance(elementos, list) and elementos:
        conteudo_c22 += f"{nome} queria incluir no livro: {', '.join(elementos)}. "
    reflexao22 = get_safe('c22_reflexao')
    if reflexao22:
        conteudo_c22 += f"Isso era importante porque {reflexao22}. "

    if conteudo_c22:
        texto += "## 📖 CAPÍTULO 22: COMO SERÁ ESTE LIVRO\n\n" + conteudo_c22 + "\n\n"

    # Capítulo 23 – Distribuição
    conteudo_c23 = ""
    formato = get_safe('c23_formato', [])
    publicacao = get_safe('c23_publicacao')
    if isinstance(formato, list) and formato:
        conteudo_c23 += f"Imaginava sua biografia em {', '.join(formato)}. "
    if publicacao:
        conteudo_c23 += f"Pretendia publicar de forma {publicacao.lower()}. "
    reflexao23 = get_safe('c23_reflexao')
    if reflexao23:
        conteudo_c23 += f"Sobre a publicação, {nome} dizia: {reflexao23}. "

    if conteudo_c23:
        texto += "## 📦 CAPÍTULO 23: PUBLICANDO A HISTÓRIA\n\n" + conteudo_c23 + "\n\n"

    # Capítulo 24 – Experiência visual
    conteudo_c24 = ""
    mapas = get_safe('c24_mapas')
    estetica = get_safe('c24_estetica')
    apoios = get_safe('c24_apoios', [])
    if mapas == "Sim":
        conteudo_c24 += f"{nome} queria incluir mapas mentais. "
    if estetica:
        conteudo_c24 += f"Imaginava a estética assim: {estetica}. "
    if isinstance(apoios, list) and apoios:
        conteudo_c24 += f"Recursos de apoio: {', '.join(apoios)}. "

    if conteudo_c24:
        texto += "## 🎨 CAPÍTULO 24: A EXPERIÊNCIA VISUAL\n\n" + conteudo_c24 + "\n\n"

    # Capítulo 25 – Vendas
    conteudo_c25 = ""
    vendas = get_safe('c25_vendas', [])
    if isinstance(vendas, list) and vendas:
        conteudo_c25 += f"{nome} pretendia estruturar vendas por {', '.join(vendas)}. "
    reflexao25 = get_safe('c25_reflexao')
    if reflexao25:
        conteudo_c25 += f"Acreditava que o livro alcançaria pessoas porque {reflexao25}. "

    if conteudo_c25:
        texto += "## 💰 CAPÍTULO 25: COMO ALCANÇAR AS PESSOAS\n\n" + conteudo_c25 + "\n\n"

    # Capítulo 26 – Legado final
    conteudo_c26 = ""
    sinestesia = get_safe('c26_sinestesia', [])
    legado = get_safe('c26_legado')
    if isinstance(sinestesia, list) and sinestesia:
        conteudo_c26 += f"{nome} queria que o livro despertasse os sentidos: {', '.join(sinestesia)}. "
    if legado:
        conteudo_c26 += f"Sua mensagem final de legado era: {legado}. "

    if conteudo_c26:
        texto += "## 💌 CAPÍTULO 26: O LEGADO FINAL\n\n" + conteudo_c26 + "\n\n"

    # Conclusão
    texto += "---\n"
    texto += "## 🌈 E VIVERAM FELIZES PARA SEMPRE...\n\n"
    texto += f"Essa é a história de {nome}, {artigo} {personagem} que continua escrevendo novos capítulos todos os dias, com muita coragem, amor e esperança. E quem sabe um dia você também não escreve a sua? Afinal, cada um de nós tem uma história única e especial, cheia de aventuras, aprendizados e magia.\n\n"
    texto += f"*Fim – com todo carinho do mundo para {nome}*"
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















