import streamlit as st
from datetime import datetime

# --- CONFIGURAÇÃO E ESTILO ---
st.set_page_config(page_title="Editor de Biografias Profissional", layout="wide")

def get_safe(key, default=""):
    valor = st.session_state.get(key)
    if valor:
        if isinstance(valor, list):
            return ", ".join(valor) if len(valor) > 0 else default
        return str(valor)
    return default

# --- LISTA DAS 41 VIRTUDES ---
VIRTUDES_LISTA = [
    "Amor", "Alegria", "Auto-domínio", "Bondade", "Benignidade", "Benevolência", 
    "Compaixão", "Coragem", "Cortesias", "Castidade", "Discernimento", "Disciplina", 
    "Diligência", "Esperança", "Entusiasmo", "Fé", "Fidelidade", "Fortaleza", 
    "Generosidade", "Gratidão", "Gentileza", "Honra", "Humildade", "Honestidade", 
    "Justiça", "Lealdade", "Longanimidade", "Moderação", "Mansidão", "Obediência", 
    "Ordem", "Paciência", "Perdão", "Prudência", "Piedade", "Respeito", 
    "Responsabilidade", "Sabedoria", "Temperança", "Tolerância", "Zelo"
]

# --- INTERFACE ---
st.title("📘 Sistema de Biografias Trampolim")

tab_a, tab_b, tab_c, tab_d = st.tabs(["Bloco A", "Bloco B", "Bloco C", "📖 Livro Gerado"])

with tab_a:
    st.text_input("Nome Completo:", key='nome_autor')
    with st.expander("Cap. 1 a 5"):
        st.text_area("O que é renovar a mente para você? (Cap 1)", key='c1_renovar')
        st.text_area("Como os desafios revelam sua identidade? (Cap 2)", key='c2_reflexao')
        st.multiselect("Práticas de corpo e espírito: (Cap 3)", ["Oração", "Exercício", "Leitura", "Jejum"], key='c3_praticas')
        st.text_input("Seus maiores talentos: (Cap 4)", key='c4_talentos')
        st.text_area("Por que sua história deve ser contada? (Cap 5)", key='c5_reflexao')

with tab_b:
    with st.expander("Cap. 11 a 20"):
        st.text_area("Momento de virada: (Cap 12)", key='c12_virada')
        st.text_input("Hobby principal: (Cap 14)", key='c14_hobby')
        st.text_area("Origem do Hobby: (Cap 14)", key='c14_origem')
        # AQUI ESTÃO AS 41 VIRTUDES
        st.multiselect("Escolha as virtudes que definem o seu caráter: (Cap 16)", VIRTUDES_LISTA, key='c16_virtudes')
        st.text_area("Exemplo de virtude em ação:", key='c16_exemplo')
        st.text_input("Brincadeira de infância: (Cap 19)", key='c19_infancia')

with tab_c:
    with st.expander("Cap. 21 a 26"):
        st.text_area("Seu grande sonho: (Cap 21)", key='c21_sonho')
        st.text_area("Como imagina que este livro alcançará pessoas? (Cap 25)", key='c25_alcance')
        st.text_area("Mensagem de legado final: (Cap 26)", key='c26_legado')

# --- GERADOR ROBUSTO ---
def gerar_narrativa_completa(estilo, genero=None):
    nome = get_safe('nome_autor', 'Viajante')
    virtudes = get_safe('c16_virtudes')
    
    # Construção do texto baseando-se em TODAS as respostas
    intro = f"# A JORNADA DE {nome.upper()}\n\n"
    
    corpo = f"A história de {nome} não é apenas um relato de tempo, mas de renovação mental. "
    corpo += f"Para {nome}, o ato de evoluir significa: '{get_safe('c1_renovar')}'. \n\n"
    
    corpo += f"## 💎 O ALICERCE DAS VIRTUDES\n"
    corpo += f"No centro do seu caráter, encontramos o cultivo de virtudes fundamentais: {virtudes}. "
    corpo += f"Um exemplo prático disso foi quando {get_safe('c16_exemplo')}. \n\n"
    
    corpo += f"## 🚀 IMPACTO E LEGADO\n"
    corpo += f"Com um olhar voltado para o futuro, o sonho de {nome} é {get_safe('c21_sonho')}. "
    corpo += f"Este livro nasce com uma missão clara: '{get_safe('c25_alcance')}'. \n\n"
    
    corpo += f"---\n**MENSAGEM FINAL:** {get_safe('c26_legado')}"
    
    return intro + corpo

# --- SIDEBAR ---
with st.sidebar:
    estilo = st.selectbox("Estilo:", ["Hobby", "Infantil", "Profissional"])
    if st.button("🚀 GERAR BIOGRAFIA ROBUSTA"):
        st.session_state.livro_gerado = gerar_narrativa_completa(estilo)

with tab_d:
    if st.session_state.livro_gerado:
        st.markdown(st.session_state.livro_gerado)

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




















