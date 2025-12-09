# ALP Matematika Diskrit

Proyek ini merupakan implementasi sistem berbasis Python untuk mempelajari teori graf menggunakan library NetworkX. Proyek ini dibuat sebagai bagian dari tugas Matematika Diskrit yang mencakup analisis graf, visualisasi, dan penyelesaian problem AFL-3.

## 👨‍💻 Informasi Project

- **Nama**: Muhammad Habbibie Zikrillah (0806022329001)
- **Prodi**: IMT-AI
- **Mata Kuliah**: Matematika Diskrit
- **Institusi**: Universitas Ciputra - Kampus Makassar
- **Library**: NetworkX, Matplotlib

## 📋 Deskripsi

Project ini mengimplementasikan kelas `Graf` yang menyediakan berbagai metode untuk:
- Membuat dan memanipulasi graf (berarah dan tak berarah)
- Analisis properti graf (derajat, konektivitas, cycle)
- Algoritma traversal (BFS, DFS)
- Algoritma jalur terpendek (Dijkstra)
- Visualisasi graf dan jalur terpendek

## ✨ Fitur Utama

### Metode Dasar
1. **`add_node(node)`** - Menambahkan node ke graf
2. **`add_edge(node1, node2, weight)`** - Menambahkan edge dengan bobot
3. **`visualize_graph()`** - Visualisasi graf
4. **`shortest_path(start, end)`** - Mencari jalur terpendek
5. **`visual_shortest_path(start, end)`** - Visualisasi jalur terpendek

### Metode Tambahan
6. **`degree(node)`** - Menghitung derajat node
7. **`is_connected()`** - Mengecek konektivitas graf
8. **`get_neighbors(node)`** - Mendapatkan tetangga node
9. **`number_of_nodes()`** - Menghitung jumlah node
10. **`number_of_edges()`** - Menghitung jumlah edge
11. **`all_degrees()`** - Menampilkan derajat semua node
12. **`find_cycles()`** - Menemukan semua cycle
13. **`bfs(start)`** - Breadth-First Search
14. **`dfs(start)`** - Depth-First Search (rekursif)
15. **`dijkstra(start)`** - Algoritma Dijkstra lengkap

## 🚀 Cara Instalasi

### 1. Clone Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install Dependencies
```bash
pip install networkx matplotlib
```

### 3. Jalankan Program
```bash
python graf.py
```

## 📖 Cara Penggunaan

### Contoh Dasar

```python
from graf import Graf

# 1. Membuat objek graf
graph = Graf()

# 2. Menambah node
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)

# 3. Menambah edge dengan bobot
graph.add_edge(1, 2, weight=4.5)
graph.add_edge(2, 3, weight=3.2)

# 4. Visualisasi graf
graph.visualize_graph()

# 5. Mencari jalur terpendek
graph.shortest_path(1, 3)

# 6. Visualisasi jalur terpendek
graph.visual_shortest_path(1, 3)
```

### Membuat Graf Berarah

```python
# Graf berarah
directed_graph = Graf(directed=True)
directed_graph.add_node('A')
directed_graph.add_node('B')
directed_graph.add_edge('A', 'B', weight=5)
```

### Menggunakan Metode Tambahan

```python
# Cek derajat node
graph.degree(1)

# Cek konektivitas
graph.is_connected()

# BFS dan DFS
graph.bfs('A')
graph.dfs('A')

# Dijkstra
distances, paths = graph.dijkstra('A')
```

---

## 📝 Penyelesaian AFL-3

### **Soal 1 — Graf Tak Berarah, Derajat, dan Konektivitas**

**Diberikan:**
- V = {A, B, C, D, E, F}
- E = {(A, B), (A, C), (B, D), (C, E), (D, E), (E, F), (C, F)}

#### a. Visualisasi Graf

```python
graph = Graf(directed=False)
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
for node in nodes:
    graph.add_node(node)

edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), 
         ('D', 'E'), ('E', 'F'), ('C', 'F')]
for edge in edges:
    graph.add_edge(edge[0], edge[1])

graph.visualize_graph("Soal 1: Graf Tak Berarah")
```

**Hasil:** Graf tak berarah dengan 6 node (A-F) dan 7 edge akan ditampilkan dalam visualisasi matplotlib.

#### b. Derajat Setiap Simpul

```python
graph.all_degrees()
```

**Output:**
```
Derajat semua simpul:
  A: 2
  B: 2
  C: 3
  D: 2
  E: 3
  F: 2
```

**Analisis:**
- Node C dan E memiliki derajat tertinggi (3)
- Node lainnya memiliki derajat 2
- Total derajat = 14 (2 × jumlah edge = 2 × 7 = 14) ✓

#### c. Cycle dalam Graf

```python
cycles = graph.find_cycles()
```

**Output:**
```
Mencari cycle dalam graf:
Ditemukan 2 cycle:
  Cycle 1: ['A', 'C', 'E', 'D', 'B']
  Cycle 2: ['C', 'E', 'F']
```

**Penjelasan:**
- **Cycle 1**: A → C → E → D → B → A
- **Cycle 2**: C → E → F → C

Graf memiliki cycle, sehingga ini **bukan graf pohon (tree)**.

#### d. Konektivitas Graf

```python
graph.is_connected()
```

**Output:**
```
Graf connected: True
```

**Penjelasan:**
Graf ini **connected** karena terdapat jalur antara setiap pasangan simpul. Semua node dapat dijangkau dari node lainnya melalui edge-edge yang ada.

---

### **Soal 3 — BFS, DFS, dan Dijkstra**

**Diberikan:**
- V = {A, B, C, D, E, F, G}
- E = {(A,B,2), (A,C,5), (B,D,4), (B,E,6), (C,F,3), (D,G,2), (E,F,4), (F,G,1)}

#### a. Visualisasi Graf

```python
graph = Graf(directed=False)
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for node in nodes:
    graph.add_node(node)

edges = [('A', 'B', 2), ('A', 'C', 5), ('B', 'D', 4), ('B', 'E', 6),
         ('C', 'F', 3), ('D', 'G', 2), ('E', 'F', 4), ('F', 'G', 1)]
for edge in edges:
    graph.add_edge(edge[0], edge[1], weight=edge[2])

graph.visualize_graph("Soal 3: Graf Berbobot")
```

**Hasil:** Graf berbobot dengan 7 node dan 8 edge dengan bobot yang berbeda-beda akan ditampilkan dalam visualisasi matpDF4lotlib.

#### b. Breadth-First Search (BFS) dari A

```python
graph.bfs('A')
```

**Output:**
```
BFS dimulai dari A:
  Urutan kunjungan: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
```

**Penjelasan:**
BFS mengunjungi node secara level-by-level:
1. **Level 0**: A (start)
2. **Level 1**: B, C (tetangga A)
3. **Level 2**: D, E (tetangga B), F (tetangga C)
4. **Level 3**: G (tetangga D dan F)

#### c. Depth-First Search (DFS) dari A

```python
graph.dfs('A')
```

**Output:**
```
DFS dimulai dari A:
  Urutan kunjungan: ['A', 'B', 'D', 'G', 'F', 'C', 'E']
```

**Penjelasan:**
DFS mengunjungi node secara mendalam (rekursif) dengan urutan tetangga berdasarkan alfabet:
- A → B (tetangga pertama alfabetis)
- B → D (tetangga pertama alfabetis dari B)
- D → G (tetangga pertama alfabetis dari D)
- G → F (backtrack dan lanjut)
- F → C (backtrack dan lanjut)
- C → E (tetangga dari C yang belum dikunjungi)

#### d.1. Jarak Minimum dari A ke Seluruh Simpul (Dijkstra)

```python
distances, paths = graph.dijkstra('A')
```

**Output:**
```
Jarak minimum dari A ke seluruh simpul:
  A -> A: 0
  A -> B: 2
  A -> C: 5
  A -> D: 6
  A -> E: 8
  A -> F: 8
  A -> G: 8

Jalur terpendek dari A ke seluruh simpul:
  A -> A: A
  A -> B: A -> B
  A -> C: A -> C
  A -> D: A -> B -> D
  A -> E: A -> B -> E
  A -> F: A -> C -> F
  A -> G: A -> B -> D -> G
```

**Tabel Jarak Minimum:**

| Tujuan | Jarak | Jalur |
|--------|-------|-------|
| A | 0 | A |
| B | 2 | A → B |
| C | 5 | A → C |
| D | 6 | A → B → D |
| E | 8 | A → B → E |
| F | 8 | A → C → F |
| G | 8 | A → B → D → G |

#### d.2. Jalur Terpendek dari A ke G

```python
path, distance = graph.shortest_path_dijkstra('A', 'G')
```

**Output:**
```
Jalur terpendek dari A ke G:
  Path: A -> B -> D -> G
  Jarak: 8
```

**Penjelasan:**
- **Jalur**: A → B → D → G
- **Total jarak**: 2 + 4 + 2 = **8**
- **Alternatif**: A → C → F → G = 5 + 3 + 1 = 9 (lebih panjang)
- Visualisasi jalur terpendek akan ditampilkan dengan node hijau dan edge merah

---

## 📦 Dependencies

Buat file `requirements.txt`:
```txt
networkx>=3.0
matplotlib>=3.5.0
```

Install semua dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

```bash
# Clone repository
git clone <your-repo-url>
cd <repository-name>

# Install dependencies
pip install -r requirements.txt

# Run program
python graf.py
```

## 🤝 Kontribusi

Project ini dibuat untuk keperluan akademik. Saran dan masukan dapat disampaikan melalui Issues atau Pull Request.

