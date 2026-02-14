import streamlit as st
from datetime import datetime

# Criação das abas (agora com 4 abas)
tab_a, tab_b, tab_c, tab_d = st.tabs([
    "Bloco A: Fundamentos",
    "Bloco B: Legado e Relações",
    "Bloco C: Estrutura",
    "📖 Livro Gerado"
])

# Configuração da página
st.set_page_config(page_title="Biografia App", layout="wide")
st.title("📘 Trampolim Adaptável - Seu Aplicativo Auxiliar da sua Biografia")

# Inicializa o estado para o livro gerado
if 'livro_gerado' not in st.session_state:
    st.session_state.livro_gerado = ""


# ==================================================
# BLOCO 1: CAPÍTULOS 1 A 5 (e até 10 na verdade)
# ==================================================
with tab_a:
    st.header("Bloco A: Fundamentos, Identidade e Organização")

    nome_autor = st.text_input("Nome Completo:", "Autor Desconhecido", key="nome_autor")

    # ==================================================
    # CAPÍTULO 1 – NEUROPLASTICIDADE E MINDSET
    # ==================================================
    with st.expander("Cap. 1 – Neuroplasticidade e Mudança de Mindset"):
        c1_mudanca = st.radio(
            "Você acredita que é possível mudar padrões de pensamento e comportamento ao longo da vida?",
            ["Sim", "Não", "Não tenho certeza"],
            key="c1_mudanca"
        )

        c1_aprendizado = st.selectbox(
            "Com que frequência você busca aprender algo novo (curso, leitura, habilidade)?",
            ["Diariamente", "Semanalmente", "Raramente", "Nunca"],
            key="c1_aprendizado"
        )

        c1_reacao = st.radio(
            "Quando enfrenta um desafio, você tende a:",
            ["Desistir facilmente", "Persistir e buscar novas estratégias", "Esperar que alguém resolva"],
            key="c1_reacao"
        )

        c1_habitos = st.radio(
            "Você já percebeu mudanças positivas após criar novos hábitos?",
            ["Sim", "Não", "Ainda estou tentando"],
            key="c1_habitos"
        )

        c1_mentalidade = st.radio(
            "Qual dessas frases mais representa sua mentalidade atual?",
            ["“Nasci assim, não posso mudar.”", "“Posso aprender e evoluir sempre.”", "“Depende das circunstâncias.”"],
            key="c1_mentalidade"
        )

        c1_erro = st.radio(
            "Quando algo dá errado, você costuma pensar:",
            ["“Sou um fracasso.”", "“Posso aprender com isso.”", "“A culpa é dos outros.”"],
            key="c1_erro"
        )

        c1_afirmacoes = st.radio(
            "Você pratica a repetição de pensamentos positivos ou afirmações diárias?",
            ["Sim, todos os dias", "Às vezes", "Não"],
            key="c1_afirmacoes"
        )

        c1_fe_influencia = st.radio(
            "Você acredita que sua fé pode influenciar sua forma de pensar e agir?",
            ["Sim", "Não", "Tenho dúvidas"],
            key="c1_fe_influencia"
        )

        c1_ora_freq = st.radio(
            "Com que frequência você ora ou medita sobre a Palavra de Deus?",
            ["Diariamente", "Algumas vezes por semana", "Raramente", "Nunca"],
            key="c1_ora_freq"
        )

        c1_ora_ajuda = st.radio(
            "Quando você ora ou reflete, sente que isso ajuda a reorganizar seus pensamentos e emoções?",
            ["Sim", "Às vezes", "Não"],
            key="c1_ora_ajuda"
        )

        c1_transformacao = st.radio(
            "Você acredita que pode se tornar uma pessoa completamente diferente com o tempo e esforço certos?",
            ["Sim", "Não", "Talvez"],
            key="c1_transformacao"
        )

        c1_pratica_fortalecer = st.selectbox(
            "Qual dessas práticas você mais precisa fortalecer para transformar sua mente?",
            ["Leitura e estudo", "Oração e fé", "Hábitos saudáveis", "Relacionamentos positivos"],
            key="c1_pratica_fortalecer"
        )

        c1_motiva = st.text_input("Em uma palavra, o que mais te motiva a mudar?", key="c1_motiva")
        c1_habito_substituir = st.text_input("Qual hábito você gostaria de substituir por outro mais saudável?", key="c1_habito_substituir")
        c1_renovar = st.text_area("O que significa para você 'renovar a mente'?", key="c1_renovar")
        c1_jesus_fonte = st.radio("Você acredita que Jesus é a nossa fonte de todas as informações?", ["Sim", "Não"], key="c1_jesus_fonte")

    # ==================================================
    # CAPÍTULO 2 – IDENTIDADE EM CRISTO (HERDEIRO)
    # ==================================================
    with st.expander("Cap. 2 – Identidade em Cristo e Herança"):
        c2_heranca = st.radio(
            "1. Identidade e Consciência de Herança",
            [
                "Sinto-me verdadeiramente herdeiro(a) de Deus e coerdeiro com Cristo.",
                "Às vezes me esqueço dessa verdade, especialmente em tempos difíceis.",
                "Ainda não compreendo plenamente o que significa ser herdeiro do Pai."
            ],
            key="c2_heranca"
        )

        c2_desafios = st.radio(
            "2. Propósito e Postura diante dos Desafios",
            [
                "Encaro os desafios como oportunidades de manifestar a herança que recebi.",
                "Costumo reagir aos desafios com medo ou dúvida sobre meu valor em Cristo.",
                "Tenho dificuldade em ver propósito nas lutas que enfrento."
            ],
            key="c2_desafios"
        )

        c2_promessas = st.radio(
            "3. Promessas e Fé",
            [
                "Vivo com base nas promessas de Deus e as declaro em minha caminhada.",
                "Conheço algumas promessas, mas nem sempre as aplico no dia a dia.",
                "Não costumo refletir sobre as promessas bíblicas em minha vida."
            ],
            key="c2_promessas"
        )

        c2_experiencias = st.radio(
            "4. Experiências de Herança Espiritual",
            [
                "Já experimentei paz, provisão e direção como sinais da herança divina.",
                "Reconheço poucas situações em que percebi essa herança.",
                "Ainda não identifiquei experiências claras relacionadas à herança em Cristo."
            ],
            key="c2_experiencias"
        )

        c2_esperanca = st.radio(
            "5. Esperança e Futuro",
            [
                "Tenho convicção de que minha história aponta para uma herança eterna.",
                "Às vezes duvido que minha vida tenha um propósito eterno.",
                "Não costumo pensar na herança eterna como parte da minha biografia."
            ],
            key="c2_esperanca"
        )

        c2_aplicacao = st.radio(
            "6. Aplicação na Biografia Pessoal",
            [
                "Já consigo escrever minha história com a consciência de ser herdeiro do Pai.",
                "Estou aprendendo a incluir essa verdade na forma como vejo minha trajetória.",
                "Ainda não sei como aplicar esse conceito à minha biografia."
            ],
            key="c2_aplicacao"
        )

    # ==================================================
    # CAPÍTULO 3 – ORGANIZAÇÃO (CORPO E ESPÍRITO)
    # ==================================================
    with st.expander("Cap. 3 – Organização do Corpo e do Espírito"):
        st.subheader("Corpo")
        c3_rotina = st.radio("Eu mantenho uma rotina diária que me permite cumprir minhas responsabilidades?", ["Sim", "Não"], key="c3_rotina")
        c3_instintos = st.radio("Eu confio nos meus instintos ao tomar decisões importantes?", ["Sim", "Não"], key="c3_instintos")
        c3_atividade_fisica = st.radio("Eu pratico atividades físicas regularmente?", ["Sim", "Não"], key="c3_atividade_fisica")
        c3_sinais_corpo = st.radio("Eu presto atenção aos sinais que meu corpo me dá (cansaço, fome, dor)?", ["Sim", "Não"], key="c3_sinais_corpo")
        c3_alimentacao = st.radio("Eu considero minha alimentação saudável e equilibrada?", ["Sim", "Não"], key="c3_alimentacao")

        st.subheader("Espírito")
        c3_conexao = st.radio("Eu sinto uma conexão com algo maior do que eu?", ["Sim", "Não"], key="c3_conexao")
        c3_intuicao = st.radio("Eu costumo seguir minha intuição?", ["Sim", "Não"], key="c3_intuicao")
        c3_praticas_espirituais = st.radio("Eu dedico tempo para práticas espirituais (meditação, oração, etc.)?", ["Sim", "Não"], key="c3_praticas_espirituais")
        c3_espiritualidade_influencia = st.radio("Eu acredito que a espiritualidade influencia minhas decisões?", ["Sim", "Não"], key="c3_espiritualidade_influencia")
        c3_paz_proposito = st.radio("Eu me sinto em paz com o meu propósito de vida?", ["Sim", "Não"], key="c3_paz_proposito")

        c3_equilibrio = st.text_area("Como você percebe o equilíbrio (ou desequilíbrio) entre corpo e espírito?", key="c3_equilibrio")

    # ==================================================
    # CAPÍTULO 4 – POSIÇÃO VERTICAL E HORIZONTAL
    # ==================================================
    with st.expander("Cap. 4 – Autoconhecimento e Posição na Vida"):
        c4_autentico = st.text_area("Descreva um momento em que você se sentiu verdadeiramente autêntico(a):", key="c4_autentico")
        c4_talentos = st.text_input("Quais são seus três maiores talentos?", key="c4_talentos")
        c4_valor_pessoal = st.text_area("Qual valor pessoal é mais importante para você e como ele se manifesta em suas ações?", key="c4_valor_pessoal")
        c4_desafio = st.text_area("Relate um desafio significativo que você superou:", key="c4_desafio")
        c4_aprendizado = st.text_area("O que esse desafio te ensinou sobre você mesmo(a)?", key="c4_aprendizado")
        c4_decisao_dificil = st.text_area("Qual foi a decisão mais difícil que você já tomou e por quê?", key="c4_decisao_dificil")
        c4_fracasso = st.text_area("Como você lida com o fracasso ou a adversidade?", key="c4_fracasso")
        c3_palavras_personalidade = st.text_input("Quais são as três palavras que melhor descrevem sua personalidade? (separadas por vírgula)", key="c3_palavras_personalidade")
        c4_influencia_familiar = st.text_area("Quais são os aspectos da sua história familiar que mais te influenciaram?", key="c4_influencia_familiar")
        c4_paixoes = st.text_area("Quais são suas maiores paixões e como elas moldam sua identidade?", key="c4_paixoes")
        c4_interesses_diversos = st.text_area("Quais são seus interesses mais diversos e aparentemente não relacionados?", key="c4_interesses_diversos")
        c4_equilibrio_interesses = st.text_area("Como você equilibra seus múltiplos interesses e paixões em sua vida?", key="c4_equilibrio_interesses")
        c4_valor_multipotencial = st.text_area("Qual o valor de ser multipotencial em sua opinião?", key="c4_valor_multipotencial")
        c4_conexoes_experiencias = st.text_area("Quais experiências aparentemente distintas se conectam e criam um padrão em sua vida?", key="c4_conexoes_experiencias")
        c4_influencia_passado = st.text_area("Como suas experiências passadas influenciam suas decisões atuais?", key="c4_influencia_passado")
        c4_licao_conexao = st.text_area("Qual a principal lição que você aprendeu com a conexão de suas experiências?", key="c4_licao_conexao")

    # ==================================================
    # CAPÍTULO 5 – POSIÇÃO LOCAL, REGIONAL E INTERNACIONAL
    # ==================================================
    with st.expander("Cap. 5 – Alcance da Sua História"):
        st.subheader("Expansão Internacional")
        c5_viveu_outro_pais = st.radio("Você já viveu ou trabalhou em outro país?", ["Sim", "Não"], key="c5_viveu_outro_pais")
        c5_viajou_outro_pais = st.radio("Você já viajou para outro país a lazer ou a negócios?", ["Sim", "Não"], key="c5_viajou_outro_pais")
        c5_busca_oportunidades_internacionais = st.radio("Você busca oportunidades que o permitam expandir seus horizontes internacionalmente?", ["Sim", "Não"], key="c5_busca_oportunidades_internacionais")
        c5_perspectiva_global = st.radio("Você considera importante ter uma perspectiva global em sua vida pessoal e profissional?", ["Sim", "Não"], key="c5_perspectiva_global")

        st.subheader("Contato com Outras Culturas")
        c5_conforto_interacao = st.radio("Você se sente à vontade interagindo com pessoas de diferentes culturas?", ["Sim", "Não"], key="c5_conforto_interacao")
        c5_idioma_estrangeiro = st.radio("Você já aprendeu um idioma estrangeiro?", ["Sim", "Não"], key="c5_idioma_estrangeiro")
        c5_interesse_costumes = st.radio("Você se interessa por conhecer costumes e tradições de outros países?", ["Sim", "Não"], key="c5_interesse_costumes")
        c5_aprender_culturas = st.radio("Você busca ativamente oportunidades para aprender sobre outras culturas?", ["Sim", "Não"], key="c5_aprender_culturas")

        st.subheader("Adaptação")
        c5_adaptavel = st.radio("Você se considera uma pessoa adaptável a novas situações e ambientes?", ["Sim", "Não"], key="c5_adaptavel")
        c5_superou_desafio_cultural = st.radio("Você já enfrentou desafios em um ambiente cultural diferente e conseguiu superá-los?", ["Sim", "Não"], key="c5_superou_desafio_cultural")
        c5_comunicacao_eficaz = st.radio("Você consegue se comunicar eficazmente com pessoas que têm diferentes estilos de comunicação?", ["Sim", "Não"], key="c5_comunicacao_eficaz")
        c5_zona_conforto = st.radio("Você se sente confortável saindo da sua zona de conforto para experimentar coisas novas?", ["Sim", "Não"], key="c5_zona_conforto")

        st.subheader("Mensagem Universal")
        c5_historia_inspira = st.radio("Você acredita que sua história pessoal pode inspirar pessoas de diferentes culturas?", ["Sim", "Não"], key="c5_historia_inspira")
        c5_valores_universais = st.radio("Você busca transmitir valores e princípios que são universais e relevantes para todos?", ["Sim", "Não"], key="c5_valores_universais")
        c5_contribuir_mundo = st.radio("Você considera importante contribuir para um mundo mais justo e igualitário?", ["Sim", "Não"], key="c5_contribuir_mundo")
        c5_impacto_positivo = st.radio("Você acredita que suas ações podem ter um impacto positivo na vida de outras pessoas, independentemente de sua nacionalidade?", ["Sim", "Não"], key="c5_impacto_positivo")

        st.subheader("Legado Além das Fronteiras")
        c5_legado_internacional = st.radio("Você deseja que seu legado se estenda além de sua comunidade local ou nacional?", ["Sim", "Não"], key="c5_legado_internacional")
        c5_construindo_beneficio = st.radio("Você está construindo algo que possa beneficiar as futuras gerações em diferentes partes do mundo?", ["Sim", "Não"], key="c5_construindo_beneficio")
        c5_impacto_mundo = st.radio("Você se preocupa em deixar um impacto positivo no mundo, independentemente de onde você esteja?", ["Sim", "Não"], key="c5_impacto_mundo")
        c5_futuro_melhor = st.radio("Você acredita que suas ações podem contribuir para um futuro melhor para a humanidade como um todo?", ["Sim", "Não"], key="c5_futuro_melhor")

    # ==================================================
    # CAPÍTULO 6 – POSIÇÃO CONFORME A BÍBLIA
    # ==================================================
    with st.expander("Cap. 6 – Posição Conforme a Bíblia"):
        c6_crise_oportunidade = st.radio("Em momentos de crise, você geralmente busca oportunidades de aprendizado e crescimento?", ["Sim", "Não"], key="c6_crise_oportunidade")
        c6_licoes_dificeis = st.radio("Você consegue identificar lições valiosas em situações difíceis que enfrentou?", ["Sim", "Não"], key="c6_licoes_dificeis")
        c6_decisoes_refletem_valores = st.radio("Você acredita que suas decisões refletem seus valores e princípios mais profundos?", ["Sim", "Não"], key="c6_decisoes_refletem_valores")
        c6_responsavel_consequencias = st.radio("Você se sente responsável pelas consequências de suas escolhas, boas ou ruins?", ["Sim", "Não"], key="c6_responsavel_consequencias")
        c6_emocoes_sinais = st.radio("Você presta atenção às suas emoções como indicadores de suas necessidades e desejos?", ["Sim", "Não"], key="c6_emocoes_sinais")
        c6_compreender_emocoes = st.radio("Você busca compreender a origem de suas emoções antes de reagir a elas?", ["Sim", "Não"], key="c6_compreender_emocoes")
        c6_reconhecer_erros = st.radio("Você é capaz de reconhecer seus erros e se arrepender sinceramente?", ["Sim", "Não"], key="c6_reconhecer_erros")
        c6_arrependimento_mudanca = st.radio("Você utiliza o arrependimento como um catalisador para mudanças positivas em sua vida?", ["Sim", "Não"], key="c6_arrependimento_mudanca")
        c6_alinhar_proposito = st.radio("Você busca alinhar suas ações com um propósito maior que sua própria satisfação pessoal?", ["Sim", "Não"], key="c6_alinhar_proposito")
        c6_proposito_acima_imagem = st.radio("Você acredita que seu propósito de vida é mais importante do que sua imagem ou reputação?", ["Sim", "Não"], key="c6_proposito_acima_imagem")
        c6_fiel_invisivel = st.radio("Você se mantém fiel aos seus compromissos mesmo quando ninguém está observando?", ["Sim", "Não"], key="c6_fiel_invisivel")
        c6_integridade = st.radio("Você valoriza a integridade e a honestidade em todas as áreas de sua vida, mesmo nas menores coisas?", ["Sim", "Não"], key="c6_integridade")
        c6_reflexao = st.text_area("Como os princípios bíblicos influenciam suas decisões diárias?", key="c6_reflexao")

    # ==================================================
    # CAPÍTULO 7 – SITUAÇÃO ATUAL (TRAMPOLIM)
    # ==================================================
    with st.expander("Cap. 7 – Situação Atual e Impulso para o Trampolim"):
        c7_dificuldades_forca = st.radio("Você acredita que suas maiores dificuldades podem ser transformadas em seus maiores trunfos?", ["Sim", "Não"], key="c7_dificuldades_forca")
        c7_forcas_desafios = st.radio("Você já conseguiu identificar pontos fortes que se desenvolveram a partir de desafios?", ["Sim", "Não"], key="c7_forcas_desafios")
        c7_aprender_erros = st.radio("Você se sente capaz de aprender e crescer com seus erros?", ["Sim", "Não"], key="c7_aprender_erros")
        c7_construindo_futuro = st.radio("Você está ativamente construindo o futuro que deseja no presente?", ["Sim", "Não"], key="c7_construindo_futuro")
        c7_controle_escolhas = st.radio("Você se sente no controle das suas escolhas diárias?", ["Sim", "Não"], key="c7_controle_escolhas")
        c7_acoes_impactam = st.radio("Você acredita que suas ações de hoje impactarão significativamente seu futuro?", ["Sim", "Não"], key="c7_acoes_impactam")
        c7_proativo = st.radio("Você se considera uma pessoa proativa?", ["Sim", "Não"], key="c7_proativo")
        c7_adiar_decisoes = st.radio("Você costuma adiar decisões importantes?", ["Sim", "Não"], key="c7_adiar_decisoes")
        c7_acao_fundamental = st.radio("Você acredita que a ação é fundamental para alcançar seus objetivos?", ["Sim", "Não"], key="c7_acao_fundamental")
        c7_preparado_oportunidades = st.radio("Você está se preparando ativamente para aproveitar as oportunidades que surgem?", ["Sim", "Não"], key="c7_preparado_oportunidades")
        c7_investe_habilidades = st.radio("Você investe tempo e energia em desenvolver suas habilidades?", ["Sim", "Não"], key="c7_investe_habilidades")
        c7_confianca_proximo_passo = st.radio("Você se sente confiante para dar o próximo passo em direção aos seus sonhos?", ["Sim", "Não"], key="c7_confianca_proximo_passo")
        c7_disposto_sair_zona = st.radio("Você está disposto(a) a sair da sua zona de conforto?", ["Sim", "Não"], key="c7_disposto_sair_zona")
        c7_limites_autoimpostos = st.radio("Você acredita que seus limites são autoimpostos?", ["Sim", "Não"], key="c7_limites_autoimpostos")
        c7_superar_medos = st.radio("Você se sente capaz de superar seus medos e inseguranças?", ["Sim", "Não"], key="c7_superar_medos")
        c7_estagnacao = st.radio("Você sente que está estagnado(a) em alguma área da vida?", ["Sim", "Não"], key="c7_estagnacao")
        c7_area = st.text_input("Se sim, em qual área você sente maior estagnação?", key="c7_area")
        c7_decisao = st.radio("Você sente que chegou o momento de mudar?", ["Sim", "Não", "Ainda estou refletindo"], key="c7_decisao")
        c7_reflexao = st.text_area("O que hoje funciona como trampolim para o seu próximo nível?", key="c7_reflexao")

    # ==================================================
    # CAPÍTULO 8 – COMEMORAÇÃO E MARCOS
    # ==================================================
    with st.expander("Cap. 8 – Comemoração e Reconhecimento de Conquistas"):
        c8_celebra = st.selectbox("Você costuma celebrar pequenas vitórias do seu dia a dia?", ["Sempre", "Às vezes", "Raramente", "Nunca"], key="c8_celebra")
        c8_gratidao_caminho = st.radio("Ao alcançar um objetivo, você sente gratidão pelo caminho percorrido?", ["Sim, sempre", "Na maioria das vezes", "Raramente", "Nunca"], key="c8_gratidao_caminho")
        c8_registra = st.radio("Você registra suas conquistas de alguma forma (anotações, fotos, lembranças)?", ["Sim, regularmente", "Ocasionalmente", "Raramente", "Nunca"], key="c8_registra")
        c8_compartilha = st.radio("Compartilhar suas conquistas com outras pessoas é algo importante para você?", ["Sim", "Às vezes", "Não"], key="c8_compartilha")
        c8_celebrar_motiva = st.radio("Você acredita que celebrar suas vitórias aumenta sua motivação para novos desafios?", ["Concordo totalmente", "Concordo parcialmente", "Discordo parcialmente", "Discordo totalmente"], key="c8_celebrar_motiva")
        c8_conquistas_passadas_inspiram = st.radio("Ao olhar para suas conquistas passadas, você se sente inspirado(a) a continuar evoluindo?", ["Sempre", "Às vezes", "Raramente", "Nunca"], key="c8_conquistas_passadas_inspiram")
        c8_fortalecer_identidade = st.radio("Você considera que comemorar suas vitórias ajuda a fortalecer sua identidade pessoal?", ["Sim", "Não", "Não sei dizer"], key="c8_fortalecer_identidade")
        c8_resultado_processo = st.radio("A celebração das suas conquistas é mais voltada para o resultado ou para o processo vivido?", ["Resultado", "Processo", "Ambos igualmente"], key="c8_resultado_processo")
        c8_memoria = st.text_area("Descreva uma conquista que marcou sua vida:", key="c8_memoria")
        c8_aprendizado = st.text_area("O que essa conquista te ensinou?", key="c8_aprendizado")

    # ==================================================
    # CAPÍTULO 9 – PRA QUEM, POR QUÊ E COMO
    # ==================================================
    with st.expander("Cap. 9 – Público, Propósito e Forma"):
        st.subheader("Pra quem: Definindo seu público-alvo")
        c9_perfil_demografico = st.text_area("Qual é o perfil demográfico predominante do seu público (idade, profissão, interesses)?", key="c9_perfil_demografico")
        c9_publico_amplo_especifico = st.radio("Seu público é mais amplo ou mais específico?", ["Amplo (ex: público geral)", "Específico (ex: amigos/familiares, profissionais da área)"], key="c9_publico_amplo_especifico")
        c9_expectativas_publico = st.text_area("Quais são as expectativas e interesses principais do seu público ao ler sua história?", key="c9_expectativas_publico")
        c9_linguagem_tom = st.text_area("Que tipo de linguagem e tom seriam mais adequados para se conectar com seu público?", key="c9_linguagem_tom")
        c9_aprender_sentir = st.text_area("O que o seu público espera aprender ou sentir ao ler sua biografia?", key="c9_aprender_sentir")
        c9_publico_opcoes = st.multiselect(
            "Para quem esta biografia é direcionada? (opções adicionais)",
            ["Amigos e familiares", "Colegas de trabalho", "Estudantes", "Público geral interessado em [sua área de interesse]", "Outro"],
            key="c9_publico_opcoes"
        )
        if "Outro" in c9_publico_opcoes:
            c9_publico_outro = st.text_input("Especifique outro público:", key="c9_publico_outro")

        st.subheader("Por quem: Sua Identidade como Autor")
        c9_descricao_autor = st.text_area("Como você se descreveria para alguém que não o conhece?", key="c9_descricao_autor")
        c9_perspectiva_unica = st.text_area("Qual é a sua perspectiva única sobre sua própria vida?", key="c9_perspectiva_unica")
        c9_aspectos_enfatizar = st.text_area("Existem aspectos da sua personalidade que você deseja enfatizar na biografia?", key="c9_aspectos_enfatizar")
        c9_nivel_conforto = st.selectbox("Qual é o seu nível de conforto ao compartilhar detalhes pessoais?", ["Muito confortável", "Confortável", "Pouco confortável", "Desconfortável"], key="c9_nivel_conforto")
        c9_equilibrio_narrativa = st.text_area("Como você pretende equilibrar objetividade e subjetividade na narrativa?", key="c9_equilibrio_narrativa")
        c9_estilo_autor = st.multiselect(
            "Estilo de escrita pretendido:",
            ["Reservado", "Aberto", "Analítico", "Emocional", "Humorístico"],
            key="c9_estilo_autor"
        )

        st.subheader("Por que: O Propósito da Sua Biografia")
        c9_objetivo_principal = st.text_area("Qual é o principal objetivo da sua biografia (inspirar, documentar, entreter, etc.)?", key="c9_objetivo_principal")
        c9_mensagem_lição = st.text_area("Que mensagem ou lição você espera que os leitores extraiam da sua história?", key="c9_mensagem_lição")
        c9_valores_transmitir = st.text_area("Existem valores ou princípios que você deseja transmitir?", key="c9_valores_transmitir")
        c9_proposito_especifico = st.text_area("A biografia tem um propósito específico (ex: deixar um legado, contar uma história não contada)?", key="c9_proposito_especifico")
        c9_impacto_desejado = st.text_area("Qual o impacto que você deseja causar nos leitores?", key="c9_impacto_desejado")
        c9_proposito_opcoes = st.multiselect(
            "Por que você deseja contar sua história? (opções)",
            ["Inspirar outros", "Registrar minha história", "Compartilhar aprendizados", "Entreter", "Outro"],
            key="c9_proposito_opcoes"
        )
        if "Outro" in c9_proposito_opcoes:
            c9_proposito_outro = st.text_input("Especifique outro propósito:", key="c9_proposito_outro")

        st.subheader("Quando, Onde, O Que: Conteúdo e Escopo")
        c9_periodo_abrangido = st.multiselect(
            "Qual período da sua vida a biografia irá abranger?",
            ["Infância e adolescência", "Vida adulta", "Carreira profissional", "Eventos específicos"],
            key="c9_periodo_abrangido"
        )
        if "Eventos específicos" in c9_periodo_abrangido:
            c9_eventos_especificos = st.text_input("Quais eventos específicos?", key="c9_eventos_especificos")
        c9_eventos_essenciais = st.text_area("Quais eventos ou momentos são essenciais para incluir na biografia?", key="c9_eventos_essenciais")
        c9_lugares_importantes = st.text_area("Existem lugares ou ambientes que desempenharam um papel crucial na sua história?", key="c9_lugares_importantes")
        c9_info_compartilhar = st.text_area("Que tipo de informações você está disposto a compartilhar (pessoais, profissionais, etc.)?", key="c9_info_compartilhar")
        c9_nivel_detalhe = st.text_area("Qual o nível de detalhe que você pretende usar ao descrever eventos e pessoas?", key="c9_nivel_detalhe")

        st.subheader("Quanto: Investimento Pessoal")
        c9_tempo_dedicado = st.selectbox("Quanto tempo você pode dedicar à escrita da biografia por semana/mês?", ["Pouco tempo (algumas horas por semana)", "Tempo moderado (várias horas por semana)", "Tempo integral"], key="c9_tempo_dedicado")
        c9_investir_recursos = st.radio("Você está disposto a investir em recursos adicionais (pesquisa, edição, etc.)?", ["Sim", "Não"], key="c9_investir_recursos")
        c9_prazo_estimado = st.text_input("Qual é o seu prazo estimado para concluir a biografia?", key="c9_prazo_estimado")
        c9_ajuda_profissional = st.radio("Você pretende buscar ajuda profissional (escritor fantasma, editor)?", ["Sim", "Não"], key="c9_ajuda_profissional")
        c9_orcamento = st.text_input("Qual o seu orçamento para este projeto?", key="c9_orcamento")

        st.subheader("Como: Método de Escrita")
        c9_ordem_escrita = st.radio("Você prefere escrever em ordem cronológica ou por temas?", ["Cronológica", "Temática", "Combinação de ambas"], key="c9_ordem_escrita")
        c9_entrevistas = st.radio("Você fará entrevistas com outras pessoas para obter diferentes perspectivas?", ["Sim", "Não"], key="c9_entrevistas")
        c9_materiais_apoio = st.radio("Você pretende usar fotos, documentos ou outros materiais de apoio?", ["Sim", "Não"], key="c9_materiais_apoio")
        c9_processo_revisao = st.text_area("Qual será o seu processo de revisão e edição?", key="c9_processo_revisao")
        c9_estilo_escrita = st.text_input("Que tipo de estilo de escrita você pretende adotar (formal, informal, narrativo, etc.)?", key="c9_estilo_escrita")

    # ==================================================
    # CAPÍTULO 10 – ANÁLISE CURRICULAR E HISTÓRICO
    # ==================================================
    with st.expander("Cap. 10 – Análise Curricular e Experiências"):
        c10_cursos = st.text_area("Quais cursos, treinamentos ou workshops você realizou que foram significativos para o seu desenvolvimento?", key="c10_cursos")
        c10_graduacoes = st.text_area("Quais graduações ou pós-graduações você possui? Qual foi a mais impactante e por quê?", key="c10_graduacoes")
        c10_certificacoes = st.text_area("Há alguma certificação ou título que você considera um diferencial em sua trajetória?", key="c10_certificacoes")
        c10_talentos_naturais = st.text_area("Quais são seus talentos naturais ou habilidades que você desenvolveu ao longo do tempo?", key="c10_talentos_naturais")
        c10_atividades_destaque = st.text_area("Em que atividades ou projetos você se destaca e se sente mais realizado?", key="c10_atividades_destaque")
        c10_uso_talentos = st.text_area("Como você utiliza seus talentos e habilidades em sua vida pessoal e profissional?", key="c10_uso_talentos")
        c10_experiencias_marcantes = st.text_area("Quais foram as experiências mais marcantes em sua vida pessoal e profissional?", key="c10_experiencias_marcantes")
        c10_licoes_experiencias = st.text_area("Que lições você aprendeu com essas experiências e como elas influenciaram suas decisões?", key="c10_licoes_experiencias")
        c10_maiores_desafios = st.text_area("Quais foram os maiores desafios que você enfrentou e como os superou?", key="c10_maiores_desafios")
        c10_aplicacao_conhecimento = st.text_area("Como você aplica o conhecimento que adquiriu em sua área de atuação?", key="c10_aplicacao_conhecimento")
        c10_especialista = st.text_area("Em quais situações você é considerado um especialista ou referência?", key="c10_especialista")
        c10_resultados_concretos = st.text_area("Quais são os resultados concretos que você obteve ao aplicar seu conhecimento e expertise?", key="c10_resultados_concretos")
        c10_reflexao = st.text_area("Como sua trajetória prepara você para o futuro?", key="c10_reflexao")

# ==================================================
# BLOCO 3 — CAPÍTULOS 11 A 20
# ==================================================
with tab_b:
    st.header("Bloco B: Seleção, Legado, Talento e Relações")

    # ==================================================
    # CAPÍTULO 11 – TÉCNICAS DE SELEÇÃO
    # ==================================================
    with st.expander("Cap. 11 – Técnicas de Seleção e Critérios"):
        c11_exp_contribuiram = st.radio("Sinto que minhas experiências profissionais anteriores contribuíram significativamente para o meu desenvolvimento pessoal.", ["Sim", "Não"], key="c11_exp_contribuiram")
        c11_desafios_carreira = st.radio("Já enfrentei desafios significativos na minha carreira que me proporcionaram aprendizados importantes.", ["Sim", "Não"], key="c11_desafios_carreira")
        c11_habilidades_alinhadas = st.radio("Considero que minhas habilidades técnicas e comportamentais estão alinhadas com as exigências do mercado atual.", ["Sim", "Não"], key="c11_habilidades_alinhadas")
        c11_clareza_forcas_fracos = st.radio("Tenho clareza sobre os meus pontos fortes e fracos no âmbito profissional.", ["Sim", "Não"], key="c11_clareza_forcas_fracos")
        c11_busca_aprimoramento = st.radio("Busco constantemente aprimorar minhas competências por meio de cursos, treinamentos ou outras formas de desenvolvimento.", ["Sim", "Não"], key="c11_busca_aprimoramento")

        st.subheader("Valores e Propósito")
        c11_importante_trabalho = st.text_area("O que é mais importante para você no seu trabalho?", key="c11_importante_trabalho")
        c11_objetivo_profissional = st.text_area("Qual o seu principal objetivo profissional?", key="c11_objetivo_profissional")

        st.subheader("Perfil e Habilidades")
        c11_conflitos = st.text_area("Como você lida com situações de conflito no ambiente de trabalho?", key="c11_conflitos")
        c11_principal_caracteristica = st.text_area("Qual a sua principal característica como profissional?", key="c11_principal_caracteristica")

        st.subheader("Experiências e Valores")
        c11_prioriza_experiencia = st.radio("Ao selecionar candidatos, você prioriza a experiência comprovada em relação ao potencial de aprendizado?", ["Sim", "Não"], key="c11_prioriza_experiencia")
        c11_contratou_potencial = st.radio("Você já contratou alguém que não possuía todas as qualificações exigidas, mas demonstrou grande potencial e adaptabilidade?", ["Sim", "Não"], key="c11_contratou_potencial")
        c11_aspecto_importante = st.selectbox(
            "Qual dos seguintes aspectos você considera mais importante ao avaliar um candidato?",
            ["Habilidades técnicas", "Habilidades interpessoais", "Adequação à cultura da empresa", "Histórico de sucesso em projetos anteriores"],
            key="c11_aspecto_importante"
        )
        c11_instinto = st.radio("Você se considera uma pessoa que segue o instinto ao tomar decisões de contratação, mesmo que os dados não sejam totalmente conclusivos?", ["Sim", "Não"], key="c11_instinto")
        c11_etica = st.radio("A ética e a honestidade são fatores determinantes em suas decisões de seleção, mesmo que isso signifique perder um talento promissor?", ["Sim", "Não"], key="c11_etica")

        st.subheader("Decisões e Práticas")
        c11_pressao = st.radio("Em situações de alta pressão, você tende a tomar decisões de contratação mais rapidamente ou prefere manter o processo seletivo completo?", ["Rápido", "Completo"], key="c11_pressao")
        c11_dilema_etico = st.radio("Você já enfrentou um dilema ético ao selecionar um candidato?", ["Sim", "Não"], key="c11_dilema_etico")
        c11_envolve_equipe = st.radio("Você costuma envolver outras pessoas da equipe no processo de seleção?", ["Sim", "Não"], key="c11_envolve_equipe")
        c11_fonte_candidatos = st.selectbox(
            "Qual a sua principal fonte de candidatos?",
            ["Indicações", "Anúncios online", "Empresas de recrutamento", "Redes sociais profissionais"],
            key="c11_fonte_candidatos"
        )
        c11_metodos_evoluidos = st.radio("Você considera que seus métodos de seleção evoluíram significativamente ao longo da sua carreira?", ["Sim", "Não"], key="c11_metodos_evoluidos")

        st.subheader("Contratações para o Livro")
        c11_contratacoes = st.multiselect(
            "Você considera contratar apoio para este projeto?",
            ["Editora", "Ghost Writer", "Designer", "Gráfica", "Nenhum"],
            key="c11_contratacoes"
        )
        c11_criterios = st.text_area("Quais critérios você considera essenciais ao selecionar pessoas ou projetos?", key="c11_criterios")

    # ==================================================
    # CAPÍTULO 12 – TÉCNICAS DE TREINAMENTO
    # ==================================================
    with st.expander("Cap. 12 – Treinamento, Aprendizado e Virada"):
        st.subheader("Transformação Pessoal")
        c12_experiencia_transformadora = st.radio("Você já passou por alguma experiência de vida que o transformou profundamente?", ["Sim", "Não"], key="c12_experiencia_transformadora")
        c12_superacao_desafios = st.radio("Sua história inclui momentos de superação de grandes desafios?", ["Sim", "Não"], key="c12_superacao_desafios")
        c12_inspirar_outros = st.radio("Acredita que suas experiências podem inspirar outras pessoas a mudarem suas vidas?", ["Sim", "Não"], key="c12_inspirar_outros")

        st.subheader("Delegação e Colaboração")
        c12_delegou_tarefas = st.radio("Em sua jornada, você precisou delegar tarefas importantes para alcançar seus objetivos?", ["Sim", "Não"], key="c12_delegou_tarefas")
        c12_valoriza_colaboracao = st.radio("Você valoriza a colaboração e o trabalho em equipe?", ["Sim", "Não"], key="c12_valoriza_colaboracao")
        c12_aprendeu_confiar = st.radio("Já aprendeu algo valioso ao confiar em outras pessoas para realizar tarefas cruciais?", ["Sim", "Não"], key="c12_aprendeu_confiar")

        st.subheader("Aplicação Prática e Feedback")
        c12_aplicacao = st.radio("Você costuma aplicar o que aprende em situações práticas do dia a dia?", ["Sim", "Não"], key="c12_aplicacao")
        c12_busca_feedback = st.radio("Busca constantemente feedback para melhorar seu desempenho?", ["Sim", "Não"], key="c12_busca_feedback")
        c12_ajustou_feedback = st.radio("Já ajustou seus métodos ou comportamentos com base no feedback recebido?", ["Sim", "Não"], key="c12_ajustou_feedback")

        st.subheader("Diagnóstico Inicial")
        c12_identifica_forcas_fracos = st.radio("Você consegue identificar os pontos fortes e fracos em sua trajetória?", ["Sim", "Não"], key="c12_identifica_forcas_fracos")
        c12_momento_virada = st.radio("Sua história possui um momento de 'virada' ou 'descoberta' que mudou tudo?", ["Sim", "Não"], key="c12_momento_virada")
        c12_final_inspirador = st.radio("Deseja que o final de sua biografia seja inspirador e motivacional para seus leitores?", ["Sim", "Não"], key="c12_final_inspirador")

        c12_virada = st.text_area("Descreva um momento decisivo de virada na sua vida:", key="c12_virada")
        c12_aprendeu = st.text_area("O que esse momento te ensinou?", key="c12_aprendeu")

    # ==================================================
    # CAPÍTULO 13 – LEGADO
    # ==================================================
    with st.expander("Cap. 13 – Legado e Postura Pessoal"):
        c13_iniciativa = st.radio("Você só faz as atividades do seu trabalho quando te mandam ou você sugere novas atividades?", ["Só quando mandam", "Sugiro novas atividades"], key="c13_iniciativa")
        c13_horario = st.radio("Você vai embora pontualmente quando o horário termina ou você conclui aquele relatório que está finalizando?", ["Vou embora pontualmente", "Concluo o que estou fazendo"], key="c13_horario")
        c13_tarefas_extras = st.radio("Você faz tarefas que não são da sua obrigação ou cumpre exatamente o que lhe é atribuído?", ["Faço tarefas extras", "Cumpro exatamente o que é atribuído"], key="c13_tarefas_extras")
        c13_proativo = st.radio("Você é proativo?", ["Sim", "Não"], key="c13_proativo")
        c13_procrastina = st.radio("Você é procrastinador?", ["Sim", "Não"], key="c13_procrastina")
        c13_plano_carreira = st.radio("Você tem perspectivas de plano de carreira ou de estagnação de vida?", ["Plano de carreira", "Estagnação"], key="c13_plano_carreira")
        c13_tempo = st.text_area("O que costuma roubar seu tempo e energia?", key="c13_tempo")
        c13_mudanca = st.text_area("O que você sente que precisa mudar para deixar um legado melhor?", key="c13_mudanca")

    # ==================================================
    # CAPÍTULO 14 – TALENTO E HOBBY
    # ==================================================
    with st.expander("Cap. 14 – Talento, Hobby e Fonte de Paz"):
        c14_hobby = st.text_input("Qual talento ou hobby faz parte da sua história?", key="c14_hobby")
        c14_origem = st.text_area("Como esse talento ou hobby surgiu e quem te influenciou?", key="c14_origem")
        c14_paz = st.text_area("Relate um momento em que esse hobby trouxe paz, cura ou alegria:", key="c14_paz")
        c14_frase_capa = st.text_input("Crie uma frase curta sobre esse talento para a capa do livro:", key="c14_frase_capa")

        c14_tres_prazeres = st.text_area("Liste 3 coisas que você faz naturalmente e que te dão prazer:", key="c14_tres_prazeres")
        c14_servir_inspirar = st.text_area("Reflita: como seu hobby pode servir ou inspirar outras pessoas?", key="c14_servir_inspirar")
        c14_cenario_exposicao = st.text_area("Imagine um cenário onde seu hobby/talento é exposto (exposição, livro, apresentação). Escreva como você se sentiria:", key="c14_cenario_exposicao")
        c14_cinco_conquistas = st.text_area("Liste suas 5 maiores conquistas nesse hobby até hoje, mesmo que sejam simples:", key="c14_cinco_conquistas")
        c14_erro_aprendizado = st.text_area("Escreva um erro que virou aprendizado dentro do seu hobby:", key="c14_erro_aprendizado")
        c14_compartilhou = st.text_area("Anote de que forma você já compartilhou seu talento com alguém (ou como poderia fazer isso):", key="c14_compartilhou")
        c14_carta_familia = st.text_area("Escreva uma carta curta para alguém da sua família falando sobre como você gostaria que lembrassem do seu hobby/talento no futuro:", key="c14_carta_familia")

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
        c15_avaliacao = st.text_area("Para cada papel, avalie se está sendo bem representado ou se há falta (opcional):", key="c15_avaliacao")

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
        c16_exemplo = st.text_area("Cite uma situação em que uma virtude fez diferença na sua vida:", key="c16_exemplo")

    # ==================================================
    # CAPÍTULO 17 – GALARDÃO
    # ==================================================
    with st.expander("Cap. 17 – Galardão e Motivação"):
        c17_conquistas = st.radio(
            "Quando penso em minhas conquistas, considero mais importante:",
            ["O reconhecimento das pessoas", "A fidelidade ao propósito que Deus me deu"],
            key="c17_conquistas"
        )
        c17_dons = st.radio(
            "Ao usar meus dons e talentos, sinto que:",
            ["Estou apenas expressando algo pessoal", "Estou semeando algo que pode gerar frutos eternos"],
            key="c17_dons"
        )
        c17_acoes = st.radio(
            "Em relação às minhas ações diárias, acredito que:",
            ["O valor está no resultado visível", "O valor está na intenção e no amor com que faço"],
            key="c17_acoes"
        )
        c17_desafios = st.radio(
            "Quando enfrento desafios, costumo:",
            ["Desanimar por não ver resultados imediatos", "Permanecer firme, confiando que nada é em vão diante de Deus"],
            key="c17_desafios"
        )
        c17_biografia = st.radio(
            "Ao pensar em minha biografia, percebo que ela:",
            ["É uma coleção de experiências humanas", "É também um testemunho espiritual que aponta para o eterno"],
            key="c17_biografia"
        )
        c17_motivacao = st.radio(
            "O que mais me motiva a continuar escrevendo minha história é:",
            ["O desejo de ser lembrado pelas pessoas", "O desejo de agradar a Deus e inspirar outros"],
            key="c17_motivacao"
        )
        c17_vida_diante_deus = st.radio(
            "Se minha vida fosse lida diante de Deus hoje, eu diria que:",
            ["Ainda tenho muito a construir com propósito", "Tenho vivido de forma fiel, buscando o galardão eterno"],
            key="c17_vida_diante_deus"
        )
        c17_reflexao = st.text_area("Como essa motivação influencia suas decisões diárias?", key="c17_reflexao")

    # ==================================================
    # CAPÍTULO 18 – TERCEIRIZAÇÃO
    # ==================================================
    with st.expander("Cap. 18 – Terceirização e Confiança"):
        c18_sozinho = st.radio(
            "Você costuma assumir todas as tarefas sozinho(a), mesmo quando poderia contar com ajuda?",
            ["Sempre", "Às vezes", "Raramente", "Nunca"],
            key="c18_sozinho"
        )
        c18_peso_decisao = st.radio(
            "Quando precisa decidir entre fazer algo ou delegar, o que mais pesa na sua escolha?",
            ["Controle sobre o resultado", "Tempo disponível", "Custo financeiro", "Confiança em outras pessoas"],
            key="c18_peso_decisao"
        )
        c18_areas_sobrecarga = st.multiselect(
            "Em quais áreas da sua vida você sente maior sobrecarga?",
            ["Profissional", "Familiar", "Espiritual", "Pessoal"],
            key="c18_areas_sobrecarga"
        )
        c18_atividades_outros = st.radio(
            "Você já identificou atividades que outra pessoa poderia fazer melhor ou mais rápido?",
            ["Sim, várias", "Algumas", "Poucas", "Nenhuma"],
            key="c18_atividades_outros"
        )
        c18_sentimento_delegar = st.radio(
            "Quando pensa em terceirizar ou delegar, qual é seu principal sentimento?",
            ["Alívio", "Insegurança", "Dúvida", "Entusiasmo"],
            key="c18_sentimento_delegar"
        )
        c18_delegar_crescimento = st.radio(
            "Você acredita que delegar pode ajudá-lo(a) a crescer e alcançar mais pessoas?",
            ["Sim, totalmente", "Em parte", "Ainda tenho dúvidas", "Não acredito"],
            key="c18_delegar_crescimento"
        )
        c18_frase_realidade = st.radio(
            "Qual dessas frases mais se aproxima da sua realidade atual?",
            ["Faço tudo sozinho(a) e me sinto sobrecarregado(a)",
             "Já delego algumas tarefas, mas ainda me sinto preso(a)",
             "Tenho uma boa rede de apoio e foco no que é essencial",
             "Estou começando a aprender a confiar mais nos outros"],
            key="c18_frase_realidade"
        )
        c18_sabe_pedir_ajuda = st.radio(
            "Ao olhar para sua história, você se considera alguém que sabe pedir ajuda?",
            ["Sim", "Às vezes", "Raramente", "Não"],
            key="c18_sabe_pedir_ajuda"
        )
        c18_desejo_terceirizar = st.radio(
            "O que você mais deseja conquistar ao aprender a terceirizar melhor?",
            ["Mais tempo livre", "Crescimento profissional", "Equilíbrio emocional", "Impacto maior na vida de outras pessoas"],
            key="c18_desejo_terceirizar"
        )
        c18_biografia_frase = st.radio(
            "Se pudesse descrever sua biografia em uma frase hoje, ela seria mais sobre:",
            ["Esforço individual", "Aprendizado e superação", "Cooperação e crescimento", "Transição e descoberta"],
            key="c18_biografia_frase"
        )
        c18_dificuldade = st.text_area("O que mais dificulta para você confiar tarefas a outras pessoas?", key="c18_dificuldade")
        c18_aprendizado = st.text_area("O que você já aprendeu ao delegar ou tentar fazer tudo sozinho(a)?", key="c18_aprendizado")

    # ==================================================
    # CAPÍTULO 19 – FASES DA VIDA
    # ==================================================
    with st.expander("Cap. 19 – Fases da Vida"):
        c19_infancia_brincadeiras = st.text_area("Quais brincadeiras ou jogos que amava na infância?", key="c19_infancia_brincadeiras")
        c19_adolescencia_confianca = st.text_area("O que te fazia confiante e especial na adolescência?", key="c19_adolescencia_confianca")
        c19_juventude_empolgacao = st.text_area("O que te trouxe maior empolgação e motivação na juventude?", key="c19_juventude_empolgacao")
        c19_adulta_auge = st.text_area("Qual foi seu auge na fase adulta, o que estava fazendo?", key="c19_adulta_auge")
        c19_tempo_livre = st.text_area("O que fazia no tempo livre?", key="c19_tempo_livre")
        c19_diferenciava = st.text_area("O que te diferenciava, te deixava único e te surpreendeu com sua própria capacidade?", key="c19_diferenciava")
        c19_algo_queria = st.text_area("Algo que queria, mas não teve chance?", key="c19_algo_queria")
        c19_perdeu_nocao_tempo = st.text_area("O que te fez perder a noção do tempo?", key="c19_perdeu_nocao_tempo")

        st.subheader("Analisando Habilidades e Talentos")
        c19_habilidade_responsabilidade = st.text_area("Que habilidade descobriu ao assumir responsabilidade?", key="c19_habilidade_responsabilidade")
        c19_maior_desafio_superacao = st.text_area("Qual foi seu maior desafio e superação com habilidades?", key="c19_maior_desafio_superacao")
        c19_talento_nao_explorado = st.text_area("Que talento ainda não explorou, mas sabe que possui?", key="c19_talento_nao_explorado")
        c19_tres_talentos = st.text_input("Quais são seus 3 talentos? (separados por vírgula)", key="c19_tres_talentos")
        c19_confiavam_resolver = st.text_area("O que confiavam a você resolver?", key="c19_confiavam_resolver")
        c19_conquista_orgulho = st.text_area("Qual conquista te encheu de orgulho?", key="c19_conquista_orgulho")
        c19_habilidade_mais_resultado = st.text_area("Que habilidade usada gera mais resultado?", key="c19_habilidade_mais_resultado")
        c19_facilidade_dificuldade_outros = st.text_area("O que faz com facilidade, enquanto os outros fazem com dificuldade?", key="c19_facilidade_dificuldade_outros")

        st.subheader("Projetando o Futuro")
        c19_meta = st.text_input("Qual a sua meta? Mês e ano?", key="c19_meta")
        c19_talentos_nao_explorados = st.text_area("Quais talentos não explorados?", key="c19_talentos_nao_explorados")
        c19_escolheria_fazer = st.text_area("O que escolheria fazer o dia inteiro?", key="c19_escolheria_fazer")
        c19_mais_tempo_projeto = st.text_area("O que faria se pudesse dispor de mais tempo a determinado projeto?", key="c19_mais_tempo_projeto")
        c19_como_utiliza_los = st.text_area("Como pode utilizá-los?", key="c19_como_utiliza_los")

    # ==================================================
    # CAPÍTULO 20 – PEQUENAS AÇÕES E CONSTÂNCIA
    # ==================================================
    with st.expander("Cap. 20 – Pequenas Ações e Perseverança"):
        c20_iniciou_acao = st.radio("Você considera que já iniciou alguma pequena ação que transformou sua vida?", ["Sim", "Não"], key="c20_iniciou_acao")
        c20_freq_avaliacao = st.selectbox("Com que frequência você avalia o seu progresso pessoal?", ["Diariamente", "Semanalmente", "Raramente", "Nunca"], key="c20_freq_avaliacao")
        c20_ajustes_rapidos = st.radio("Quando percebe que algo não está funcionando, você costuma fazer ajustes rapidamente?", ["Sempre", "Às vezes", "Raramente", "Nunca"], key="c20_ajustes_rapidos")
        c20_perseverante = st.radio("Você se considera uma pessoa perseverante diante de desafios?", ["Sim", "Parcialmente", "Não"], key="c20_perseverante")
        c20_erro_oportunidade = st.radio("Ao errar, você tende a ver o erro como uma oportunidade de aprendizado?", ["Sempre", "Às vezes", "Nunca"], key="c20_erro_oportunidade")
        c20_experimentar_novas_formas = st.radio("Você costuma experimentar novas formas de agir quando quer mudar algo em sua vida?", ["Sim", "Às vezes", "Não"], key="c20_experimentar_novas_formas")
        c20_habito = st.radio("Você consegue manter um hábito positivo por pelo menos 21 dias seguidos?", ["Sim", "Ainda não, mas estou tentando", "Não"], key="c20_habito")
        c20_comparacao = st.radio("Quando se compara com outras pessoas, isso o(a) motiva ou o(a) desanima?", ["Motiva", "Desanima", "Não costumo me comparar"], key="c20_comparacao")
        c20_celebra_pequenas = st.radio("Você reconhece e celebra suas pequenas conquistas?", ["Sempre", "Às vezes", "Nunca"], key="c20_celebra_pequenas")
        c20_ritmo_satisfatorio = st.radio("Seu ritmo atual de crescimento pessoal é satisfatório para você?", ["Sim", "Parcialmente", "Não"], key="c20_ritmo_satisfatorio")
        c20_exemplo = st.text_area("Cite um pequeno hábito que já trouxe grande mudança:", key="c20_exemplo")
        c20_dificuldade = st.text_area("O que mais dificulta sua constância?", key="c20_dificuldade")

# ==================================================
# BLOCO 4 — CAPÍTULOS 21 A 26
# ==================================================
with tab_c:
    st.header("Bloco C: Estrutura do Livro, Vendas e Experiência")

    # ==================================================
    # CAPÍTULO 21 – PLANEJAMENTO E VISÃO DE FUTURO
    # ==================================================
    with st.expander("Cap. 21 – Planejamento, Tempo e Futuro"):
        c21_foco = st.radio("Você se considera uma pessoa mais voltada para o presente, o passado ou o futuro?", ["Passado", "Presente", "Futuro"], key="c21_foco")
        c21_motivacao_principal = st.selectbox(
            "O que melhor define sua motivação principal na vida?",
            ["Família", "Carreira", "Fé", "Realização pessoal", "Contribuição social"],
            key="c21_motivacao_principal"
        )
        c21_fase_marcante = st.selectbox(
            "Qual fase da sua vida você considera mais marcante até agora?",
            ["Infância", "Adolescência", "Vida adulta", "Atualidade"],
            key="c21_fase_marcante"
        )
        c21_desafio_mudou_visao = st.radio("Você já enfrentou um desafio que mudou sua forma de ver o mundo?", ["Sim", "Não"], key="c21_desafio_mudou_visao")
        c21_trajetoria = st.selectbox(
            "Como você descreveria sua trajetória até aqui?",
            ["Linear e estável", "Cheia de reviravoltas", "Em constante construção"],
            key="c21_trajetoria"
        )
        c21_decisoes_guiadas = st.selectbox(
            "Suas decisões mais importantes foram guiadas por:",
            ["Razão", "Emoção", "Intuição", "Conselhos de outras pessoas"],
            key="c21_decisoes_guiadas"
        )
        c21_aprende = st.radio("Você costuma aprender mais com:", ["Erros", "Acertos", "Observando outras pessoas"], key="c21_aprende")
        c21_maior_aprendizado = st.selectbox(
            "O que melhor representa seu maior aprendizado até hoje?",
            ["Perseverança", "Fé", "Autoconhecimento", "Resiliência"],
            key="c21_maior_aprendizado"
        )
        c21_biografia_inspirar = st.radio("Você gostaria que sua biografia inspirasse outras pessoas?", ["Sim", "Não", "Ainda não pensei sobre isso"], key="c21_biografia_inspirar")
        c21_como_lembrado = st.selectbox(
            "Como você gostaria de ser lembrado(a)?",
            ["Pela sua história", "Pelos suas conquistas", "Pelo impacto que causou", "Pelo amor que compartilhou"],
            key="c21_como_lembrado"
        )
        c21_comecou_registrar = st.radio("Você já começou a registrar sua história de vida?", ["Sim", "Não, mas pretendo", "Ainda não pensei nisso"], key="c21_comecou_registrar")

        st.subheader("Cenário de Publicação")
        c21_cenario = st.radio(
            "Qual cenário você acredita que se dará a sua publicação?",
            [
                "Realista (Ebook gratuito, construção de comunidade, teste de aceitação)",
                "Otimista (Versão física + digital paga, venda via Instagram + Amazon, engajamento com palestras)",
                "Visionário (Presença em grandes livrarias, bestseller, traduções internacionais)"
            ],
            key="c21_cenario"
        )

        c21_sonho = st.text_area("Qual é o principal sonho ou objetivo para os próximos anos?", key="c21_sonho")
        c21_plano = st.text_area("Que passos práticos você acredita que precisa dar a partir de agora?", key="c21_plano")

    # ==================================================
    # CAPÍTULO 22 – FLUXOGRAMA EDITORIAL
    # ==================================================
    with st.expander("Cap. 22 – Estrutura e Fluxograma do Livro"):
        c22_elementos = st.multiselect(
            "Quais elementos você deseja incluir no livro?",
            [
                "Título com essência", "Capa profissional", "Orelhas / Sinopse", "Folha de rosto",
                "Epígrafe", "Dedicatória", "Sumário", "Corpo do texto", "Apêndices", "Fotos",
                "Ficha catalográfica", "QR Code com música", "Agradecimentos finais"
            ],
            key="c22_elementos"
        )
        st.subheader("Checklist adicional")
        c22_titulo_essencia = st.checkbox("O título do seu livro reflete sua essência e trajetória?", key="c22_titulo_essencia")
        c22_capa_comunica = st.checkbox("O design da capa comunica claramente quem você é?", key="c22_capa_comunica")
        c22_orelhas_apresentacao = st.checkbox("Você incluiu uma breve apresentação pessoal nas orelhas do livro?", key="c22_orelhas_apresentacao")
        c22_orelhas_frase = st.checkbox("Há uma frase ou sinopse que desperte curiosidade no leitor?", key="c22_orelhas_frase")
        c22_folha_rosto_clara = st.checkbox("Seu nome e o título estão apresentados de forma clara e profissional?", key="c22_folha_rosto_clara")
        c22_epigrafe = st.checkbox("Você escolheu uma citação ou pensamento que representa sua jornada?", key="c22_epigrafe")
        c22_dedicatoria = st.checkbox("Você mencionou pessoas ou instituições que foram importantes na sua trajetória?", key="c22_dedicatoria")
        c22_sumario_organizado = st.checkbox("Os capítulos estão organizados de forma lógica e envolvente?", key="c22_sumario_organizado")
        c22_corpo_texto = st.checkbox("Sua narrativa está dividida em capítulos coerentes e equilibrados?", key="c22_corpo_texto")
        c22_reflexoes = st.checkbox("Você incluiu reflexões e aprendizados pessoais?", key="c22_reflexoes")
        c22_apendices = st.checkbox("Há fotos, cartas ou documentos que complementam sua história?", key="c22_apendices")
        c22_conclusao = st.checkbox("Você deixou uma mensagem final que inspire o leitor?", key="c22_conclusao")
        c22_biografia_autor = st.checkbox("Sua biografia atual está clara e mostra sua trajetória profissional e pessoal?", key="c22_biografia_autor")
        c22_creditos = st.checkbox("As informações técnicas e de direitos autorais estão completas?", key="c22_creditos")
        c22_contracapa = st.checkbox("A sinopse e os comentários na contracapa despertam interesse pela leitura?", key="c22_contracapa")
        c22_musica = st.checkbox("Você escolheu uma música que representa sua história e pode ser compartilhada por link ou qrcode?", key="c22_musica")
        c22_mapas_mentais = st.checkbox("Haverão mapas mentais explicativos?", key="c22_mapas_mentais")
        c22_registros = st.checkbox("Haverão registros, documentos, fotos e outros complementos para a obra biográfica?", key="c22_registros")

        c22_reflexao = st.text_area("Por que esses elementos são importantes para você?", key="c22_reflexao")

    # ==================================================
    # CAPÍTULO 23 – ORGANIZAÇÃO E DISTRIBUIÇÃO
    # ==================================================
    with st.expander("Cap. 23 – Organização e Distribuição"):
        c23_formato = st.multiselect(
            "Em quais formatos você imagina sua biografia?",
            ["Livro físico", "E-book (PDF)", "Audiobook", "Curso", "Material terapêutico", "Material ministerial"],
            key="c23_formato"
        )
        c23_publicacao = st.radio(
            "Como você pretende publicar?",
            ["Independente", "Plataformas digitais", "Editoras", "Ainda não sei"],
            key="c23_publicacao"
        )
        c23_reflexao = st.text_area("O que mais te anima (ou preocupa) sobre a publicação?", key="c23_reflexao")

    # ==================================================
    # CAPÍTULO 24 – EXPERIÊNCIA VISUAL E APOIOS
    # ==================================================
    with st.expander("Cap. 24 – Experiência Visual e Apoios"):
        c24_mapas = st.radio("Você deseja incluir mapas mentais ou esquemas visuais no livro?", ["Sim", "Não"], key="c24_mapas")
        c24_estetica = st.text_area("Como você imagina a estética visual do livro?", key="c24_estetica")
        c24_apoios = st.multiselect(
            "Quais recursos visuais ou de apoio você gostaria de incluir?",
            ["Ilustrações", "Fotos pessoais", "Gráficos", "Checklists", "Exercícios práticos", "Espaço para anotações"],
            key="c24_apoios"
        )

    # ==================================================
    # CAPÍTULO 25 – VENDA, DIVULGAÇÃO E ALCANCE
    # ==================================================
    with st.expander("Cap. 25 – Vendas, Divulgação e Alcance"):
        st.subheader("Checklist de preparação para vendas")
        c25_email_profissional = st.checkbox("Já criou um e-mail profissional?", key="c25_email_profissional")
        c25_cadastro_kiwify = st.checkbox("Já cadastrou na Kiwify?", key="c25_cadastro_kiwify")
        c25_produto_digital = st.checkbox("Já criou um produto digital ou físico?", key="c25_produto_digital")
        c25_arquivos_membros = st.checkbox("Já subiu arquivos e organizou a área de membros?", key="c25_arquivos_membros")
        c25_link_venda = st.checkbox("Já gerou um link de venda?", key="c25_link_venda")
        c25_link_bio = st.checkbox("Já inseriu o link na bio, stories e posts do Instagram?", key="c25_link_bio")
        c25_renda_passiva = st.checkbox("Já criou uma renda passiva com bônus e promoções?", key="c25_renda_passiva")
        c25_monitoramento = st.checkbox("Já monitorou o desempenho e ajustou estratégias?", key="c25_monitoramento")

        c25_vendas = st.multiselect(
            "Quais etapas de venda você pretende estruturar?",
            ["E-mail profissional", "Página de vendas", "Cadastro em plataforma (ex: Kiwify)", "Link na bio do Instagram", "Conteúdo de divulgação", "Renda passiva"],
            key="c25_vendas"
        )
        c25_reflexao = st.text_area("Como você imagina que esse livro pode alcançar pessoas?", key="c25_reflexao")

    # ==================================================
    # CAPÍTULO 26 – EXPERIÊNCIA SINESTÉSICA E LEGADO FINAL
    # ==================================================
    with st.expander("Cap. 26 – Experiência Sinestésica e Legado"):
        c26_sinestesia = st.multiselect(
            "Quais sentidos você gostaria que seu livro despertasse?",
            [
                "Visão (design, marca-páginas)", "Tato (papel, textura)", "Olfato (aroma, memória afetiva)",
                "Audição (playlist, áudio)", "Paladar (brinde simbólico)", "Experiência de entrega (caixa especial)"
            ],
            key="c26_sinestesia"
        )
        st.subheader("Detalhamento da experiência")
        c26_caixa = st.radio("Seu livro será distribuído numa caixa?", ["Sim", "Não"], key="c26_caixa")
        c26_textura = st.radio("Seu livro terá textura (tato)?", ["Sim", "Não"], key="c26_textura")
        c26_marca_paginas = st.radio("Seu livro terá marca-páginas com a arte da capa (visão)?", ["Sim", "Não"], key="c26_marca_paginas")
        c26_balinhas = st.radio("Seu livro terá balinhas personalizadas (paladar)?", ["Sim", "Não"], key="c26_balinhas")
        c26_perfume = st.radio("Seu livro terá perfume de papel (olfato)?", ["Sim", "Não"], key="c26_perfume")
        c26_musica = st.radio("Seu livro terá música do Spotify incluindo seus gostos prediletos (audição)?", ["Sim", "Não"], key="c26_musica")

        c26_legado = st.text_area("Qual mensagem final você deseja deixar como legado?", key="c26_legado")

def gerar_biografia():
    nome = st.session_state.get('nome_autor', 'Autor Desconhecido')
    data = datetime.now().strftime("%d/%m/%Y")

    # Função auxiliar para obter valor com fallback
    def get(key, default=""):
        return st.session_state.get(key, default)

    # Introdução
    texto = f"""# MINHA BIOGRAFIA
## {nome}
*Gerado em {data}*

---

## INTRODUÇÃO

Meu nome é {nome} e esta é a história da minha vida. Ao longo destas páginas, compartilho minhas experiências, aprendizados, desafios e conquistas. Cada capítulo revela um pouco de quem sou, de onde vim e para onde pretendo ir. Espero que minha jornada possa inspirar você, leitor, a refletir sobre a sua própria história.

---

"""
    # Capítulo 1 – Neuroplasticidade e Mindset
    texto += "## CAPÍTULO 1 – A Jornada da Mente\n\n"
    if get('c1_mudanca') == "Sim":
        texto += "Sempre acreditei que é possível mudar padrões de pensamento. "
    elif get('c1_mudanca') == "Não":
        texto += "Por muito tempo, pensei que não era possível mudar a forma de pensar, mas hoje sei que podemos evoluir. "
    else:
        texto += "Acredito que a mudança de pensamento é um processo possível, embora nem sempre fácil. "

    freq = get('c1_aprendizado', '').lower()
    if freq:
        texto += f"Busco aprender coisas novas {freq}. "

    reacao = get('c1_reacao', '')
    if "Persistir" in reacao:
        texto += "Quando enfrento desafios, costumo persistir e buscar novas estratégias. "
    elif "Desistir" in reacao:
        texto += "Já tive tendência a desistir, mas hoje procuro persistir mais. "
    else:
        texto += "Às vezes espero que os outros resolvam, mas tenho aprendido a agir por mim mesmo. "

    habitos = get('c1_habitos', '')
    if "Sim" in habitos:
        texto += "Já percebi mudanças positivas ao criar novos hábitos. "
    elif "Não" in habitos:
        texto += "Ainda não notei mudanças significativas com novos hábitos, mas continuo tentando. "
    else:
        texto += "Estou no processo de tentar novos hábitos e ver seus efeitos. "

    mentalidade = get('c1_mentalidade', '')
    if "aprender" in mentalidade.lower():
        texto += "Minha mentalidade é de crescimento: acredito que posso aprender e evoluir sempre. "
    elif "nasci" in mentalidade.lower():
        texto += "Às vezes penso que nasci assim e não posso mudar, mas estou aprendendo a evoluir. "
    else:
        texto += "Minha mentalidade depende das circunstâncias, mas busco cultivar uma visão positiva. "

    if get('c1_erro') == "“Posso aprender com isso.”":
        texto += "Quando algo dá errado, procuro enxergar como oportunidade de aprendizado. "
    else:
        texto += "Ainda estou aprendendo a lidar com erros de forma construtiva. "

    if get('c1_afirmacoes') != "Não":
        texto += "Pratico afirmações positivas e isso tem me ajudado a manter o foco. "

    if get('c1_fe_influencia') == "Sim":
        texto += "Minha fé influencia profundamente minha forma de pensar e agir. "
        if get('c1_ora_freq') != "Nunca":
            texto += f"Costumo orar ou meditar {get('c1_ora_freq', '')}. "
        if get('c1_ora_ajuda') != "Não":
            texto += "A oração me ajuda a reorganizar pensamentos e emoções. "

    if get('c1_transformacao') != "Não":
        texto += "Acredito que posso me transformar com tempo e esforço. "

    pratica = get('c1_pratica_fortalecer', '').lower()
    if pratica:
        texto += f"Para fortalecer minha mente, preciso focar em {pratica}. "

    if get('c1_motiva'):
        texto += f"O que mais me motiva a mudar é {get('c1_motiva')}. "

    if get('c1_habito_substituir'):
        texto += f"Gostaria de substituir o hábito de {get('c1_habito_substituir')} por algo mais saudável. "

    if get('c1_renovar'):
        texto += f"Para mim, 'renovar a mente' significa: {get('c1_renovar')}. "

    texto += f"Minha fé em Jesus é a base de tudo; acredito que Ele é a fonte de todas as informações.\n\n"

    # Capítulo 2 – Identidade em Cristo
    texto += "## CAPÍTULO 2 – Quem Eu Sou em Cristo\n\n"
    heranca = get('c2_heranca', '')
    if "herdeiro" in heranca.lower():
        texto += "Sinto-me verdadeiramente herdeiro de Deus, e isso transforma minha identidade. "
    elif "esqueço" in heranca.lower():
        texto += "Às vezes me esqueço de que sou herdeiro de Deus, especialmente nos momentos difíceis. "
    else:
        texto += "Ainda estou compreendendo o que significa ser herdeiro do Pai. "

    desafios = get('c2_desafios', '')
    if "oportunidades" in desafios.lower():
        texto += "Encaro os desafios como oportunidades de manifestar essa herança. "
    elif "medo" in desafios.lower():
        texto += "Reajo aos desafios com medo, mas busco lembrar do meu valor em Cristo. "
    else:
        texto += "Tenho dificuldade em ver propósito nas lutas, mas sei que Deus tem um plano. "

    promessas = get('c2_promessas', '')
    if "vivo" in promessas.lower():
        texto += "Vivo com base nas promessas de Deus e as declaro em minha caminhada. "
    elif "conheço" in promessas.lower():
        texto += "Conheço as promessas, mas nem sempre as aplico no dia a dia. "
    else:
        texto += "Preciso refletir mais sobre as promessas bíblicas. "

    if get('c2_experiencias') and "experimentei" in get('c2_experiencias').lower():
        texto += "Já experimentei paz, provisão e direção como sinais da herança divina. "

    if get('c2_esperanca') and "convicção" in get('c2_esperanca').lower():
        texto += "Tenho convicção de que minha história aponta para uma herança eterna. "
    else:
        texto += "Ainda estou construindo essa esperança. "

    if get('c2_aplicacao') and "consigo" in get('c2_aplicacao').lower():
        texto += "Já consigo escrever minha história com a consciência de ser herdeiro do Pai. "
    else:
        texto += "Estou aprendendo a incluir essa verdade na forma como vejo minha trajetória.\n\n"

    # Capítulo 3 – Corpo e Espírito
    texto += "## CAPÍTULO 3 – Equilíbrio entre Corpo e Espírito\n\n"
    corpo_sim = 0
    if get('c3_rotina') == "Sim": corpo_sim += 1
    if get('c3_instintos') == "Sim": corpo_sim += 1
    if get('c3_atividade_fisica') == "Sim": corpo_sim += 1
    if get('c3_sinais_corpo') == "Sim": corpo_sim += 1
    if get('c3_alimentacao') == "Sim": corpo_sim += 1

    if corpo_sim >= 4:
        texto += "Cuido bem do meu corpo: tenho rotina, atividade física, alimentação equilibrada e atenção aos sinais. "
    elif corpo_sim >= 2:
        texto += "Tenho alguns cuidados com o corpo, mas preciso melhorar em certas áreas. "
    else:
        texto += "Reconheço que preciso cuidar mais do meu corpo, que é templo do Espírito Santo. "

    espirito_sim = 0
    if get('c3_conexao') == "Sim": espirito_sim += 1
    if get('c3_intuicao') == "Sim": espirito_sim += 1
    if get('c3_praticas_espirituais') == "Sim": espirito_sim += 1
    if get('c3_espiritualidade_influencia') == "Sim": espirito_sim += 1
    if get('c3_paz_proposito') == "Sim": espirito_sim += 1

    if espirito_sim >= 4:
        texto += "Minha vida espiritual é forte: sinto conexão com Deus, sigo minha intuição e tenho paz com meu propósito. "
    elif espirito_sim >= 2:
        texto += "Busco manter uma vida espiritual ativa, embora haja altos e baixos. "
    else:
        texto += "Sinto que preciso fortalecer minha espiritualidade, dedicando mais tempo à oração e à meditação. "

    if get('c3_equilibrio'):
        texto += f"Refletindo sobre equilíbrio: {get('c3_equilibrio')} "
    texto += "\n\n"

    # Capítulo 4 – Autoconhecimento
    texto += "## CAPÍTULO 4 – Minha História e Autoconhecimento\n\n"
    if get('c4_autentico'):
        texto += f"Um momento em que me senti verdadeiramente autêntico foi {get('c4_autentico')}. "
    if get('c4_talentos'):
        texto += f"Meus três maiores talentos são {get('c4_talentos')}. "
    if get('c4_valor_pessoal'):
        texto += f"O valor mais importante para mim é {get('c4_valor_pessoal')}. "
    if get('c4_desafio'):
        texto += f"Superei um grande desafio: {get('c4_desafio')}. "
    if get('c4_aprendizado'):
        texto += f"Com isso, aprendi {get('c4_aprendizado')}. "
    if get('c4_decisao_dificil'):
        texto += f"A decisão mais difícil que tomei foi {get('c4_decisao_dificil')}. "
    if get('c4_fracasso'):
        texto += f"Lido com o fracasso da seguinte forma: {get('c4_fracasso')}. "
    if get('c3_palavras_personalidade'):
        texto += f"As palavras que me descrevem são {get('c3_palavras_personalidade')}. "
    if get('c4_influencia_familiar'):
        texto += f"Minha família me influenciou em {get('c4_influencia_familiar')}. "
    if get('c4_paixoes'):
        texto += f"Minhas paixões moldam minha identidade: {get('c4_paixoes')}. "
    texto += "\n\n"

    # Capítulo 5 – Alcance Internacional
    texto += "## CAPÍTULO 5 – Minha História no Mundo\n\n"
    if get('c5_viveu_outro_pais') == "Sim" or get('c5_viajou_outro_pais') == "Sim":
        texto += "Já tive a oportunidade de viver ou viajar para outros países, o que ampliou minha visão de mundo. "
    if get('c5_busca_oportunidades_internacionais') == "Sim":
        texto += "Busco ativamente oportunidades internacionais. "
    if get('c5_perspectiva_global') == "Sim":
        texto += "Considero importante ter uma perspectiva global. "
    if get('c5_conforto_interacao') == "Sim":
        texto += "Sinto-me à vontade com pessoas de diferentes culturas. "
    if get('c5_idioma_estrangeiro') == "Sim":
        texto += "Aprendi um idioma estrangeiro. "
    if get('c5_adaptavel') == "Sim":
        texto += "Sou adaptável a novos ambientes. "
    if get('c5_historia_inspira') == "Sim":
        texto += "Acredito que minha história pode inspirar pessoas de diferentes culturas. "
    if get('c5_legado_internacional') == "Sim":
        texto += "Desejo que meu legado ultrapasse fronteiras. "
    texto += "\n\n"

    # Capítulo 6 – Posição Bíblica
    texto += "## CAPÍTULO 6 – Minha Vida à Luz da Bíblia\n\n"
    if get('c6_crise_oportunidade') == "Sim":
        texto += "Nas crises, busco aprendizado. "
    if get('c6_licoes_dificeis') == "Sim":
        texto += "Consigo identificar lições em situações difíceis. "
    if get('c6_decisoes_refletem_valores') == "Sim":
        texto += "Minhas decisões refletem meus valores. "
    if get('c6_responsavel_consequencias') == "Sim":
        texto += "Sinto-me responsável pelas consequências. "
    if get('c6_emocoes_sinais') == "Sim":
        texto += "Presto atenção às emoções como sinais. "
    if get('c6_reconhecer_erros') == "Sim":
        texto += "Reconheço erros e me arrependo. "
    if get('c6_fiel_invisivel') == "Sim":
        texto += "Mantenho-me fiel mesmo quando ninguém está vendo. "
    if get('c6_reflexao'):
        texto += f"Os princípios bíblicos influenciam minhas decisões: {get('c6_reflexao')}. "
    texto += "\n\n"

    # Capítulo 7 – Trampolim
    texto += "## CAPÍTULO 7 – O Momento de Dar o Salto\n\n"
    if get('c7_dificuldades_forca') == "Sim":
        texto += "Acredito que minhas dificuldades podem se tornar meus maiores trunfos. "
    if get('c7_aprender_erros') == "Sim":
        texto += "Aprendo e cresço com meus erros. "
    if get('c7_construindo_futuro') == "Sim":
        texto += "Estou ativamente construindo o futuro que desejo. "
    if get('c7_proativo') == "Sim":
        texto += "Sou uma pessoa proativa. "
    else:
        texto += "Preciso ser mais proativo. "
    if get('c7_estagnacao') == "Sim":
        texto += f"Sinto estagnação em {get('c7_area', 'alguma área')}. "
    if get('c7_decisao') != "Não":
        texto += f"Sinto que {get('c7_decisao', 'é hora de mudar')}. "
    if get('c7_reflexao'):
        texto += f"O que hoje funciona como trampolim: {get('c7_reflexao')}. "
    texto += "\n\n"

    # Capítulo 8 – Comemoração
    texto += "## CAPÍTULO 8 – Celebrando Cada Passo\n\n"
    if get('c8_celebra') in ["Sempre", "Às vezes"]:
        texto += "Costumo celebrar minhas vitórias, mesmo as pequenas. "
    else:
        texto += "Preciso aprender a celebrar mais minhas conquistas. "
    if get('c8_memoria'):
        texto += f"Uma conquista que marcou minha vida: {get('c8_memoria')}. "
    if get('c8_aprendizado'):
        texto += f"Com ela, aprendi {get('c8_aprendizado')}. "
    texto += "\n\n"

    # Capítulo 9 – Público e Propósito
    texto += "## CAPÍTULO 9 – Para Quem Escrevo e Por Quê\n\n"
    if get('c9_perfil_demografico'):
        texto += f"Meu público-alvo são {get('c9_perfil_demografico')}. "
    if get('c9_publico_opcoes'):
        texto += f"Esta biografia é direcionada a {', '.join(get('c9_publico_opcoes'))}. "
    if get('c9_objetivo_principal'):
        texto += f"Meu objetivo principal é {get('c9_objetivo_principal')}. "
    if get('c9_mensagem_lição'):
        texto += f"Espero que os leitores aprendam {get('c9_mensagem_lição')}. "
    if get('c9_impacto_desejado'):
        texto += f"Quero causar o seguinte impacto: {get('c9_impacto_desejado')}. "
    texto += "\n\n"

    # Capítulo 10 – Currículo e Experiências
    texto += "## CAPÍTULO 10 – Minha Trajetória Profissional e de Vida\n\n"
    if get('c10_cursos'):
        texto += f"Realizei cursos significativos como {get('c10_cursos')}. "
    if get('c10_graduacoes'):
        texto += f"Minha formação inclui {get('c10_graduacoes')}. "
    if get('c10_talentos_naturais'):
        texto += f"Meus talentos naturais são {get('c10_talentos_naturais')}. "
    if get('c10_experiencias_marcantes'):
        texto += f"Experiências marcantes: {get('c10_experiencias_marcantes')}. "
    if get('c10_maiores_desafios'):
        texto += f"Os maiores desafios que enfrentei: {get('c10_maiores_desafios')}. "
    if get('c10_reflexao'):
        texto += f"Tudo isso me prepara para o futuro: {get('c10_reflexao')}. "
    texto += "\n\n"

    # Capítulo 11 – Técnicas de Seleção
    texto += "## CAPÍTULO 11 – Como Escolho e Decido\n\n"
    if get('c11_importante_trabalho'):
        texto += f"No trabalho, o mais importante para mim é {get('c11_importante_trabalho')}. "
    if get('c11_objetivo_profissional'):
        texto += f"Meu objetivo profissional é {get('c11_objetivo_profissional')}. "
    if get('c11_conflitos'):
        texto += f"Lido com conflitos assim: {get('c11_conflitos')}. "
    if get('c11_etica') == "Sim":
        texto += "A ética é determinante em minhas escolhas. "
    if get('c11_contratacoes'):
        texto += f"Para este livro, considero contratar {', '.join(get('c11_contratacoes'))}. "
    texto += "\n\n"

    # Capítulo 12 – Treinamento e Virada
    texto += "## CAPÍTULO 12 – Momentos que Mudaram Tudo\n\n"
    if get('c12_experiencia_transformadora') == "Sim":
        texto += "Passei por experiências que me transformaram profundamente. "
    if get('c12_momento_virada') == "Sim":
        texto += "Minha história tem um momento de virada marcante. "
    if get('c12_virada'):
        texto += f"Esse momento foi: {get('c12_virada')}. "
    if get('c12_aprendeu'):
        texto += f"Aprendi que {get('c12_aprendeu')}. "
    texto += "\n\n"

    # Capítulo 13 – Legado
    texto += "## CAPÍTULO 13 – O Legado que Quero Deixar\n\n"
    if get('c13_proativo') == "Sim":
        texto += "Sou proativo e isso me ajuda a construir meu legado. "
    if get('c13_procrastina') == "Sim":
        texto += "A procrastinação é um desafio que enfrento. "
    if get('c13_tempo'):
        texto += f"O que rouba meu tempo: {get('c13_tempo')}. "
    if get('c13_mudanca'):
        texto += f"Preciso mudar {get('c13_mudanca')} para deixar um legado melhor. "
    texto += "\n\n"

    # Capítulo 14 – Talento e Hobby
    texto += "## CAPÍTULO 14 – Meu Talento, Minha Paz\n\n"
    if get('c14_hobby'):
        texto += f"Um hobby/talento que faz parte da minha história é {get('c14_hobby')}. "
    if get('c14_origem'):
        texto += f"Surgiu assim: {get('c14_origem')}. "
    if get('c14_paz'):
        texto += f"Em um momento difícil, esse hobby me trouxe paz: {get('c14_paz')}. "
    if get('c14_frase_capa'):
        texto += f"Se fosse uma frase de capa, seria: {get('c14_frase_capa')}. "
    texto += "\n\n"

    # Capítulo 15 – Papéis Sociais
    texto += "## CAPÍTULO 15 – Meus Papéis na Vida\n\n"
    if get('c15_escolhidos'):
        texto += f"Exerço os papéis de {', '.join(get('c15_escolhidos'))}. "
    if get('c15_reflexao'):
        texto += f"Esses papéis me influenciam porque {get('c15_reflexao')}. "
    texto += "\n\n"

    # Capítulo 16 – Virtudes
    texto += "## CAPÍTULO 16 – Minhas Virtudes\n\n"
    if get('c16_virtudes'):
        texto += f"As virtudes que reconheço em mim ou desejo desenvolver são {', '.join(get('c16_virtudes'))}. "
    if get('c16_exemplo'):
        texto += f"Um exemplo de virtude em ação: {get('c16_exemplo')}. "
    texto += "\n\n"

    # Capítulo 17 – Galardão
    texto += "## CAPÍTULO 17 – O que me Move\n\n"
    if get('c17_conquistas'):
        texto += f"Sobre minhas conquistas, considero mais importante {get('c17_conquistas')}. "
    if get('c17_motivacao'):
        texto += f"Minha maior motivação é {get('c17_motivacao')}. "
    if get('c17_reflexao'):
        texto += f"Isso influencia minhas decisões: {get('c17_reflexao')}. "
    texto += "\n\n"

    # Capítulo 18 – Terceirizar
    texto += "## CAPÍTULO 18 – Aprender a Delegar\n\n"
    if get('c18_sozinho') in ["Sempre", "Às vezes"]:
        texto += "Costumo assumir tudo sozinho, mas estou aprendendo a delegar. "
    if get('c18_sentimento_delegar'):
        texto += f"Meu sentimento ao delegar é {get('c18_sentimento_delegar')}. "
    if get('c18_dificuldade'):
        texto += f"O que mais dificulta: {get('c18_dificuldade')}. "
    if get('c18_aprendizado'):
        texto += f"Já aprendi que {get('c18_aprendizado')}. "
    texto += "\n\n"

    # Capítulo 19 – Fases da Vida
    texto += "## CAPÍTULO 19 – Minhas Fases\n\n"
    if get('c19_infancia_brincadeiras'):
        texto += f"Na infância, amava {get('c19_infancia_brincadeiras')}. "
    if get('c19_adolescencia_confianca'):
        texto += f"Na adolescência, o que me fazia confiante era {get('c19_adolescencia_confianca')}. "
    if get('c19_adulta_auge'):
        texto += f"Meu auge na vida adulta foi {get('c19_adulta_auge')}. "
    if get('c19_tres_talentos'):
        texto += f"Meus talentos são {get('c19_tres_talentos')}. "
    if get('c19_meta'):
        texto += f"Minha meta atual é {get('c19_meta')}. "
    texto += "\n\n"

    # Capítulo 20 – Pequenas Ações
    texto += "## CAPÍTULO 20 – O Poder das Pequenas Coisas\n\n"
    if get('c20_iniciou_acao') == "Sim":
        texto += "Já vivi uma pequena ação que transformou minha vida. "
    if get('c20_exemplo'):
        texto += f"Um exemplo: {get('c20_exemplo')}. "
    if get('c20_dificuldade'):
        texto += f"Minha maior dificuldade para manter constância é {get('c20_dificuldade')}. "
    if get('c20_ritmo_satisfatorio') == "Sim":
        texto += "Meu ritmo atual de crescimento é satisfatório. "
    else:
        texto += "Ainda busco um ritmo mais consistente. "
    texto += "\n\n"

    # Capítulo 21 – Planejamento e Futuro
    texto += "## CAPÍTULO 21 – Olhando para o Futuro\n\n"
    if get('c21_foco'):
        texto += f"Vivo mais focado no {get('c21_foco')}. "
    if get('c21_sonho'):
        texto += f"Meu principal sonho é {get('c21_sonho')}. "
    if get('c21_plano'):
        texto += f"Os passos que preciso dar: {get('c21_plano')}. "
    texto += "\n\n"

    # Capítulo 22 – Estrutura do Livro
    texto += "## CAPÍTULO 22 – Como Será Este Livro\n\n"
    if get('c22_elementos'):
        texto += f"Quero incluir {', '.join(get('c22_elementos'))} no livro. "
    if get('c22_reflexao'):
        texto += f"Esses elementos são importantes porque {get('c22_reflexao')}. "
    texto += "\n\n"

    # Capítulo 23 – Distribuição
    texto += "## CAPÍTULO 23 – Publicação e Alcance\n\n"
    if get('c23_formato'):
        texto += f"Imagino minha biografia em {', '.join(get('c23_formato'))}. "
    if get('c23_publicacao'):
        texto += f"Pretendo publicar de forma {get('c23_publicacao')}. "
    if get('c23_reflexao'):
        texto += f"Sobre a publicação: {get('c23_reflexao')}. "
    texto += "\n\n"

    # Capítulo 24 – Visual
    texto += "## CAPÍTULO 24 – A Estética do Livro\n\n"
    if get('c24_mapas') == "Sim":
        texto += "Gostaria de incluir mapas mentais. "
    if get('c24_estetica'):
        texto += f"Imagino a estética assim: {get('c24_estetica')}. "
    if get('c24_apoios'):
        texto += f"Recursos visuais: {', '.join(get('c24_apoios'))}. "
    texto += "\n\n"

    # Capítulo 25 – Vendas
    texto += "## CAPÍTULO 25 – Como Farei Chegar às Pessoas\n\n"
    if get('c25_vendas'):
        texto += f"Pretendo estruturar vendas por {', '.join(get('c25_vendas'))}. "
    if get('c25_reflexao'):
        texto += f"Acredito que o livro pode alcançar pessoas porque {get('c25_reflexao')}. "
    texto += "\n\n"

    # Capítulo 26 – Experiência Sensorial
    texto += "## CAPÍTULO 26 – Uma Experiência Completa\n\n"
    if get('c26_sinestesia'):
        texto += f"Quero que o livro desperte os sentidos: {', '.join(get('c26_sinestesia'))}. "
    if get('c26_legado'):
        texto += f"Minha mensagem final de legado é: {get('c26_legado')}. "
    texto += "\n\n"

    # Conclusão
    texto += "---\n"
    texto += "## CONCLUSÃO\n\n"
    texto += "Esta é a minha história, contada a partir das minhas próprias reflexões. Cada capítulo revela um pouco de quem sou, do que acredito e do que sonho. Espero que esta biografia possa inspirar outros e servir como um registro genuíno da minha jornada. Que as próximas páginas da minha vida sejam escritas com sabedoria, propósito e amor.\n\n"
    texto += f"*{nome}*"

    return texto

# ==================================================
# BOTÃO GERADOR DO LIVRO (na barra lateral)
# ==================================================
st.sidebar.markdown("---")
st.sidebar.header("📖 Gerar livro")

if st.sidebar.button("Gerar biografia em texto"):
    st.session_state.livro_gerado = gerar_biografia()
    st.sidebar.success("Biografia gerada! Vá para a aba '📖 Livro Gerado'.")

# ==================================================
# ABA DO LIVRO GERADO
# ==================================================
with tab_d:
    st.header("Sua Biografia Gerada")
    if st.session_state.livro_gerado:
        st.markdown(st.session_state.livro_gerado)
        # Botão para download
        st.download_button(
            label="📥 Baixar biografia como .txt",
            data=st.session_state.livro_gerado,
            file_name=f"biografia_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )
    else:
        st.info("Clique no botão 'Gerar biografia em texto' na barra lateral para criar sua biografia.")
