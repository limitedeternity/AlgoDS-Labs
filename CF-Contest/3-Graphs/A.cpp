#include <iostream>
#include <vector>

enum class Color
{
    WHITE,
    GRAY,
    BLACK,
};

class Graph
{
    bool has_cycle = false;
    std::vector<Color> colors;
    std::vector<std::vector<size_t>> neighbours;
    std::vector<size_t> cycle;

public:
    explicit Graph(size_t size)
    {
        neighbours.resize(size);
        colors.resize(size, Color::WHITE);
    }

    void DFS(size_t ver)
    {
        if (has_cycle || colors[ver] == Color::BLACK)
        {
            return;
        }

        colors[ver] = Color::GRAY;
        cycle.push_back(ver);

        for (const auto neigh : neighbours[ver])
        {
            if (colors[neigh] == Color::GRAY)
            {
                cycle.push_back(neigh);
                has_cycle = true;

                return;
            }
            else
            {
                DFS(neigh);
            }

            if (has_cycle)
            {
                return;
            }
        }

        colors[ver] = Color::BLACK;
        cycle.pop_back();
    }

    bool check_cycles()
    {
        for (size_t ver = 0; ver < colors.size(); ++ver)
        {
            if (colors[ver] == Color::WHITE)
            {
                DFS(ver);

                if (has_cycle)
                {
                    break;
                }
            }
        }

        return has_cycle;
    }

    void insert_oriented(size_t fst, size_t snd)
    {
        neighbours[fst].push_back(snd);
    }

    void print_cycle() const
    {
        size_t end = cycle.back();
        size_t idx = cycle.size() - 2;

        while (cycle[idx] != end)
        {
            --idx;
        }

        for (; idx < cycle.size() - 1; ++idx)
        {
            std::cout << cycle[idx] + 1 << ' ';
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

        graph.insert_oriented(ver_fst, ver_snd);
    }

    if (graph.check_cycles())
    {
        std::cout << "YES\n";
        graph.print_cycle();
    }
    else
    {
        std::cout << "NO\n";
    }

    return 0;
}
