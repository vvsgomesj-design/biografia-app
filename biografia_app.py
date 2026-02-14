import streamlit as st
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Gerador de Biografias Pro", layout="wide")

# --- LISTA DAS 41 VIRTUDES (CAP 16) ---
VIRTUDES_41 = [
    "Amor", "Alegria", "Auto-domínio", "Bondade", "Benignidade", "Benevolência", 
    "Compaixão", "Coragem", "Cortesias", "Castidade", "Discernimento", "Disciplina", 
    "Diligência", "Esperança", "Entusiasmo", "Fé", "Fidelidade", "Fortaleza", 
    "Generosidade", "Gratidão", "Gentileza", "Honra", "Humildade", "Honestidade", 
    "Justiça", "Lealdade", "Longanimidade", "Moderação", "Mansidão", "Obediência", 
    "Ordem", "Paciência", "Perdão", "Prudência", "Piedade", "Respeito", 
    "Responsabilidade", "Sabedoria", "Temperança", "Tolerância", "Zelo"
]

# --- FUNÇÃO DE BUSCA SEGURA (PUXA O CONTEÚDO DAS KEYS) ---
def get_f(key, default="..."):
    valor = st.session_state.get(key)
    if valor:
        if isinstance(valor, list):
            return ", ".join(valor) if len(valor) > 0 else default
        return str(valor)
    return default

st.title("📘 Sistema de Biografias Trampolim")

# --- ESTRUTURA DE ABAS PARA ENTRADA DE DADOS ---
tab_a, tab_b, tab_c = st.tabs(["🏛️ Bloco A: Fundamentos", "🎨 Bloco B: Jornada", "🚀 Bloco C: Estrutura"])

with tab_a:
    st.text_input("Nome Completo:", key='nome_autor')
    with st.expander("Cap. 1 a 5 – Identidade e Mente", expanded=True):
        st.text_area("O que é renovar a mente para você? (Cap 1)", key='c1_renovar')
        st.text_input("O que te motiva a mudar? (Cap 1)", key='c1_motiva')
        st.radio("Frequência de aprendizado:", ["Diariamente", "Semanalmente", "Raramente"], key='c1_aprendizado')
        st.text_area("Como os desafios revelam sua identidade? (Cap 2)", key='c2_reflexao')
        st.multiselect("Práticas de Corpo e Espírito: (Cap 3)", ["Exercícios", "Oração", "Leitura", "Sono", "Alimentação"], key='c3_praticas')
        st.text_input("Seus maiores talentos: (Cap 4)", key='c4_talentos')
        st.text_area("Um momento de autenticidade: (Cap 4)", key='c4_autentico')
        st.text_area("Por que sua história merece ser contada? (Cap 5)", key='c5_reflexao')

with tab_b:
    with st.expander("Cap. 6 a 20 – Experiências e Virtudes", expanded=True):
        st.text_area("Descreva um desafio significativo superado: (Cap 8)", key='c8_desafio')
        st.text_area("Sua formação e competências profissionais: (Cap 10)", key='c10_formacao')
        st.text_area("Momento de virada ('Uau'): (Cap 12)", key='c12_virada')
        st.text_input("Hobby favorito e sua origem: (Cap 14)", key='c14_hobby')
        st.text_area("Momento de paz com o hobby: (Cap 14)", key='c14_paz')
        st.multiselect("Escolha suas Virtudes (Cap 16):", VIRTUDES_41, key='c16_virtudes')
        st.text_area("Exemplo de virtude em ação: (Cap 16)", key='c16_exemplo')
        st.text_input("Brincadeira de infância: (Cap 19)", key='c19_infancia')
        st.text_area("Um hábito que mudou sua vida: (Cap 20)", key='c20_habito')

with tab_c:
    with st.expander("Cap. 21 a 26 – Futuro e Legado", expanded=True):
        st.text_area("Seu grande sonho: (Cap 21)", key='c21_sonho')
        st.text_area("Passos práticos para o futuro: (Cap 21)", key='c21_plano')
        st.text_area("Como o livro alcançará as pessoas? (Cap 25)", key='c25_alcance')
        st.multiselect("Sentidos do livro: (Cap 26)", ["Visão", "Tato", "Olfato", "Audição"], key='c26_sinestesia')
        st.text_area("Sua mensagem de legado final: (Cap 26)", key='c26_legado')

# --- 5. MOTOR DE NARRATIVA COERENTE ---
def gerar_biografia(estilo, gen=None):
    n = get_f('nome_autor').upper()
    
    if estilo == "Infantil":
        art, pers = ("uma", "princesa") if gen == "Menina" else ("um", "príncipe")
        pron = "ela" if gen == "Menina" else "ele"
        return f"""# 🌈 AS AVENTURAS REAIS DE {n}

Era uma vez {art} {pers} especial que descobriu que aprender algo novo {get_f('c1_aprendizado').lower()} era o segredo para o crescimento. Para {n}, renovar a mente significa: "{get_f('c1_renovar')}".

Como herdeir{'a' if gen=='Menina' else 'o'} de grandes promessas, aprendeu que desafios revelam quem somos, pois "{get_f('c2_reflexao')}". Com talentos como {get_f('c4_talentos')}, ajuda a todos, cuidando do seu castelo com {get_f('c3_praticas')}. As lições começaram cedo, brincando de {get_f('c19_infancia')}. Hoje, brilha com virtudes como {get_f('c16_virtudes')}. Seu maior sonho é {get_f('c21_sonho')}.

**Mensagem do Reino:** "{get_f('c26_legado')}" """

    elif estilo == "Talento (Profissional)":
        return f"""# 💼 TRAJETÓRIA E EXCELÊNCIA: {n}

Com formação em {get_f('c10_formacao')}, {n} pauta a sua carreira na premissa de que renovar a mente é "{get_f('c1_renovar')}". Movido por {get_f('c1_motiva')}, consolidou competências após um momento de virada: {get_f('c12_virada')}.

Seu caráter é definido pelas virtudes {get_f('c16_virtudes')}, aplicadas em desafios como {get_f('c8_desafio')}. Exemplo disso foi quando {get_f('c16_exemplo')}. O seu plano envolve {get_f('c21_plano')} para alcançar o sonho de {get_f('c21_sonho')}, impactando o mundo através de "{get_f('c25_alcance')}".

**Legado:** "{get_f('c26_legado')}" """

    else: # Hobby
        return f"""# 🎨 A ESSÊNCIA E O LAZER DE {n}

Para {n}, a vida ganha cor no hobby **{get_f('c14_hobby')}**. Surgido de {get_f('c14_origem')}, este passatempo traz paz em momentos como "{get_f('c14_paz')}". Sua autenticidade, marca registrada desde a infância ao brincar de {get_f('c19_infancia')}, revela-se quando {get_f('c4_autentico')}. Aliando os talentos de {get_f('c4_talentos')} ao hábito de {get_f('c20_habito')}, {n} constrói um caminho pleno.

**Reflexão:** "{get_f('c26_legado')}" """

# --- 6. BARRA LATERAL (BOTÃO E RESULTADO) ---
with st.sidebar:
    st.header("📖 Gerador de Conteúdo")
    estilo_sel = st.selectbox("Escolha o Estilo:", ["Talento (Profissional)", "Hobby / Passatempo", "Infantil"])
    genero_inf = None
    if estilo_sel == "Infantil":
        genero_inf = st.radio("Gênero:", ["Menina", "Menino"])
    
    if st.button("🚀 Gerar Biografia"):
        if not st.session_state.nome_autor:
            st.error("Por favor, preencha o nome no Bloco A.")
        else:
            st.session_state.livro_gerado = gerar_biografia(estilo_sel, genero_inf)

    # EXIBIÇÃO LOGO ABAIXO DO BOTÃO
    if st.session_state.livro_gerado:
        st.markdown("---")
        st.subheader("📄 Biografia Gerada:")
        st.markdown(st.session_state.livro_gerado)
        st.download_button("📥 Baixar TXT", st.session_state.livro_gerado, file_name="biografia_completa.txt")

















