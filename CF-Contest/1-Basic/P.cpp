#include <iostream>

uint64_t findKthNumber(size_t n, size_t k)
{
    uint64_t left = 1;
    uint64_t right = n * n;

    while (left < right)
    {
        uint64_t mid = left + (right - left) / 2;
        uint64_t count = 0;

        for (size_t i = 1; i <= n; i++)
        {
            count += std::min(mid / i, n);
        }

        if (count < k)
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
    }

    return left;
}

int main()
{
    size_t n, k;
    std::cin >> n >> k;

    uint64_t result = findKthNumber(n, k);
    std::cout << result << std::endl;

    return 0;
}
