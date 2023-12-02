#include <iostream>
#include <queue>

template <typename T>
class MinQueue
{
private:
    std::queue<T> Q;
    std::deque<T> D;

public:
    MinQueue() = default;

    MinQueue(const MinQueue&) = default;
    MinQueue(MinQueue&&) = default;

    MinQueue& operator=(const MinQueue&) = default;
    MinQueue& operator=(MinQueue&&) = default;

    ~MinQueue() = default;

    void push(const T& x)
    {
        Q.push(x);

        while (!D.empty() && D.back() > x)
        {
            D.pop_back();
        }

        D.push_back(x);
    }

    void pop()
    {
        if (Q.empty())
        {
            return;
        }

        if (D.front() == Q.front())
        {
            D.pop_front();
        }

        Q.pop();
    }

    T front() const
    {
        return D.front();
    }

    size_t size() const noexcept
    {
        return Q.size();
    }

    bool empty() const noexcept
    {
        return Q.empty();
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
            std::cout << pq.front() << '\n';
            continue;
        }

        std::cout << "-1\n";
    }

    return 0;
}
