import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self):
        """Inisialisasi graf kosong"""
        self.graph = nx.Graph()
    
    # ==================== METODE DASAR ====================
    
    def add_node(self, node):
        """Menambahkan node ke graf"""
        self.graph.add_node(node)
        print(f"Node {node} berhasil ditambahkan")
    
    def add_edge(self, node1, node2, weight=1):
        """Menambahkan edge antara dua node dengan bobot"""
        self.graph.add_edge(node1, node2, weight=weight)
        print(f"Edge ({node1}, {node2}) dengan bobot {weight} berhasil ditambahkan")
    
    def visualize_graph(self):
        """Menampilkan visualisasi graf"""
        pos = nx.spring_layout(self.graph)
        
        plt.figure(figsize=(10, 8))
        nx.draw(self.graph, pos, with_labels=True, 
                node_color='lightblue', 
                node_size=1500, 
                font_size=16, 
                font_weight='bold',
                edge_color='gray',
                width=2)
        
        # Menampilkan bobot edge
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels, font_size=12)
        
        plt.title("Visualisasi Graf", fontsize=18, fontweight='bold')
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
            
            pos = nx.spring_layout(self.graph)
            
            plt.figure(figsize=(10, 8))
            
            # Gambar semua node dan edge
            nx.draw(self.graph, pos, with_labels=True,
                    node_color='lightblue',
                    node_size=1500,
                    font_size=16,
                    font_weight='bold',
                    edge_color='gray',
                    width=2)
            
            # Highlight jalur terpendek
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path,
                                   node_color='lightgreen', node_size=1500)
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges,
                                   edge_color='red', width=3)
            
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
    
    def is_connected(self):
        """Mengecek apakah graf terhubung (connected)"""
        connected = nx.is_connected(self.graph)
        print(f"Graf terhubung: {connected}")
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


# ==================== CONTOH PENGGUNAAN ====================

if __name__ == "__main__":
    # 1. Membuat Object
    graph = Graf()
    
    # 2. Menambah Node (titik)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    
    # 3. Menambah sisi (Edge)
    graph.add_edge(1, 2, weight=4.5)
    graph.add_edge(1, 3, weight=3.2)
    graph.add_edge(2, 4, weight=2.7)
    graph.add_edge(3, 4, weight=1.8)
    graph.add_edge(1, 4, weight=6.7)
    graph.add_edge(3, 5, weight=2.7)
    
    print("\n" + "="*50)
    
    # 4. Visualisasi Graf
    print("\n4. Visualisasi Graf:")
    graph.visualize_graph()
    
    # 5. Jalur terpendek
    print("\n5. Jalur Terpendek:")
    graph.shortest_path(1, 5)
    
    # 6. Visualisasi Jalur terpendek
    print("\n6. Visualisasi Jalur Terpendek:")
    graph.visual_shortest_path(1, 5)
    
    # Demonstrasi Metode Tambahan
    print("\n" + "="*50)
    print("METODE TAMBAHAN:")
    print("="*50)
    
    print("\n1. Derajat Node:")
    graph.degree(1)
    graph.degree(3)
    
    print("\n2. Cek Konektivitas Graf:")
    graph.is_connected()
    
    print("\n3. Tetangga Node:")
    graph.get_neighbors(1)
    graph.get_neighbors(4)
    
    print("\n4. Jumlah Node:")
    graph.number_of_nodes()
    
    print("\n5. Jumlah Edge:")
    graph.number_of_edges()