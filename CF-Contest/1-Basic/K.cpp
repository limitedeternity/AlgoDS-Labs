#include <iostream>
#include <algorithm>

bool time_in_range(uint64_t t, uint64_t N, uint64_t x, uint64_t y)
{
    return t / x + t / y < N - 1;
}

uint64_t search(uint64_t N, uint64_t x, uint64_t y)
{
    uint64_t L = 0;
    uint64_t R = (N - 1) * std::max(x, y);

    while (R - L > 1)
    {
        uint64_t M = (L + R) / 2;

        if (time_in_range(M, N, x, y))
        {
            L = M;
        }
        else
        {
            R = M;
        }
    }

    return R + std::min(x, y);
}

int main()
{
    uint64_t N, x, y;
    std::cin >> N >> x >> y;

    if (x > y)
    {
        std::swap(x, y);
    }

    std::cout << search(N, x, y) << std::endl;
    return 0;
}
