import streamlit as st
from sqlalchemy import text

list_status = ['', 'Tersedia', 'Dipinjam']
list_genre = ['', 'Romantis', 'Anak-anak', 'Horor', 'Sci-Fi', 'Aksi', 'Misteri', 'Pengembangan Diri']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://nadia.2043221105:P4YglWGXSp3e@ep-muddy-rice-61227326.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS buku (id serial, code VARCHAR, title VARCHAR(255), genre VARCHAR(255), year TEXT, author VARCHAR(255), publisher VARCHAR(255), rack VARCHAR(5), status VARCHAR(255));')
    session.execute(query)

st.header('DATABASE BUKU PERPUSTAKAAN')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
  data = conn.query('SELECT * FROM buku ORDER BY id;', ttl="0").set_index('id')
  st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO buku ("Kode Buku", "Judul Buku", "Genre", "Tahun Terbit", "Pengarang", "Penerbit", "Kode Rak", "Status") \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':''})
            session.commit()

    data = conn.query('SELECT * FROM buku ORDER BY id;')
    for _, result in data.iterrows():
        id = result['id']
        code_lama = result['Kode Buku']
        title_lama = result["Judul Buku"]
        genre_lama = result["Genre"]
        year_lama = result["Tahun Terbit"]
        author_lama = result["Pengarang"]
        publisher_lama = result["Penerbit"]
        rack_lama = result["Kode Rak"]
        status_lama = result["Status"]

        with st.expander(f'Judul Buku {title_lama}'):
            with st.form(f'data-{id}'):
                code_baru = st.text_input("Kode Buku", code_lama)
                title_baru = st.text_input("Judul Buku", title_lama)
                genre_baru = st.selectbox("Genre", list_genre, list_genre.index(genre_lama))
                year_baru = st.text_input("Tahun Terbit", year_lama)
                author_baru = st.text_input("Pengarang", author_lama)
                publisher_baru = st.text_input("Penerbit", publisher_lama)
                rack_baru = st.text_input("Kode Rak", rack_lama)
                status_baru = st.selectbox("Status", list_status, list_status.index(status_lama))

                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE buku \
                                          SET "Kode Buku"=:1, "Judul Buku"=:2, "Genre"=:3, "Tahun Terbit"=:4, \
                                          "Pengarang"=:5, "Penerbit"=:6, "Kode Rak"=:7, "Status"=:8 \
                                          WHERE id=:9;')
                            session.execute(query, {'1':code_baru, '2':title_baru, '3':genre_baru, '4':year_baru, '5':author_baru, 
                                                    '6':publisher_baru, '7':rack_baru, '8':status_baru, '9':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM buku WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
