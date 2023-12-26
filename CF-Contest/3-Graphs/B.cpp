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
    std::vector<size_t> answer;

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

        for (const auto neigh : neighbours[ver])
        {
            if (colors[neigh] == Color::GRAY)
            {
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
        answer.push_back(ver);
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

    void print_answer() const
    {
        for (auto it = answer.rbegin(); it != answer.rend(); ++it)
        {
            std::cout << *it + 1 << ' ';
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
        std::cout << "-1\n";
    }
    else
    {
        graph.print_answer();
    }

    return 0;
}
