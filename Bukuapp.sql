CREATE TABLE buku (
    id serial,
    "Kode Buku" VARCHAR PRIMARY KEY,
    "Judul Buku" VARCHAR(255),
    "Genre" VARCHAR(255),
    "Tahun Terbit" INTEGER,
    "Pengarang" VARCHAR(255),
    "Penerbit" VARCHAR (255),
    "Kode Rak" VARCHAR(5),
    "Status" VARCHAR (255),
);

--isi--
insert into buku ("Kode Buku", "Judul Buku", "Genre", "Tahun Terbit", "Pengarang", "Penerbit", "Kode Rak", "Status") 
values
	('ROM001', 'Matahari Terbenam di Pantai', 'Romantis', '2018', 'Aulia Nuryani', 'Cinta Sejati Publishing', 'N001', 'Tersedia'),
	('ANK001', 'Petualangan Budi Si Penjelajah', 'Anak-anak', '2020', 'Dian Anugerah', 'Dunia Anak Nusantara', 'N001', 'Dipinjam'),
	('HOR001', 'Teror di Rumah Hantu', 'Horor', '2019', 'Wira Kusuma', 'Dunia Horor Indonesia', 'N001', 'Dipinjam'),
	('SCF001', 'Galaksi Pencarian', 'Sci-Fi', '2021', 'Irfan Galaksi', 'Antariksa Sci-Fi Press', 'N002', 'Tersedia'),
	('AKS001', 'Operasi Rahasia: Kode Hitam', 'Aksi', '2019', 'Andi Kusuma', 'Pena Aksi Nusantara', 'N001', 'Tersedia'),
	('MSR001', 'Rahasia di Balik Pintu Kuno', 'Misteri', '2022', 'Siti Nurjanah', 'Tebak Misteri Publishing', 'N002', 'Tersedia'),
	('PED001', 'Langkah Menuju Kesuksesan', 'Pengembangan Diri', '2017', 'Dini Rahayu', 'Inspirasi Mandiri', 'N002', 'Tersedia'),
	('ROM002', 'Dalam Pelukan Bintang', 'Romantis', '2016', 'Rizky Amelia', 'Cinta Abadi Books', 'N001', 'Dipinjam'),
	('ANK002', 'Petualangan Si Kecil Pemberani', 'Anak-anak', '2018', 'Anisa Putri', 'Cerita Anak Hebat', 'N001', 'Dipinjam'),
	('HOR002', 'Malam Jumat Kliwon', 'Horor', '2020', 'Ahmad Zaki', 'Penerbit Teror Malam Press', 'N001', 'Tersedia'),
	('SCF002', 'Revolt of the Machines', 'Sci-Fi', '2019', 'Xavier Quantum', 'Future Tech Publishing', 'N002', 'Tersedia'),
	('PED002', 'Langkah Menuju Kesuksesan', 'Pengembangan Diri', '2017', 'Dini Rahayu', 'Inspirasi Mandiri','N002', 'Tersedia'),
	('AKS002', 'Kepahlawanan Sang Pemuda', 'Aksi', '2021', 'Aditya Prakasa', 'Pena Pahlawan Nusantara', 'N001', 'Tersedia'),
	('MSR002', 'Jejak Misterius Di Hutan Gelap', 'Misteri', '2018', 'Sari Wijaya', 'Penyelidik Misteri', 'N002', 'Dipinjam')
	;
	
