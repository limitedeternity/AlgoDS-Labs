#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    size_t n, k;
    std::cin >> n >> k;

    std::vector<size_t> v(n), w(n);
    for (size_t i = 0; i < n; ++i)
    {
        std::cin >> v[i] >> w[i];
    }

    std::vector<double> a(n);

    double left = 0, right = 1e6;
    while (right - left > 1e-6)
    {
        double middle = (left + right) / 2;

        for (size_t i = 0; i < n; ++i)
        {
            a[i] = v[i] - middle * w[i];
        }

        std::stable_sort(a.begin(), a.end(), std::greater<>());

        double sum = 0;
        for (size_t i = 0; i < k; ++i)
        {
            sum += a[i];
        }

        if (sum >= 0)
        {
            left = middle;
        }
        else
        {
            right = middle;
        }
    }

    std::vector<std::pair<double, size_t>> res(n);
    for (size_t i = 0; i < n; ++i)
    {
        res[i].first = v[i] - left * w[i];
        res[i].second = -i;
    }


    std::stable_sort(res.begin(), res.end(), std::greater<>());

    for (size_t i = 0; i < k; ++i)
    {
        std::cout << -res[i].second + 1 << "\n";
    }

    return 0;
}
