#include <iostream>
#include <queue>

int main()
{
    std::priority_queue<uint64_t> pq;

    size_t N;
    std::cin >> N;

    for (size_t i = 0; i < N; ++i)
    {
        char cmd;
        std::cin >> cmd;

        switch (cmd)
        {
        case '0':
            {
                uint64_t value;
                std::cin >> value;

                pq.push(value);
                continue;
            }

        case '1':
            {
                std::cout << pq.top() << std::endl;

                pq.pop();
                continue;
            }

        default:
            throw std::runtime_error("Unknown command");
        }
    }

    return 0;
}
