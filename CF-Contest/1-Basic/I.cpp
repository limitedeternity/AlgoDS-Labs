#include <iostream>
#include <vector>
#include <algorithm>

size_t lower_index(const std::vector<long long>& arr, size_t n, long long x) {
    size_t l = 0;
    size_t h = n;

    while (l < h) {
        size_t mid = l + (h - l) / 2;

        if (arr[mid] >= x) {
            h = mid;
        } else {
            l = mid + 1;
        }
    }

    return l;
}

size_t upper_index(const std::vector<long long>& arr, size_t n, long long x) {
    size_t l = 0;
    size_t h = n;

    while (l < h) {
        size_t mid = l + (h - l) / 2;

        if (arr[mid] <= x) {
            l = mid + 1;
        } else {
            h = mid;
        }
    }

    return l;
}

size_t solve(const std::vector<long long>& arr, size_t n, long long x, long long y) {
    return upper_index(arr, n, y) - lower_index(arr, n, x);
}

int main() {
    size_t n;
    std::cin >> n;

    std::vector<long long> arr(n);
    for (auto& x : arr)
    {
        std::cin >> x;
    }

    std::sort(arr.begin(), arr.end());

    size_t q;
    std::cin >> q;

    for (size_t i = 0; i < q; ++i) {
        long long l, r;
        std::cin >> l >> r;
        std::cout << solve(arr, n, l, r) << " ";
    }

    return 0;
}
