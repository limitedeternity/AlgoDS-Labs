#include <deque>
#include <iostream>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    size_t n, k;
    std::cin >> n >> k;

    std::deque<size_t> deq;
    for (size_t i = 0; i < n; ++i)
    {
        size_t val;
        std::cin >> val;

        deq.push_back(val);
    }

    for (size_t i = 0; i < k; ++i)
    {
        size_t x = deq.front();
        size_t y = deq.back();

        if (x < y)
        {
            deq.pop_front();
            deq.push_back((x + y) & ((1 << 30) - 1));
        }
        else
        {
            deq.pop_back();
            deq.push_front((y - x) & ((1 << 30) - 1));
        }
    }

    for (const auto val : deq)
    {
        std::cout << val << " ";
    }

    return 0;
}
