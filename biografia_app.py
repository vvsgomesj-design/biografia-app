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
# ==================================================
# BLOCO 3 — CAPÍTULOS 11 A 15
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
            [
                "Editora",
                "Ghost Writer",
                "Designer",
                "Gráfica",
                "Nenhum"
            ]
        )

        c11_criterios = st.text_area(
            "Quais critérios você considera essenciais ao selecionar pessoas ou projetos?"
        )

    # ==================================================
    # CAPÍTULO 12 – TÉCNICAS DE TREINAMENTO
    # ==================================================
    with st.expander("Cap. 12 – Treinamento, Aprendizado e Virada"):
        c12_virada = st.text_area(
            "Descreva um momento decisivo de virada na sua vida:"
        )

        c12_aprendeu = st.text_area(
            "O que esse momento te ensinou?"
        )

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

        c13_tempo = st.text_area(
            "O que costuma roubar seu tempo e energia?"
        )

        c13_mudanca = st.text_area(
            "O que você sente que precisa mudar para deixar um legado melhor?"
        )

    # ==================================================
    # CAPÍTULO 14 – TALENTO E HOBBY
    # ==================================================
    with st.expander("Cap. 14 – Talento, Hobby e Fonte de Paz"):
        c14_hobby = st.text_input(
            "Qual talento ou hobby faz parte da sua história?"
        )

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

        c15_reflexao = st.text_area(
            "Como esses papéis influenciam quem você é?"
        )
# ==================================================
# BLOCO 4 — CAPÍTULOS 16 A 21
# ==================================================

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

# =========================
# TAB_C
# =========================
with tab_c:

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

        c21_sonho = st.text_area(
            "Qual é o principal sonho ou objetivo para os próximos anos?"
        )

        c21_plano = st.text_area(
            "Que passos práticos você acredita que precisa dar a partir de agora?"
        )
# ==================================================
# BLOCO 5 — CAPÍTULOS 22 A 26
# ==================================================
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
