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
    # certificacoes foi removido (não existe no código de coleta)

    if formacao:
        conteudo_c10 += f"• {formacao}\n"
    if cursos:
        conteudo_c10 += f"• Cursos: {cursos}\n"
    if graduacoes:
        conteudo_c10 += f"• Graduações: {graduacoes}\n"

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

    # ---- CAPÍTULO 4: DESAFIOS E SUPERAÇÕES ----
    conteudo_desafios = ""
    desafio = get_safe('c4_desafio')
    aprendizado = get_safe('c4_aprendizado')
    # maiores_desafios foi removido

    if desafio:
        conteudo_desafios += f"• **Desafio marcante:** {desafio}\n"
    if aprendizado:
        conteudo_desafios += f"• **Aprendizado:** {aprendizado}\n"

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

    texto += "---\n## CONSIDERAÇÕES FINAIS\n\n"
    texto += f"A trajetória de {nome} é um exemplo de como a determinação, o aprendizado constante e a paixão pelo trabalho podem construir uma carreira significativa. Que este perfil sirva de inspiração e de registro para as futuras conquistas que ainda virão.\n\n"
    texto += f"*{nome}*"
    return texto


def gerar_biografia_infantil(genero):
    nome = get_safe('nome_autor', 'Autor Desconhecido')
    data = datetime.now().strftime("%d/%m/%Y")

    # Configuração de Gênero e Pronomes
    if genero == "Menina":
        artigo, pronome_sujeito, pronome_objeto = "uma", "ela", "a"
        pronome_possessivo, artigo_definido, personagem = "sua", "a", "princesa"
    else:
        artigo, pronome_sujeito, pronome_objeto = "um", "ele", "o"
        pronome_possessivo, artigo_definido, personagem = "seu", "o", "príncipe"

    texto = f"""# 🌈 A GRANDE JORNADA DE {nome.upper()}
## Uma história de coragem, aprendizado e propósito
*Gerado em {data}*

---

### 🌟 ERA UMA VEZ...

Era uma vez {artigo} {personagem} muito especial chamad{artigo_definido} **{nome}**. {pronome_sujeito.capitalize()} vivia em um lugar onde os sonhos eram como sementes que, com cuidado, podiam se transformar em grandes árvores. Seu coração era cheio de bondade e {pronome_possessivo} mente vivia cheia de perguntas curiosas, buscando sempre entender as maravilhas do mundo. Vamos conhecer {pronome_possessivo} linda história?

---
"""

    # Capítulo 1 – Aprendizado e Mindset
    conteudo_c1 = ""
    mudanca = get_safe('c1_mudanca')
    if mudanca == "Sim":
        conteudo_c1 += f"{nome} descobriu algo incrível: que podia aprender coisas novas todos os dias e treinar seu pensamento para ser cada vez mais forte! "
    
    freq = get_safe('c1_aprendizado')
    if freq and freq != "Nunca":
        conteudo_c1 += f"{pronome_sujeito.capitalize()} amava aprender {freq.lower()}, sempre em busca de novas descobertas. "

    reacao = get_safe('c1_reacao')
    if "Persistir" in str(reacao):
        conteudo_c1 += f"Quando encontrava um caminho difícil, {pronome_sujeito} não parava: respirava fundo, pensava em uma nova estratégia e seguia em frente com coragem. "

    if conteudo_c1:
        texto += "## 📖 CAPÍTULO 1: O PODER DE APRENDER\n\n" + conteudo_c1 + "\n\n"

    # Capítulo 2 – Identidade e Herança
    conteudo_c2 = ""
    heranca = get_safe('c2_heranca')
    if "herdeiro" in str(heranca).lower():
        conteudo_c2 += f"{nome} sabia que tinha uma identidade real: {pronome_sujeito} era filh{artigo_definido} amad{artigo_definido} do Rei do Universo, herdeir{artigo_definido} de promessas valiosas. "
    
    desafios = get_safe('c2_desafios')
    if "oportunidades" in str(desafios).lower():
        conteudo_c2 += f"Encarava as dificuldades como degraus para subir mais alto e ficar ainda mais forte. "

    if conteudo_c2:
        texto += "## 👑 CAPÍTULO 2: QUEM EU SOU DE VERDADE\n\n" + conteudo_c2 + "\n\n"

    # Capítulo 3 – Corpo e Espírito
    conteudo_c3 = ""
    corpo = get_safe('c3_corpo')
    if corpo:
        conteudo_c3 += f"{nome} cuidava do seu corpo com muito carinho, praticando {corpo.lower()}. "
    
    espirito = get_safe('c3_espirito')
    if espirito:
        conteudo_c3 += f"Para manter seu coração em paz, {pronome_sujeito} gostava de {espirito.lower()}, fortalecendo seu espírito. "

    if conteudo_c3:
        texto += "## ❤️ CAPÍTULO 3: CUIDANDO DO MEU TESOURO\n\n" + conteudo_c3 + "\n\n"

    # Capítulo 4 – Talentos
    conteudo_c4 = ""
    talentos = get_safe('c4_talentos')
    if talentos:
        conteudo_c4 += f"{nome} recebeu dons especiais, como {talentos}. Quando usava esses talentos, sentia que podia ajudar muitas pessoas! "

    autentico = get_safe('c4_autentico')
    if autentico:
        conteudo_c4 += f"Um dos momentos em que {pronome_sujeito} foi mais verdadeiro(a) foi quando {autentico}. "

    if conteudo_c4:
        texto += "## ✨ CAPÍTULO 4: MEUS DONS ESPECIAIS\n\n" + conteudo_c4 + "\n\n"

    # Capítulos 5 a 10 – Propósito e História
    conteudo_c5_10 = ""
    if get_safe('c5_reflexao'):
        conteudo_c5_10 += f"Sua história merecia ser contada para inspirar outros, pois {get_safe('c5_reflexao')}. "
    
    memoria = get_safe('c8_memoria')
    if memoria:
        conteudo_c5_10 += f"Uma grande vitória que {nome} celebrou foi {memoria}. "

    if conteudo_c5_10:
        texto += "## 🚀 CAPÍTULO 5-10: UMA HISTÓRIA PARA CONTAR\n\n" + conteudo_c5_10 + "\n\n"

    # Capítulos 11 a 15 – Escolhas e Relações
    conteudo_c11_15 = ""
    virada = get_safe('c12_virada')
    if virada:
        conteudo_c11_15 += f"Houve um momento marcante de mudança: {virada}. "
    
    papeis = get_safe('c15_escolhidos')
    if papeis:
        conteudo_c11_15 += f"Nesta jornada, {nome} desempenhava com amor os papéis de {papeis}. "

    if conteudo_c11_15:
        texto += "## 👨‍👩‍👧 CAPÍTULO 11-15: CAMINHOS E AMIGOS\n\n" + conteudo_c11_15 + "\n\n"

    # Capítulo 16 – Virtudes (O Caráter)
    virtudes = get_safe('c16_virtudes')
    if virtudes:
        texto += f"## 💎 CAPÍTULO 16: VIRTUDES QUE BRILHAM\n\nComo {artigo} {personagem} valente, {nome} carregava consigo virtudes como {virtudes}. Elas eram como pedras preciosas que guiavam cada passo.\n\n"

    # Capítulos 19 e 20 – Fases e Hábitos
    conteudo_c19_20 = ""
    infancia = get_safe('c19_infancia')
    if infancia:
        conteudo_c19_20 += f"As sementes dessa história foram plantadas quando {nome} brincava de {infancia}. "
    
    habito = get_safe('c20_exemplo')
    if habito:
        conteudo_c19_20 += f"Hoje, {pronome_sujeito} entende que pequenas atitudes, como {habito}, trazem grandes frutos. "

    if conteudo_c19_20:
        texto += "## 🕰️ CAPÍTULO 19-20: AS SEMENTES DO TEMPO\n\n" + conteudo_c19_20 + "\n\n"

    # Capítulo 21 a 26 – Futuro e Legado
    conteudo_final = ""
    sonho = get_safe('c21_sonho')
    if sonho:
        conteudo_final += f"O maior sonho de {nome} para os próximos capítulos desta aventura é {sonho}. "
    
    legado = get_safe('c26_legado')
    if legado:
        conteudo_final += f"\nA mensagem final que {pronome_sujeito} deixa para o mundo é: \"{legado}\"."

    if conteudo_final:
        texto += "## 🌠 CAPÍTULO 21-26: NOVOS HORIZONTES\n\n" + conteudo_final + "\n\n"

    # Conclusão
    texto += "---\n"
    texto += "## 🌈 A JORNADA CONTINUA...\n\n"
    texto += f"Esta é a história de {nome}, {artigo} {personagem} que nos ensina que, com propósito, fé e perseverança, cada um de nós pode escrever um livro maravilhoso com a própria vida.\n\n"
    texto += f"*Fim (por enquanto...) – Com admiração para {nome}*"
    
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
















