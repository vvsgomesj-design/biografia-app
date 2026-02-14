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

with tab_a:
    st.header("Identidade e Mindset")
    st.text_input("Nome Completo:", key='nome_autor')
    
    with st.expander("Capítulos 1 a 5", expanded=True):
        st.text_area("O que é renovar a mente para você? (Cap 1)", key='c1_renovar')
        st.text_input("O que te motiva a mudar? (Cap 1)", key='c1_motiva')
        st.radio("Frequência de aprendizado:", ["Diariamente", "Semanalmente", "Raramente", "Nunca"], key='c1_frequencia')
        st.text_area("Como os desafios revelam sua identidade? (Cap 2)", key='c2_reflexao')
        st.multiselect("Práticas de saúde/espírito: (Cap 3)", ["Exercícios", "Oração", "Leitura", "Sono", "Alimentação"], key='c3_praticas')
        st.text_input("Seus maiores talentos: (Cap 4)", key='c4_talentos')
        st.text_area("Momento de autenticidade: (Cap 4)", key='c4_autentico')
        st.text_area("Por que sua história merece ser contada? (Cap 5)", key='c5_contada')

with tab_b:
    st.header("Histórico e Caráter")
    with st.expander("Capítulos 6 a 20", expanded=True):
        st.text_area("Um desafio significativo superado: (Cap 8)", key='c8_desafio')
        st.text_area("Formação e competências profissionais: (Cap 10)", key='c10_formacao')
        st.text_area("Momento de virada ('Uau'): (Cap 12)", key='c12_virada')
        st.text_input("Hobby favorito e origem: (Cap 14)", key='c14_hobby')
        st.text_area("Paz encontrada no hobby: (Cap 14)", key='c14_paz')
        st.multiselect("Selecione suas Virtudes principais (Cap 16):", VIRTUDES_41, key='c16_virtudes')
        st.text_area("Exemplo de virtude em ação: (Cap 16)", key='c16_exemplo')
        st.text_input("Brincadeira de infância: (Cap 19)", key='c19_infancia')
        st.text_area("Hábito que mudou sua vida: (Cap 20)", key='c20_habito')

with tab_c:
    st.header("Futuro e Mensagem")
    with st.expander("Capítulos 21 a 26", expanded=True):
        st.text_area("Seu grande sonho: (Cap 21)", key='c21_sonho')
        st.text_area("Passos práticos (Plano): (Cap 21)", key='c21_plano')
        st.text_area("Como o livro alcançará as pessoas? (Cap 25)", key='c25_alcance')
        st.multiselect("Sentidos despertados pelo livro: (Cap 26)", ["Visão", "Tato", "Olfato", "Audição", "Paladar"], key='c26_sinestesia')
        st.text_area("Sua mensagem de legado final: (Cap 26)", key='c26_legado')

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


















