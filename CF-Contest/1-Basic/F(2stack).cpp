#include <iostream>
#include <stack>
#include <utility>

template <typename T>
class MinQueue
{
private:
    std::stack<std::pair<T, T>> S1, S2;

public:
    MinQueue() = default;

    MinQueue(const MinQueue&) = default;
    MinQueue(MinQueue&&) = default;

    MinQueue& operator=(const MinQueue&) = default;
    MinQueue& operator=(MinQueue&&) = default;

    ~MinQueue() = default;

    void push(const T& x)
    {
        S2.push(std::pair(x, S2.empty() ? x : std::min(x, S2.top().second)));
    }

    void pop()
    {
        if (S1.empty())
        {
            while (!S2.empty())
            {
                auto top = S2.top();
                S2.pop();

                top.second = S1.empty() ? top.first : std::min(top.first, S1.top().second);
                S1.push(std::move(top));
            }
        }

        if (S1.empty())
        {
            return;
        }

        S1.pop();
    }

    T front() const
    {
        if (empty())
        {
            throw std::runtime_error("Empty queue");
        }

        return S1.empty() ? S2.top().second : (S2.empty() ? S1.top().second : std::min(S1.top().second, S2.top().second));
    }

    size_t size() const noexcept
    {
        return S1.size() + S2.size();
    }

    bool empty() const noexcept
    {
        return S1.empty() && S2.empty();
    }
};

int main()
{
    MinQueue<uint64_t> pq;

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    size_t N;
    std::cin >> N;

    for (size_t i = 0; i < N; ++i)
    {
        char cmd;
        std::cin >> cmd;

        switch (cmd)
        {
        case '+':
            {
                uint64_t value;
                std::cin >> value;

                pq.push(value);
                break;
            }

        case '-':
            {
                pq.pop();
                break;
            }

        default:
            throw std::runtime_error("Unknown command");
        }

        if (!pq.empty())
        {
            std::cout << pq.front() << std::endl;
            continue;
        }

        std::cout << "-1" << std::endl;
    }

    return 0;
}
