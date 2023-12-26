#include <iostream>
#include <vector>

class Graph
{
    std::vector<size_t> colors;
    std::vector<std::vector<size_t>> neighbours;

public:
    explicit Graph(size_t size)
    {
        neighbours.resize(size);
        colors.resize(size, 0);
    }

    void DFS(size_t ver, size_t color)
    {
        if (colors[ver] != 0)
        {
            return;
        }

        colors[ver] = color;

        for (const auto neigh : neighbours[ver])
        {
            DFS(neigh, color);
        }
    }

    void color_vertices()
    {
        size_t color = 1;
        
        for (size_t i = 0; i < colors.size(); ++i)
        {
            if (colors[i] == 0)
            {
                DFS(i, color);
                ++color;
            }
        }
    }

    void insert_unoriented(size_t fst, size_t snd)
    {
        neighbours[fst].push_back(snd);
        neighbours[snd].push_back(fst);
    }

    void print_answer() const
    {
        for (auto color : colors)
        {
            std::cout << color << ' ';
        }

        std::cout << '\n';
    }
};

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    size_t vertices, edges;
    size_t ver_fst, ver_snd;

    std::cin >> vertices >> edges;
    Graph graph(vertices);

    for (size_t i = 0; i < edges; ++i)
    {
        std::cin >> ver_fst >> ver_snd;
        --ver_fst, --ver_snd;

        graph.insert_unoriented(ver_fst, ver_snd);
    }

    graph.color_vertices();
    graph.print_answer();

    return 0;
}
