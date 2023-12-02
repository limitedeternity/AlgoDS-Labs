#include <algorithm>
#include <iostream>
#include <vector>

std::vector<int> count_sort(const std::vector<int>& input)
{
    size_t N = input.size();
    int M = *std::max_element(input.begin(), input.end());

    std::vector<size_t> count(M + 1, 0);

    for (size_t i = 0; i < N; ++i)
    {
        ++count[input[i]];
    }

    for (int i = 1; i <= M; ++i)
    {
        count[i] += count[i - 1];
    }

    std::vector<int> output(N, 0);

    for (size_t i = N; i > 0; --i)
    {
        output[count[input[i - 1]] - 1] = input[i - 1];
        --count[input[i - 1]];
    }

    return output;
}

int main()
{
    size_t n = 0;
    std::cin >> n;

    std::vector<int> input(n, 0);
    for (size_t i = 0; i < n; ++i)
    {
        std::cin >> input[i];
    }

    std::vector<int> output = count_sort(input);
    for (size_t i = 0; i < n; ++i)
    {
        std::cout << output[i] << " ";
    }

    return 0;
}
