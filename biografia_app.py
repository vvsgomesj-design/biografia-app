import streamlit as st
from datetime import datetime

# --- 1. CONFIGURAÇÃO E INICIALIZAÇÃO SEGURA ---
st.set_page_config(page_title="Gerador de Biografias Pro", layout="wide")

# Inicializa o estado para evitar o erro AttributeError de chave inexistente
if 'livro_gerado' not in st.session_state:
    st.session_state.livro_gerado = ""

# --- 2. LISTA INTEGRAL DAS 41 VIRTUDES (Cap. 16) ---
VIRTUDES_41 = [
    "Amor", "Alegria", "Auto-domínio", "Bondade", "Benignidade", "Benevolência", 
    "Compaixão", "Coragem", "Cortesias", "Castidade", "Discernimento", "Disciplina", 
    "Diligência", "Esperança", "Entusiasmo", "Fé", "Fidelidade", "Fortaleza", 
    "Generosidade", "Gratidão", "Gentileza", "Honra", "Humildade", "Honestidade", 
    "Justiça", "Lealdade", "Longanimidade", "Moderação", "Mansidão", "Obediência", 
    "Ordem", "Paciência", "Perdão", "Prudência", "Piedade", "Respeito", 
    "Responsabilidade", "Sabedoria", "Temperança", "Tolerância", "Zelo"
]

# --- 3. FUNÇÃO PARA COLETAR RESPOSTAS COM SEGURANÇA ---
def get_v(key, default="..."):
    valor = st.session_state.get(key)
    if valor:
        if isinstance(valor, list):
            return ", ".join(valor) if len(valor) > 0 else default
        return str(valor)
    return default

st.title("📘 Sistema de Biografias Trampolim")

# --- 4. ENTRADAS DE DADOS (BASEADO NO SEU ARQUIVO FUNCIONANDO) ---
tab_a, tab_b, tab_c = st.tabs(["🏛️ Bloco A: Fundamentos", "🎨 Bloco B: Jornada", "🚀 Bloco C: Estrutura"])

# --- BLOCO 1: CAPÍTULOS 1 A 5 ---
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

        c1_motiva = st.text_input(
            "Em uma palavra, o que mais te motiva a mudar?"
        )

        c1_renovar = st.text_area(
            "O que significa para você 'renovar a mente'?"
        )

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

        c4_talentos = st.text_input(
            "Quais são seus três maiores talentos?"
        )

        c4_desafio = st.text_area(
            "Relate um desafio significativo que você superou:"
        )

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

        c8_memoria = st.text_area(
            "Descreva uma conquista que marcou sua vida:"
        )

        c8_aprendizado = st.text_area(
            "O que essa conquista te ensinou?"
        )

    # ==================================================
    # CAPÍTULO 9 – PRA QUEM, POR QUÊ E COMO
    # ==================================================
    with st.expander("Cap. 9 – Público, Propósito e Forma"):
        c9_publico = st.multiselect(
            "Para quem esta biografia é direcionada?",
            [
                "Família",
                "Amigos",
                "Estudantes",
                "Líderes",
                "Público em geral"
            ]
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
            [
                "Acolhedora",
                "Inspiradora",
                "Realista",
                "Transformadora",
                "Leve"
            ]
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
# =========================
# CONTINUA NA TAB_B
# =========================
with tab_b:

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
            [
                "Alívio",
                "Insegurança",
                "Medo de perder o controle",
                "Entusiasmo"
            ]
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

        c19_adolescencia = st.text_area(
            "O que mais marcou sua adolescência?"
        )

        c19_adulta = st.text_area(
            "Qual foi (ou é) o auge da sua fase adulta?"
        )

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

        c20_exemplo = st.text_area(
            "Cite um pequeno hábito que já trouxe grande mudança:"
        )

        c20_dificuldade = st.text_area(
            "O que mais dificulta sua constância?"
        )

with tab_c:
    st.header("Bloco C: Estrutura do Livro, Vendas e Experiência")

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

        c22_reflexao = st.text_area(
            "Por que esses elementos são importantes para você?"
        )

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
            [
                "Independente",
                "Plataformas digitais",
                "Editoras",
                "Ainda não sei"
            ]
        )

        c23_reflexao = st.text_area(
            "O que mais te anima (ou preocupa) sobre a publicação?"
        )

    # ==================================================
    # CAPÍTULO 24 – EXPERIÊNCIA VISUAL E MAPAS
    # ==================================================
    with st.expander("Cap. 24 – Experiência Visual e Apoios"):
        c24_mapas = st.radio(
            "Você deseja incluir mapas mentais ou esquemas visuais no livro?",
            ["Sim", "Não"]
        )

        c24_estetica = st.text_area(
            "Como você imagina a estética visual do livro?"
        )

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

        c26_legado = st.text_area(
            "Qual mensagem final você deseja deixar como legado?"
        )

# --- 5. MOTOR DE NARRATIVA COESA E ESTRUTURADA ---
def gerar_narrativa(estilo, genero_inf=None):
    nome = get_v('nome_autor').upper()
    
    if estilo == "Infantil":
        art, pers = ("uma", "princesa") if genero_inf == "Menina" else ("um", "príncipe")
        pron = "ela" if genero_inf == "Menina" else "ele"
        return f"""# 🌈 AS AVENTURAS REAIS DE {nome}

Era uma vez {art} {pers} especial. {nome} descobriu que aprender algo novo {get_v('c1_frequencia').lower()} era como regar um jardim mágico. Para {nome}, renovar a mente é "{get_v('c1_renovar')}".

Como herdeir{'a' if genero_inf=='Menina' else 'o'} de promessas, {pron} entendeu que desafios revelam quem somos: "{get_v('c2_reflexao')}". Com talentos como {get_v('c4_talentos')}, ajuda a todos, cuidando do castelo com {get_v('c3_praticas')}. As lições começaram cedo, brincando de {get_v('c19_infancia')}. Hoje, brilha com virtudes como {get_v('c16_virtudes')}. Seu maior sonho é {get_v('c21_sonho')}.

**Mensagem do Reino:** "{get_v('c26_legado')}" """

    elif estilo == "Talento (Profissional)":
        return f"""# 💼 TRAJETÓRIA E EXCELÊNCIA: {nome}

Com formação em {get_v('c10_formacao')}, {nome} pauta sua carreira na premissa de que renovar a mente é "{get_v('c1_renovar')}". Movido por {get_v('c1_motiva')}, consolidou competências após um momento de virada: {get_v('c12_virada')}.

Seu caráter é forjado pelas virtudes {get_v('c16_virtudes')}, aplicadas em desafios como {get_v('c8_desafio')}. Um exemplo de sua integridade foi quando {get_v('c16_exemplo')}. O seu plano envolve {get_v('c21_plano')} para alcançar o sonho de {get_v('c21_sonho')}, impactando o mundo pois "{get_v('c25_alcance')}".

**Legado:** "{get_v('c26_legado')}" """

    else: # Hobby
        return f"""# 🎨 A ESSÊNCIA E O LAZER DE {nome}

Para {nome}, a vida ganha cor no hobby **{get_v('c14_hobby')}**. Surgido de {get_v('c14_origem')}, este passatempo traz paz em momentos como "{get_v('c14_paz')}". Sua autenticidade, marca registrada desde a infância ao brincar de {get_v('c19_infancia')}, revela-se quando {get_v('c4_autentico')}. Aliando talentos de {get_v('c4_talentos')} ao hábito de {get_v('c20_habito')}, {nome} constrói um caminho pleno.

**Reflexão:** "{get_v('c26_legado')}" """

# --- 6. BARRA LATERAL (BOTÃO E EXIBIÇÃO DO RESULTADO) ---
with st.sidebar:
    st.header("📖 Gerar Biografia")
    estilo_sel = st.selectbox("Escolha o Estilo:", ["Talento (Profissional)", "Hobby / Passatempo", "Infantil"])
    gen_inf = None
    if estilo_sel == "Infantil":
        gen_inf = st.radio("Gênero:", ["Menina", "Menino"])
    
    if st.button("🚀 Gerar agora"):
        if not st.session_state.nome_autor or st.session_state.nome_autor == "Autor Desconhecido":
            st.error("Por favor, preencha o nome no Bloco A.")
        else:
            st.session_state.livro_gerado = gerar_narrativa(estilo_sel, gen_inf)

    # EXIBIÇÃO NA SIDEBAR LOGO ABAIXO DO BOTÃO
    if st.session_state.livro_gerado:
        st.markdown("---")
        st.subheader("📄 Resultado:")
        st.markdown(st.session_state.livro_gerado)
        st.download_button("📥 Baixar TXT", st.session_state.livro_gerado, file_name="biografia_completa.txt")



















