import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Graf:
    def __init__(self, directed=False):
        """Inisialisasi graf (default: tak berarah)"""
        if directed:
            self.graph = nx.DiGraph()
        else:
            self.graph = nx.Graph()
        self.directed = directed
    
    # ==================== METODE DASAR ====================
    
    def add_node(self, node):
        """Menambahkan node ke graf"""
        self.graph.add_node(node)
        print(f"Node {node} berhasil ditambahkan")
    
    def add_edge(self, node1, node2, weight=1):
        """Menambahkan edge antara dua node dengan bobot"""
        self.graph.add_edge(node1, node2, weight=weight)
        print(f"Edge ({node1}, {node2}) dengan bobot {weight} berhasil ditambahkan")
    
    def visualize_graph(self, title="Visualisasi Graf"):
        """Menampilkan visualisasi graf"""
        pos = nx.spring_layout(self.graph, seed=42)
        
        plt.figure(figsize=(10, 8))
        nx.draw(self.graph, pos, with_labels=True, 
                node_color='lightblue', 
                node_size=1500, 
                font_size=16, 
                font_weight='bold',
                edge_color='gray',
                width=2,
                arrows=self.directed,
                arrowsize=20)
        
        # Menampilkan bobot edge
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels, font_size=12)
        
        plt.title(title, fontsize=18, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def shortest_path(self, start, end):
        """Mencari jalur terpendek antara dua node"""
        try:
            path = nx.shortest_path(self.graph, source=start, target=end, weight='weight')
            print(f"Jalur terpendek dari {start} ke {end}: {path}")
            return path
        except nx.NetworkXNoPath:
            print(f"Tidak ada jalur dari {start} ke {end}")
            return None
    
    def visual_shortest_path(self, start, end):
        """Visualisasi jalur terpendek"""
        try:
            path = nx.shortest_path(self.graph, source=start, target=end, weight='weight')
            path_edges = list(zip(path, path[1:]))
            
            pos = nx.spring_layout(self.graph, seed=42)
            
            plt.figure(figsize=(10, 8))
            
            # Gambar semua node dan edge
            nx.draw(self.graph, pos, with_labels=True,
                    node_color='lightblue',
                    node_size=1500,
                    font_size=16,
                    font_weight='bold',
                    edge_color='gray',
                    width=2,
                    arrows=self.directed,
                    arrowsize=20)
            
            # Highlight jalur terpendek
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path,
                                   node_color='lightgreen', node_size=1500)
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges,
                                   edge_color='red', width=3,
                                   arrows=self.directed,
                                   arrowsize=20)
            
            # Menampilkan bobot edge
            edge_labels = nx.get_edge_attributes(self.graph, 'weight')
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels, font_size=12)
            
            plt.title(f"Jalur Terpendek dari {start} ke {end}", fontsize=18, fontweight='bold')
            plt.axis('off')
            plt.tight_layout()
            plt.show()
            
        except nx.NetworkXNoPath:
            print(f"Tidak ada jalur dari {start} ke {end}")
    
    # ==================== METODE TAMBAHAN ====================
    
    def degree(self, node):
        """Menghitung derajat (degree) dari suatu node"""
        deg = self.graph.degree(node)
        print(f"Derajat node {node}: {deg}")
        return deg
    
    def all_degrees(self):
        """Menampilkan derajat semua node"""
        print("\nDerajat semua simpul:")
        degrees = dict(self.graph.degree())
        for node, deg in degrees.items():
            print(f"  {node}: {deg}")
        return degrees
    
    def is_connected(self):
        """Mengecek apakah graf terhubung (connected)"""
        if self.directed:
            connected = nx.is_strongly_connected(self.graph)
            print(f"Graf strongly connected: {connected}")
        else:
            connected = nx.is_connected(self.graph)
            print(f"Graf connected: {connected}")
        return connected
    
    def get_neighbors(self, node):
        """Mendapatkan daftar tetangga (neighbors) dari suatu node"""
        neighbors = list(self.graph.neighbors(node))
        print(f"Tetangga dari node {node}: {neighbors}")
        return neighbors
    
    def number_of_nodes(self):
        """Menghitung jumlah node dalam graf"""
        count = self.graph.number_of_nodes()
        print(f"Jumlah node: {count}")
        return count
    
    def number_of_edges(self):
        """Menghitung jumlah edge dalam graf"""
        count = self.graph.number_of_edges()
        print(f"Jumlah edge: {count}")
        return count
    
    # ==================== METODE UNTUK AFL-3 ====================
    
    def find_cycles(self):
        """Menemukan semua cycle dalam graf"""
        print("\nMencari cycle dalam graf:")
        if self.directed:
            try:
                cycles = list(nx.simple_cycles(self.graph))
                if cycles:
                    print(f"Ditemukan {len(cycles)} cycle:")
                    for i, cycle in enumerate(cycles, 1):
                        print(f"  Cycle {i}: {cycle}")
                    return cycles
                else:
                    print("  Tidak ada cycle")
                    return []
            except:
                print("  Tidak ada cycle")
                return []
        else:
            try:
                cycles = nx.cycle_basis(self.graph)
                if cycles:
                    print(f"Ditemukan {len(cycles)} cycle:")
                    for i, cycle in enumerate(cycles, 1):
                        print(f"  Cycle {i}: {cycle}")
                    return cycles
                else:
                    print("  Tidak ada cycle")
                    return []
            except:
                print("  Tidak ada cycle")
                return []
    
    def bfs(self, start):
        """Breadth-First Search dari node start"""
        print(f"\nBFS dimulai dari {start}:")
        visited = []
        queue = deque([start])
        visited_set = {start}
        
        while queue:
            node = queue.popleft()
            visited.append(node)
            
            # Urutkan tetangga berdasarkan alfabet/nilai
            neighbors = sorted(self.graph.neighbors(node))
            for neighbor in neighbors:
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    queue.append(neighbor)
        
        print(f"  Urutan kunjungan: {visited}")
        return visited
    
    def dfs(self, start):
        """Depth-First Search dari node start"""
        print(f"\nDFS dimulai dari {start}:")
        visited = []
        self._dfs_recursive(start, visited, set())
        print(f"  Urutan kunjungan: {visited}")
        return visited
    
    def _dfs_recursive(self, node, visited, visited_set):
        """Helper function untuk DFS rekursif"""
        visited.append(node)
        visited_set.add(node)
        
        # Urutkan tetangga berdasarkan alfabet/nilai
        neighbors = sorted(self.graph.neighbors(node))
        for neighbor in neighbors:
            if neighbor not in visited_set:
                self._dfs_recursive(neighbor, visited, visited_set)
    
    def dijkstra(self, start):
        """Algoritma Dijkstra untuk mencari jarak terpendek dari start ke semua node"""
        print(f"\nDijkstra dari {start}:")
        
        # Hitung jarak terpendek ke semua node
        distances = nx.single_source_dijkstra_path_length(self.graph, start, weight='weight')
        paths = nx.single_source_dijkstra_path(self.graph, start, weight='weight')
        
        print("\nJarak minimum dari", start, "ke seluruh simpul:")
        for node in sorted(distances.keys()):
            print(f"  {start} -> {node}: {distances[node]}")
        
        print("\nJalur terpendek dari", start, "ke seluruh simpul:")
        for node in sorted(paths.keys()):
            print(f"  {start} -> {node}: {' -> '.join(map(str, paths[node]))}")
        
        return distances, paths
    
    def shortest_path_dijkstra(self, start, end):
        """Mencari jalur terpendek dari start ke end menggunakan Dijkstra"""
        try:
            distance = nx.dijkstra_path_length(self.graph, start, end, weight='weight')
            path = nx.dijkstra_path(self.graph, start, end, weight='weight')
            print(f"\nJalur terpendek dari {start} ke {end}:")
            print(f"  Path: {' -> '.join(map(str, path))}")
            print(f"  Jarak: {distance}")
            return path, distance
        except nx.NetworkXNoPath:
            print(f"Tidak ada jalur dari {start} ke {end}")
            return None, None


# ==================== PENYELESAIAN AFL-3 ====================

def soal_1():
    """Soal 1 — Graf Tak Berarah, Derajat, dan Konektivitas"""
    print("="*70)
    print("SOAL 1 — Graf Tak Berarah, Derajat, dan Konektivitas")
    print("="*70)
    
    # Membuat graf tak berarah
    graph = Graf(directed=False)
    
    # Menambah node
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    for node in nodes:
        graph.add_node(node)
    
    print()
    
    # Menambah edge
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), 
             ('D', 'E'), ('E', 'F'), ('C', 'F')]
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    
    # a. Gambar graf
    print("\n" + "="*70)
    print("a. Visualisasi Graf:")
    print("="*70)
    graph.visualize_graph("Soal 1: Graf Tak Berarah")
    
    # b. Derajat setiap simpul
    print("\n" + "="*70)
    print("b. Derajat Setiap Simpul:")
    print("="*70)
    graph.all_degrees()
    
    # c. Cek cycle
    print("\n" + "="*70)
    print("c. Cycle dalam Graf:")
    print("="*70)
    cycles = graph.find_cycles()
    
    # d. Cek connected
    print("\n" + "="*70)
    print("d. Konektivitas Graf:")
    print("="*70)
    graph.is_connected()
    print("Penjelasan: Graf ini connected karena semua simpul dapat dijangkau dari simpul lainnya.")
    

def soal_3():
    """Soal 3 — BFS, DFS, dan Dijkstra"""
    print("\n\n" + "="*70)
    print("SOAL 3 — BFS, DFS, dan Dijkstra")
    print("="*70)
    
    # Membuat graf berbobot
    graph = Graf(directed=False)
    
    # Menambah node
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for node in nodes:
        graph.add_node(node)
    
    print()
    
    # Menambah edge dengan bobot
    edges = [('A', 'B', 2), ('A', 'C', 5), ('B', 'D', 4), ('B', 'E', 6),
             ('C', 'F', 3), ('D', 'G', 2), ('E', 'F', 4), ('F', 'G', 1)]
    for edge in edges:
        graph.add_edge(edge[0], edge[1], weight=edge[2])
    
    # a. Gambar graf
    print("\n" + "="*70)
    print("a. Visualisasi Graf:")
    print("="*70)
    graph.visualize_graph("Soal 3: Graf Berbobot")
    
    # b. BFS dari A
    print("\n" + "="*70)
    print("b. Breadth-First Search (BFS) dari A:")
    print("="*70)
    graph.bfs('A')
    
    # c. DFS dari A
    print("\n" + "="*70)
    print("c. Depth-First Search (DFS) dari A:")
    print("="*70)
    graph.dfs('A')
    
    # d. Dijkstra dari A
    print("\n" + "="*70)
    print("d. Algoritma Dijkstra dari A:")
    print("="*70)
    distances, paths = graph.dijkstra('A')
    
    print("\n" + "="*70)
    print("d.2. Jalur Terpendek dari A ke G:")
    print("="*70)
    path, distance = graph.shortest_path_dijkstra('A', 'G')
    
    # Visualisasi jalur terpendek A ke G
    print("\nVisualisasi Jalur Terpendek A -> G:")
    graph.visual_shortest_path('A', 'G')


# ==================== MAIN PROGRAM ====================

if __name__ == "__main__":
    # Jalankan penyelesaian AFL-3
    soal_1()
    soal_3()
    
    # Uncomment untuk melihat contoh dasar
    # print("\n\n")
    # contoh_dasar()