import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Biografia App", layout="wide")
st.title("📘 Minha Biografia")

# Inicializa o estado para o livro gerado
if 'livro_gerado' not in st.session_state:
    st.session_state.livro_gerado = ""

# --- FUNÇÃO DE BUSCA SEGURA ---
def get_safe(key, default=""):
    """Recupera o valor do session_state garantindo que ele exista."""
    valor = st.session_state.get(key)
    if valor:
        if isinstance(valor, list):
            return ", ".join(valor) if len(valor) > 0 else default
        return valor
    return default

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
    st.header("Bloco A: Fundamentos e Identidade")
    st.text_input("Nome Completo:", "Autor Desconhecido", key='nome_autor')

    with st.expander("Cap. 1 a 3 – Mente, Identidade e Organização"):
        col1, col2 = st.columns(2)
        with col1:
            st.radio("É possível mudar padrões de pensamento?", ["Sim", "Não", "Não tenho certeza"], key='c1_mudanca')
            st.selectbox("Frequência de aprendizado:", ["Diariamente", "Semanalmente", "Raramente", "Nunca"], key='c1_aprendizado')
            st.radio("Reação a desafios:", ["Desistir facilmente", "Persistir e buscar novas estratégias", "Esperar que alguém resolva"], key='c1_reacao')
            st.text_area("O que significa 'renovar a mente'?", key='c1_renovar')
        with col2:
            st.radio("Relação com herança espiritual:", ["Sinto-me herdeiro(a) de Deus", "Às vezes me esqueço", "Ainda não compreendo"], key='c2_heranca')
            st.radio("Como encara os desafios?", ["Como oportunidade de crescimento", "Com medo ou insegurança"], key='c2_desafios')
            st.multiselect("Práticas para o corpo:", ["Atividade física", "Alimentação equilibrada", "Sono regulado"], key='c3_corpo')
            st.multiselect("Práticas para o espírito:", ["Oração", "Meditação", "Leitura espiritual"], key='c3_espirito')

    with st.expander("Cap. 4 a 10 – Talentos, Impacto e Histórico"):
        st.text_area("Um momento em que foi autêntico(a):", key='c4_autentico')
        st.text_input("Seus três maiores talentos:", key='c4_talentos')
        st.text_area("Um desafio significativo superado:", key='c4_desafio')
        st.text_area("Por que sua história merece ser contada?", key='c5_reflexao')
        st.text_area("Descreva uma conquista marcante (Cap 8):", key='c8_memoria')
        st.text_area("Formação acadêmica e Experiências (Cap 10):", key='c10_formacao')

# ==================================================
# BLOCO B – CAPÍTULOS 11 A 20
# ==================================================
with tab_b:
    st.header("Bloco B: Seleção, Legado e Relações")
    
    with st.expander("Cap. 11 a 14 – Decisões e Hobby"):
        st.text_area("Critérios para selecionar pessoas/projetos:", key='c11_criterios')
        st.text_area("Momento decisivo de virada:", key='c12_virada')
        st.text_input("Qual o seu Hobby principal?", key='c14_hobby')
        st.text_area("Como surgiu esse hobby e quem influenciou?", key='c14_origem')
        st.text_area("Momento em que o hobby trouxe paz:", key='c14_paz')

    with st.expander("Cap. 15 a 16 – Papéis e Virtudes"):
        st.multiselect("Papéis que exerce hoje:", ["Mãe/Pai", "Filho(a)", "Líder", "Amigo(a)", "Mentor"], key='c15_escolhidos')
        st.multiselect("Virtudes principais:", ["Perdão", "Honra", "Gratidão", "Paciência", "Coragem", "Disciplina"], key='c16_virtudes')
        st.text_area("Exemplo de virtude em ação:", key='c16_exemplo')

    with st.expander("Cap. 19 a 20 – Fases e Hábitos"):
        st.text_input("Brincadeira de Infância:", key='c19_infancia')
        st.text_area("O que marcou sua adolescência?", key='c19_adolescencia')
        st.text_area("Um hábito que trouxe mudança real:", key='c20_exemplo')

# ==================================================
# BLOCO C – CAPÍTULOS 21 A 26
# ==================================================
with tab_c:
    st.header("Bloco C: Planejamento e Futuro")
    with st.expander("Cap. 21 a 26 – Visão e Mensagem Final"):
        st.text_area("Principal sonho para os próximos anos:", key='c21_sonho')
        st.text_area("Passos práticos necessários:", key='c21_plano')
        st.multiselect("Sentidos que o livro deve despertar:", ["Visão", "Tato", "Olfato", "Audição"], key='c26_sinestesia')
        st.text_area("Qual mensagem final deseja deixar como legado?", key='c26_legado')

# ==================================================
# LÓGICA DE NARRATIVA (INSPIRADA NO SEU ARQUIVO)
# ==================================================

def gerar_biografia_hobby():
    nome = get_safe('nome_autor')
    texto = f"""# OS PASSATEMPOS DE {nome.upper()}
## Uma Jornada de Descoberta e Prazer
*Gerado em {datetime.now().strftime("%d/%m/%Y")}*

### INTRODUÇÃO
Para **{nome}**, passatempos são fontes de vida. Momentos em que a alma se reconecta.

## 🌟 MEU HOBBY FAVORITO
{nome} adora **{get_safe('c14_hobby')}**. Esta paixão começou {get_safe('c14_origem')}. Em um momento marcante, trouxe paz: "{get_safe('c14_paz')}".

## ✨ TALENTOS E AUTENTICIDADE
Além do hobby, possui talentos como {get_safe('c4_talentos')}. Um momento de pura autenticidade foi quando {get_safe('c4_autentico')}. Superou o desafio de {get_safe('c4_desafio')}, aprendendo o valor da resiliência.

## 🌱 RAÍZES E HÁBITOS
Desde a infância, brincando de {get_safe('c19_infancia')}, até hoje, cultivando o hábito de {get_safe('c20_exemplo')}, sua trajetória é constante.

**Mensagem Final:** {get_safe('c26_legado')}"""
    return texto

def gerar_biografia_profissional():
    nome = get_safe('nome_autor')
    texto = f"""# PERFIL PROFISSIONAL DE {nome.upper()}
## Trajetória e Competências

**Formação e Experiência:** {get_safe('c10_formacao')}
**Momento de Virada:** {get_safe('c12_virada')}

{nome} opera sob os critérios de {get_safe('c11_criterios')}, pautando sua carreira nas virtudes: {get_safe('c16_virtudes')}. 
Acredita que renovar a mente é "{get_safe('c1_renovar')}".

**Visão de Futuro:** Planeja alcançar {get_safe('c21_sonho')} através de {get_safe('c21_plano')}.
**Legado:** {get_safe('c26_legado')}"""
    return texto

def gerar_biografia_infantil(genero):
    nome = get_safe('nome_autor')
    art, pers = ("uma", "princesa") if genero == "Menina" else ("um", "príncipe")
    pron = "ela" if genero == "Menina" else "ele"
    
    texto = f"""# 🌈 A GRANDE JORNADA DE {nome.upper()}
## Uma história de aprendizado e propósito

Era uma vez {art} {pers} muito especial chamad{'a' if genero=='Menina' else 'o'} **{nome}**. {pron.capitalize()} vivia num lugar onde sonhos eram sementes.

## 📖 O PODER DE APRENDER
{nome} descobriu que podia aprender coisas novas {get_safe('c1_aprendizado').lower()}. Quando surgia um desafio, {pron} persistia com coragem. 

## 👑 IDENTIDADE REAL
{nome} sabe que é filh{'a' if genero=='Menina' else 'o'} do Rei do Universo. Encara dificuldades como degraus para ficar mais forte.

## ✨ DONS E VIRTUDES
Com seus talentos ({get_safe('c4_talentos')}), {nome} ajuda muita gente. Carrega virtudes como {get_safe('c16_virtudes')}.

## 🕰️ O TEMPO
Tudo começou brincando de {get_safe('c19_infancia')}. Hoje, exerce com amor o papel de {get_safe('c15_escolhidos')}.

**Mensagem para o Mundo:** "{get_safe('c26_legado')}" """
    return texto

# ==================================================
# SIDEBAR E GERAÇÃO
# ==================================================
with st.sidebar:
    st.header("📖 Gerar Biografia")
    estilo = st.selectbox("Estilo da narrativa:", ["Hobby / Passatempo", "Profissional", "Infantil"])
    gen = st.radio("Gênero (Para Infantil):", ["Menina", "Menino"]) if estilo == "Infantil" else None
    
    if st.button("Gerar agora"):
        if estilo == "Hobby / Passatempo":
            st.session_state.livro_gerado = gerar_biografia_hobby()
        elif estilo == "Profissional":
            st.session_state.livro_gerado = gerar_biografia_profissional()
        else:
            st.session_state.livro_gerado = gerar_biografia_infantil(gen)
        st.success("Biografia gerada!")

# ABA DO LIVRO
with tab_d:
    if st.session_state.livro_gerado:
        st.markdown(st.session_state.livro_gerado)
        st.download_button("📥 Baixar Biografia", st.session_state.livro_gerado, file_name="biografia.txt")
    else:
        st.info("Preencha as informações e clique em 'Gerar' na lateral.")

















