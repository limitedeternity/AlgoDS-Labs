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

long long find_closest(const std::vector<long long>& arr, size_t n, long long target) {
    size_t lower_pos = lower_index(arr, n, target);

    if (lower_pos == 0) {
        return arr[0];
    }

    if (lower_pos >= n) {
        return arr[n - 1];
    }

    auto closest = arr[lower_pos];

    if (std::abs(arr[lower_pos - 1] - target) <= std::abs(closest - target)) {
        closest = arr[lower_pos - 1];
    }

    if (lower_pos + 1 < n && std::abs(arr[lower_pos + 1] - target) <= std::abs(closest - target)) {
        closest = arr[lower_pos + 1];
    }

    return closest;
}

int main() {
    size_t n, k;
    std::cin >> n >> k;

    std::vector<long long> arr(n);
    for (auto& x : arr)
    {
        std::cin >> x;
    }

    for (size_t i = 0; i < k; ++i)
    {
        long long target;
        std::cin >> target;
        std::cout << find_closest(arr, n, target) << std::endl;
    }

    return 0;
}
