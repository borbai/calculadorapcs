import streamlit as st

st.set_page_config(page_title="Calculadora de PCS", page_icon=":computer:")
st.title("Calculadora de PCS")
st.write("Bem-vindo à Calculadora de PCS! Aqui você pode calcular o salário de enquadramento no Plano de Cargos e Salários (PCS).")
st.write("Por favor, insira os detalhes necessários para o cálculo.")
cargo = st.selectbox("Selecione o cargo atual:", ["PTA", "PNA", "PMET", "ASIII: ENA", "PEM", "ASIII: MEG", "ASI: PSI", "ASIV: ENG", "ASII: ADM"])
salario_atual = st.number_input("Digite o salário atual (R$):", min_value=0.0, step=0.01, format="%.2f")
anos_experiencia = st.number_input("Digite o tempo de empresa:", min_value=0, step=1)
if st.button("Calcular Salário de Enquadramento"):
    if cargo == "PTA":
        salario_base = 5632.54
        salario_final = 12448.20
    elif cargo == "PNA":
        salario_base = 5632.54
        salario_final = 12448.20
    elif cargo == "PMET":
        salario_base = 5632.54
        salario_final = 12448.20
    elif cargo == "ASIII: ENA":
        salario_base = 6607.20
        salario_final = 14602.28
    elif cargo == "PEM":
        salario_base = 4389.37
        salario_final = 9700.71
    elif cargo == "ASIII: MEG":
        salario_base = 6607.20
        salario_final = 14602.28
    elif cargo == "ASI: PSI":
        salario_base = 5861.82
        salario_final = 12954.92
    elif cargo == "ASIV: ENG":
        salario_base = 10299.14
        salario_final = 16503.71
    elif cargo == "ASII: ADM":
        salario_base = 5861.82
        salario_final = 12954.92

    if salario_atual < salario_base:
        salario_enquadramento = salario_base
    else: salario_enquadramento = salario_atual
    
    salario_enquadramento = salario_enquadramento * 1.04

    if anos_experiencia <= 5:
        percentil_enquadramento = 5
    elif anos_experiencia > 5 and anos_experiencia <= 10:
        percentil_enquadramento = 14
    elif anos_experiencia > 10 and anos_experiencia <= 20:
        percentil_enquadramento = 24
    elif anos_experiencia > 20 and anos_experiencia <= 25:
        percentil_enquadramento = 32
    elif anos_experiencia > 25:
        percentil_enquadramento = 40

    percentil = salario_final - salario_base
    percentil = percentil / 100
    percentil = percentil * percentil_enquadramento
    percentil = salario_base + percentil
    
    limite_aumento = salario_atual * 1.2

    if salario_enquadramento <= percentil:
        salario_enquadramento = percentil

    if salario_enquadramento > limite_aumento:
        salario_enquadramento = limite_aumento

    st.success(f"O salário de enquadramento para o cargo de {cargo} com {anos_experiencia} anos de empresa é: R$ {salario_enquadramento:.2f}")
    st.info("Este é um cálculo não oficial, baseado em um das interpretações do PCS apresentado pela empresa.")

