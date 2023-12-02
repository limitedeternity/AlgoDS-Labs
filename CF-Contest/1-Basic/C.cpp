#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

auto psum(const std::vector<long long>& input)
{
    std::vector<long long> result(input.size() + 1);
    std::partial_sum(input.cbegin(), input.cend(), result.begin() + 1);
    return result;
}

int main()
{
    size_t N, Q;
    std::cin >> N >> Q;

    std::vector<long long> input(N, 0);
    for (auto& x : input)
    {
        std::cin >> x;
    }

    auto result = psum(input);
    for (size_t i = 0; i < Q; ++i)
    {
        size_t l, r;
        std::cin >> l >> r;
        std::cout << result[r] - result[l - 1] << std::endl;
    }

    return 0;
}
