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

    # Hobby principal
    hobby = get_safe('c14_hobby')
    if hobby:
        texto += f"## 🌟 Meu Hobby Favorito\n\n"
        texto += f"Entre todas as atividades que poderiam preencher seu tempo livre, **{nome}** elegeu {hobby} como sua favorita. "
        origem = get_safe('c14_origem')
        if origem:
            texto += f"Essa paixão não surgiu por acaso: ela nasceu {origem}, talvez em um momento de descoberta ou inspiração. "
        paz = get_safe('c14_paz')
        if paz:
            texto += f"Em meio às atribulações da vida, {hobby} se tornou um refúgio. {nome} recorda com emoção: *\"{paz}\"*. "
        frase = get_safe('c14_frase_capa')
        if frase:
            texto += f"\n\nSe fosse preciso resumir esse hobby em uma frase, ela seria: **\"{frase}\"**. "
        texto += "\n\n"

    # Outros talentos (capítulo 4)
    talentos = get_safe('c4_talentos')
    if talentos:
        texto += f"## ✨ Talentos que Brilham\n\n"
        texto += f"Além do hobby principal, {nome} é dotado de talentos especiais: {talentos}. "
        texto += f"São habilidades que, muitas vezes, surpreendem até a si mesmo. "
        desafio = get_safe('c4_desafio')
        if desafio:
            texto += f"Um dia, ao enfrentar o desafio de {desafio}, {nome} descobriu que seus talentos podiam ir muito além do que imaginava. "
        aprendizado = get_safe('c4_aprendizado')
        if aprendizado:
            texto += f"Essa experiência trouxe uma lição valiosa: {aprendizado}. "
        texto += "\n\n"

    # Infância e fases da vida
    infancia = get_safe('c19_infancia')
    adolescencia = get_safe('c19_adolescencia')
    adulta = get_safe('c19_adulta')
    if infancia or adolescencia or adulta:
        texto += f"## 🌱 Ao Longo da Vida\n\n"
        if infancia:
            texto += f"Na infância, {infancia}. Esses momentos ajudaram a moldar sua personalidade. "
        if adolescencia:
            texto += f"Na adolescência, {adolescencia}. Foi uma fase de descobertas e de formação de caráter. "
        if adulta:
            texto += f"Na vida adulta, {adulta}. Essa etapa trouxe maturidade e novas perspectivas. "
        aprendizado_fases = get_safe('c19_aprendizado')
        if aprendizado_fases:
            texto += f"Olhando para trás, {nome} reflete: *\"{aprendizado_fases}\"*. "
        texto += "\n\n"

    # Conquistas marcantes
    memoria = get_safe('c8_memoria')
    if memoria:
        texto += f"## 🏆 Conquistas que Marcaram\n\n"
        texto += f"Entre tantas memórias, uma se destaca: {memoria}. "
        aprendizado_conquista = get_safe('c8_aprendizado')
        if aprendizado_conquista:
            texto += f"Essa conquista ensinou que {aprendizado_conquista}. "
        texto += "\n\n"

    # Pequenos hábitos, grandes mudanças
    exemplo_habito = get_safe('c20_exemplo')
    if exemplo_habito:
        texto += f"## 🌿 Pequenas Ações, Grandes Transformações\n\n"
        texto += f"{nome} acredita no poder dos pequenos hábitos. Um exemplo marcante foi quando {exemplo_habito}. "
        dificuldade = get_safe('c20_dificuldade')
        if dificuldade:
            texto += f"Claro, nem sempre é fácil manter a constância; a maior dificuldade enfrentada é {dificuldade}. "
        texto += "Mesmo assim, a perseverança tem sido uma companheira fiel.\n\n"

    # Reflexão sobre o futuro (capítulo 21)
    sonho = get_safe('c21_sonho')
    if sonho:
        texto += f"## 🔮 Olhando para o Futuro\n\n"
        texto += f"Quando pensa no amanhã, {nome} nutre um sonho especial: {sonho}. "
        plano = get_safe('c21_plano')
        if plano:
            texto += f"Para torná-lo realidade, já vislumbra alguns passos: {plano}. "
        texto += "\n\n"

    # Legado final (capítulo 26)
    legado = get_safe('c26_legado')
    if legado:
        texto += f"## 💖 Mensagem Final\n\n"
        texto += f"{legado}\n\n"

    # Conclusão inspiradora
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
    # Formação acadêmica e capacitação
    formacao = get_safe('c10_formacao')
    cursos = get_safe('c10_cursos')
    graduacoes = get_safe('c10_graduacoes')
    certificacoes = get_safe('c10_certificacoes')
    if formacao or cursos or graduacoes or certificacoes:
        texto += "## 📚 FORMAÇÃO ACADÊMICA E CAPACITAÇÃO\n\n"
        if graduacoes:
            texto += f"**Graduações:** {graduacoes}\n\n"
        if formacao:
            texto += f"**Formação complementar:** {formacao}\n\n"
        if cursos:
            texto += f"**Cursos e treinamentos:** {cursos}\n\n"
        if certificacoes:
            texto += f"**Certificações de destaque:** {certificacoes}\n\n"

    # Experiências profissionais
    experiencias = get_safe('c10_experiencias')
    if experiencias:
        texto += "## 💼 EXPERIÊNCIAS PROFISSIONAIS RELEVANTES\n\n"
        texto += f"{experiencias}\n\n"

    # Competências e habilidades
    competencias = get_safe('c10_competencias')
    talentos = get_safe('c4_talentos')
    if competencias or talentos:
        texto += "## ⚡ COMPETÊNCIAS E HABILIDADES\n\n"
        if talentos:
            texto += f"**Principais talentos:** {talentos}\n\n"
        if competencias:
            texto += f"**Competências desenvolvidas:** {competencias}\n\n"

    # Desafios e superações
    desafio = get_safe('c4_desafio')
    aprendizado = get_safe('c4_aprendizado')
    maiores_desafios = get_safe('c10_maiores_desafios')
    if desafio or maiores_desafios:
        texto += "## 🚀 DESAFIOS E SUPERAÇÕES\n\n"
        if desafio:
            texto += f"Um dos desafios mais marcantes foi: {desafio}. "
        if aprendizado:
            texto += f"Essa experiência trouxe o aprendizado de que {aprendizado}. "
        if maiores_desafios:
            texto += f"Além disso, {nome} enfrentou outros obstáculos: {maiores_desafios}. "
        texto += "\n\n"

    # Aplicação do conhecimento
    aplicacao = get_safe('c10_aplicacao_conhecimento')
    if aplicacao:
        texto += "## 🧠 APLICAÇÃO DO CONHECIMENTO\n\n"
        texto += f"{aplicacao}\n\n"

    # Resultados alcançados
    resultados = get_safe('c10_resultados_concretos')
    if resultados:
        texto += "## 📈 RESULTADOS ALCANÇADOS\n\n"
        texto += f"{resultados}\n\n"

    # Objetivo profissional
    objetivo = get_safe('c11_objetivo_profissional')
    if objetivo:
        texto += "## 🎯 OBJETIVO PROFISSIONAL\n\n"
        texto += f"{objetivo}\n\n"

    # Visão de futuro
    sonho = get_safe('c21_sonho')
    plano = get_safe('c21_plano')
    if sonho or plano:
        texto += "## 🔮 VISÃO DE FUTURO\n\n"
        if sonho:
            texto += f"{nome} sonha com {sonho}. "
        if plano:
            texto += f"Para chegar lá, planeja {plano}. "
        texto += "\n\n"

    # Legado e mensagem final
    legado = get_safe('c26_legado')
    if legado:
        texto += "## 💬 MENSAGEM DE LEGADO\n\n"
        texto += f"{legado}\n\n"

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
    else:  # Menino
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

Era uma vez {artigo} {personagem} muito especial chamad**{artigo_definido}** **{nome}**. {pronome_sujeito.capitalize()} morava em um lugar onde os sonhos podiam voar e a imaginação não tinha limites. Seu coração era cheio de bondade e {pronome_possessivo} mente vivia cheia de perguntas curiosas sobre o mundo. Vamos conhecer {pronome_possessivo} linda história?

---
"""

    # Capítulo 1 – Aprendizado
    texto += "## 📖 CAPÍTULO 1: A MENTE QUE APRENDE\n\n"
    mudanca = get_safe('c1_mudanca')
    if mudanca == "Sim":
        texto += f"{nome} sabia que podia mudar e aprender coisas novas todos os dias. Para {pronome_objeto}, cada dia era uma nova aventura de aprendizado. "
    else:
        texto += f"{nome} estava descobrindo que aprender coisas novas é uma grande aventura, mesmo quando parece difícil. "
    freq = get_safe('c1_aprendizado')
    if freq and freq != "Nunca":
        texto += f"{pronome_sujeito.capitalize()} gostava de aprender {freq.lower()}, sempre curioso(a) para saber mais. "
    reacao = get_safe('c1_reacao')
    if reacao and "Persistir" in reacao:
        texto += f"Quando um desafio aparecia, {pronome_sujeito} não desistia: respirava fundo e tentava de novo, de um jeito diferente. "
    elif reacao and "Desistir" in reacao:
        texto += f"Às vezes {pronome_sujeito} queria desistir, mas aprendia que pedir ajuda também é uma forma de vencer. "
    habitos = get_safe('c1_habitos')
    if habitos == "Sim":
        texto += f"Já percebeu que, quando criava novos hábitos, coisas boas começavam a acontecer ao {pronome_possessivo} redor. "
    motiva = get_safe('c1_motiva')
    if motiva:
        texto += f"O que mais {pronome_objeto} motivava a mudar era {motiva}. "
    texto += "\n\n"

    # Capítulo 2 – Identidade
    texto += "## 👑 CAPÍTULO 2: QUEM EU SOU\n\n"
    heranca = get_safe('c2_heranca')
    if heranca and "herdeiro" in heranca.lower():
        texto += f"{nome} sabia que era muito especial: {pronome_sujeito} era filho amado de Deus, herdeiro de um grande Rei! Isso fazia {pronome_objeto} se sentir protegido(a) e amado(a) para sempre. "
    else:
        texto += f"{nome} estava aprendendo que cada pessoa é única e tem um valor imenso, assim como {pronome_sujeito}. "
    desafios = get_safe('c2_desafios')
    if desafios and "oportunidades" in desafios.lower():
        texto += f"Quando enfrentava dificuldades, lembrava que podia crescer com elas, como uma árvore que fica mais forte depois da tempestade. "
    promessas = get_safe('c2_promessas')
    if promessas and "promessas" in promessas.lower():
        texto += f"Guardava no coração as promessas de Deus, como um tesouro precioso. "
    texto += "\n\n"

    # Capítulo 3 – Corpo e Espírito
    texto += "## ❤️ CAPÍTULO 3: O CORPO E O CORAÇÃO\n\n"
    corpo = get_safe('c3_corpo', [])
    if isinstance(corpo, list) and corpo:
        texto += f"{nome} cuidava do {pronome_possessivo} corpo como quem cuida de um jardim: {', '.join(corpo)}. "
    else:
        texto += f"{nome} estava aprendendo a cuidar melhor do corpo, que é a casa onde moramos. "
    espirito = get_safe('c3_espirito', [])
    if isinstance(espirito, list) and espirito:
        texto += f"Para o espírito, {pronome_sujeito} gostava de {', '.join(espirito)}. "
    equilibrio = get_safe('c3_equilibrio')
    if equilibrio:
        texto += f"Refletindo sobre o equilíbrio entre corpo e espírito, {nome} pensava: \"{equilibrio}\". "
    texto += "\n\n"

    # Capítulo 4 – Talentos
    talentos = get_safe('c4_talentos')
    if talentos:
        texto += f"## ✨ CAPÍTULO 4: TALENTOS ESPECIAIS\n\n"
        texto += f"{nome} tinha talentos incríveis, como {talentos}. Eram dons que faziam {pronome_objeto} brilhar. "
        desafio = get_safe('c4_desafio')
        if desafio:
            texto += f"Um dia, enfrentou um desafio: {desafio}. Mas, com coragem, seguiu em frente. "
        aprendizado = get_safe('c4_aprendizado')
        if aprendizado:
            texto += f"Com isso, aprendeu que {aprendizado}. "
    texto += "\n\n"

    # Capítulo 8 – Conquistas
    memoria = get_safe('c8_memoria')
    if memoria:
        texto += f"## 🏅 CAPÍTULO 8: UMA CONQUISTA MUITO ESPECIAL\n\n"
        texto += f"Um momento que marcou {pronome_possessivo} vida para sempre foi: {memoria}. "
        aprendizado_conquista = get_safe('c8_aprendizado')
        if aprendizado_conquista:
            texto += f"Com essa conquista, {pronome_sujeito} aprendeu que {aprendizado_conquista}. "
    texto += "\n\n"

    # Capítulo 14 – Hobby
    hobby = get_safe('c14_hobby')
    if hobby:
        texto += f"## 🎨 CAPÍTULO 14: {artigo_definido.upper()} PASSATEMPO PREFERIDO\n\n"
        texto += f"Nas horas vagas, {nome} adorava {hobby}. Era o momento em que {pronome_sujeito} se sentia mais feliz e livre. "
        origem = get_safe('c14_origem')
        if origem:
            texto += f"Essa paixão começou {origem}, talvez com uma pessoa querida ou uma descoberta inesperada. "
        paz = get_safe('c14_paz')
        if paz:
            texto += f"Era um momento de paz e alegria, como quando {paz}. "
    texto += "\n\n"

    # Capítulo 19 – Infância
    infancia = get_safe('c19_infancia')
    if infancia:
        texto += f"## 🧸 CAPÍTULO 19: QUANDO ERA PEQUENO(A)\n\n"
        texto += f"Quando {pronome_sujeito} era pequeno(a), {infancia}. "
        adolescencia = get_safe('c19_adolescencia')
        if adolescencia:
            texto += f"Na adolescência, {adolescencia}. "
        adulta = get_safe('c19_adulta')
        if adulta:
            texto += f"Na vida adulta, {adulta}. "
        aprendizado_fases = get_safe('c19_aprendizado')
        if aprendizado_fases:
            texto += f"Olhando para cada fase, {pronome_sujeito} percebeu que {aprendizado_fases}. "
    texto += "\n\n"

    # Capítulo 20 – Pequenos hábitos
    exemplo_habito = get_safe('c20_exemplo')
    if exemplo_habito:
        texto += f"## 🌱 CAPÍTULO 20: PEQUENAS SEMENTES, GRANDES ÁRVORES\n\n"
        texto += f"{nome} descobriu que pequenas ações podem gerar grandes mudanças. Por exemplo, {exemplo_habito}. "
        dificuldade = get_safe('c20_dificuldade')
        if dificuldade:
            texto += f"Claro, nem sempre foi fácil manter a constância, pois {dificuldade}. Mas {pronome_sujeito} não desistiu. "
    texto += "\n\n"

    # Capítulo 21 – Sonhos
    sonho = get_safe('c21_sonho')
    if sonho:
        texto += f"## 🌠 CAPÍTULO 21: SONHOS PARA O FUTURO\n\n"
        texto += f"Quando pensa no amanhã, {nome} sonha com {sonho}. "
        plano = get_safe('c21_plano')
        if plano:
            texto += f"Para que esse sonho se realize, {pronome_sujeito} já pensa em dar alguns passos: {plano}. "
    texto += "\n\n"

    # Mensagem final
    legado = get_safe('c26_legado')
    if legado:
        texto += f"## 💌 MENSAGEM FINAL\n\n"
        texto += f"{legado}\n\n"

    # Conclusão encantada
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













