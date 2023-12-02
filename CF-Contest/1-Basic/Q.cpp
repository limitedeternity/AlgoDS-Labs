#include <algorithm>
#include <iostream>
#include <vector>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    int n;
    long long k;
    std::cin >> n >> k;

    std::vector<int> a(n), b(n);
    for (int i = 0; i < n; ++i)
    {
        std::cin >> a[i];
    }

    for (int i = 0; i < n; ++i)
    {
        std::cin >> b[i];
    }

    std::sort(a.begin(), a.end());
    std::sort(b.begin(), b.end());

    long long left = 0, right = 9223372036854775807LL;
    while (right - left > 1)
    {
        int i = 0, j = n - 1;
        long long count = 0;
        long long middle = (left + right) / 2;

        while (i < n && j >= 0)
        {
            if (a[i] + b[j] < middle)
            {
                count += j + 1;
                ++i;
            }
            else
            {
                --j;
            }
        }

        if (count < k)
        {
            left = middle;
        }
        else
        {
            right = middle;
        }
    }

    std::cout << left << "\n";
    return 0;
}
