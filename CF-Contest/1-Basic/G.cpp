#include <iostream>
#include <stack>
#include <vector>

int main()
{
    size_t N;
    std::cin >> N;

    std::vector<int64_t> meteors(N);
    for (auto& meteor : meteors)
    {
        std::cin >> meteor;
    }

    std::vector<int64_t> stack;
    for (auto meteor : meteors)
    {
        bool restarted = false;

restart:
        if (stack.empty() || stack.back() < 0 || meteor > 0)
        {
            stack.push_back(meteor);
            continue;
        }

        if (stack.back() == -meteor)
        {
            stack.pop_back();
            continue;
        }

        if (restarted)
        {
            continue;
        }

        while (!stack.empty() && stack.back() > 0 && stack.back() < -meteor)
        {
            stack.pop_back();
        }

        restarted = true;
        goto restart;
    }

    std::cout << stack.size() << std::endl;
    for (auto meteor : stack)
    {
        std::cout << meteor << " ";
    }

    return 0;
}
