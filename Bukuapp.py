import streamlit as st
from sqlalchemy import text

list_status = ['', 'Tersedia', 'Dipinjam']
list_genre = ['', 'Romantis', 'Anak-anak', 'Horor', 'Sci-Fi', 'Aksi', 'Misteri', 'Pengembangan Diri']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://nadia.2043221105:P4YglWGXSp3e@ep-muddy-rice-61227326.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS buku (id serial, code VARCHAR, title VARCHAR(255), genre VARCHAR(255), year INTEGER, author VARCHAR(255), publisher VARCHAR(255), rack VARCHAR(5), status VARCHAR(255), pict OID);')
    session.execute(query)

st.header('DATABASE BUKU PERPUSTAKAAN')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM buku ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO buku (code, title, genre, year, author, publisher, rack, status, pict) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':'', '9':''})
            session.commit()

    data = conn.query('SELECT * FROM buku ORDER By code;')
    for _, result in data.iterrows():
        id = result['id']
        code_lama = result['Kode Buku']
        title_lama = result["Judul Buku"]
        genre_lama = result["Genre"]
        year_lama = result["Tahun Terbit"]
        author_lama = result["Pengarang"]
        publisher_lama = result["Penerbit"]
        rack_lama = result["Rak Buku"]
        status_lama = result["Status"]
        pict_lama = result["Gambar Buku"]

        with st.expander(f'Judul Buku {title_lama}'):
            with st.form(f'data-{id}'):
                code_baru = st.text_input("Kode Buku", code_lama)
                title_baru = st.text_input("Judul Buku", title_lama)
                genre_number_baru = st.selectbox("Genre", list_genre, list_genre.index(genre_lama))
                year_baru = st.text_input("Tahun Terbit", year_lama)
                author_baru = st.text_input("Pengarang", author_lama)
                publisher_baru = st.text_input("Penerbit", publisher_lama)
                rack_baru = st.text_input("Rak Buku", rack_lama)
                status_baru = st.selectbox("Status", list_status, list_status.index(status_lama))
                pict_baru = st.file_uploader(
                    "Gambar Buku",
                    type=None,
                    accept_multiple_files=False,
                    key=None,
                    help=None,
                    on_change=None,
                    args=None,
                    kwargs=None,
                    disabled=False,
                    label_visibility="visible"
                )

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE buku \
                                          SET code=:1, title=:2, genre=:3, year=:4, \
                                          author=:5, publisher=:6, rack=:7, status=:8, pict=:9 \
                                          WHERE id=:10;')
                            session.execute(query, {'1':code_baru, '2':title_baru, '3':genre_baru, '4':(year_baru), 
                                                    '5':author_baru, '6':publisher_baru, '7':rack_baru, '8':status_baru, '9':pict_baru, '10':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM buku WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
