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
# COLE AQUI TODO O SEU CÓDIGO DE COLETA DE DADOS
# (capítulos 1 a 26 com st.radio, st.text_input, etc.)
# Isso deve preencher o st.session_state com as respostas.
# ==================================================

# ==================================================
# FUNÇÕES DE GERAÇÃO (cada uma com seu estilo)
# ==================================================

def gerar_biografia_hobby():
    nome = st.session_state.get('nome_autor', 'Autor Desconhecido')
    data = datetime.now().strftime("%d/%m/%Y")

    def get(key, default=""):
        return st.session_state.get(key, default)

    texto = f"""# Os Passatempos de {nome}
## O que faz o coração bater mais forte
*Gerado em {data}*

---

### Introdução

Você já parou para pensar no que realmente faz a gente se sentir vivo? Para **{nome}**, a resposta está nos pequenos prazeres, nas atividades que trazem paz, alegria e desconexão do mundo. Vamos conhecer um pouco desse universo pessoal.

---
"""

    # Hobby principal
    if get('c14_hobby'):
        texto += f"## Meu Hobby Favorito\n\n"
        texto += f"{nome} adora {get('c14_hobby')}. "
        if get('c14_origem'):
            texto += f"Essa paixão começou {get('c14_origem')}. "
        if get('c14_tres_prazeres'):
            texto += f"\n\nAlgumas coisas que faz naturalmente e que dão prazer: {get('c14_tres_prazeres')}.\n"
        texto += "\n"

    if get('c14_paz'):
        texto += f"## Um Momento de Paz\n\n{get('c14_paz')}\n\n"
    if get('c14_cinco_conquistas'):
        texto += f"## Conquistas (mesmo as pequenas)\n\n{get('c14_cinco_conquistas')}\n\n"
    if get('c14_erro_aprendizado'):
        texto += f"## Aprendizados\n\n{get('c14_erro_aprendizado')}\n\n"
    if get('c14_compartilhou'):
        texto += f"## Compartilhando com o Mundo\n\n{get('c14_compartilhou')}\n\n"
    if get('c14_frase_capa'):
        texto += f"## Uma Frase que me Representa\n\n*\"{get('c14_frase_capa')}\"*\n\n"
    if get('c14_carta_familia'):
        texto += f"## Carta para Quem Amo\n\n{get('c14_carta_familia')}\n\n"

    if get('c19_infancia_brincadeiras'):
        texto += f"## Desde Pequeno...\n\nNa infância, {nome} amava {get('c19_infancia_brincadeiras')}. "
    if get('c19_adolescencia_confianca'):
        texto += f"Na adolescência, o que fazia sentir-se especial era {get('c19_adolescencia_confianca')}. "
    if get('c19_perdeu_nocao_tempo'):
        texto += f"O que fazia perder a noção do tempo? {get('c19_perdeu_nocao_tempo')}. "
    texto += "\n\n---\n"
    texto += f"## Para Sempre...\n\nEsses são os passatempos que fazem parte da história de {nome}. Mais do que atividades, são pedaços da alma, momentos de cura, alegria e expressão. Que venham muitos outros hobbies e descobertas!\n\n*Com carinho, {nome}*"
    return texto


def gerar_biografia_profissional():
    nome = st.session_state.get('nome_autor', 'Autor Desconhecido')
    data = datetime.now().strftime("%d/%m/%Y")

    def get(key, default=""):
        return st.session_state.get(key, default)

    texto = f"""# Perfil Profissional de {nome}
## Trajetória, Competências e Realizações
*Gerado em {data}*

---

## Resumo Profissional

**{nome}** construiu uma trajetória marcada por dedicação, aprendizado contínuo e resultados expressivos. Ao longo da carreira, desenvolveu competências técnicas e comportamentais que o(a) tornam um profissional diferenciado.

---
"""
    if get('c10_cursos') or get('c10_graduacoes'):
        texto += "## Formação Acadêmica e Capacitação\n\n"
        if get('c10_graduacoes'):
            texto += f"- **Graduações:** {get('c10_graduacoes')}\n"
        if get('c10_cursos'):
            texto += f"- **Cursos e treinamentos:** {get('c10_cursos')}\n"
        if get('c10_certificacoes'):
            texto += f"- **Certificações relevantes:** {get('c10_certificacoes')}\n"
        texto += "\n"

    if get('c10_experiencias_marcantes'):
        texto += "## Experiências Profissionais Relevantes\n\n"
        texto += f"{get('c10_experiencias_marcantes')}\n\n"

    if get('c4_talentos') or get('c10_talentos_naturais'):
        texto += "## Competências e Habilidades\n\n"
        if get('c4_talentos'):
            texto += f"- **Principais talentos:** {get('c4_talentos')}\n"
        if get('c10_talentos_naturais'):
            texto += f"- **Habilidades desenvolvidas:** {get('c10_talentos_naturais')}\n"
        if get('c10_atividades_destaque'):
            texto += f"- **Áreas de destaque:** {get('c10_atividades_destaque')}\n"
        texto += "\n"

    if get('c4_desafio') or get('c10_maiores_desafios'):
        texto += "## Desafios e Superações\n\n"
        if get('c4_desafio'):
            texto += f"**Desafio significativo:** {get('c4_desafio')}\n"
        if get('c4_aprendizado'):
            texto += f"**Aprendizado:** {get('c4_aprendizado')}\n"
        if get('c10_maiores_desafios'):
            texto += f"**Outros desafios:** {get('c10_maiores_desafios')}\n"
        texto += "\n"

    if get('c10_aplicacao_conhecimento'):
        texto += "## Aplicação do Conhecimento\n\n"
        texto += f"{get('c10_aplicacao_conhecimento')}\n\n"

    if get('c10_resultados_concretos'):
        texto += "## Resultados Alcançados\n\n"
        texto += f"{get('c10_resultados_concretos')}\n\n"

    if get('c11_objetivo_profissional'):
        texto += "## Objetivo Profissional\n\n"
        texto += f"{get('c11_objetivo_profissional')}\n\n"

    if get('c21_sonho') or get('c21_plano'):
        texto += "## Perspectivas Futuras\n\n"
        if get('c21_sonho'):
            texto += f"**Sonho/objetivo:** {get('c21_sonho')}\n"
        if get('c21_plano'):
            texto += f"**Passos planejados:** {get('c21_plano')}\n"
        texto += "\n"

    texto += "---\n## Considerações Finais\n\n"
    texto += f"{nome} segue em constante evolução, buscando novos desafios e contribuindo com excelência em todas as áreas em que atua. Esta trajetória é um testemunho de comprometimento, paixão pelo que faz e visão de futuro.\n\n*{nome}*"
    return texto


def gerar_biografia_infantil(genero):
    nome = st.session_state.get('nome_autor', 'Autor Desconhecido')
    data = datetime.now().strftime("%d/%m/%Y")

    # Definir pronomes e artigos conforme o gênero
    if genero == "Menina":
        artigo = "uma"
        pronome_sujeito = "ela"
        pronome_objeto = "a"
        pronome_possessivo = "sua"
        artigo_definido = "a"
    else:  # Menino
        artigo = "um"
        pronome_sujeito = "ele"
        pronome_objeto = "o"
        pronome_possessivo = "seu"
        artigo_definido = "o"

    def get(key, default=""):
        return st.session_state.get(key, default)

    texto = f"""# A História de {nome}
## Contada de um jeito bem gostoso de ler
*Gerado em {data}*

---

### Era uma vez...

Era uma vez {artigo} pessoa muito especial chamada **{nome}**. {pronome_sujeito.capitalize()} tinha um coração cheio de sonhos e uma mente curiosa, sempre pronta para aprender coisas novas. Vamos conhecer um pouco da sua história?

---
"""

    # Capítulo 1
    texto += "## Capítulo 1 – A Mente que Aprende\n\n"
    if get('c1_mudanca') == "Sim":
        texto += f"{nome} sabia que podia mudar e aprender coisas novas todos os dias. "
    else:
        texto += f"{nome} estava descobrindo que aprender coisas novas é uma grande aventura. "
    if get('c1_aprendizado') != "Nunca":
        texto += f"{pronome_sujeito.capitalize()} gostava de aprender {get('c1_aprendizado', '').lower()}. "
    if "Persistir" in get('c1_reacao', ''):
        texto += f"Quando um desafio aparecia, {pronome_sujeito} não desistia: tentava de novo, de um jeito diferente. "
    if get('c1_habitos') == "Sim":
        texto += f"Já percebeu que, quando criava novos hábitos, coisas boas aconteciam. "
    if get('c1_motiva'):
        texto += f"O que mais {pronome_objeto} motivava a mudar era {get('c1_motiva')}. "
    texto += "\n\n"

    # Capítulo 2 – Identidade
    texto += "## Capítulo 2 – Quem Eu Sou\n\n"
    if "herdeiro" in get('c2_heranca', '').lower():
        texto += f"{nome} sabia que era muito especial: filho amado de Deus, herdeiro de um grande Rei! "
    if "oportunidades" in get('c2_desafios', '').lower():
        texto += f"Quando enfrentava dificuldades, lembrava que podia crescer com elas. "
    if "promessas" in get('c2_promessas', '').lower():
        texto += f"Guardava no coração as promessas de Deus, como um tesouro. "
    texto += "\n\n"

    # Capítulo 3 – Corpo e Espírito
    texto += "## Capítulo 3 – O Corpo e o Coração\n\n"
    corpo_sim = sum([
        get('c3_rotina') == "Sim",
        get('c3_atividade_fisica') == "Sim",
        get('c3_alimentacao') == "Sim"
    ])
    if corpo_sim >= 2:
        texto += f"{nome} cuidava bem do {pronome_possessivo} corpo, como quem cuida de um jardim. "
    else:
        texto += f"{nome} estava aprendendo a cuidar melhor do {pronome_possessivo} corpo. "
    if get('c3_conexao') == "Sim":
        texto += f"Também gostava de conversar com Deus e sentir paz no coração. "
    if get('c3_paz_proposito') == "Sim":
        texto += f"Sabia que tinha um propósito especial. "
    texto += "\n\n"

    # Capítulo 4 – Talentos
    if get('c4_talentos'):
        texto += f"## Capítulo 4 – Talentos Especiais\n\n"
        texto += f"{nome} tinha talentos incríveis, como {get('c4_talentos')}. "
    if get('c4_desafio'):
        texto += f"Um dia, enfrentou um desafio: {get('c4_desafio')}. "
    if get('c4_aprendizado'):
        texto += f"Com isso, aprendeu que {get('c4_aprendizado')}. "
    texto += "\n\n"

    # Capítulo 8 – Conquistas
    if get('c8_memoria'):
        texto += f"## Capítulo 8 – Uma Conquista Muito Especial\n\n"
        texto += f"Um momento que marcou {pronome_possessivo} vida foi: {get('c8_memoria')}. "
    if get('c8_aprendizado'):
        texto += f"Com essa conquista, aprendeu que {get('c8_aprendizado')}. "
    texto += "\n\n"

    # Capítulo 14 – Hobby
    if get('c14_hobby'):
        texto += f"## Capítulo 14 – {artigo_definido.capitalize()} Passatempo Preferido\n\n"
        texto += f"Nas horas vagas, {nome} adorava {get('c14_hobby')}. "
    if get('c14_origem'):
        texto += f"Essa paixão começou {get('c14_origem')}. "
    if get('c14_paz'):
        texto += f"Era um momento de paz e alegria, como quando {get('c14_paz')}. "
    texto += "\n\n"

    # Capítulo 19 – Infância
    if get('c19_infancia_brincadeiras'):
        texto += f"## Capítulo 19 – Quando Era Pequeno(a)\n\n"
        texto += f"Quando {pronome_sujeito} era pequeno(a), adorava {get('c19_infancia_brincadeiras')}. "
    if get('c19_adolescencia_confianca'):
        texto += f"Na adolescência, o que fazia {pronome_objeto} sentir-se especial era {get('c19_adolescencia_confianca')}. "
    texto += "\n\n"

    # Conclusão
    texto += "---\n"
    texto += "## E viveram felizes para sempre...\n\n"
    texto += f"Essa é a história de {nome}, {artigo} pessoa que continua escrevendo novos capítulos todos os dias. E quem sabe um dia você também não escreve a sua? Afinal, cada um de nós tem uma história única e especial!\n\n"
    texto += f"*Fim – com carinho para {nome}*"
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
    else:
        st.session_state.livro_gerado = gerar_biografia_infantil(genero)
    st.sidebar.success("Biografia gerada! Vá para a aba '📖 Livro Gerado'.")


