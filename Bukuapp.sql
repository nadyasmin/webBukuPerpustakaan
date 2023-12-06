CREATE TABLE buku (
    id serial,
    "Kode Buku" VARCHAR(255),
    "Judul Buku" VARCHAR(255),
    "Genre" VARCHAR(255),
    "Tahun Terbit" TEXT,
    "Pengarang" VARCHAR(255),
    "Penerbit" VARCHAR (255),
    "Kode Rak" VARCHAR(255),
    "Status" VARCHAR (255)
);

--isi--
insert into buku ("Kode Buku", "Judul Buku", "Genre", "Tahun Terbit", "Pengarang", "Penerbit", "Kode Rak", "Status") 
values
	('ROM001', 'Matahari Terbenam di Pantai', 'Romantis', '2018', 'Aulia Nuryani', 'Cinta Sejati Publishing', 'N001', 'Tersedia')
	;
	
