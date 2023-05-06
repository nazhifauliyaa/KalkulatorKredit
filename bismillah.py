import streamlit as st
import locale
locale.setlocale(locale.LC_ALL, 'id_ID')

st.set_page_config(page_title="Simulasi Pinjaman", page_icon=":money:", layout="wide")

#Judul Aplikasi
st.subheader('Rencanakan Peminjaman Anda')
st.title("💸 Kalkulator Kredit 💸")

#Intro Aplikasi
st.write('Selamat datang di aplikasi Kalkulator Kredit. Aplikasi ini dapat membantu Anda menghitung estimasi cicilan kredit berdasarkan jumlah pinjaman, jangka waktu, dan suku bunga. Dengan adanya aplikasi ini, diharapkan dapat mempermudah Anda dalam melakukan perencanaan pinjaman dan membantu Anda dalam pengambilan keputusan yang lebih baik dalam melakukan kredit.')
st.write('---')

st.markdown('__**INPUT DATA**__')
# Masukkan jumlah pinjaman dalam rupiah
import locale

# Set lokalisasi ke bahasa Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID')

import babel.numbers as numbers

# Masukkan jumlah pinjaman dalam rupiah
loan_amount = st.number_input(
    "Masukkan jumlah pinjaman (dalam rupiah):",
    min_value=1000000,
    max_value=1000000000,
    step=100000,
    format='%d'
)

# Format bilangan menjadi string dengan pemisah ribuan dan simbol mata uang IDR
loan_amount_formatted = numbers.format_currency(loan_amount, 'IDR', locale='id_ID')

# Tampilkan jumlah pinjaman dengan format yang sesuai
st.write(f"Jumlah pinjaman: {loan_amount_formatted}")

# Masukkan jangka waktu dalam tahun
tenure = st.number_input("Masukkan jangka waktu (dalam tahun):", min_value=1, max_value=30, step=1)

# Masukkan suku bunga dalam persen per tahun
interest_rate = st.number_input(
    "Masukkan suku bunga (dalam persen per tahun):",
    min_value=1.0,
    max_value=20.0,
    step=0.1,
    help=("Suku bunga adalah persentase yang harus Anda bayar setiap tahun sebagai biaya penggunaan uang yang dipinjamkan. Misalnya, jika Anda meminjam 10 juta rupiah dengan suku bunga 10%, maka Anda harus membayar 1 juta rupiah per tahun sebagai biaya penggunaan uang tersebut.")
)

# Buat tombol untuk menghitung angsuran
if st.button("Hitung angsuran"):
    # Hitung angsuran per bulan
    monthly_interest_rate = interest_rate / 1200
    num_payments = tenure * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-num_payments))

    # Tampilkan hasil perhitungan
    st.write("Angsuran per bulan yang harus dibayar: Rp.{:,.2f}".format(monthly_payment))

    # Hitung total pembayaran dan total bunga
    total_payment = monthly_payment * num_payments
    total_interest = total_payment - loan_amount

    # Tampilkan total pembayaran dan total bunga
    st.write("Total pembayaran selama {} tahun: Rp.{:,.2f}".format(tenure, total_payment))
    st.write("Total bunga: Rp.{:,.2f}".format(total_interest))